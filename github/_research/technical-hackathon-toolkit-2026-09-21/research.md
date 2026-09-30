---
title: 'technical research: hackathon toolkit'
type: 'technical'
topic: 'hackathon toolkit'
decision: 'Which standards, prompt macros, tools, and GitHub repos to adopt in a per-field hackathon toolkit (Hackathons, Frontend, Backend, AI & RAG, Tools & MCP)'
source: 'native run'
status: complete
preset: 'standard'
validation: 'normal'
created: '2026-09-21'
updated: '2026-09-22'
claims_verified: 44
claims_unverified: 6
---

<!-- markdownlint-disable-next-line MD025 -->
# Technical research: hackathon toolkit

<!-- markdownlint-disable MD013 MD025 MD052 -->

**Decision this research serves:** which standards, prompt macros, tools and GitHub repos to adopt in a per-field hackathon toolkit.

## Executive summary

> **Deepen 2026-09-22:** added sections 6–11 (11 = MCP ecosystem and AI dev tools) (voice & realtime, Web3, mobile, product plumbing & credits, app deployment, MCP & dev tools) and closed 11 of 14 open questions. **Load-bearing change:** Supabase enforces opt-in table grants on all existing projects on **2026-10-30** [57]. Conclusions below are unchanged.

**Adopt a Next.js 16 + Supabase + Clerk + Vercel AI SDK stack, with a small, security-scoped MCP set.** Standardise every field on current primary specs: WCAG 2.2 AA, Core Web Vitals, DTCG tokens, RFC 9457 and OWASP API 2023. Treat pitch and compliance as first-class work, not an afterthought.

The three findings that drive this:

1. **Judges reward clarity and a working demo.** They prefer simpler projects they understand, want to see something working in about 90 seconds, and penalise backend-only builds [1][2]. Major events now **enforce AI disclosure and git hygiene**: ETHGlobal wants file-level AI disclosure, bans AI voiceover, and may disqualify a project that arrives as one giant commit [5]. MLH allows AI with disclosure but bans code written before the event [6].
2. **Several common patterns are now wrong.**
   - The Clerk→Supabase JWT template has been deprecated since 2025-04-01 [24][25].
   - Next.js 16 renamed `middleware.ts` to `proxy.ts`. The rename is stated by Clerk [26]; the Next.js v16 guide uses `proxy.ts` throughout but doesn't state the rename [27].
   - Claude 4.6+ rejects assistant prefill with a 400 error [38].
   - 21st "Magic" keys were reset and its tools renamed [47].
   - Several popular starters are stale or archived [54].

   A toolkit built from older tutorials would break on day one.
3. **MCP servers are the biggest leverage and the biggest risk.** Context7, Supabase, Playwright, shadcn, 21st and Stitch each save hours. But every vendor's docs warn about prompt injection and require scoping: read-only mode, a project ref, human confirmation [43][48][51][52].

**Biggest caveat:** the official Stitch MCP endpoint (`stitch.googleapis.com/mcp`) is confirmed, but a Claude Code issue reports its API-key header being ignored in favour of OAuth discovery, which fails [45]. Keep the community proxy as a fallback [46].

---

## 1. Hackathon strategy and pitching

- **What wins:** clarity over complexity; one feature done well; the problem up front; working within about 90 s; mock slow or flaky parts [1]. Named Devpost judges list what kills a submission: backend-only projects with no UI, ambiguity, barely changed templates, recycled projects, and unequal team contribution [2]. Some judges look at visual appeal first [2].
- **Criteria:**
  - Devpost's common set has no weights: implementation, ease of use, demo, impact, idea quality, design [3].
  - ETHGlobal: Technicality, Originality, Practicality, Usability, WOW [5].
  - MLH science fair: about 3 min per team, stack-ranked top 3 [7].
  - One unverified snippet says MLH doesn't judge pitch or idea quality. That contradicts sponsor-judge practice, so read each event's rubric (low confidence).
- **Video and demo:**
  - Devpost: allow 2–3 h before the deadline; videos are usually under 3 min; write your own script [4].
  - ETHGlobal: 2–4 min, at least 720p, intro of 20 s or less, no TTS or AI voiceover, no phone recording, no sped-up footage [5].
  - MLH digital events: 2 min or less, naming the event [6].
- **Gaps:** no fetched primary source on which AI tools are used at hackathons, and no hour-by-hour timelines from winners.

## 2. Frontend standards and tooling

- **Performance:** Core Web Vitals "good" is LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 at p75 [8]. No 2025–26 change was found (medium confidence). JS budgets rest on a 2018 heuristic: about 170 KB compressed critical path and Lighthouse ≥ 80 [9] (low confidence, stale).
- **Accessibility:** WCAG 2.2 has been a Recommendation since 2024-12. It asks for 4.5:1 text contrast, 3:1 for UI components, visible focus that isn't fully obscured, and targets of at least 24×24 CSS px [10][11]. WCAG 3 is still a Working Draft (2026-09-10), with a final version expected no earlier than about 2028 [12] (medium confidence).
- **Tokens:** the DTCG spec reached its first stable version, 2025.10 [13]. Tailwind v4 `@theme` emits variables and utilities, and a single `--spacing` base drives the scale [14]. Atlassian's 8 px spacing scale is 0–80 px [15].
- **Anti-slop tooling:**
  - Impeccable is 1 skill with 24 commands and 61 deterministic detector rules, built on Anthropic's frontend-design skill [16][17].
  - Blogs cite older figures (18 skills, 23 commands, 58 rules). The README wins.
- **Tools:**
  - Stitch was relaunched on 2026-05-19 with an agent canvas. Official exports go to Antigravity and Netlify [18]; Figma is reached through a plugin (low–medium confidence).
  - 21st AI generates shadcn/React variants via MCP or CLI, on a daily free allowance [19].
  - shadcn changes monthly: Base UI became the default primitive layer in Jul 2026, and it has had an MCP server since Aug 2025 [20].

## 3. Backend standards and stack

