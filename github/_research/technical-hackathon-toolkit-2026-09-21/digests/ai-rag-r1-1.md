# Digest: AI model selection, prompt engineering, RAG (round 1)

Run date: 2026-09-21. All claims come from pages fetched this session. Where a page showed no date, it is marked "undated" and the price was checked live on the access date.

## Findings

1. Anthropic API list prices (per MTok, input/output): Fable 5.1 $10/$50; Opus 5 $5/$25 (Opus 4.5 through 4.8 are the same); Sonnet 5 $2/$10; Sonnet 4.6 and 4.5 $3/$15; Haiku 4.5 $1/$5. Mythos 5/5.1 are "limited availability". | https://platform.claude.com/docs/en/about-claude/pricing | Anthropic | undated (live page) | accessed 2026-09-21 | high | pricing
2. Sonnet 5's $2/$10 price was announced as introductory through 2026-08-31. It is now the standard price, and the planned rise to $3/$15 on 2026-09-01 "will not occur". That makes Sonnet 5 cheaper than Sonnet 4.6. | same | Anthropic | undated | accessed 2026-09-21 | high | pricing
3. Anthropic prompt caching: a 5-minute write costs 1.25x base input, a 1-hour write 2x, and a cache read 0.1x (0.025x on Fable/Mythos 5.1). A 5-minute cache pays off after one read. There is also an "automatic caching" option: one top-level `cache_control` field. The Batch API gives 50% off, and batch and caching discounts stack. | same | Anthropic | undated | accessed 2026-09-21 | high | pricing
4. Claude 4.7+ models use a new tokenizer that produces about 30% more tokens for the same text, so cost comparisons at equal list price are not like for like. The full 1M-token context is billed at standard price on 4.6+ models. | same | Anthropic | undated | accessed 2026-09-21 | high | pricing
5. Anthropic's own model guidance: "Choose Haiku for simple tasks, Sonnet for most production workloads, and Opus for the most complex reasoning." Fast mode (Opus 5 / 4.8) costs $10/$50. Web search tool costs $10 per 1k searches. Web fetch has no extra charge. New users get "a small amount of free credits". | same | Anthropic | undated | accessed 2026-09-21 | high | pricing
6. OpenAI standard-tier prices (per 1M tokens, input/cached/output): GPT-6 Astra $10/$1/$50; GPT-5.6 Sol $4/$0.40/$20; GPT-5.6 Terra $2/$0.20/$12; GPT-5.6 Luna $0.20/$0.02/$1.20; GPT-5.4-mini $0.75/$4.50; GPT-5-mini $0.25/$2; GPT-5-nano $0.05/$0.40; GPT-4.1-mini $0.40/$1.60; GPT-4o-mini $0.15/$0.60. | https://developers.openai.com/api/docs/pricing | OpenAI | undated (live page) | accessed 2026-09-21 | med (read through a summarizer; openai.com/api/pricing returned 403) | pricing
7. Secondary sources say the GPT-5.6 Sol $4/$20 price is "promotional through at least November 21, 2026". They also say cached input is automatic at 10% of input, Batch is 50% off, and a 10% regional-processing uplift applies to models released on or after 2026-03-05. | https://www.morphllm.com/openai-api-pricing ; https://developer.puter.com/tutorials/openai-api-pricing/ (search snippets) | third-party | 2026-09 | accessed 2026-09-21 | low-med (snippets only, not confirmed on the official page) | pricing
8. OpenAI embeddings: text-embedding-3-small costs $0.02 per 1M tokens and text-embedding-3-large $0.13 per 1M. | https://developers.openai.com/api/docs/pricing | OpenAI | undated | accessed 2026-09-21 | high | pricing
9. Gemini paid tier (per 1M tokens, input/output): Gemini 3.8 Flash and 3.7 Flash $0.75/$3.75 "through Dec 31, 2026"; 3.5 Flash $1.50/$9.00; 3.5 Flash-Lite $0.30/$2.50; 2.5 Flash-Lite $0.10/$0.40; 3.1 Pro Preview $2/$12 (prompts up to 200k). There is a free tier on all models, but free-tier content is "used to improve our products". Batch and Flex are 50% off. Page last updated 2026-09-16. | https://ai.google.dev/gemini-api/docs/pricing | Google | 2026-09 | accessed 2026-09-21 | med (summarizer output; newer 3.8 Flash being cheaper than 3.5 Flash looks like a time-limited price and should be re-checked) | pricing
10. Gemini Embedding 2 costs $0.20 per 1M text tokens, 10x text-embedding-3-small. | same | Google | 2026-09 | accessed 2026-09-21 | med | pricing
11. Voyage embeddings (per 1M tokens): voyage-4-large $0.12, voyage-4 $0.06, voyage-4-lite $0.02, voyage-context-4 $0.12, voyage-code-4 $0.12. Rerankers: rerank-3 $0.05, rerank-3-lite $0.02. The first 200M tokens are free on the newer models, which covers any hackathon. | https://docs.voyageai.com/docs/pricing | Voyage AI | undated | accessed 2026-09-21 | high | pricing
12. Anthropic prompt-engineering prerequisites: before prompting, have success criteria, a way to test against them, and a first draft. There is a metaprompt "prompt generator" notebook in claude-cookbooks. Some latency and cost problems are better fixed by choosing a different model. | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview | Anthropic | undated | accessed 2026-09-21 | high | technique
13. Anthropic techniques: be clear and direct (the "golden rule" is to show the prompt to a colleague with little context). Explain why an instruction matters. Use 3-5 examples that are relevant, diverse, and wrapped in `<example>`/`<examples>` tags. Wrap each kind of content in its own XML tag (`<instructions>`, `<context>`, `<input>`). Put a one-sentence role in the system prompt. | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices | Anthropic | undated | accessed 2026-09-21 | high | technique
14. Anthropic long-context advice (20k+ tokens): put documents at the top and the query at the end. The page says queries at the end "can improve response quality by up to 30 percent in tests" (single vendor source, flag as benchmark). Wrap each doc in `<document>` with `<source>` and `<document_content>` tags. Ask the model to extract quotes into `<quotes>` before answering. | same | Anthropic | undated | accessed 2026-09-21 | high (technique) / med (the 30% figure) | technique
15. Prefill on the last assistant turn is not supported from Claude 4.6 onward and returns a 400 error. For JSON, use Structured Outputs or tools. For classification, use a tool with an enum field. To stop preamble, add "Respond directly without preamble..." to the system prompt. Tell the model what to do, not what not to do. Match the prompt's style to the output style you want. | same | Anthropic | undated | accessed 2026-09-21 | high | technique
16. Thinking: `budget_tokens` has been replaced by `effort`. Few-shot examples can contain `<thinking>` tags to model the reasoning. Manual chain of thought with `<thinking>`/`<answer>` tags is a fallback. On Opus 5, prefer thinking on at low effort over thinking off. The latest models make parallel tool calls, and the page gives a `<use_parallel_tool_calls>` prompt to push this to about 100%. | same | Anthropic | undated | accessed 2026-09-21 | high | technique
17. OpenAI prompting: the `developer` role outranks `user`. The developer message should run in this order: Identity, then Instructions, then Examples, then Context. Use Markdown headers for sections and XML tags to mark content boundaries. Include few-shot examples. Reasoning models do best with a high-level goal, while GPT models need precise, explicit logic. Put reusable content first so caching applies. | https://developers.openai.com/api/docs/guides/prompt-engineering | OpenAI | undated | accessed 2026-09-21 | high | technique
18. Anthropic's Contextual Retrieval method: before embedding and BM25 indexing, prepend 50-100 tokens of LLM-written context to each chunk (about 800-token chunks). Pass the top 20 chunks to the model. Reranking scores the top 150 down to 20 (Cohere reranker). Failure-rate cuts: contextual embeddings -35% (5.7% to 3.7%), plus contextual BM25 -49% (to 2.9%), plus rerank -67% (to 1.9%). | https://www.anthropic.com/news/contextual-retrieval | Anthropic | 2024-09 | accessed 2026-09-21 | high (method) / med (numbers come from one vendor source; the post is 2 years old, so possibly stale on model choice) | technique/benchmark
19. Contextual Retrieval prompt, verbatim: "Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval." | same | Anthropic | 2024-09 | accessed 2026-09-21 | high | technique
20. Supabase says "HNSW should be your default choice" over IVFFlat, because it can be built right after the table is created. Opclasses are `vector_cosine_ops`, `vector_ip_ops`, and `vector_l2_ops`. For 3072-dimension vectors, index a `halfvec(3072)` cast with `halfvec_cosine_ops`. The page gives no m or ef_construction defaults. | https://supabase.com/docs/guides/ai/vector-indexes/hnsw-indexes | Supabase | undated | accessed 2026-09-21 | high | pattern
21. Supabase hybrid search: a generated `tsvector` column with a GIN index, plus a `vector` column with an HNSW index, fused with Reciprocal Rank Fusion. Defaults: `rrf_k = 50`, full_text_weight = semantic_weight = 1. Each side fetches `least(match_count,30)*2` candidates. | https://supabase.com/docs/guides/ai/hybrid-search | Supabase | undated | accessed 2026-09-21 | high | pattern
22. Pinecone's $0 Starter tier gives about 2GB storage and 1M reads/month. Qdrant Cloud free gives a single node with 0.5 vCPU, 1GB RAM, 4GB disk, and free cloud inference. One source claims a 1-collection, 1M-vector cap. Chroma is Apache-2.0 and can run embedded via pip; its cloud free tier was not found. | https://www.layer3labs.io/guides/is-pinecone-worth-it ; https://costbench.com/software/vector-databases/qdrant/free-plan/ ; https://theneuralbase.com/qdrant/learn/advanced/free-tier-limits/ (search snippets) | third-party | 2026 | accessed 2026-09-21 | low (secondary snippets, not official pricing pages) | pricing
23. The Vercel AI SDK (vercel/ai) is actively maintained: pushed 2026-09-21, 26.9k stars. It describes itself as "the AI Toolkit for TypeScript ... for building AI-powered applications and agents". | https://api.github.com/repos/vercel/ai | GitHub API | 2026-09 | accessed 2026-09-21 | high | repo
24. LlamaIndex's `create-llama` scaffolder has not been pushed since 2025-07-16, so it is stale for a 2026 toolkit. | https://api.github.com/repos/run-llama/create-llama | GitHub API | 2025-07 | accessed 2026-09-21 | high | repo
25. Ragas has moved: `explodinggradients/ragas` now redirects to `vibrantlabsai/ragas` (15.8k stars). Last push was 2026-02-24, about 7 months ago, so maintenance pace is slowing. | https://api.github.com/repos/explodinggradients/ragas | GitHub API | 2026-02 | accessed 2026-09-21 | high | repo
26. The Vercel AI chatbot template is now `vercel/chatbot` (the old ai-chatbot redirects there): 21k stars, last push 2026-07-08. The Claude cookbook is now `anthropics/claude-cookbooks` (plural): 52.9k stars, last push 2026-09-18. | GitHub API (see Repos) | GitHub | 2026 | accessed 2026-09-21 | high | repo

