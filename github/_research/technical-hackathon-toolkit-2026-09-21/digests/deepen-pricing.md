# Deepen: pricing / free-tier closure (2026-09-22)

Method: official vendor pages via WebFetch (summarised by fetch model; quotes are as returned). Budget 12 calls. Supabase page fetch failed (ECONNREFUSED).

## Findings

1. OpenAI GPT-5.6 Terra (Standard): $2.00 input / $0.20 cached / $12.00 output per 1M tokens | https://developers.openai.com/api/docs/pricing | OpenAI | no date shown | accessed 2026-09-22 | high | pricing
2. OpenAI GPT-5.6 Luna (Standard): $0.20 input / $0.02 cached / $1.20 output per 1M | same URL | OpenAI | no date shown | accessed 2026-09-22 | high | pricing
3. OpenAI GPT-5.6 Sol (Standard): $4.00 input / $0.40 cached / $20.00 output per 1M; page says "GPT-5.6 Sol's promotional pricing is available at least through November 21, 2026." | same URL | OpenAI | no date shown | accessed 2026-09-22 | high | pricing
4. OpenAI text-embedding-3-small: $0.02 per 1M input tokens (Standard) | same URL | OpenAI | no date shown | accessed 2026-09-22 | high | pricing
5. Gemini 3.8 Flash paid tier: input "$0.75 through December 31, 2026. $1.50 starting January 1, 2027"; output "$3.75 through December 31, 2026. $7.50 starting January 1, 2027"; free tier: free input & output tokens | https://ai.google.dev/gemini-api/docs/pricing | Google | last updated 2026-09-16 | accessed 2026-09-22 | high | pricing
6. Gemini 3.5 Flash: paid $1.50 input / $9.00 output per 1M; free tier available (free input & output) | same URL | Google | 2026-09-16 | accessed 2026-09-22 | high | pricing
7. Gemini 3.1 Pro Preview: no free tier; paid $2.00 input (<=200k prompts) / $4.00 (>200k); $12.00 output (<=200k) / $18.00 (>200k) | same URL | Google | 2026-09-16 | accessed 2026-09-22 | high | pricing
8. Gemini free-tier data use: free tier content "used to improve our products"; paid tier "not used to improve our products" | same URL | Google | 2026-09-16 | accessed 2026-09-22 | high | free-tier
9. Pinecone Starter (free): up to 2 GB storage, 2M write units/mo, 1M read units/mo, 1 GB/mo egress, up to 5 indexes, 100 namespaces/index, 1 project, AWS us-east-1 only, up to 2 users. Paid: Builder $20/mo flat; Standard $50/mo min usage; Enterprise $500/mo min | https://www.pinecone.io/pricing/ | Pinecone | no date shown | accessed 2026-09-22 | high | free-tier
10. Qdrant Cloud free cluster: "0.5 vCPU / 1GB RAM / 4 GB Disk", single node, "Free Cloud Inference With Selected Models"; page did not state card requirement or inactivity suspension | https://qdrant.tech/pricing/ | Qdrant | no date shown | accessed 2026-09-22 | high | free-tier
11. Chroma Cloud Starter: $0/mo + usage, "$5 in complimentary credits monthly"; Team $250/mo + usage with $100 monthly included credits (no rollover) | https://www.trychroma.com/pricing | Chroma | no date shown | accessed 2026-09-22 | high | free-tier
12. Weaviate Cloud Free: "Always free"; 100,000 objects, 1 GB memory, 10 GB disk, 1 collection up to 3 tenants, embeddings 2,000 req/day, Query Agent 1,000 req/mo; no card (per fetch summary). Flex from $45/mo, Premium from $400/mo | https://weaviate.io/pricing | Weaviate | no date shown | accessed 2026-09-22 | high (no-card detail: medium) | free-tier
13. 21st.dev plans: Free (Hobby) $0; Builder $6/mo yearly or $8/mo quarterly; Builder + AI $15-60/mo yearly ($20-80 quarterly) for 500-2,000 monthly credits; Team $7.50/seat (no AI) or $18.75/seat (AI, shared credits); extra credits "+100 for $5 (one-time, rolls over)" | https://21st.dev/pricing | 21st.dev | no date shown | accessed 2026-09-22 | high | pricing
14. 21st.dev Free includes: marketplace browsing, component/UI inspiration/theme/icon libraries, unlimited UI inspirations, unlimited SVG logo search, "2 free copies / day", "5 free Design Bug Bot reviews", community support (no AI credits listed) | same URL | 21st.dev | no date shown | accessed 2026-09-22 | high | free-tier
15. Inngest is self-hostable: "Self-hosting support for Inngest is supported as of the 1.0 release"; single CLI binary (Docker/npm/binary); SQLite default, Redis (in-memory or external) for queue/state, PostgreSQL for production; no guaranteed support for self-hosted, enterprise option for guarantees | https://www.inngest.com/docs/self-hosting | Inngest | no date shown | accessed 2026-09-22 | high | capability

## Answers to each question

1. Terra $2/$12 (cached $0.20), Luna $0.20/$1.20 (cached $0.02), Sol $4/$20 (cached $0.40); Sol price is explicitly promotional, "at least through November 21, 2026"; text-embedding-3-small $0.02/1M [F1-F4].
2. Yes: 3.8 Flash $0.75/$3.75 is limited-time through 2026-12-31, rising to $1.50/$7.50 on 2027-01-01 [F5]. 3.5 Flash $1.50/$9.00 [F6]; 3.1 Pro (Preview) $2/$12 (<=200k), no free tier [F7]. Free-tier content is used to improve Google products; paid is not [F8].
3. Pinecone Starter [F9], Qdrant 0.5vCPU/1GB/4GB free cluster [F10], Chroma Cloud $5/mo free credits [F11], Weaviate always-free sandbox [F12]. Supabase pgvector-in-free-tier: unresolved (fetch failed).
4. Free Hobby plan with 2 copies/day and 5 Design Bug Bot reviews; AI credits only on Builder + AI (500-2,000/mo) [F13-F14].
5. Yes, self-hostable since 1.0 via single binary; SQLite/Redis/Postgres [F15]. License not stated on page (unresolved).

## Not found

- Supabase pricing page (ECONNREFUSED): Free plan limits and pgvector inclusion unresolved.
- OpenAI pricing page last-updated date; platform.openai.com/docs/pricing not fetched (budget).
- Qdrant free cluster card requirement / inactivity suspension not stated on page.
- Inngest license not stated on self-hosting page.