- **Errors:** RFC 9457 (2023-07) obsoletes RFC 7807. It uses `application/problem+json` with `type`, `title`, `status`, `detail` and `instance`, plus extensions such as an `errors[]` array with JSON pointers. Don't leak internals [21][27].
- **Free tiers:**
  - Supabase: 2 projects, 500 MB DB, **pauses after 1 week idle**, 50k MAU [22].
  - Clerk Hobby: 50k **MRU**, 7-day fixed sessions [23].
- **Auth:**
  - Clerk + Supabase now uses Supabase Third-Party Auth: a `role: authenticated` claim plus supabase-js `accessToken()`. The JWT template has been deprecated since 2025-04-01 [24][25].
  - On Next.js 16 `clerkMiddleware()` lives in `proxy.ts` [26]. Next.js warns never to rely on proxy alone for authorization [27].
- **Data access:** Next.js recommends a server-only Data Access Layer returning DTOs. Treat Server Actions as public endpoints and re-check auth in each one. Rate-limit Route Handlers with 429 [27][28].
- **RLS:** write one policy per operation, scope it `to authenticated`, use `(select auth.uid())`, and index the policy columns [29]. Supabase plans to make default table grants opt-in (**no date given**); opting in now is recommended [30]. Its sample rate limiter returns a non-standard 420 [30].
- **Migrations:** `migration new` → `db diff` → `db reset` → `db push`; never edit the remote database directly [31].
- **Security baseline:** the OWASP API Top 10 2023 is still the latest edition [32].
- **API style:** REST, GraphQL or tRPC guidance comes only from blogs [33] (low confidence). By inference from [27][28]: Server Components + DAL for reads, Server Actions for mutations, REST only for webhooks.

## 4. AI model selection, prompting and RAG

- **Anthropic prices (per MTok):** Sonnet 5 $2/$10 (the planned rise to $3/$15 was cancelled), Opus 5 $5/$25, Haiku 4.5 $1/$5, Fable 5.1 $10/$50. Cache reads cost 0.1× and Batch is 50% off. Tokenizers on 4.7+ produce about 30% more tokens [34].
- **Other providers:**
  - OpenAI GPT-5.6 Terra $2/$12, Luna $0.20/$1.20; text-embedding-3-small $0.02 [35]. Medium confidence: read through a summariser.
  - Gemini 3.8 Flash $0.75/$3.75, time-limited to 2026-12-31; the free tier trains on your data [36].
  - Voyage embeddings from $0.02 with 200M free tokens [37].
- **Prompting:**
  - Anthropic: XML-tagged sections, 3–5 examples, long documents first and the query last. **Prefill returns a 400 from 4.6 onward**, so use structured outputs or tools. `effort` replaces `budget_tokens` [38].
  - OpenAI: developer message ordered Identity → Instructions → Examples → Context [39].
- **RAG:**
  - Contextual Retrieval prepends 50–100 tokens of context to ~800-token chunks. Combined with hybrid BM25 and reranking, it cut retrieval failures by 67% [40]. That figure is from a single vendor source and is 2 years old, so medium confidence.
  - Supabase recommends HNSW as the default index and does hybrid search through RRF with k=50 [41][42].
  - Vector-store free tiers come only from third-party pages [55] (low confidence).
- **Repos [54]:**
  - Current: vercel/ai; vercel/chatbot; anthropics/claude-cookbooks (plural name).
  - Stale: create-llama (last push 2025-07).
  - Moved: Ragas is now vibrantlabsai/ragas (last push 2026-02).

## 5. Tools and MCP

- **Claude Code mechanics:**
  - `claude mcp add` supports `--transport http` and the `--` form for stdio servers.
  - Scopes are local (default), project (`.mcp.json`, committed) and user. `.mcp.json` expands `${VAR}`.
  - Output warns at 10k tokens and is capped at 25k.
  - Official warning: trust servers first, because anything that fetches external content can inject prompts [43].
- **Stitch:**
  - The official flow is Stitch → pull design context → `DESIGN.md` → React/Tailwind [44].
  - The remote endpoint `stitch.googleapis.com/mcp` with an `X-Goog-Api-Key` header is confirmed, but Claude Code issue #41664 (2026-03, closed as not planned) reports the header ignored and OAuth DCR failing [45].
  - The community proxy `@_davideast/stitch-mcp` is explicitly not Google-affiliated [46].
  - The sync is **one-way**. No source shows code→Stitch CSS sync.
- **21st:**
  - "Magic MCP is now the 21st MCP." Tools are `generate`, `get_inspiration` and `search_logo`, and old keys were reset [47].
  - The README (plugin marketplace) and the website (`npx @21st-dev/cli@latest init --client claude`) give different install routes [19][47].
  - `generate` requires AI access on the account. No prices are published.
- **Others (primary READMEs and docs):**
  - Supabase MCP: `read_only=true`, `project_ref`, feature groups; never production [48].
  - Playwright MCP: Microsoft itself suggests its CLI plus skills is more token-efficient, and says the MCP server is not a security boundary [49].
  - Context7: community docs, accuracy not guaranteed [50].
  - Vercel MCP: official beta with full account power, including deploying and purchases [51].
  - Stripe: sandbox, restricted keys, human confirmation [52].
  - shadcn: `mcp init --client claude` [53].
  - GitHub: `--read-only` and toolsets [56].

---

## 6. Voice and realtime AI

*Deepen 2026-09-22.*

- **Speech-to-speech APIs:**
  - OpenAI `gpt-realtime` is generally available (snapshot 2025-08-28). It takes audio and text over WebRTC, WebSocket or SIP. Audio costs $32 input / $64 output per 1M tokens, and $0.40 for cached input [69].
  - Google names Gemini 3.8 Live as its current realtime voice model and calls the older Live previews legacy [70] (medium confidence, search snippet).
  - **No public Anthropic realtime speech-to-speech API was found.** Claude's voice mode is a consumer and Claude Code feature (absence of evidence).
