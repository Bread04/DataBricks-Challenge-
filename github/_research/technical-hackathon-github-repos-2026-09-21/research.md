---
title: 'technical research: hackathon github repos'
type: 'technical'
topic: 'hackathon github repos'
decision: 'Which high-star, actively maintained GitHub repos to adopt as hackathon accelerators (frontend UI, backend/infra, data/ML, force-multipliers), and which popular ones to avoid'
source: 'native run'
status: complete
preset: 'standard'
validation: 'normal'
created: '2026-09-21'
updated: '2026-09-22'
claims_verified: 15
claims_unverified: 3
claims_disputed: 1
---

<!-- markdownlint-disable-next-line MD025 -->
# Technical research: hackathon GitHub repos

<!-- markdownlint-disable MD013 MD025 MD052 -->

**Decision this research serves:** which high-star, actively maintained GitHub repos to adopt as hackathon accelerators, and which popular ones to avoid.

**Deliverable:** [`../../06-repo-catalog/README.md`](../../06-repo-catalog/README.md), a catalogue of 259 recommended and 15 avoided repos with API-verified metrics (the "metrics import", `imports/github-metrics.json` [1]).

## Executive summary

**Adopt the default kit in `06-repo-catalog/README.md`:** shadcn/ui plus React Bits or Magic UI for the UI; Supabase with Better Auth and Drizzle for the backend; Vercel AI SDK or LangGraph with Ollama, MarkItDown/Docling, Firecrawl and pgvector for AI; Gradio and DuckDB/Polars for data demos. Every one is actively pushed (within the last month as of 2026-09-22) with a permissive or standard license [1].

The three findings that drive this:

1. **Popularity and activity have come apart.** 15 widely recommended repos (combined >800k stars) are archived, deprecated or stale. They include Flowise (archived [1][2]), AutoGen (maintenance mode [3]), react-beautiful-dnd [4], Lucia [5], Hugging Face TGI [1][6], Roo Code [1], localtunnel [1] and GPT4All [1]. A list built from star counts alone would steer you into dead projects.
2. **Several defaults changed hands or names in 2025–26.** Auth.js now gets only security and urgent fixes under Better Auth [7], NextUI became HeroUI [8] (the source was unreachable during the citation check; the renamed repo `heroui-inc/heroui` is confirmed by the API [1]), Framer Motion became Motion [9], shadcn/ui defaults to Base UI [10], Payload went to Figma [11], Langfuse to ClickHouse [12], and the Gemini CLI free service ended [13][14]. The GitHub API caught four repo renames that older docs don't reflect [1].
3. **The fastest-growing categories are AI-native.** React Bits out-grew shadcn/ui in 2025 [15]. AI app builders (Onlook, Dyad) were top JS risers [15], and document/web-to-LLM tools (MarkItDown 186k, Firecrawl 182k) now rival long-established libraries in stars [1].

**Biggest caveat:** stars measure attention, not fitness. Some Claude Code skill repos show 100k–290k stars [1], and third-party aggregators disagree on counts [16]. Use `06-repo-catalog/README.md`'s status column and license, not stars alone.

---

## 1. Frontend UI

- **Components:** shadcn/ui (124k) leads, with ant-design and MUI (~99k each), DaisyUI, Chakra (v3 on Ark UI), Mantine and HeroUI (30.8k) [1]. shadcn/ui switched its default primitives to Base UI in Jul 2026 [10]. NextUI is now HeroUI v3 on React Aria + Tailwind v4 [8]. Origin UI is now coss ui [17].
- **Wow factor:** React Bits was 2025's top-rising UI project (+32.8k stars; #2 overall behind n8n) [15]; Magic UI has 22k stars [1]. GSAP is reportedly fully free after the Webflow acquisition [18] (medium confidence). lottie-web is stale, so use dotLottie [1].
- **Charts:** Chart.js ranked #1 in State of JS 2025 "other tools" [19]. Recharts is described as "the most practical default" [20]. Tremor went to Vercel (components now free) but was last pushed 2025-10 [1][21].
- **Canvas, editors, flows:** tldraw (50k) needs a production license key [22]; xyflow, Tiptap and BlockNote are all active [1].
- **Design-to-code:** screenshot-to-code (79k), Onlook, Dyad and bolt.diy are active [1][15].

## 2. Backend and infra