## Repos

| repo | URL | stars | last push | why useful |
|---|---|---|---|---|
| vercel/ai | https://github.com/vercel/ai | 26,870 | 2026-09-21 | Provider-agnostic TypeScript SDK (streaming, tools, structured output). Fastest path for a Next.js hackathon app. [23] |
| vercel/chatbot (formerly ai-chatbot) | https://github.com/vercel/chatbot | 20,960 | 2026-07-08 | "Full-featured, hackable Next.js AI chatbot". Fork-and-go chat UI. [26] |
| supabase-community/chatgpt-your-files | https://github.com/supabase-community/chatgpt-your-files | 516 | 2026-05-12 | "Production-ready MVP for securely chatting with your documents using pgvector". Reference for upload, chunk, embed, and RLS on Supabase. |
| anthropics/claude-cookbooks | https://github.com/anthropics/claude-cookbooks | 52,861 | 2026-09-18 | Official recipes, including the metaprompt prompt generator and RAG/contextual-retrieval notebooks. [12][26] |
| vibrantlabsai/ragas (formerly explodinggradients) | https://github.com/vibrantlabsai/ragas | 15,803 | 2026-02-24 | LLM/RAG evaluation metrics. Maintenance is slowing, so pin the version. [25] |
| run-llama/create-llama | https://github.com/run-llama/create-llama | 1,492 | 2025-07-16 | Stale. Do not recommend as a default. [24] |