- **Cascaded pipeline** (for using Claude as the brain):
  - Deepgram gives $200 of free credit with no card. Streaming STT costs $0.0048–$0.0078/min and Aura-1 TTS costs $0.015 per 1K characters [71].
  - ElevenLabs Flash TTS costs $0.05 per 1K characters (~75 ms) and Scribe v2 Realtime STT costs $0.39/hr. The free quota isn't stated [72].
  - Kokoro-82M is an Apache-licensed offline TTS model (repo last pushed 2025-08) [101].
- **Frameworks:** LiveKit Agents (14.3k stars) and Pipecat (15.8k) are both pushed daily [101]. Vocode was last pushed 2024-11, so it is stale [101]. Hosted Vapi and Retell each give about $10 of trial credit (low confidence, third-party sources).
- **Browser gotcha:** `getUserMedia` needs a secure context (HTTPS or localhost). An iframe needs `allow="microphone"`, and a denied or insecure page throws `NotAllowedError` [73].

## 7. Web3 (ETHGlobal-style)

*Deepen 2026-09-22.*

- **Starting point:** `npx create-eth@latest` (Scaffold-ETH 2) wires up Next.js, wagmi, viem and RainbowKit, and lets you choose Foundry or Hardhat [75]. The repo was pushed 2026-08 [101].
- **Toolchain:** Hardhat 3 is stable, and Nomic claims it covers most of Foundry's functionality, including Solidity tests and fuzzing [74] (a vendor claim). Foundry (10.6k stars) and Hardhat (8.5k) are both active [101]. No source recommending one over the other was found, so use whichever the team knows.
- **Wallets:** WalletConnect is now **Reown**, and Web3Modal is now **Reown AppKit** [78]. RainbowKit was last pushed 2026-05 [101]. Coinbase Smart Wallet is branded Base Account (secondary source). EIP-7702 has been live on mainnet since Pectra (2025-05-07) [76].
- **Networks:** Holesky has been sunset. Use Sepolia for apps and Hoodi for validators [76]. Base Sepolia faucets (CDP, Alchemy) give 0.1 ETH per 24 h [77].
- **Onboarding:** Privy has a free tier, but its MAU cap is disputed (499 vs 1,000) [102].
- **Security:** start from OpenZeppelin Contracts (27.2k stars) and its Wizard [101]. Deploy to testnets only.

## 8. Mobile

*Deepen 2026-09-22.*

- **Expo:** SDK 57 is stable (React Native 0.86, React 19.2), and SDK 58 went to beta on 2026-09-15 [79]. React Native has run only on the New Architecture since 0.82 [82].
- **Getting it onto judges' phones:**
  - Expo Go for SDK 57 was still awaiting App Store approval on iOS as of 2026-08-13 [79].
  - EAS Free gives 15 Android + 15 iOS builds a month (low-priority queue) and EAS Update to 1K MAUs [80].
  - An Android APK can be installed directly. iOS ad hoc distribution needs UDIDs and a paid account, capped at 100 devices [81].
- **UI:** NativeWind v5 is pre-release, so use v4 [83]. React Native Reusables (8.7k stars), gluestack-ui, Tamagui (14.2k) and HeroUI Native (3.7k) are all active [101].
- **Auth:** `@clerk/clerk-expo` is deprecated in favour of `@clerk/expo`. Its native components need a development build [84].

## 9. Product plumbing and free credits

*Deepen 2026-09-22.*

- **Analytics and errors:**
  - PostHog free: 1M events, 5K session replays and 100K exceptions a month, no card [85].
  - Vercel Web Analytics on Hobby: 50K events and no custom events [86].
- **Payments:** Stripe sandboxes simulate payments with test card 4242 4242 4242 4242. Using real cards for testing is prohibited [87].
- **Maps:**
  - Mapbox free: 50K web map loads and 100K geocoding and directions requests [88].
  - OpenFreeMap: keyless and unlimited tiles for MapLibre, attribution required [89].
- **Email:** Resend free gives 3K emails a month, capped at 100 a day [90].
- **Credits:** the GitHub Student Developer Pack includes Azure $100, Copilot, Codespaces, free domains, MongoDB Atlas $50, Sentry and Stripe $25 [91] (medium confidence on the exact offer wording).
- **Not found:** Sentry's standalone free-plan limits, Google Maps free usage, and AI-vendor hackathon credit programmes.

## 10. App deployment beyond Vercel and Railway

*Deepen 2026-09-22.*

- **Render Free:** sleeps after 15 min idle and takes about 1 min to wake. It gives 750 instance-hours a month, and free Postgres expires after 30 days [92].
- **Railway:** a one-time $5 trial, then a $1/mo Free plan (0.5 GB RAM). A card is now required [93].
- **Fly.io:** a trial only, lasting 2 machine-hours or 7 days [94] (medium confidence).
- **Cloudflare Workers Free:** 100K requests/day and 10 ms CPU per request [95].
- **Netlify:** 300 credits a month, and each production deploy costs 15 credits [96].
- **Hugging Face Spaces:** Gradio and Docker Spaces now need PRO. Free accounts older than 30 days get up to 2 ZeroGPU Gradio Spaces, and static Spaces stay free [97].
- **Streamlit Community Cloud:** apps sleep after 12 h without traffic [98].
- **Modal:** $30/mo of free compute [99].
- **Demo-day implication:** open every free-tier URL 5–10 minutes before presenting.

## 11. MCP ecosystem and AI dev tools

*Deepen #2, 2026-09-22 (cost tags: 🆓 free · 🆓* free tier · 💳 trial · 💰 paid).*

- **Spec:** the current MCP spec is **2026-07-28**. It has a stateless core (no handshake or session header), multi round-trip requests, and CIMD + RFC 9207 auth. **SSE, Sampling, Roots and Logging are deprecated** [103].
- **Registry:** the Official MCP Registry has been in preview since 2025-09-08 [104]. A third party counted about 9.6K servers in May 2026 (low confidence).
- **Claude Code:**
  - MCP tool search is **on by default**, and output is capped at 25K tokens [43].
  - `claude-plugins-official` bundles MCP servers for github, supabase, vercel, sentry, linear, notion, figma, slack and others [105].
  - Community plugins are screened and pinned to a commit SHA, but Anthropic doesn't control the MCP servers they bundle [105].
