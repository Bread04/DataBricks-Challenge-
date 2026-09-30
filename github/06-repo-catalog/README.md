# 📦 06 · Hackathon Repo Catalog

<!-- markdownlint-disable MD013 -->

> 🟢 **In plain English:** a shopping list of free, ready-made code (from GitHub) you can use so you don't build everything from scratch. **Just read the "default hackathon kit" table below.** It's the short list that covers most projects. Everything else is for browsing later.
>
> **The index:** the default kit, what changed in 2025–26, and the avoid list. The **298 high-star, actively maintained GitHub repos** that speed up a hackathon, are split into each folder's `docs/repos.md` (see "Browse by folder"). There are also **18 popular ones to avoid**. Every star count, last-push date, license and archive status comes from the GitHub API (2026-09-22).
> Evidence: [`../_research/technical-hackathon-github-repos-2026-09-21/research.md`](../_research/technical-hackathon-github-repos-2026-09-21/research.md)

**Status legend:** ✅ pushed in the last 6 months · ⚠️ slowing, maintenance mode or caution (see note) · ❌ in the Avoid table. Stars are a popularity signal, not a quality guarantee: check the license and last push before building on anything.

---

## 🧰 The default hackathon kit (start here)

**Cost tags:** 🆓 free / open source · 🆓* free tier (account or limits) · 💳 trial credits only · 💰 paid. Details and a full $0 stack: [`free-ai-dev-tools.md`](../05-tools-and-mcp/docs/free-ai-dev-tools.md)

These picks are a **judgement call** based on verified activity, stars and fit with this toolkit's stack (Next.js 16 + Supabase). Everything else is in the tables below.

