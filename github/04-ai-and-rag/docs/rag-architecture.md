# 🔎 RAG Architecture Standard

<!-- markdownlint-disable MD013 -->

> Contextual Retrieval + hybrid search + reranking, all inside Supabase Postgres. Verified 2026-09-21.

---

## Reference pipeline

```text
INGEST                                   QUERY
──────                                   ─────
docs → chunk (~800 tok)                  user question
     → contextualize each chunk            → embed query
       (cheap model + cached full doc)     → hybrid search: BM25-ish (tsvector) + vector (HNSW)
     → prepend 50–100 tok context             fused with RRF (k=50), ~150 candidates
     → embed  +  tsvector                  → rerank → top 20
     → Postgres (pgvector)                 → LLM with long-context prompt shape (docs first, query last)
```

### Why this shape

Anthropic's **Contextual Retrieval** results (retrieval failure rate, top-20) ([Anthropic, 2024-09](https://www.anthropic.com/news/contextual-retrieval)):

| Setup | Failure rate | Reduction |
| --- | --- | --- |
| Baseline embeddings | 5.7% | — |
| + Contextual embeddings | 3.7% | −35% |
| + Contextual BM25 | 2.9% | −49% |
| + Reranking | 1.9% | **−67%** |

> [!NOTE]
> These are **single-vendor figures from 2024**, so the model choices may be dated. The *pattern* is sound and widely copied. Measure on your own data.

**Contextualisation prompt (key sentence verbatim from Anthropic):**

```text
<document>
{{WHOLE_DOCUMENT}}
</document>
Here is the chunk we want to situate within the whole document
<chunk>
{{CHUNK_CONTENT}}
</chunk>
Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval. Answer only with the succinct context and nothing else.
```

The key sentence ("Please give a short succinct context…") is verbatim from the source. The `<document>`/`<chunk>` wrapper and the last sentence are reconstructed and weren't verified in this research, so compare them with the Anthropic post or the cookbook notebook before relying on them. Run it on **Haiku 4.5** with **prompt caching** of the full document and the **Batch API**.

---

## Defaults