- **Reference servers:** `modelcontextprotocol/servers` keeps only 7 (Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking, Time). Postgres, SQLite, GitHub, Brave, Redis, Sentry, Slack and Puppeteer are **archived** [106].
- **Vendor servers:**
  - Chrome DevTools MCP (🆓; sends usage stats unless you opt out) [107].
  - DBHub for any Postgres (🆓) [43].
  - Neon, MongoDB, Redis, Netlify, Firecrawl, Exa, Ref, awslabs (all active) [122].
  - The Browserbase MCP repo is **archived** [122].
  - Figma MCP needs a **paid Dev/Full seat** (💰) [108].
- **Claude Code cost:** it is **not** on the Free plan. It needs Pro ($20/month) or more, or an API key (💳/💰) [109].
- **Hooks:** official hooks can auto-format after edits and block edits to protected files (exit code 2) [110].
- **Free dev tools:**
  - Copilot Free gives 2,000 completions/month [111].
  - Lovable Free gives 5 build credits/day (up to 30/month) [112].
  - Figma Starter gives 150 AI credits/day [113].
  - The Gemini API no longer publishes fixed free limits; check them in AI Studio [114].
  - Antigravity ($0), Kiro (50 credits), v0 ($5/month), Bolt (300K tokens/day), Groq, Cerebras and OpenRouter free tiers come from search summaries only (medium confidence).