| Need | Pick | Alternative | Cost |
| --- | --- | --- | --- |
| UI components | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | [heroui-inc/heroui](https://github.com/heroui-inc/heroui), [mantinedev/mantine](https://github.com/mantinedev/mantine) | 🆓 |
| The "wow" moment | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits), [magicuidesign/magicui](https://github.com/magicuidesign/magicui) | [motiondivision/motion](https://github.com/motiondivision/motion), [greensock/GSAP](https://github.com/greensock/GSAP) | 🆓 |
| Charts | [recharts/recharts](https://github.com/recharts/recharts) | [apache/echarts](https://github.com/apache/echarts) (large data) | 🆓 |
| Forms + validation | [react-hook-form](https://github.com/react-hook-form/react-hook-form) + [zod](https://github.com/colinhacks/zod) | — | 🆓 |
| Server state / client state | [TanStack/query](https://github.com/TanStack/query) / [pmndrs/zustand](https://github.com/pmndrs/zustand) | [pmndrs/jotai](https://github.com/pmndrs/jotai) | 🆓 |
| Icons | [lucide-icons/lucide](https://github.com/lucide-icons/lucide) | [simple-icons](https://github.com/simple-icons/simple-icons) (brand logos) | 🆓 |
| Backend-as-a-service | [supabase/supabase](https://github.com/supabase/supabase) | [pocketbase/pocketbase](https://github.com/pocketbase/pocketbase) (single binary), [appwrite](https://github.com/appwrite/appwrite) | 🆓 OSS · 🆓* hosted |
| Auth (self-owned) | [better-auth/better-auth](https://github.com/better-auth/better-auth) | Supabase Auth / Clerk (managed) | 🆓 (Clerk/Supabase Auth 🆓*) |
| ORM | [drizzle-team/drizzle-orm](https://github.com/drizzle-team/drizzle-orm) | [prisma/orm](https://github.com/prisma/orm) | 🆓 |
| Python API | [fastapi/fastapi](https://github.com/fastapi/fastapi) | [honojs/hono](https://github.com/honojs/hono) (TypeScript, edge) | 🆓 |
| Background jobs | [triggerdotdev/trigger.dev](https://github.com/triggerdotdev/trigger.dev) | [taskforcesh/bullmq](https://github.com/taskforcesh/bullmq) | 🆓 OSS · 🆓* cloud |
| Expose localhost to judges | [cloudflare/cloudflared](https://github.com/cloudflare/cloudflared) | [fatedier/frp](https://github.com/fatedier/frp) | 🆓 |
| API testing | [usebruno/bruno](https://github.com/usebruno/bruno) | [hoppscotch/hoppscotch](https://github.com/hoppscotch/hoppscotch) | 🆓 |
| LLM app SDK | [vercel/ai](https://github.com/vercel/ai) | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) (Python) | 🆓 SDK · 💰 model API (Gemini 🆓*, Ollama 🆓) |
| Agents | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | [openai/openai-agents-python](https://github.com/openai/openai-agents-python), [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 🆓 framework · 💰 model API |
| Docs → text for RAG | [microsoft/markitdown](https://github.com/microsoft/markitdown), [docling-project/docling](https://github.com/docling-project/docling) | [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | 🆓 |
| Web → LLM-ready data | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | 🆓 OSS · 🆓* hosted |
| Vector search | [pgvector/pgvector](https://github.com/pgvector/pgvector) (in Supabase) | [chroma-core/chroma](https://github.com/chroma-core/chroma), [qdrant/qdrant](https://github.com/qdrant/qdrant) | 🆓 (pgvector in Supabase 🆓*) |
| Local models | [ollama/ollama](https://github.com/ollama/ollama) | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 🆓 |
| ML demo UI | [gradio-app/gradio](https://github.com/gradio-app/gradio) | [streamlit/streamlit](https://github.com/streamlit/streamlit) | 🆓 |
| Data wrangling | [duckdb/duckdb](https://github.com/duckdb/duckdb), [pola-rs/polars](https://github.com/pola-rs/polars) | — | 🆓 |
| Datathon / Tabular ML | [autogluon/autogluon](https://github.com/autogluon/autogluon), [catboost/catboost](https://github.com/catboost/catboost) | [microsoft/LightGBM](https://github.com/microsoft/LightGBM), [slundberg/shap](https://github.com/slundberg/shap) | 🆓 |
| Datathon starters & kit | [`08-datathon-handbook/`](../08-datathon-handbook/README.md) | [Jeremy123W/Citadel-1st-Place](https://github.com/Jeremy123W/Citadel-SoCal-Datathon-2018-1st-Place-Winners), [DataSciComp](https://github.com/iphysresearch/DataSciComp) | 🆓 |
| Vision | [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | [google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe) | 🆓 (AGPL, check license) |
| Speech-to-text | [m-bain/whisperX](https://github.com/m-bain/whisperX) | [openai/whisper](https://github.com/openai/whisper) | 🆓 |
| LLM tracing / eval | [langfuse/langfuse](https://github.com/langfuse/langfuse), [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | [comet-ml/opik](https://github.com/comet-ml/opik) | 🆓 OSS · 🆓* cloud |
| Data & API ideas | [public-apis/public-apis](https://github.com/public-apis/public-apis), [awesomedata/awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets) | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 🆓 |
| Mock data | [faker-js/faker](https://github.com/faker-js/faker) | [mswjs/msw](https://github.com/mswjs/msw) (mock APIs) | 🆓 |
| Diagrams & slides | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw), [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) | [slidevjs/slidev](https://github.com/slidevjs/slidev) | 🆓 |
| Demo recording (terminal) | [charmbracelet/vhs](https://github.com/charmbracelet/vhs) | — | 🆓 |
| Voice agent | [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat) (cascade with Claude) | [livekit/agents](https://github.com/livekit/agents); OpenAI `gpt-realtime` over WebRTC | 🆓 framework · 💳/💰 speech APIs (Deepgram $200 credit) |
| Web3 dApp | [scaffold-eth/scaffold-eth-2](https://github.com/scaffold-eth/scaffold-eth-2) (`npx create-eth@latest`) | [foundry-rs/foundry](https://github.com/foundry-rs/foundry) or [NomicFoundation/hardhat](https://github.com/NomicFoundation/hardhat) · [wevm/viem](https://github.com/wevm/viem) | 🆓 (testnet) |
| Mobile app | Expo SDK 57 + [nativewind/nativewind](https://github.com/nativewind/nativewind) v4 | [founded-labs/react-native-reusables](https://github.com/founded-labs/react-native-reusables), [tamagui/tamagui](https://github.com/tamagui/tamagui) | 🆓 (EAS Free 🆓*) |
| Analytics + errors | [PostHog/posthog](https://github.com/PostHog/posthog) (1M events/mo free) | [getsentry/sentry](https://github.com/getsentry/sentry) | 🆓* |
| Maps without a key | MapLibre + [hyperknot/openfreemap](https://github.com/hyperknot/openfreemap) | Mapbox (50K loads free) | 🆓 |

---

## 🔄 What changed in 2025–26 (why older lists are wrong)

| # | Change | Source |
| --- | --- | --- |
| F1 | shadcn/ui switched its default primitives from Radix to **Base UI** (Jul 2026); Radix is still supported | [shadcn changelog](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default) |
| F2 | **NextUI → HeroUI** (repo confirmed by the GitHub API); v3 is a rewrite on React Aria + Tailwind v4 (source unreachable at re-check) | [InfoQ, 2026-07](https://www.infoq.com/news/2026/07/heroui-v3-rewrite/) |
| F3 | **Origin UI → coss ui** (`cosscom/coss`), built on Base UI | [cosscom/coss](https://github.com/cosscom/coss) |
| F4 | GSAP is now **100% free**, including the formerly paid plugins (secondary source) | [Annnimate](https://annnimate.com/compare/best-animation-libraries) |
| F5 | tldraw SDK needs a **license key for production** (free in development) | [tldraw license](https://tldraw.dev/community/license) |
| F6 | `react-beautiful-dnd` **archived** 2025-08-18; use dnd-kit or Pragmatic drag-and-drop | [Atlassian issue](https://github.com/atlassian/react-beautiful-dnd/issues/2672) |
| F7 | Framer Motion is now **Motion** (`motion`, `motion/react`) | [motion.dev](https://motion.dev/) |
| F8 | **Auth.js/NextAuth** is maintained by the Better Auth team, with security and urgent fixes only (since 2025-09-22) | [Better Auth blog](https://better-auth.com/blog/authjs-joins-better-auth) |
| F9 | **Lucia deprecated** (Mar 2025), now a learning resource | [lucia-auth/lucia](https://github.com/lucia-auth/lucia) |
| F10 | RedwoodJS → **RedwoodGraphQL** (maintenance mode); community fork `cedarjs/cedar` | [Wasp, 2026-09](https://wasp.sh/resources/2026/09/09/redwoodjs-alternatives-2026) |
| F11 | **Figma acquired Payload** (Jun 2025); still open source | [Figma](https://www.figma.com/blog/payload-joins-figma/) |
| F12 | Drizzle is overtaking Prisma for new projects; Prisma's repo is now `prisma/orm` | [MakerKit](https://makerkit.dev/blog/tutorials/drizzle-vs-prisma) · GitHub API |
| F13 | `localtunnel` stale (last push 2025-08); use cloudflared or frp | GitHub API |
| F14 | **AutoGen in maintenance mode**; Microsoft Agent Framework 1.0 GA (April 2026) | [AgentMarketCap](https://agentmarketcap.ai/blog/2026/04/13/microsoft-autogen-maintenance-mode-agent-framework-sunset-2026) |
| F15 | **ClickHouse acquired Langfuse** (Jan 2026); still OSS and self-hostable | [ClickHouse](https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability) |
| F16 | Ragas moved to `vibrantlabsai/ragas`; last push 2026-02 | GitHub API |
| F17 | Chainlit founders stepped back; community-maintained (low-confidence source) | [HeyClaude](https://heyclau.de/compare/ml-app-ui-frameworks) |
| F18 | **Flowise archived** (GitHub API), after the Workday acquisition (2025-08-14) | [Workday](https://newsroom.workday.com/2025-08-14-Workday-Acquires-Flowise,-Bringing-Powerful-AI-Agent-Builder-Capabilities-to-the-Workday-Platform) · GitHub API |
| F19 | Hugging Face **TGI archived / maintenance mode** (2026-03-21); use vLLM or SGLang | [DEV](https://dev.to/sreeraj-sreenivasan/the-complete-guide-to-local-llm-inference-tools-in-july-2026-llamacpp-ollama-vllm-sglang-and-4mh1) · GitHub API |
| F20 | **Gemini CLI** stopped serving free/individual users 2026-06-18; replaced by closed-source Antigravity CLI | [Hacker News](https://news.ycombinator.com/item?id=48196867) · [InventiveHQ](https://inventivehq.com/blog/gemini-cli-deprecated-antigravity-cli-migration) |
| F21 | **Roo Code archived** (2026-05-15). ⚠️ Claims that *Continue* is archived are **wrong**: the GitHub API shows it active | GitHub API |
| F22 | Repo moves: `sst/opencode` → `anomalyco/opencode`, `block/goose` → `aaif-goose/goose`, `comfyanonymous/ComfyUI` → `Comfy-Org/ComfyUI` | [goose blog](https://goose-docs.ai/blog/2026/04/07/goose-moves-to-aaif/) · GitHub API |
| F23 | React Bits was 2025's top-rising UI project (+32.8k stars), ahead of shadcn/ui | [Best of JS Rising Stars 2025](https://risingstars.js.org/2025/en) |
| F24 | *(Deepen 2026-09-22)* GSAP free claim **confirmed** on gsap.com: 100% free including all plugins | [GSAP pricing](https://gsap.com/pricing/) |
| F25 | Chainlit: community-maintained since 2025-05-01; ChainLeak CVEs fixed in **2.9.4**, so pin ≥2.9.4 | [Chainlit README](https://github.com/Chainlit/chainlit) · [GHSA](https://github.com/advisories/GHSA-gm79-2pvc-wc75) |
| F26 | oRPC's repo is `middleapi/orpc`; Pi moved from `badlogic/pi-mono` to `earendil-works/pi`; DeepSeek Harness is `deepseek-ai/deepseek-harness` | GitHub API |
| F27 | WalletConnect → **Reown**; Web3Modal → **Reown AppKit**; Holesky testnet sunset (use Sepolia) | [Reown](https://reown.com/blog/walletconnect-is-now-reown) · [EF](https://blog.ethereum.org/2025/09/01/holesky-shutdown-announcement) |
| F28 | `@clerk/clerk-expo` deprecated → `@clerk/expo`; NativeWind v5 is pre-release (use v4); RN is New-Architecture-only since 0.82 | [npm](https://www.npmjs.com/package/@clerk/clerk-expo) · [RN blog](https://reactnative.dev/blog/2025/10/08/react-native-0.82) |
| F29 | Hugging Face Spaces: **Gradio/Docker now need PRO**; free accounts get 2 ZeroGPU Gradio Spaces; static stays free | [HF docs](https://huggingface.co/docs/hub/spaces-overview) |
| F30 | Vocode (voice) last pushed 2024-11, so it's stale; use Pipecat or LiveKit Agents | GitHub API |
| F31 | *(MCP run)* `modelcontextprotocol/servers` keeps only **7** reference servers; Postgres, SQLite, GitHub, Brave, Redis, Sentry, Slack and Puppeteer were **archived**, so use vendor servers | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| F32 | **GitHub Models fully retired 2026-07-30**; **Firebase Studio** closed to new users (shuts down 2027-03-22) | [GitHub changelog](https://github.blog/changelog/2026-07-30-github-models-is-now-retired/) · [Firebase](https://firebase.google.com/docs/studio/migrating-project) |
| F33 | `mcp-scan` is now **Snyk Agent Scan** (`snyk/agent-scan`); Browserbase MCP repo archived; DXT is now **MCPB** | GitHub API · [snyk/agent-scan](https://github.com/snyk/agent-scan) |
| F34 | MCP spec **2026-07-28**: stateless core; SSE, Sampling, Roots and Logging deprecated. Claude Code tool search is on by default | [MCP blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/) |

---

## 📂 Browse by folder

The full category tables now live next to the docs they support:

| Folder | Categories | File |
| --- | --- | --- |
| 🎨 Frontend | Components, animation & 3D, charts, forms & state, icons, canvas & editors, design-to-code, **mobile (React Native)**, awesome lists | [`02-frontend/docs/repos.md`](../02-frontend/docs/repos.md) |
| ⚙️ Backend | BaaS & CMS, auth, ORMs, API frameworks, starters, realtime, jobs, PaaS, tunnels, API testing, email, **Web3**, **product plumbing**, mock data & testing | [`03-backend/docs/repos.md`](../03-backend/docs/repos.md) |
| 🤖 AI & ML | **Voice & realtime**, LLM & agent frameworks, ingestion & crawling, RAG engines, vector DBs, local models, serving, low-code, demo UIs, classic ML, HF, speech & vision, eval & MLOps, datasets, browser automation | [`04-ai-and-rag/docs/repos.md`](../04-ai-and-rag/docs/repos.md) |
| 🔧 Tools | **MCP servers & registries**, AI coding agents, Claude Code skills & plugins, internal tools | [`05-tools-and-mcp/docs/repos.md`](../05-tools-and-mcp/docs/repos.md) |
| 🗺️ Playbook | Public APIs & datasets, diagrams/slides/demo recording, mega lists, hackathon-specific | [`01-hackathon-playbook/docs/repos.md`](../01-hackathon-playbook/docs/repos.md) |

## ❌ Avoid: archived, deprecated or stale

Popular repos you'll see recommended in older guides. Don't build new projects on them.

| Repo | ⭐ | Last push | Why / use instead | Area |
| --- | --- | --- | --- | --- |
| [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | 245.1k | 2024-11-19 | stale since 2024-11 | 🚀 Hackathon force-multipliers |
| [jlevy/the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line) | 162.5k | 2024-06-25 | stale since 2024-06 | 🚀 Hackathon force-multipliers |
| [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | 77.4k | 2025-05-27 | no push since 2025-05; use Ollama or Jan | 🤖 Data & ML |
| [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | 64.5k | 2026-05-31 | archived | 🚀 Hackathon force-multipliers |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 61.1k | 2026-04-15 | maintenance mode; use Microsoft Agent Framework | 🤖 Data & ML |
| [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | 55.5k | 2026-08-13 | archived (after Workday acquisition) | 🤖 Data & ML |
| [atlassian/react-beautiful-dnd](https://github.com/atlassian/react-beautiful-dnd) | 33.9k | 2025-08-18 | archived; use dnd-kit / Pragmatic DnD | 🎨 Frontend UI |
| [airbnb/lottie-web](https://github.com/airbnb/lottie-web) | 32.1k | 2025-09-01 | stale; use LottieFiles/dotlottie-web | 🎨 Frontend UI |
| [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) | 24.3k | 2026-05-15 | archived 2026-05-15; use Cline or Kilo Code | 🚀 Hackathon force-multipliers |
| [localtunnel/localtunnel](https://github.com/localtunnel/localtunnel) | 22.5k | 2025-08-29 | stale; use cloudflared or frp | ⚙️ Backend & infra |
| [huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference) | 10.9k | 2026-03-21 | archived/maintenance; use vLLM or SGLang | 🤖 Data & ML |
| [lucia-auth/lucia](https://github.com/lucia-auth/lucia) | 10.4k | 2026-08-08 | deprecated; use Better Auth | ⚙️ Backend & infra |
| [serafimcloud/21st](https://github.com/serafimcloud/21st) | 5.5k | 2025-05-28 | stale source; use the hosted 21st.dev + 21st MCP | 🎨 Frontend UI |
| [jakobhoeg/shadcn-chat](https://github.com/jakobhoeg/shadcn-chat) | 1.6k | 2025-08-12 | stale; shadcn added chat components (Jun 2026) | 🎨 Frontend UI |
| [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) | 3.4k | 2026-07-20 | archived; use Playwright MCP or Chrome DevTools MCP | 🚀 Hackathon force-multipliers |
| [modelcontextprotocol/servers-archived](https://github.com/modelcontextprotocol/servers-archived) | 303 | 2025-05-28 | archived reference servers (Postgres, SQLite, GitHub, Brave, Redis, Sentry, Slack, Puppeteer…); use vendor servers | 🚀 Hackathon force-multipliers |
| [vocodedev/vocode-core](https://github.com/vocodedev/vocode-core) | 3.8k | 2024-11-15 | stale; use Pipecat or LiveKit Agents | 🤖 Data & ML |
| [2-fly-4-ai/awesome-shadcnui](https://github.com/2-fly-4-ai/awesome-shadcnui) | 564 | 2025-06-19 | stale; use birobirobiro/awesome-shadcn-ui | 🎨 Frontend UI |

---

## 🔬 Method and caveats

- **Discovery:** 4 parallel researchers (frontend, backend, data/ML, force-multipliers) used 2025–26 sources: Best of JS Rising Stars, GitHub ranking lists, star-history, vendor docs and comparison articles.
- **Verification:** all 280 candidate slugs were checked in batches through the GitHub search API, with renamed repos resolved individually (2026-09-22). Repos whose slug resolved to the wrong project were excluded (for example oRPC's redirect).
- **Not covered:** stars are not a quality score, and a very large star count can reflect hype (some Claude Code skill repos have 100k–290k stars). "Hackathon use" lines are researcher summaries. The status notes come from the findings table above, and some are lower confidence (F4, F17).
- **Freshness:** star counts and push dates go stale within weeks. Re-run with `/bmad-deep-recon` → **Refresh** on the research folder.