## Practical material

### Model-pick table (Sep 2026, list prices per 1M in/out) [1][2][5][6][9]
| Role | Anthropic | OpenAI | Google |
|---|---|---|---|
| Default workhorse (demo quality, sane cost) | Sonnet 5, $2/$10 | GPT-5.6 Terra, $2/$12 | Gemini 3.8 Flash, $0.75/$3.75 (time-limited price) |
| Hard reasoning / agent core | Opus 5, $5/$25 | GPT-5.6 Sol, $4/$20 (promo) | Gemini 3.1 Pro Preview, $2/$12 |
| Cheap / high-volume (classify, extract, contextualize chunks) | Haiku 4.5, $1/$5 | GPT-5.6 Luna $0.20/$1.20; GPT-5-nano $0.05/$0.40 | 2.5 Flash-Lite, $0.10/$0.40 |
| Zero-budget prototyping | small signup credits | n/a (not checked) | free tier (data used for training) |
Hackathon rule of thumb: start on the workhorse tier. Move bulk preprocessing (such as contextual-retrieval chunk summaries) to the cheap tier with batch and caching. Keep the big-tier models for the one step judges will see. Latency was not measured in any source fetched this run.

### Embedding pick [8][10][11]
- Default: OpenAI text-embedding-3-small at $0.02/M, or voyage-4-lite at $0.02/M with 200M free tokens. voyage-context-4 is a context-aware option.
- Quality: voyage-4-large at $0.12/M or text-embedding-3-large at $0.13/M. At 3072 dimensions, index as halfvec [20].
- Reranker: Voyage rerank-3-lite at $0.02/M, with 200M free tokens.