- **Gone:** **GitHub Models was retired on 2026-07-30** [115]. **Firebase Studio** closed to new users on 2026-06-22 and shuts down on 2027-03-22 [116]. Both were verified by the lead.
- **Security:**
  - Tool poisoning and rug pulls [117].
  - GitHub MCP "toxic agent flow" (May 2025) [117].
  - **postmark-mcp npm backdoor** (Sep 2025, BCC'd all mail from v1.0.16) [118].
  - Spec rules: no token passthrough, sandbox local servers, minimal scopes [119].
  - Claude Code: `/sandbox`, and trust prompts that are skipped under `claude -p` [120].
  - `mcp-scan` is now **Snyk Agent Scan**: `uvx snyk-agent-scan@latest`, needs `SNYK_TOKEN`, and sends tool descriptions to Snyk [121].

## Deepen 2026-09-22: resolved open questions

| Question | Answer | Status | Sources |
| --- | --- | --- | --- |
| OpenAI prices | Terra $2/$12, Luna $0.20/$1.20, Sol $4/$20 (promo at least to 2026-11-21), embedding-3-small $0.02, now read from the official page | ✅ verified (was medium) | [35] |
| Gemini prices | 3.8 Flash $0.75/$3.75 **until 2026-12-31, then $1.50/$7.50**; 3.1 Pro Preview has no free tier; free-tier data is used to improve products | ✅ verified | [36] |
| Supabase opt-in grants date | Default for new projects from **2026-05-30**, enforced on **all existing projects 2026-10-30**; `auto_expose_new_tables` removed that day | ✅ verified (lead confirmed via the changelog) | [57] |
| Vector-DB free tiers | Pinecone Starter 2 GB / 5 indexes; Qdrant 0.5 vCPU / 1 GB / 4 GB; Chroma Cloud $5/mo credits; Weaviate always-free 100K objects | ✅ official pages | [58][59][60][61] |
| 21st.dev pricing | Free: 2 copies/day, no AI credits; Builder $6–8/mo; Builder + AI $15–80/mo (500–2,000 credits) | ✅ | [62] |
| Inngest self-hosting | Yes, since 1.0 (single binary; SQLite, Redis, Postgres) | ✅ | [63] |
| Stitch MCP header bug | #41664 closed as a duplicate, **not fixed**; a related regression is reported through Claude Code v2.1.211 | ⚠️ still open | [45][64] |
| GSAP free | 100% free including all plugins | ✅ | [65] |
| Chainlit | Community-maintained since 2025-05-01; ChainLeak CVEs fixed in **2.9.4** | ✅ | [66][67] |
| oRPC slug | `middleapi/orpc` (5.6k stars) | ✅ | [101] |
| DeepSeek Harness / Pi | `deepseek-ai/deepseek-harness` (232.8k stars); Pi = `earendil-works/pi` (108.3k stars, moved from badlogic/pi-mono) | ✅ | [100][101] |
| JS budget | Russell 2026: ~1.5 MiB (JS-light) / ~935 KiB (JS-heavy) of critical-path bytes for a 3 s load on a Galaxy A24-class device | ⚠️ labels unconfirmed | [68] |
| WCAG 3 timeline | Unchanged: Working Draft; CR ~Q4 2027 | ⚠️ secondary sources | [12] |
| Devpost criteria, AI tools used at hackathons | Not researched this run | ❌ open | — |

---

## Cross-dimension insights

- **Compliance and tooling meet in git.** ETHGlobal's disqualification for a single giant commit and its file-level AI disclosure [5] suit an agentic build style of small commits per story. But they turn the AI-usage log into a *submission artefact*, so it has to be kept from hour 0 rather than written at the end.
- **The anti-slop and judging dimensions reinforce each other.** Judges look at visuals first and punish barely changed templates [2]. Impeccable's detector specifically flags template tells (Inter, purple gradients, nested cards) [16]. Running `/impeccable audit` directly targets a known judging penalty.
- **Free-tier limits hit on judging day.** Supabase pauses idle projects after a week [22] and Clerk sessions are fixed at 7 days [23]. A demo prepared early can be asleep or logged out when the judges arrive.
- **One Postgres serves two fields.** Supabase covers both backend (RLS, auth) and RAG (pgvector HNSW and hybrid search) [29][41][42]. That removes a separate vector database and its unverified free-tier limits [55].
- **Security guidance lines up across fields.** OWASP API10 "unsafe consumption of APIs" [32], Next.js's "treat Server Actions as public" [28] and every MCP vendor's prompt-injection warning [43][48][51] all say the same thing: treat LLM and third-party output as untrusted input.

## Recommendations

| # | Recommendation | Feeds | Confidence |
| --- | --- | --- | --- |
| R1 | Default stack: Next.js 16 (`proxy.ts`) + Supabase (RLS, opt-in grants) + Clerk via Third-Party Auth + Vercel AI SDK | `03-backend/docs/`, `skills/hackathon-backend/` | High [22–28] |
| R2 | Error envelope = RFC 9457 `application/problem+json`, with a helper plus Zod mapping | ../../03-backend/docs/api-standards.md | High [21] |
| R3 | Frontend gate: WCAG 2.2 AA checklist + CWV budget + `/impeccable audit` before the feature freeze | `02-frontend/docs/`, `skills/hackathon-frontend/` | High for standards [8][10]; low for the JS budget [9] |
| R4 | Tokens: Tailwind v4 `@theme` primitives → semantic via `@theme inline`; DTCG JSON only if a tool needs it | ../../02-frontend/docs/design-system-variables.md | High [13][14] |
| R5 | Model defaults: Sonnet 5 as workhorse, Haiku 4.5 for bulk work, Opus 5 for the one judged reasoning step; no prefill | ../../04-ai-and-rag/docs/model-selection.md | High (Anthropic) [34][38]; medium (OpenAI/Gemini) [35][36] |
| R6 | RAG default: Supabase pgvector HNSW + hybrid RRF + contextual chunks + rerank | ../../04-ai-and-rag/docs/rag-architecture.md | High for the pattern [41][42]; medium for the gains [40] |
| R7 | MCP core set: Context7, Supabase (read-only, dev), Playwright, shadcn, 21st; Stitch optional with a proxy fallback; project `.mcp.json` with `${VAR}` only | `05-tools-and-mcp/docs/` | High [43][47][48]; medium for Stitch [45][46] |
| R8 | Start an AI-usage log and small commits from hour 0 | ../../01-hackathon-playbook/battle-plan.md | High [5][6] |

## Open questions

- **MCP run:** Snyk Agent Scan free-tier terms; Railway/Render/Slack MCP endpoints; Official MCP Registry GA status; Docker MCP Toolkit pricing; OSS agent setup requirements; Zed/JetBrains/Windsurf free terms.

*Updated by the Deepen run on 2026-09-22; see the "resolved open questions" table above for what was answered.*

- **Stitch MCP header bug:** still unfixed as of Claude Code v2.1.211 [64]. Test the stdio proxy before relying on it.
- **Devpost official criteria** and **primary evidence on AI tools used at hackathons:** not researched yet.
- **WCAG 3 timeline:** still secondary sources only [12].
- **Voice:** Gemini Live pricing, OpenAI TTS pricing, ElevenLabs free quota, and LiveKit/Pipecat feature comparison.
- **Web3:** Foundry vs Hardhat recommendation, RainbowKit/ConnectKit 2026 status, Dynamic/thirdweb free tiers, Privy MAU cap (499 vs 1,000) [102].
- **Mobile:** whether Expo Go SDK 57 reached the iOS App Store after 2026-08-13; SDK 58 stable date.
- **Plumbing and credits:** Sentry standalone free plan, Google Maps free usage, AI-vendor and cloud credit programmes, MLH perks.
- **Deployment:** Fly.io pricing page (read only via search summaries), HF Spaces sleep duration, keep-warm guidance.

## Source appendix

| # | Supports | Publisher | Pub date | Accessed | Confidence |
| --- | --- | --- | --- | --- | --- |
| [1] | Judging-table advice | [JetBrains Blog](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/) | 2026-06 | 2026-09-21 | medium |
| [2] | Submission killers | [Devpost](https://info.devpost.com/blog/hackathon-judging-tips) | undated | 2026-09-21 | medium |
| [3] | Common criteria | [Devpost](https://info.devpost.com/blog/understanding-hackathon-submission-and-judging-criteria) | undated | 2026-09-21 | high |
| [4] | Video tips | [Devpost](https://info.devpost.com/blog/6-tips-for-making-a-hackathon-demo-video) | undated | 2026-09-21 | high |
| [5] | ETHGlobal format, AI rules | [ETHGlobal](https://ethglobal.com/events/tokyo2026/info/details) | 2026 | 2026-09-21 | high |
| [6] | MLH rules | [MLH (GitHub)](https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md) | living | 2026-09-21 | high |
| [7] | MLH judging plan | [MLH Guide](https://guide.mlh.com/general-information/judging-and-submissions/judging-plan) | undated | 2026-09-21 | high |
| [8] | CWV thresholds | [web.dev](https://web.dev/articles/vitals) | 2024-10 | 2026-09-21 | high |
| [9] | Perf budgets | [web.dev](https://web.dev/articles/performance-budgets-101) | 2018-11 | 2026-09-21 | low |
| [10] | WCAG 2.2 | [W3C](https://www.w3.org/TR/WCAG22/) | 2024-12 | 2026-09-21 | high |
| [11] | Target size | [W3C WAI](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) | undated | 2026-09-21 | high |
| [12] | WCAG 3 status | [W3C WAI](https://www.w3.org/WAI/news/2026-09-10/wcag3/) | 2026-09 | 2026-09-21 | medium |
| [13] | DTCG stable | [W3C DTCG](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/) | 2025-10 | 2026-09-21 | high |
| [14] | Tailwind @theme | [Tailwind Labs](https://tailwindcss.com/docs/theme) | undated | 2026-09-21 | high |
| [15] | Spacing scale | [Atlassian](https://atlassian.design/foundations/spacing) | undated | 2026-09-21 | high |
| [16] | Impeccable | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 2026-09 | 2026-09-21 | high |
| [17] | frontend-design skill | [Anthropic](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) | 2026-09 | 2026-09-21 | high |
| [18] | Stitch relaunch | [Google](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-updates/) | 2026-05 | 2026-09-21 | high |
| [19] | 21st AI / MCP site | [21st.dev](https://21st.dev/mcp) | undated | 2026-09-21 | medium |
| [20] | shadcn changelog | [shadcn](https://ui.shadcn.com/docs/changelog) | 2026-09 | 2026-09-21 | medium |
| [21] | RFC 9457 | [RFC Editor](https://www.rfc-editor.org/rfc/rfc9457.html) | 2023-07 | 2026-09-21 | high |
| [22] | Supabase free tier | [Supabase](https://supabase.com/pricing) | live | 2026-09-21 | high |
| [23] | Clerk free tier | [Clerk](https://clerk.com/pricing) | live | 2026-09-21 | high |
| [24] | Clerk third-party auth | [Supabase docs](https://supabase.com/docs/guides/auth/third-party/clerk) | undated | 2026-09-21 | high |
| [25] | Clerk↔Supabase guide | [Clerk docs](https://clerk.com/docs/guides/development/integrations/databases/supabase) | undated | 2026-09-21 | high |
| [26] | Clerk Next.js quickstart | [Clerk docs](https://clerk.com/docs/nextjs/getting-started/quickstart) | undated | 2026-09-21 | high |
| [27] | Next.js BFF / proxy | [Vercel](https://nextjs.org/docs/app/guides/backend-for-frontend) | 2026-06 | 2026-09-21 | high |
| [28] | Next.js data security | [Vercel](https://nextjs.org/docs/app/guides/data-security) | 2026-08 | 2026-09-21 | high |
| [29] | RLS | [Supabase docs](https://supabase.com/docs/guides/database/postgres/row-level-security) | undated | 2026-09-21 | high |
| [30] | Securing API | [Supabase docs](https://supabase.com/docs/guides/api/securing-your-api) | undated | 2026-09-21 | high |
| [31] | Migrations | [Supabase docs](https://supabase.com/docs/guides/deployment/database-migrations) | undated | 2026-09-21 | high |
| [32] | OWASP API Top 10 | [OWASP](https://api-security.owasp.org/editions/2023/en/0x11-t10) | 2023 | 2026-09-21 | high |
| [33] | REST/GraphQL/tRPC | [Directus](https://directus.io/blog/rest-graphql-tprc) | undated | 2026-09-21 | low |
| [34] | Anthropic pricing | [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) | live | 2026-09-21 | high |
| [35] | OpenAI pricing | [OpenAI](https://developers.openai.com/api/docs/pricing) | live | 2026-09-22 | high (re-read on the official page in the Deepen run) |
| [36] | Gemini pricing | [Google](https://ai.google.dev/gemini-api/docs/pricing) | 2026-09-16 | 2026-09-22 | high (Deepen re-check) |
| [37] | Voyage pricing | [Voyage AI](https://docs.voyageai.com/docs/pricing) | undated | 2026-09-21 | high |
| [38] | Claude prompting | [Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | undated | 2026-09-21 | high |
| [39] | OpenAI prompting | [OpenAI](https://developers.openai.com/api/docs/guides/prompt-engineering) | undated | 2026-09-21 | high |
| [40] | Contextual Retrieval | [Anthropic](https://www.anthropic.com/news/contextual-retrieval) | 2024-09 | 2026-09-21 | medium |
| [41] | HNSW default | [Supabase docs](https://supabase.com/docs/guides/ai/vector-indexes/hnsw-indexes) | undated | 2026-09-21 | high |
| [42] | Hybrid search | [Supabase docs](https://supabase.com/docs/guides/ai/hybrid-search) | undated | 2026-09-21 | high |
| [43] | Claude Code MCP | [Anthropic](https://code.claude.com/docs/en/mcp) | undated | 2026-09-21 | high |
| [44] | Stitch codelab | [Google Codelabs](https://codelabs.developers.google.com/design-to-code-with-antigravity-stitch) | undated | 2026-09-21 | high |
| [45] | Stitch header issue | [anthropics/claude-code #41664](https://github.com/anthropics/claude-code/issues/41664) | 2026-03 | 2026-09-21 | high |
| [46] | Stitch proxy | [davideast/stitch-mcp](https://github.com/davideast/stitch-mcp) | 2026-05 | 2026-09-21 | high |
| [47] | 21st MCP | [21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp) | 2026-09 | 2026-09-21 | high |
| [48] | Supabase MCP | [Supabase docs](https://supabase.com/docs/guides/getting-started/mcp) | undated | 2026-09-21 | high |
| [49] | Playwright MCP | [Microsoft](https://github.com/microsoft/playwright-mcp) | 2026-09 | 2026-09-21 | high |
| [50] | Context7 | [Upstash](https://github.com/upstash/context7) | 2026-09 | 2026-09-21 | high |
| [51] | Vercel MCP | [Vercel](https://vercel.com/docs/agent-resources/vercel-mcp) | 2026-09 | 2026-09-21 | high |
| [52] | Stripe MCP | [Stripe](https://docs.stripe.com/mcp) | 2026 | 2026-09-21 | high |
| [53] | shadcn MCP | [shadcn](https://ui.shadcn.com/docs/mcp) | undated | 2026-09-21 | high |
| [54] | Repo stars / push dates | [GitHub REST API](https://api.github.com/) | 2026-09 | 2026-09-21 | high |
| [55] | Vector free tiers | [layer3labs](https://www.layer3labs.io/guides/is-pinecone-worth-it) | 2026 | 2026-09-21 | low |
| [56] | GitHub MCP | [GitHub](https://github.com/github/github-mcp-server) | 2026-09 | 2026-09-21 | high |
| [57] | Supabase opt-in grants dates | [Supabase changelog](https://supabase.com/changelog/45329-breaking-change-tables-not-exposed-to-data-and-graphql-api-automatically) | 2026 | 2026-09-22 | high |
| [58] | Pinecone free tier | [Pinecone](https://www.pinecone.io/pricing/) | live | 2026-09-22 | high |
| [59] | Qdrant free cluster | [Qdrant](https://qdrant.tech/pricing/) | live | 2026-09-22 | high |
| [60] | Chroma Cloud free credits | [Chroma](https://www.trychroma.com/pricing) | live | 2026-09-22 | high |
| [61] | Weaviate free sandbox | [Weaviate](https://weaviate.io/pricing) | live | 2026-09-22 | high |
| [62] | 21st.dev plans | [21st.dev](https://21st.dev/pricing) | live | 2026-09-22 | high |
| [63] | Inngest self-hosting | [Inngest](https://www.inngest.com/docs/self-hosting) | live | 2026-09-22 | high |
| [64] | Claude Code header/OAuth regression | [anthropics/claude-code #78534](https://github.com/anthropics/claude-code/issues/78534) | 2026 | 2026-09-22 | medium |
| [65] | GSAP free | [GSAP](https://gsap.com/pricing/) | live | 2026-09-22 | high |
| [66] | Chainlit maintenance | [Chainlit README](https://github.com/Chainlit/chainlit) | 2026 | 2026-09-22 | high |
| [67] | ChainLeak CVEs | [GitHub Advisory](https://github.com/advisories/GHSA-gm79-2pvc-wc75) | 2026-01 | 2026-09-22 | high |
| [68] | JS budget 2026 | [Infrequently Noted](https://infrequently.org/2025/11/performance-inequality-gap-2026/) | 2025-11 | 2026-09-22 | medium |
| [69] | gpt-realtime | [OpenAI](https://developers.openai.com/api/docs/models/gpt-realtime) | live | 2026-09-22 | medium |
| [70] | Gemini Live | [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-real-time-voice-applications-gemini-audio/) | 2026 | 2026-09-22 | medium |
| [71] | Deepgram pricing | [Deepgram](https://deepgram.com/pricing) | live | 2026-09-22 | high |
| [72] | ElevenLabs API pricing | [ElevenLabs](https://elevenlabs.io/pricing/api) | live | 2026-09-22 | high |
| [73] | getUserMedia secure context | [MDN](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia) | live | 2026-09-22 | high |
| [74] | Hardhat 3 stable | [Nomic Foundation](https://blog.nomic.foundation/hardhat-3-is-now-stable/) | 2026-06 | 2026-09-22 | high |
| [75] | Scaffold-ETH 2 | [scaffold-eth-2](https://github.com/scaffold-eth/scaffold-eth-2) | 2026 | 2026-09-22 | high |
| [76] | Holesky sunset; Pectra | [Ethereum Foundation](https://blog.ethereum.org/2025/09/01/holesky-shutdown-announcement) | 2025-09 | 2026-09-22 | high |
| [77] | Base Sepolia faucets | [Base docs](https://docs.base.org/base-chain/network-information/network-faucets) | live | 2026-09-22 | high |
| [78] | Reown rebrand | [Reown](https://reown.com/blog/walletconnect-is-now-reown) | 2024-09 | 2026-09-22 | high |
| [79] | Expo SDK 57 | [Expo changelog](https://expo.dev/changelog/sdk-57) | 2026-06 | 2026-09-22 | high |
| [80] | EAS free plan | [Expo pricing](https://expo.dev/pricing) | live | 2026-09-22 | high |
| [81] | Internal distribution | [Expo docs](https://docs.expo.dev/build/internal-distribution/) | live | 2026-09-22 | high |
| [82] | RN New Architecture only | [React Native blog](https://reactnative.dev/blog/2025/10/08/react-native-0.82) | 2025-10 | 2026-09-22 | high |
| [83] | NativeWind v5 pre-release | [NativeWind](https://www.nativewind.dev/v5) | 2026 | 2026-09-22 | medium |
| [84] | @clerk/expo | [npm](https://www.npmjs.com/package/@clerk/clerk-expo) | 2026 | 2026-09-22 | medium |
| [85] | PostHog free tier | [PostHog](https://posthog.com/pricing) | live | 2026-09-22 | high |
| [86] | Vercel Analytics limits | [Vercel](https://vercel.com/docs/analytics/limits-and-pricing) | 2026-08 | 2026-09-22 | high |
| [87] | Stripe testing | [Stripe](https://docs.stripe.com/testing) | live | 2026-09-22 | high |
| [88] | Mapbox free tier | [Mapbox](https://www.mapbox.com/pricing) | live | 2026-09-22 | high |
| [89] | OpenFreeMap | [OpenFreeMap](https://openfreemap.org/) | live | 2026-09-22 | high |
| [90] | Resend free plan | [Resend](https://resend.com/pricing) | live | 2026-09-22 | high |
| [91] | GitHub Student Pack | [GitHub Education](https://education.github.com/pack) | live | 2026-09-22 | medium |
| [92] | Render free | [Render](https://render.com/docs/free) | live | 2026-09-22 | high |
| [93] | Railway plans | [Railway](https://docs.railway.com/reference/pricing/plans) | live | 2026-09-22 | high |
| [94] | Fly.io trial | [Fly.io](https://fly.io/docs/about/free-trial/) | live | 2026-09-22 | medium |
| [95] | Cloudflare Workers limits | [Cloudflare](https://developers.cloudflare.com/workers/platform/limits/) | 2026-09 | 2026-09-22 | high |
| [96] | Netlify credits | [Netlify](https://www.netlify.com/pricing/) | live | 2026-09-22 | high |
| [97] | HF Spaces plans | [Hugging Face](https://huggingface.co/docs/hub/spaces-overview) | live | 2026-09-22 | high |
| [98] | Streamlit Cloud sleep | [Streamlit](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app) | live | 2026-09-22 | high |
| [99] | Modal free credit | [Modal](https://modal.com/pricing) | live | 2026-09-22 | high |
| [100] | DeepSeek Harness | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 2026 | 2026-09-22 | high |
| [101] | Repo stars/push/archive for new repos | [GitHub REST API](https://api.github.com/) (`../technical-hackathon-github-repos-2026-09-21/imports/github-metrics-deepen.json`) | 2026-09-22 | 2026-09-22 | high |
| [102] | Privy free tier (MAU cap disputed) | [Privy](https://www.privy.io/pricing) | 2026 | 2026-09-22 | medium |
| [103] | MCP spec 2026-07-28 | [MCP blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/) | 2026-07-28 | 2026-09-22 | high |
| [104] | MCP Registry preview | [MCP blog](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/) | 2025-09-08 | 2026-09-22 | medium |
| [105] | Claude Code plugin marketplaces | [Anthropic](https://code.claude.com/docs/en/discover-plugins) | live | 2026-09-22 | high |
| [106] | Reference servers archived | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | live | 2026-09-22 | high |
| [107] | Chrome DevTools MCP | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | live | 2026-09-22 | high |
| [108] | Figma MCP seat requirement | [Figma](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/) | live | 2026-09-22 | medium |
| [109] | Claude plans (Code not on Free) | [Anthropic](https://claude.com/pricing) | live | 2026-09-22 | high |
| [110] | Claude Code hooks | [Anthropic](https://code.claude.com/docs/en/hooks-guide) | live | 2026-09-22 | high |
| [111] | Copilot Free | [GitHub](https://github.com/features/copilot/plans) | live | 2026-09-22 | high |
| [112] | Lovable Free | [Lovable](https://lovable.dev/pricing) | live | 2026-09-22 | high |
| [113] | Figma Starter AI credits | [Figma](https://www.figma.com/pricing/) | live | 2026-09-22 | high |
| [114] | Gemini rate limits page | [Google](https://ai.google.dev/gemini-api/docs/rate-limits) | live | 2026-09-22 | high |
| [115] | GitHub Models retired | [GitHub changelog](https://github.blog/changelog/2026-07-30-github-models-is-now-retired/) | 2026-07-30 | 2026-09-22 | high |
| [116] | Firebase Studio sunset | [Firebase](https://firebase.google.com/docs/studio/migrating-project) | 2026 | 2026-09-22 | high |
| [117] | Tool poisoning; GitHub toxic flow | [Invariant Labs](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) | 2025-04 | 2026-09-22 | high |
| [118] | postmark-mcp backdoor | [The Hacker News](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html) | 2025-09 | 2026-09-22 | high |
| [119] | MCP security best practices | [MCP spec](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices) | draft | 2026-09-22 | high |
| [120] | Claude Code security | [Anthropic](https://code.claude.com/docs/en/security) | live | 2026-09-22 | high |
| [121] | Snyk Agent Scan | [snyk/agent-scan](https://github.com/snyk/agent-scan) | live | 2026-09-22 | high |
| [122] | Repo metrics for MCP repos | [GitHub REST API](https://api.github.com/) (`../technical-hackathon-github-repos-2026-09-21/imports/github-metrics-mcp.json`) | 2026-09-22 | 2026-09-22 | high |

## Staleness map

Re-check dates come from `recon_kit.py staleness`, using the technical pack's freshness windows: versions and pricing 1 month, AI-adjacent tooling 3 months, ecosystem signals 6 months, standards and patterns 24 months.

| Claim | Class | Pub | Re-check by | Status |
| --- | --- | --- | --- | --- |
| Stitch MCP header/OAuth issue #41664 [45] | install | 2026-03 | 2026-04-01 | ⚠️ **Overdue: test live before relying on it** |
| Stitch relaunch capabilities / exports [18] | tooling | 2026-05 | 2026-08-01 | ⚠️ **Overdue: re-check** |
| Contextual-retrieval 67% gain [40] | benchmark | 2024-09 | 2024-12-01 | ⚠️ Dated vendor benchmark: the pattern holds, the number is historical |
| Next.js 16 `proxy.ts` rename [27] | version | 2026-06 | 2026-07-01 | Flagged by date; live docs (v16.3.5) confirmed it 2026-09-21 |
| Clerk JWT template deprecation [24][25] | version | 2025-04 | 2025-05-01 | Flagged by date; both vendors' live docs confirm it 2026-09-21 |
| RFC 9457 [21] | standard | 2023-07 | 2025-07-01 | Flagged by date; the RFC is still current (no successor) |
| OWASP API Top 10 2023 [32] | security | 2023 | 2025-01-01 | Flagged by date; still the latest edition per the live site |
| Supabase / Clerk free tiers [22][23] | pricing | 2026-09 | 2026-10-01 | Fresh |
| Anthropic / OpenAI / Gemini prices [34][35][36] | pricing | 2026-09 | 2026-10-01 | Fresh (Gemini promo ends 2026-12-31) |
| 21st MCP, Vercel MCP, Claude Code MCP [43][47][51] | install | 2026-09 | 2026-10-01 | Fresh |
| Impeccable counts [16] | version | 2026-09 | 2026-10-01 | Fresh |
| Claude prefill removal [38] | technique | 2026-09 | 2026-12-01 | Fresh |
| Core Web Vitals [8] | standard | 2024-10 | 2026-10-01 | Due soon |
| WCAG 2.2 [10] | standard | 2024-12 | 2026-12-01 | Fresh |
| DTCG stable [13] | standard | 2025-10 | 2027-10-01 | Fresh |
| Judging advice, rules [1][5][6] | strategy/judging | 2026 | 2027-01 → 2028-06 | Fresh; re-read each event's own rules |

**Earliest re-check:** now. The Stitch MCP items [45][18] are overdue, and the pricing and install rows all come due by **2026-10-01**. Run a *Refresh* on this folder before your next hackathon.

### Deepen 2026-09-22 additions

| Claim class | Window | Re-check by |
| --- | --- | --- |
| Free tiers and pricing for new services [58]–[63], [71]–[72], [80], [85]–[99] | 1 month | **2026-10-22** |
| Supabase grants enforcement [57] | Event date | **2026-10-30** (confirm it happened) |
| Versions: Expo SDK, Hardhat, NativeWind [74], [79], [83] | 1 month | 2026-10-22 |
| Stitch/Claude Code header bug [64] | 1 month | 2026-10-22 |
