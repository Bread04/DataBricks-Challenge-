# 🔎 RAG & Vector Search Macros

<!-- markdownlint-disable MD013 -->

> Copy-paste prompts for building a Supabase pgvector RAG pipeline. Reference: `docs/rag-architecture.md`

---

## Contents

| Code | Macro |
| --- | --- |
| [R1](#r1--rag-design-decision) | RAG design decision |
| [R2](#r2--hybrid-schema) | Hybrid schema |
| [R3](#r3--ingestion-pipeline) | Ingestion pipeline |
| [R4](#r4--contextualise-chunks) | Contextualise chunks |
| [R5](#r5--retrieval--rerank) | Retrieval + rerank |
| [R6](#r6--answer-with-citations) | Answer with citations |
| [R7](#r7--golden-set--eval) | Golden set + eval |
| [R8](#r8--rag-debug) | RAG debug |
| [R9](#r9--add-guardrails) | Add guardrails |
| [R10](#r10--query-rewriting) | Query rewriting |

> R9–R10 are adapted from [help-me-papi](https://github.com/maxi-cmyk/help-me-papi) `AI/PROMPTS-RAG.md` (`ADD_GUARDRAILS`) and `AI/skills/retrieval.md`.

---

### R1 · RAG design decision

```text
Corpus: <what, how many docs, avg size, update frequency>. Users ask: <example questions>. Per-user data? <yes/no>.
Decide: do we need RAG at all (vs. stuffing into a 1M-context prompt with caching)? If RAG: chunk size, embedding model, hybrid vs vector-only, rerank yes/no, top-K.
Default to: ~800-token chunks, contextual retrieval, Supabase pgvector HNSW + tsvector hybrid (RRF k=50), rerank 150→20. Justify any deviation.
```

### R2 · Hybrid schema

```text
Write a Supabase migration for hybrid search:
- enable vector extension (schema extensions)
- documents(id, source, owner_id text null, content, fts tsvector generated from content, embedding vector(<dims>))
- GIN index on fts, HNSW index on embedding with <vector_cosine_ops | vector_ip_ops> (halfvec cast if dims > 2000)
- hybrid_search(query_text, query_embedding, match_count, full_text_weight=1, semantic_weight=1, rrf_k=50) using RRF, operator consistent with the opclass
- RLS: owners read their own rows; shared rows (owner_id null) readable by authenticated.
```

*Pattern:* [Supabase hybrid search](https://supabase.com/docs/guides/ai/hybrid-search), [HNSW](https://supabase.com/docs/guides/ai/vector-indexes/hnsw-indexes)

### R3 · Ingestion pipeline

```text
Build scripts/ingest.ts:
1. Load files from <dir> (md, pdf→text, html→text).
2. Chunk at ~800 tokens on heading/paragraph boundaries with small overlap.
3. Contextualize each chunk (see R4) — batch it.
4. Embed "context + chunk" with <embedding model>.
5. Upsert into documents (idempotent by source+chunk index).
Print counts and total token cost. Resume safely if interrupted.
```

### R4 · Contextualise chunks

```text
For each chunk, call Haiku 4.5 with the WHOLE document cached (cache_control on the document block) and this prompt:
"<document>{{DOC}}</document> Here is the chunk we want to situate within the whole document <chunk>{{CHUNK}}</chunk> Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval. Answer only with the succinct context and nothing else."
Use the Batch API if >100 chunks. Prepend the 50–100 token result to the chunk before embedding AND before tsvector indexing.
```

*Source:* [Anthropic Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval). Only the "Please give a short succinct context…" sentence is verbatim. The XML wrapper is reconstructed (see `docs/rag-architecture.md`).

### R5 · Retrieval + rerank

```text
Implement retrieve(query, userId):
1. Embed the query.
2. Call hybrid_search with match_count=30 (≈150 candidates internally is fine to tune).
3. Rerank candidates with <Voyage rerank-3-lite | Cohere>; keep top 20.
4. Return {id, source, content, score}.
Add timing logs per stage. If the reranker fails, fall back to RRF order.
```

### R6 · Answer with citations

```text
Write the answer step:
- System: "You answer questions using only the provided documents. Explain uncertainty. Respond directly without preamble."
- User: <documents> with <document index><source><document_content> for each retrieved chunk FIRST, then "Extract relevant quotes into <quotes>, then answer in <answer> citing [index] after each claim. If the documents don't contain the answer, say so." then <question> LAST.
- Parse <answer>, map [index] → source links in the UI.
No prefill (Claude 4.6+).
```

*Shape:* [Anthropic long-context tips](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

### R7 · Golden set + eval

```text
From the corpus, generate 30 realistic questions users would ask, each with the source chunk id(s) that answer it. Include 5 unanswerable questions.
Write scripts/rag-eval.ts that reports: recall@20 (is the right chunk retrieved?), answer faithfulness (LLM-judged with Haiku 4.5), and correct refusals on unanswerable ones.
Run it before and after each change (contextual → hybrid → rerank) and print a comparison table.
```

### R8 · RAG debug

```text
This query gives a bad answer: "<query>". Diagnose stage by stage:
1. Show the top 20 retrieved chunks with scores from full-text and semantic separately.
2. Is the right chunk present? If not → chunking/contextualization/embedding problem. If present but low → fusion/rerank. If present and top → prompt problem.
3. Propose the smallest fix and re-run.
```

### R9 · Add guardrails

```text
[ROLE] AI reliability engineer. [CONTEXT] Current system prompt + RAG pipeline: <paste>.
Add guardrails against hallucination and out-of-scope answers:
1. GROUNDING: "Answer only from the provided documents; if they don't contain the answer, say you don't know."
2. CITATIONS: every claim cites [index] of the supporting chunk — makes hallucination visible.
3. OUTPUT VALIDATION: structured output schema, validated before it reaches the user.
4. REFUSAL PATH: a defined, tested response for out-of-scope or unsafe queries.
5. RUNTIME FAITHFULNESS CHECK (high-stakes answers only): a cheap Haiku 4.5 judge verifies claims are supported; if not, fall back to "I couldn't find that in the sources."
Output the updated prompt + validation code + 5 test queries that now correctly refuse or hedge.
```

### R10 · Query rewriting

```text
Improve recall for conversational queries: before retrieval, have <cheap model> rewrite the user's message (plus the last 2 turns) into 2–3 standalone search queries.
Run hybrid_search for each, merge with RRF, dedupe, then rerank once.
Apply metadata filters (owner/tenant, date, source) INSIDE the SQL before similarity search — never filter after retrieval.
Log original query, rewrites, and retrieved ids for eval.
```