### Prompt skeleton (merges Anthropic [13][14][15] and OpenAI [17])
```
SYSTEM / developer:
You are <role, one sentence>. <why this matters / audience>.
<instructions>
1. ... (numbered when order matters; say what TO do)
Respond directly without preamble.
</instructions>
<examples>
  <example><input>...</input><output>...</output></example>   (3-5, diverse)
</examples>

USER:
<documents>
  <document index="1"><source>{{SRC}}</source><document_content>{{DOC}}</document_content></document>
</documents>
First extract relevant quotes into <quotes>. Then answer in <answer>.
If the answer is not in the documents, say so.
<question>{{QUERY}}</question>        (query LAST)
```
- Put stable content (system prompt, documents) first so prompt caching applies [3][17].
- For JSON, use Structured Outputs or a tool schema. Do not prefill (400 error on Claude 4.6+) [15].

### RAG pipeline defaults [18][19][20][21]
1. Chunk at about 800 tokens with light overlap. Overlap is not specified in the source; treat it as a hypothesis.
2. Contextualize each chunk with the cheap model plus prompt caching of the full document, using the verbatim prompt from [19]. Prepend the 50-100 token result to the chunk.
3. Index twice: a tsvector (BM25-ish) column and an embedding column.
4. Retrieve with hybrid RRF (k=50, weights 1/1), pull about 150 candidates, rerank, and keep the top 20 for the LLM.
5. Use the long-context prompt shape above.

### pgvector SQL (Supabase) [20][21]
```sql
create extension if not exists vector with schema extensions;
create table documents (
  id bigint primary key generated always as identity,
  content text,
  fts tsvector generated always as (to_tsvector('english', content)) stored,
  embedding extensions.vector(1536)          -- match your model's dims
);
create index on documents using gin(fts);
create index on documents using hnsw (embedding vector_cosine_ops);  -- or vector_ip_ops for normalized embeddings
-- hybrid_search(query_text, query_embedding, match_count, full_text_weight=1, semantic_weight=1, rrf_k=50): see finding 21 / Supabase docs
```
(The Supabase example uses vector(512) with `vector_ip_ops` and the `<#>` operator. Keep the operator consistent with the opclass.)

### Eval checklist [12][18][25]
- Write success criteria and a 20-50 question golden set before tuning prompts.
- Track retrieval failure rate (is the right chunk in the top-K?) separately from answer quality, as in Anthropic's recall@20-style metric.
- Change one thing at a time: contextual embeddings, then hybrid BM25, then reranking.
- Ragas is usable but has moved to vibrantlabsai and its maintenance is slowing, so pin the version.

### Macro ideas for PROMPTS-ML.md / PROMPTS-RAG.md
- `/pick-model <task> <budget>`: maps the task to the model-pick table and costs it with the caching and batch multipliers [1][3][6][9].
- `/contextualize-chunks`: runs the batch plus caching job using the prompt from [19].
- `/hybrid-schema <dims>`: emits the SQL above [21].
- `/prompt-skeleton`: emits the XML skeleton [13][14].
- `/rag-eval`: builds a golden set and reports recall@K plus answer faithfulness [18].

## Leads not chased / Looked for but not found
- Google's official prompting guide (ai.google.dev prompting strategies): not fetched because of budget.
- Cohere embed/rerank pricing: not fetched. Anthropic's post used a Cohere reranker [18].
- Official Pinecone, Qdrant, and Chroma Cloud pricing pages: only third-party snippets were found [22]. Chroma Cloud free tier was not found.
- Supabase free-tier limits (DB size, project pausing): not checked.
- Framework comparison: LangChain/LangGraph and LlamaIndex current versions and activity were not checked. Only vercel/ai and create-llama activity was checked.
- Latency or throughput benchmarks for any model: none fetched. Do not state latency claims.
- Ragas metric definitions and current API: not fetched.
- HNSW m / ef_construction defaults: not on the Supabase page. pgvector's README would have them.
- The OpenAI official page was read only through a summarizer, and openai.com/api/pricing returned 403. Re-verify GPT-6 Astra and GPT-5.6 tiers by hand.
- Oddity: Gemini 3.8/3.7 Flash are listed cheaper than 3.5 Flash with a "through Dec 31, 2026" note, so the price is time-limited. Re-check before publishing.