- **BaaS:** Supabase 110k, PocketBase 61k, Appwrite 57k, Convex self-host 12k; headless CMS: Strapi 73k, Payload 44k (Figma-owned [11]), Directus 37k [1].
- **Auth:** Better Auth (30k) now maintains Auth.js, which gets only security and urgent fixes [7]. Lucia is deprecated [5]. Keycloak, Zitadel, Logto and SuperTokens are active [1].
- **ORMs:** Drizzle is overtaking Prisma for new projects [23] (medium confidence). Prisma's repo is now `prisma/orm` [1]. Turso is a beta Rust rewrite of SQLite; libSQL is the stable option [24].
- **APIs:** FastAPI 102k, NestJS 76k, Express 69k, tRPC 40k, Fastify 37k, Hono 32k [1]. Hono's npm growth reportedly rivals Fastify [25].
- **Frameworks:** RedwoodJS is now RedwoodGraphQL in maintenance mode [26]. sahat/hackathon-starter (35k) is active [1]. create-t3-app and nextjs/saas-starter were last pushed 2025-12 [1].
- **Deploy and tunnels:** Coolify 62k, Dokploy 37k, Dokku 32k [1]. localtunnel is stale; frp (109k) and cloudflared are active [1][27].
- **API clients:** Postman now requires login; Bruno and Hoppscotch are MIT alternatives [28].

## 3. Data and ML

- **Agents:** LangChain 146k, CrewAI 58k, Agno 42k, LangGraph 42k, DSPy 38k [1]. **AutoGen is in maintenance mode**, and Microsoft Agent Framework reached 1.0 in April 2026 [3].
- **Low-code:** n8n 205k, Dify 156k, Langflow 155k [1]. **Flowise is archived** [1] after Workday bought it [2].
- **Local models:** Ollama 181k, Open WebUI 152k, llama.cpp 129k [1]. GPT4All is stale (last push 2025-05) [1]. TGI is archived, with vLLM or SGLang as the replacements [1][6].
- **Ingestion:** MarkItDown 186k, Firecrawl 182k, Crawl4AI 84k, Docling 67k [1].
- **Vector and search:** Milvus 46k, Qdrant 34k, Chroma 29k, pgvector 23k, Meilisearch 59k [1]. A comparison recommends Chroma for prototyping and pgvector if you're already on Postgres [29].
- **Eval and observability:** Langfuse (acquired by ClickHouse [12]), promptfoo 25k, Opik 22k [1]. Phoenix is ELv2, not OSI open source [30]. Ragas moved to `vibrantlabsai/ragas` and was last pushed 2026-02 [1].
- **Demo UIs:** Streamlit 45k, Gradio 43k, Reflex 28k, Marimo 22k [1]. Chainlit's founders reportedly stepped back [31] (low confidence).
- **Classic ML and vision:** scikit-learn 67k, DuckDB 41k, Polars 39k, Ultralytics 61k, OpenCV 90k, ComfyUI 134k (now `Comfy-Org`) [1]. faster-whisper was last pushed 2025-11, while WhisperX is active [1].

## 4. Force-multipliers

- **AI coding agents:** OpenCode (209k, moved to `anomalyco`), Claude Code 147k, Codex 125k, OpenHands 88k, Cline 68k, Goose (now `aaif-goose`) [1][32]. **The Gemini CLI free service ended 2026-06-18** [13][14]. **Roo Code is archived** [1]. The claim that Continue is archived is **overturned**: the API shows it active [1]. Aider was last pushed 2026-05-22 [1].
- **Lists:** public-apis 482k, free-for-dev 137k, awesome-selfhosted 320k, awesome-public-datasets 79k [1]. Two famous lists (the-book-of-secret-knowledge, the-art-of-command-line) are stale [1].
- **Automation and testing:** browser-use 115k, Playwright 96k, Puppeteer 95k, Stagehand 24k; faker-js and MSW are active [1]. json-server's last push was 2026-03-23 [1].
- **Pitch tools:** Excalidraw 132k, Mermaid 90k, reveal.js 72k, Slidev 48k, VHS 20k [1]. Slidev is recommended for developer experience and Marp for simplicity [33].

---

## Cross-dimension insights