| Parameter | Default | Source / confidence |
| --- | --- | --- |
| Chunk size | ~800 tokens | Anthropic (high) |
| Chunk overlap | 10–15% | help-me-papi practitioner guidance (not separately verified) |
| Context prefix | 50–100 tokens | Anthropic (high) |
| Candidates before rerank | ~150 | Anthropic (high) |
| Chunks passed to the LLM | 20 | Anthropic (high) |
| Vector index | **HNSW** ("should be your default choice") | [Supabase](https://supabase.com/docs/guides/ai/vector-indexes/hnsw-indexes) (high) |
| Fusion | RRF, `rrf_k = 50`, full-text weight = semantic weight = 1 | [Supabase](https://supabase.com/docs/guides/ai/hybrid-search) (high) |
| Embedding | text-embedding-3-small / voyage-4-lite ($0.02/M) | see `model-selection.md` |
| Reranker | Voyage rerank-3-lite ($0.02/M) | [Voyage](https://docs.voyageai.com/docs/pricing) |

---

## Supabase schema (pgvector + hybrid)

```sql
create extension if not exists vector with schema extensions;

create table documents (
  id bigint primary key generated always as identity,
  source text not null,
  content text not null,                                  -- context prefix + chunk
  fts tsvector generated always as (to_tsvector('english', content)) stored,
  embedding extensions.vector(1536)                       -- match your model's dimensions
);

create index on documents using gin (fts);
create index on documents using hnsw (embedding vector_cosine_ops);
-- 3072-dim models: index a halfvec cast with halfvec_cosine_ops
```

**Opclasses:** `vector_cosine_ops` (`<=>`) · `vector_ip_ops` (`<#>`, for normalised embeddings) · `vector_l2_ops` (`<->`). **Keep the operator in your query consistent with the opclass** ([Supabase HNSW](https://supabase.com/docs/guides/ai/vector-indexes/hnsw-indexes)).

### Hybrid search function (RRF)

Adapted from the [Supabase hybrid search guide](https://supabase.com/docs/guides/ai/hybrid-search):

```sql
create or replace function hybrid_search(
  query_text text,
  query_embedding extensions.vector(1536),
  match_count int,
  full_text_weight float = 1,
  semantic_weight float = 1,
  rrf_k int = 50
) returns setof documents language sql as $$
with full_text as (
  select id, row_number() over (order by ts_rank_cd(fts, websearch_to_tsquery(query_text)) desc) as rank_ix
  from documents
  where fts @@ websearch_to_tsquery(query_text)
  order by rank_ix
  limit least(match_count, 30) * 2
),
semantic as (
  select id, row_number() over (order by embedding <=> query_embedding) as rank_ix
  from documents
  order by rank_ix
  limit least(match_count, 30) * 2
)
select documents.*
from full_text
full outer join semantic on full_text.id = semantic.id
join documents on coalesce(full_text.id, semantic.id) = documents.id
order by
  coalesce(1.0 / (rrf_k + full_text.rank_ix), 0.0) * full_text_weight +
  coalesce(1.0 / (rrf_k + semantic.rank_ix), 0.0) * semantic_weight
  desc
limit least(match_count, 30);
$$;
```

> Supabase's own example uses `vector(512)` with `vector_ip_ops` and `<#>`. The version above uses cosine (`<=>`) to match the index. Check the guide if you change the opclass.

Add RLS to `documents` if the corpus is per-user (see `../../03-backend/docs/database-supabase.md`).

---

## Vector store alternatives (only if not on Supabase)

| Store | Free tier (official pricing pages, 2026-09-22) | Notes |
| --- | --- | --- |
| [Pinecone](https://www.pinecone.io/pricing/) Starter | 2 GB storage, 2M write + 1M read units/mo, 5 indexes, 1 project, AWS us-east-1 only | Builder $20/mo flat |
| [Qdrant Cloud](https://qdrant.tech/pricing/) free cluster | 0.5 vCPU, 1 GB RAM, 4 GB disk, single node, free cloud inference on selected models | Card/inactivity terms not stated |
| [Chroma Cloud](https://www.trychroma.com/pricing) Starter | $0 + usage, **$5 free credits/month** | Or run Chroma embedded via pip (Apache-2.0) |
| [Weaviate Cloud](https://weaviate.io/pricing) Free | Always free: 100K objects, 1 GB memory, 10 GB disk, 1 collection | Embeddings 2K req/day |

**Recommendation:** stay on Supabase pgvector. It's one less service and one less set of keys, and RLS applies to your embeddings too.

---

## Retrieval refinements

From help-me-papi `AI/skills/chunking.md` and `retrieval.md`. These are practitioner guidance, not separately verified.

| Technique | When |
| --- | --- |
| **Semantic chunking** (split on headings or paragraphs, then cap the size) | Default over naive fixed-size splits |
| **Code:** chunk by function or class (AST-aware), never by line count | Code-search features |
| **Tables:** repeat the header row in every chunk | Spreadsheets, CSVs, PDFs with tables |
| **Chunk metadata:** source, section heading, position (N of M), `parent_id`, timestamp | Always. It enables citations, reranking and freshness filters |
| **Context expansion:** retrieve small chunks, then pull neighbouring chunks by `parent_id` | When answers need more surrounding context |
| **Metadata filters inside the SQL** (owner, tenant, date) *before* similarity search | Always, for per-user data. Never filter after retrieval |
| **Query rewriting:** the LLM turns the chat turn into 2–3 standalone queries | Conversational interfaces (`../PROMPTS-RAG.md` R10) |

> **Top-K difference:** help-me-papi reranks 20–50 candidates down to **3–8**, while Anthropic's Contextual Retrieval passes the **top 20** to the model. Start with 20 for recall, and cut it if latency or cost hurts.

## Failure triage: classify before you fix

| Failure class | Symptom | Fix |
| --- | --- | --- |
| **Retrieval miss** | The right chunk never appears in the candidates | Better chunking, contextual prefixes, hybrid search, query rewriting |
| **Ranking miss** | The right chunk is retrieved but buried below the cut | Better reranker; adjust RRF weights |
| **Generation miss** | The right chunks are in the prompt but the answer is still wrong | Tighter grounding prompt, citations, guardrails (`../PROMPTS-RAG.md` R9) |

Don't reach for a bigger model as the default fix for every failure class. Add real failures to the golden set so they can't come back.

## Evaluation (keep it light)

1. Write **20–50 golden questions** with the chunk that should answer each one.
2. Track **retrieval** (is the right chunk in the top-K?) separately from **answer quality**.
3. Change one thing at a time: contextual chunks → hybrid → rerank.
4. Track **cost and p50/p95 latency** next to quality. A 2% quality gain that doubles latency isn't automatically a win.
5. [Ragas](https://github.com/vibrantlabsai/ragas) (moved from explodinggradients; ⭐ 15.8k; last push 2026-02, slowing) works for metrics if you pin the version.

---

## Starter repos

| Repo | Why | Status |
| --- | --- | --- |
| [supabase-community/chatgpt-your-files](https://github.com/supabase-community/chatgpt-your-files) | Upload → chunk → embed → chat with RLS on Supabase | ⭐ 516 · pushed 2026-05 |
| [vercel/chatbot](https://github.com/vercel/chatbot) (formerly ai-chatbot) | Fork-and-go Next.js chat UI | ⭐ 21k · pushed 2026-07 |
| [vercel/ai](https://github.com/vercel/ai) | Streaming, tools, structured output | ⭐ 26.9k · pushed 2026-09 |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Contextual retrieval and RAG notebooks | ⭐ 52.9k · pushed 2026-09 |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | Extension docs (HNSW `m`, `ef_construction`) | ⭐ 23k · pushed 2026-09 |
