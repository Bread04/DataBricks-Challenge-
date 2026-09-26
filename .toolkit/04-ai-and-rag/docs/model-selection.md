# 🤖 Model Selection (September 2026)

<!-- markdownlint-disable MD013 -->

> Which model for which job, with list prices. **Prices change monthly. Re-check before every event.** Verified 2026-09-21.

---

## Pick table (USD per 1M tokens, input / output)

> **Cost tags:** Anthropic and OpenAI APIs are **💰 pay-as-you-go** (small signup credits). Google Gemini has a **🆓* free tier** on Flash models (data used to improve Google's products). **🆓 $0 options:** Gemini free tier, Cerebras/Groq/OpenRouter free tiers, or local models via Ollama. See [`../../05-tools-and-mcp/docs/free-ai-dev-tools.md`](../../05-tools-and-mcp/docs/free-ai-dev-tools.md).

| Role | Anthropic 💰 | OpenAI 💰 | Google 🆓* / 💰 |
| --- | --- | --- | --- |
| **Default workhorse** | **Sonnet 5**: $2 / $10 | GPT-5.6 Terra: $2 / $12 | Gemini 3.8 Flash: $0.75 / $3.75 ⏳ |
| **Hard reasoning / agent core** | **Opus 5**: $5 / $25 | GPT-5.6 Sol: $4 / $20 (promo) | Gemini 3.1 Pro Preview: $2 / $12 |
| **Cheap / bulk** (classify, extract, chunk context) | **Haiku 4.5**: $1 / $5 | GPT-5.6 Luna: $0.20 / $1.20 · GPT-5-nano: $0.05 / $0.40 | Gemini 2.5 Flash-Lite: $0.10 / $0.40 |
| **Frontier (special cases)** | Fable 5.1: $10 / $50 | GPT-6 Astra: $10 / $50 | — |
| **Zero budget** | Small signup credits | — | Free tier (⚠️ your data is used to improve Google's products) |

Sources and confidence:

- **Anthropic:** [pricing page](https://platform.claude.com/docs/en/about-claude/pricing), high confidence. Sonnet 5's $2/$10 launch price is now permanent, and the planned rise to $3/$15 "will not occur", so **Sonnet 5 is cheaper than Sonnet 4.6** ($3/$15).
- **OpenAI:** [pricing](https://developers.openai.com/api/docs/pricing), **high confidence** (re-read on the official page in the Deepen run, 2026-09-22). The official page says GPT-5.6 Sol's price is promotional "at least through November 21, 2026".
- **Google:** [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing), **high confidence** (updated 2026-09-16, re-checked 2026-09-22). ⏳ 3.8 Flash is $0.75/$3.75 **until 2026-12-31, then $1.50/$7.50 from 2027-01-01**. 3.1 Pro Preview has **no free tier**.

> [!NOTE]
> **No latency or throughput benchmarks** were verified in this research. Don't pick on speed claims without measuring on your own prompts.

---

## Anthropic's own rule of thumb

> "Choose **Haiku** for simple tasks, **Sonnet** for most production workloads, and **Opus** for the most complex reasoning." ([Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing))

### Hackathon strategy

1. **Build everything on the workhorse** (Sonnet 5).
2. Move **bulk preprocessing** (contextualising chunks, classification, extraction) to **Haiku 4.5**, with Batch and caching.
3. Keep **Opus 5** for the *single step judges will see* reasoning, if it clearly wins there.
4. Hard-cap spend with per-user rate limits (see `../../03-backend/docs/security.md`).

---

## Cost levers (Anthropic)

| Lever | Effect |
| --- | --- |
| Prompt caching, 5-min write | 1.25× base input to write, **0.1× to read**. Pays off after 1 read |
| Prompt caching, 1-hour write | 2× to write |
| Automatic caching | One top-level `cache_control` field |
| Batch API | **50% off**; stacks with caching |
| Fast mode (Opus 5 / 4.8) | $10 / $50, a premium for speed |
| Web search tool | $10 per 1k searches; web fetch has no extra charge |
| ⚠️ Tokenizer | Claude 4.7+ models produce **~30% more tokens** for the same text, so compare costs on real prompts |
| 1M context | Billed at standard rates on 4.6+ models |

Source: [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing)

OpenAI cached input is automatic at about 10% of input, and Batch is 50% off (secondary sources). Gemini Batch and Flex are 50% off.

---

## Embeddings and rerankers

| Model | Price per 1M | Notes |
| --- | --- | --- |
| OpenAI text-embedding-3-small | $0.02 | Default; 1536 dims |
| OpenAI text-embedding-3-large | $0.13 | 3072 dims → index as `halfvec` |
| Voyage voyage-4-lite | $0.02 | **200M free tokens** on newer models |
| Voyage voyage-4 / voyage-4-large | $0.06 / $0.12 | Quality tiers |
| Voyage voyage-context-4 | $0.12 | Context-aware embeddings |
| Voyage voyage-code-4 | $0.12 | Code search |
| Gemini Embedding 2 | $0.20 | 10× text-embedding-3-small |
| Voyage rerank-3 / rerank-3-lite | $0.05 / $0.02 | 200M free tokens |

Sources: [OpenAI](https://developers.openai.com/api/docs/pricing) · [Voyage](https://docs.voyageai.com/docs/pricing) · [Gemini](https://ai.google.dev/gemini-api/docs/pricing)

**Hackathon default:** `voyage-4-lite` or `text-embedding-3-small` for embeddings, and `rerank-3-lite` for reranking. The free tokens cover any hackathon.

---

## SDK / framework choice

| Option | Status | Use when |
| --- | --- | --- |
| **[Vercel AI SDK](https://github.com/vercel/ai)** | ⭐ 26.9k · pushed 2026-09-21 | **Default for Next.js**: provider-agnostic, streaming, tools, structured output |
| Anthropic / OpenAI native SDKs | — | You need provider-specific features (caching control, batch) |
| [LangChain](https://github.com/langchain-ai/langchain) | ⭐ 147k · pushed 2026-09-21 | Complex agent graphs (LangGraph); more to learn |
| [LlamaIndex](https://github.com/run-llama/llama_index) | ⭐ 52k · pushed 2026-09-19 | Heavy document ingestion pipelines |
| ~~create-llama~~ | ❌ last push 2025-07 | Stale, so don't scaffold from it |

The framework choice wasn't evaluated in depth. Vercel AI SDK is recommended for Next.js based on its activity and fit, not on a head-to-head benchmark.