- **Acquisitions don't predict the outcome.** Payload (Figma) and Langfuse (ClickHouse) stayed open and active, while Flowise (Workday) ended up archived [1][2][11][12]. Check archive status after any acquisition rather than assuming.
- **Supabase covers three categories at once.** It appears in BaaS, auth, and vector search (pgvector) [1]. Choosing it removes three separate picks, which is why it anchors the default kit.
- **AI-native tools dominate growth in every area.** UI (React Bits, Onlook), ingestion (MarkItDown, Firecrawl) and coding agents (OpenCode, Claude Code) all show the steepest star counts or rises [1][15], so the ecosystem is moving towards AI-assisted building fastest.

## Recommendations

| # | Recommendation | Feeds | Confidence |
| --- | --- | --- | --- |
| R1 | Use the `06-repo-catalog/README.md` default kit as the starting stack | `06-repo-catalog/README.md`, `../../01-hackathon-playbook/templates/tech-stack.md` | High (API-verified activity [1]) |
| R2 | Remove Auth.js, Lucia, AutoGen, Flowise, TGI, react-beautiful-dnd, localtunnel and GPT4All from any recommendations | `06-repo-catalog/README.md` Avoid table | High [1][3][5][7] |
| R3 | Use cloudflared or frp to expose localhost to judges | `../../skills/hackathon-deployment/SKILL.md` | High [1] |
| R4 | Check archive status and license before adopting anything, and never rely on star count alone | All folders | High |

## Open questions

- **oRPC:** the correct slug couldn't be resolved (the redirect points to a 7-star repo). Check it manually.
- **GSAP "fully free"** and **Chainlit's status** rest on secondary sources. Confirm them on the vendor or GitHub pages.
- **Unresolved agent names:** "DeepSeek Harness" and "Pi" appeared in one agent ranking [32] without locatable repos.
- **Inngest self-hosting:** one source disputes it [34] and it wasn't checked further.

## Source appendix

| # | Supports | Publisher | Pub date | Accessed | Confidence |
| --- | --- | --- | --- | --- | --- |
| [1] | Stars, push dates, license, archive status, renames for 278 repos | [GitHub REST/search API](https://api.github.com/) (`imports/github-metrics.json`) | 2026-09-22 | 2026-09-22 | high |
| [2] | Workday acquires Flowise | [Workday](https://newsroom.workday.com/2025-08-14-Workday-Acquires-Flowise,-Bringing-Powerful-AI-Agent-Builder-Capabilities-to-the-Workday-Platform) | 2025-08 | 2026-09-21 | high |
| [3] | AutoGen maintenance mode; MAF 1.0 (April 2026) | [AgentMarketCap](https://agentmarketcap.ai/blog/2026/04/13/microsoft-autogen-maintenance-mode-agent-framework-sunset-2026) | 2026-04 | 2026-09-21 | high |
| [4] | react-beautiful-dnd archived | [Atlassian (GitHub)](https://github.com/atlassian/react-beautiful-dnd/issues/2672) | 2025 | 2026-09-21 | high |
| [5] | Lucia deprecated | [lucia-auth/lucia](https://github.com/lucia-auth/lucia) | 2025-03 | 2026-09-21 | high |
| [6] | TGI maintenance mode | [DEV Community](https://dev.to/sreeraj-sreenivasan/the-complete-guide-to-local-llm-inference-tools-in-july-2026-llamacpp-ollama-vllm-sglang-and-4mh1) | 2026-07 | 2026-09-21 | medium |
| [7] | Auth.js joins Better Auth | [Better Auth](https://better-auth.com/blog/authjs-joins-better-auth) | 2025-09 | 2026-09-21 | high |
| [8] | NextUI → HeroUI v3 | [InfoQ](https://www.infoq.com/news/2026/07/heroui-v3-rewrite/) | 2026-07 | 2026-09-21 | medium (HTTP 405 at citation check) |
| [9] | Framer Motion → Motion | [motion.dev](https://motion.dev/) | 2026 | 2026-09-21 | high |
| [10] | shadcn/ui Base UI default | [shadcn/ui](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default) | 2026-07 | 2026-09-21 | high |
| [11] | Figma acquires Payload | [Figma](https://www.figma.com/blog/payload-joins-figma/) | 2025-06 | 2026-09-21 | high |
| [12] | ClickHouse acquires Langfuse | [ClickHouse](https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability) | 2026-01 | 2026-09-21 | high |
| [13] | Gemini CLI shutdown | [Hacker News](https://news.ycombinator.com/item?id=48196867) | 2026-05 | 2026-09-22 | high |
| [14] | Gemini CLI → Antigravity CLI | [InventiveHQ](https://inventivehq.com/blog/gemini-cli-deprecated-antigravity-cli-migration) | 2026-06 | 2026-09-22 | high |
| [15] | 2025 rising stars (React Bits, Onlook, Dyad) | [Best of JS](https://risingstars.js.org/2025/en) | 2026-01 | 2026-09-21 | high |
| [16] | Aggregator star counts | [Leaderboarded](https://leaderboarded.com/rankings/github/top-react-ui-libraries/) | 2026-09 | 2026-09-21 | medium |
| [17] | Origin UI → coss ui | [cosscom/coss](https://github.com/cosscom/coss) | 2025-10 | 2026-09-21 | high |
| [18] | GSAP free | [Annnimate](https://annnimate.com/compare/best-animation-libraries) | 2026 | 2026-09-21 | medium |
| [19] | State of JS 2025 | [InfoQ](https://www.infoq.com/news/2026/03/state-of-js-survey-2025/) | 2026-03 | 2026-09-21 | high |
| [20] | Chart library guidance | [LogRocket](https://blog.logrocket.com/best-react-chart-libraries-2026/) | 2026 | 2026-09-21 | medium |
| [21] | Vercel acquires Tremor | [Vercel](https://vercel.com/blog/vercel-acquires-tremor) | 2025-01 | 2026-09-21 | high |
| [22] | tldraw license | [tldraw](https://tldraw.dev/community/license) | 2026 | 2026-09-21 | high |
| [23] | Drizzle vs Prisma | [MakerKit](https://makerkit.dev/blog/tutorials/drizzle-vs-prisma) | 2026 | 2026-09-21 | medium |
| [24] | Turso Rust rewrite | [OpenReplay](https://blog.openreplay.com/turso-rust-sqlite-evolution/) | 2026 | 2026-09-21 | medium |
| [25] | Hono growth | [PkgPulse](https://www.pkgpulse.com/guides/hono-vs-express-vs-fastify-vs-elysia-2026) | 2026 | 2026-09-21 | medium |
| [26] | RedwoodJS status | [Wasp](https://wasp.sh/resources/2026/09/09/redwoodjs-alternatives-2026) | 2026-09 | 2026-09-21 | high |
| [27] | Tunnel alternatives | [fxtun](https://fxtun.dev/blog/ngrok-alternatives-open-source-2026/) | 2026 | 2026-09-21 | medium |
| [28] | Bruno / Hoppscotch vs Postman | [APIScout](https://apiscout.dev/guides/bruno-vs-hoppscotch-vs-insomnia-vs-postman-2026) | 2026 | 2026-09-21 | medium |
| [29] | Vector DB fit | [Firecrawl](https://www.firecrawl.dev/blog/best-vector-databases) | 2026 | 2026-09-21 | medium |
| [30] | Phoenix license | [Inference.net](https://inference.net/content/llm-evaluation-tools-comparison/) | 2026 | 2026-09-21 | medium |
| [31] | Chainlit status | [HeyClaude](https://heyclau.de/compare/ml-app-ui-frameworks) | 2026 | 2026-09-21 | low |
| [32] | Coding-agent ranking; goose move | [goose blog](https://goose-docs.ai/blog/2026/04/07/goose-moves-to-aaif/) | 2026-04 | 2026-09-21 | high |
| [33] | Slide tools | [PkgPulse](https://www.pkgpulse.com/guides/slidev-vs-marp-vs-revealjs-code-first-presentations-2026) | 2026 | 2026-09-21 | medium |
| [34] | Inngest self-host claim | [BuildMVPFast](https://www.buildmvpfast.com/blog/inngest-vs-trigger-dev-vs-bullmq-background-jobs-nextjs-2026) | 2026 | 2026-09-21 | low |

## Staleness map

| Claim class | Window | Re-check by |
| --- | --- | --- |
| Star counts, push dates, archive status [1] | 1 month (ecosystem signals move fast) | **2026-10-22** |
| Deprecations and renames [3][5][7][8][10] | 6 months | 2027-03 |
| Acquisitions and ownership [2][11][12][21] | 12 months | 2027-09 |
| Rising-star trends [15] | Annual (next Best of JS edition) | 2027-01 |

**Earliest re-check:** 2026-10-22, for the star and activity metrics. Run a **Refresh** to re-run the API check.
