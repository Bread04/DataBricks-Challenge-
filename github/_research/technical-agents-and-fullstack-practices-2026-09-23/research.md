---
title: 'technical research: AI agents & workflows + backend/frontend practices'
type: 'technical'
topic: 'AI agents & agentic workflows; backend and frontend practices for hackathon builders'
decision: 'What to add to 04-ai-and-rag (agents doc + skills/hackathon-ai) and how to upgrade skills/hackathon-backend and skills/hackathon-frontend'
source: 'native run (web fan-out, 10 digests, 2 rounds)'
status: complete
preset: 'standard (5 subagents)'
validation: 'normal'
created: '2026-09-23'
updated: '2026-09-23'
claims_verified: 29
claims_unverified: 10
claims_disputed: 1
---

# technical research: AI agents & workflows + backend/frontend practices

<!-- markdownlint-disable MD013 -->

**Decision this research serves:** What to add to `04-ai-and-rag` (a new `docs/agents-and-tool-use.md` and a `skills/hackathon-ai` cheat sheet), and how to upgrade `skills/hackathon-backend` and `skills/hackathon-frontend`.

## Executive summary

**Do this:** teach one agent loop, not multi-agent. For TypeScript, recommend **Vercel AI SDK v7 `ToolLoopAgent`**. For Python, recommend **Pydantic AI**. For the fastest path, a plain loop over the provider SDK. Cap every loop explicitly, drop "temperature 0", and make the demo safe with recorded or cached fallbacks rather than trying to get deterministic output. On the backend, add the **Supabase GRANT** rule and a **Next.js ≥ 16.3.6** pin immediately. On the frontend, add an "AI UI" section (streaming, tool-call cards, approval prompts) built on shadcn + AI Elements.

Three findings drive that answer:

1. **The landscape has consolidated, and old tutorials are now traps.**
   - OpenAI's Assistants API shut down on 2026-08-26 [6]. AutoGen and Semantic Kernel are in maintenance mode [20].
   - AI SDK v7 renamed its core options (`stepCountIs`→`isStepCount`, `system`→`instructions`, `onFinish`→`onEnd`) and is Node 22+ and ESM-only [9].
   - MCP spec 2026-07-28 removed sessions and the `initialize` handshake [36][37].
   - Beginners copy-pasting 2025 code will hit errors, so the guide needs "old name → new name" tables.
2. **The evidence favours simple.**
   - Anthropic's pattern ladder ("start with a single call, add workflows, use agents only when steps can't be predicted") still stands [31].
   - Multi-agent systems use about 15× the tokens of chat [32] and fail when agents share context or the work is coding [32][33].
   - 2026 practitioner sentiment leans framework-free [24].
3. **Several "standard" hackathon habits are now wrong.**
   - Non-default `temperature` returns HTTP 400 on Claude Opus 4.7+ and Sonnet 5 [66]. GPT-6 models with reasoning reject it too [67].
   - New Supabase tables are not reachable without an explicit `GRANT`. This is the default for new projects since 2026-05-30 and is enforced on all projects from **2026-10-30** [74].
   - Next.js 16.2.0–16.3.5 has a critical RCE in `next/og` (CVE-2026-94545) [72][73].

**Biggest caveat:** every free-tier number here is vendor-sourced. Only Langfuse and LangSmith have a second (low-quality) confirmation. AI tooling changes monthly, and the earliest re-check dates fall in October 2026 (see the staleness map).

---

## 1. Agent frameworks & SDKs

**Landscape (Sep 2026).** Every major framework shipped a release in the ten days before this run, except smolagents (last release 2026-05-29) [21].

| Framework | Version (verified) | Lang | Licence | Model-agnostic | MCP | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Vercel AI SDK | 7.0.111 [7] | TS | Apache-2.0 | yes | yes, `@ai-sdk/mcp` [10] | active; v5/v6 still patched [7] |
| Mastra | core 1.67.0 [22] | TS | Apache-2.0 core, `ee/` source-available [22] | yes | client + server [23] | active |
| Claude Agent SDK | TS 0.3.280 [1] | TS/Py | — | Claude only | yes [1] | active, 0.x |
| OpenAI Agents SDK | Py 0.22.3 [5] | Py/TS | MIT | "provider-agnostic" [25] | yes | active, 0.x |
| Pydantic AI | 2.48.0 [14] | Py | MIT | yes | yes [14] | active |
| LangGraph / LangChain v1 | 1.2.12 [11] | Py/TS | MIT | yes | built-in `MCPAdapter` from v1.4 [13] | active |
| CrewAI | 1.15.22 [15] | Py | MIT | yes | `mcps=` [16] | active |
| Google ADK | 2.9.2 [17] | Py | Apache-2.0 | Gemini-optimised | yes [17] | active; v2 broke agent API [17] |
| MS Agent Framework | 1.19.0 [18] | Py/.NET | MIT | Azure/OpenAI-leaning | yes [19] | successor to AutoGen/SK [20] |
| smolagents | 1.26.0 [21] | Py | Apache-2.0 | yes | yes | release pace slowed (medium confidence) |

**Deprecations and consolidations.**

- OpenAI Assistants API: shut down 2026-08-26. Migrate to Responses + Conversations [6].
- OpenAI Agent Builder: discontinuation announced 2026-06-03 [6]. The Nov-30 shutdown date comes from a search snippet only (medium confidence).
- OpenAI launched a managed **Agents API** public beta on 2026-09-10 [6].
- **Claude Managed Agents** is in beta and on by default for API accounts [3]. It costs tokens plus **$0.08 per running session-hour**. The only free allowance is starter credits [4].
- AutoGen and Semantic Kernel moved into Microsoft Agent Framework (two sources) [20].

**What each is best for.**

- **Claude Agent SDK** is "Claude Code as a library": file, bash and web tools, subagents, skills and hooks. It suits agents that edit files or run code [2].
- **AI SDK v7's `ToolLoopAgent`** stops after 20 steps by default [8]. `WorkflowAgent` has no limit [8]. It also has a `HarnessAgent` that can run Claude Code or Codex [8].
- **LangChain v1 `create_agent`** runs on the LangGraph runtime and is customised through middleware [12].

**Practitioner sentiment (medium confidence, anecdotal).**

- Sep 2026 HN comments call LangChain/LiteLLM bloated. Some teams say they "code their own LLM client" [24].
- One HN team is happy with LangGraph [24].
- "Coding agents have replaced every framework I used" got 375 points (2026-02) [24].
- The rule of thumb "if the control flow fits in about 5 bullets, you don't need a framework" appears in several independent blogs (medium confidence; not in the appendix).
- The old "abstraction overhead" complaint against LangChain is only partly addressed by v1 [12][24].

**Selection matrix.**

| Situation | Pick | Why |
| --- | --- | --- |
| Next.js / TS web app | **AI SDK v7** (`ToolLoopAgent` + AI SDK UI) | model-agnostic, 20-step default cap, MCP client, approval, UI hooks [8][9][10] |
| TS, want memory/workflows built in | Mastra | MCP client/server, Apache-2.0 core [22][23] |
| Python | **Pydantic AI** | typed tools, model-agnostic, MCP [14] |
| Agent edits files / runs code | Claude Agent SDK (or OpenAI Sandbox Agents) | built-in harness [2][25] |
| Simplest possible | provider SDK + your own loop (Anthropic Tool Runner, OpenAI Responses) | Anthropic lists it as a first-class option [2][26] |
| Avoid for new builds | Assistants API, Agent Builder, AutoGen, SK | shut down or maintenance mode [6][20] |

## 2. Tools, MCP & workflow patterns

**Tool calling has converged across vendors.**

- Strict schemas: Anthropic `strict: true` [27], OpenAI strict by default in the Responses API [28], Gemini `VALIDATED` mode [29].
- Parallel calls are on by default, with a switch to disable them [26][28].
- Tool search / deferred loading for large tool sets [27][28].
- Server-side tools (web search, web fetch, code execution) need no execution code on your side and no beta header on Claude [27].

**Tool design rules (primary sources):**

- Use fewer, well-chosen tools, not one per API endpoint [30]. OpenAI suggests fewer than 20 at the start of a turn [28] (medium confidence).
- Namespace names (`asana_projects_search`) and use unambiguous parameter names [30].
- Return concise, readable output: paginate and truncate, and don't return UUIDs. Claude Code caps tool output at 25k tokens [30].
- Make error messages actionable [30].
- Use enums or poka-yoke arguments so invalid calls are hard to make [28][31].

**MCP (two sources).**

- The current spec is **2026-07-28 (final)** [35][36]. It is stateless: `Mcp-Session-Id` and the `initialize` handshake are gone. `server/discover` is new and mandatory. Tasks and MCP Apps are now extensions [37].
- Roots, Sampling, Logging and HTTP+SSE are deprecated but keep working for at least 12 months [37].
- **"It breaks old servers" is only partly true.** SDK v2 clients still talk to 2025-era servers [38][39].
- SDK status: Python SDK v2 is stable (`FastMCP` renamed `MCPServer`) [39]. TypeScript SDK v2 (`@modelcontextprotocol/server`, `@modelcontextprotocol/client`) was a beta on 2026-07-27, and its stability now is unconfirmed [38].
- The fastest beginner path is a hosted connector:
  - Anthropic `mcp_toolset`: beta `mcp-client-2025-11-20`, tools only, remote HTTP only [40].
  - OpenAI `type:"mcp"`: `require_approval` defaults to `"always"` [41].

**MCP and agent security.**

- Tool poisoning hides instructions in tool descriptions [43].
- The official best practices [42]:
  - no token passthrough
  - block SSRF to private IPs
  - show the exact command before launching a local server
  - request minimal scopes
- The spec says tool annotations are untrusted unless the server is trusted [35].
- OpenAI warns that a malicious server can exfiltrate anything in the model's context [41].
- Tie these together with the **lethal trifecta** [62]. Never combine these three in one agent:
  - private data
  - untrusted content
  - a way to send data out

**Computer and browser use.**

- Anthropic `computer_toolset_20260801` is GA. Opus 5.5 rejects the old `computer_20251124` [44], which is a trap in older tutorials.
- OpenAI computer use is GA and recommends code execution (Playwright) over the structured tool [45]. The model names in its docs are medium confidence.
- Browserbase free tier: 1 browser-hour, 15-minute sessions [46]. Stagehand is at 3.7.3 [47].
- No benchmark numbers were verified. Treat computer use as a stretch goal and prefer an API or MCP when one exists.

**A2A** is under the Linux Foundation and at v1.0 [48]. The "150+ organisations" figure is unverified. It is not worth a beginner hackathon team's time (inference).

**Patterns.**

- **The ladder:** single call + retrieval → prompt chaining → routing → parallelisation → orchestrator-workers → evaluator-optimizer → autonomous agent [31]. Use workflows when the path is predictable, and agents only when the number of steps can't be known in advance [31].
- **Frameworks:** they can hide prompts, so understand the code underneath [31].
- **Multi-agent:** Anthropic reports a 90.2% gain on its internal research eval [32] (single vendor source, medium confidence). It costs about 15× chat tokens [32] and fails on shared context and coding [32][33]. **Default to one agent. Use subagents only for independent, read-only fan-out.**
- **Context engineering:** use compaction, structured notes, just-in-time retrieval, and subagents that return summaries of about 1–2k tokens [34].
- **Human in the loop:** OpenAI's MCP tool asks for approval by default [41], and AI SDK v7 has `toolApproval` [9]. Require approval for writes, payments and messages sent on the user's behalf [42][45].

## 3. Memory, evals, observability, reliability & demo-proofing

**Memory ($0 options).**

- Keep the conversation in your own app state.
- OpenAI Agents SDK Sessions (`SQLiteSession`). Don't mix them with server-managed conversations in the same run [56].
- Anthropic memory tool (`memory_20250818`, client-side, all Claude 4+ models) [55]. Block path traversal and cap file sizes [55].
- Mem0's free tier is 1k retrievals a month (single source).
- Letta and Zep were not researched.

**Observability and tracing free tiers.**

| Tool | Free tier | Notes |
| --- | --- | --- |
| **Langfuse** | 50k units/mo, 2 users, 30 days [49] | OSS, self-hostable. Acquired by ClickHouse 2026-01-16 and stays OSS (two sources) [50][51] |
| LangSmith | 5k traces/mo, 1 seat, 14 days [52] | seat limit hurts teams |
| Braintrust | 1 GB/mo, unlimited users, 14 days [53] | |
| Helicone | — | acquired by Mintlify 2026-03-03, **maintenance mode**: don't start new projects on it [54] |

The OpenTelemetry GenAI conventions moved to their own repo, and their stability is unconfirmed. Phoenix and Weave were not researched.

**Evals in 24–48 hours.**

- Start with 20–50 tasks drawn from real failures, and grade outcomes, not tool-call paths [64].
- Use binary pass/fail, and read at least 30 traces [65].
- Validate any LLM judge against your own labels [64][65].
- Generic metrics "create false confidence" [65].
- Run multiple trials, because agents are nondeterministic [64].

**Reliability: settings to use.**

| Risk | Rule | Evidence |
| --- | --- | --- |
| Runaway loop | Always set the cap yourself: OpenAI `max_turns` (default 10, raises `MaxTurnsExceeded`, can be caught with a `"max_turns"` handler); AI SDK `stopWhen` (`ToolLoopAgent` default 20; `WorkflowAgent` has none); Anthropic tool runner `max_iterations` | [57][56][8][55] |
| 429 / 529 | The SDKs retry twice with backoff [58]. A **spend-cap 429 never recovers**, so a spend cap works as a budget kill-switch [58] | [58] |
| Serverless timeout | Vercel Hobby functions stop at **300 s including streaming** (504), with a 4.5 MB body limit [61]. Split long runs into steps or move them to Vercel Workflows (GA) [86] | [61][86] |
| Cost | Put stable system prompts and tools first so they get cached. Anthropic cache reads cost 0.1× (0.05× on Opus 5.5), with a 5-minute default TTL; the 1-hour TTL write costs 2× [59]. OpenAI caching is automatic: reads 0.1×, 30-minute retention on GPT-5.6+ [60] | [59][60] |
| Nondeterminism | **Don't set temperature.** Non-default values return 400 on Claude Opus 4.7+ and Sonnet 5, and temperature 0 "never guaranteed identical outputs" [66]. GPT-6 models with reasoning also reject it [67] | [66][67] |
| Long requests | Stream. The SDKs refuse non-streaming requests expected to run past 10 minutes [58] | [58] |

**Security.** The lethal trifecta [62] and the OWASP Top 10 for Agentic Applications 2026 (published 2025-12-09, ASI01–ASI10; list taken from a summary, medium confidence) [63].

**Demo-proofing.**

- Devpost advises recording a backup video early, because uploads can take hours [68] (medium confidence).
- JetBrains' judges say: show something working within about 90 seconds, keep to one flow, and "mock everything you can" [69].
- MLH's organiser guide treats venue Wi-Fi as a risk [MLH organiser guide; low-medium, not in the appendix].
- Since sampling parameters are out (see above), make the demo reliable with **golden or cached responses, seeded data, and a recorded fallback**.

## 4. Backend practices

**Currency check against the current cheat sheet:**

| Cheat-sheet item | Verdict |
| --- | --- |
| Next.js 16 / `proxy.ts` | ✅ current. Now **16.3.x; pin ≥ 16.3.6**. GHSA-vcvr-r3jv-pc5j / CVE-2026-94545 (CVSS 9.5) affects the Node `ImageResponse` in `>=16.2.0 <16.3.6` when user input reaches the SVG. Edge is unaffected [71][72][73]. 15.x: use 15.5.26 [73]. Multiple critical advisories in the past year [70] |
| Cache model | "Cache Components" + `use cache` is the 16.x model. 16.3 adds Instant Navigations and `catchError`/`retry()` [70] |
| Supabase RLS | ⚠️ **changed.** Tables also need an explicit `GRANT` to `anon`, `authenticated` and `service_role`. Default for new projects from 2026-05-30, all projects from **2026-10-30**. Otherwise you get "permission denied for table" [74] |
| Supabase keys | ⚠️ **changed.** `anon`/`service_role` are deprecated "by end of 2026". Use `sb_publishable_…` / `sb_secret_…`. The env var is now `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY` [75][76] |
| `getClaims()` | ✅ still the recommended server check [76] |
| Clerk via Third-Party Auth | ✅ recommended. The JWT template has been deprecated since 2025-04-01 [77] |
| Free tiers | Supabase: 2 projects, 500 MB, 50k MAU, pauses after 1 week [78]. Clerk: 50k MRU, **no MFA/passkeys** [79] |
| Upstash | ⚠️ free tier is **500K commands per month** (not per day), 256 MB [92] |
| Zod | ✅ v4 (4.6.5) [96] |
| OWASP API Top 10 2023 | ✅ still the latest API edition. The 2025 list is the separate web-app Top 10 (medium confidence) |

**Missing practices worth adding:**

- **Env validation:** `@t3-oss/env-nextjs`. Import it in `next.config.ts` so a missing variable fails the build instead of production [91].
- **Serverless Postgres:** use the Supabase transaction pooler on :6543 with prepared statements disabled. Direct :5432 connections are IPv6 [80].
- **Background jobs:** Vercel Workflows (GA 2026-04-16; Hobby includes 50k events/month and keeps run state for 1 day) [86][87]. Inngest is free for 50k executions [89]. Trigger.dev v4 has a $5 credit [90]. Vercel Queues is still beta, so avoid it [88].
- **Auth alternatives:** Better Auth, which Vercel acquired on 2026-07-07 (still MIT) [81][82], now maintains Auth.js and tells new projects to use Better Auth [83].
- **ORM:** Prisma 7 dropped the Rust engine, so the old "heavy on serverless" advice is outdated [84].
- **Email:** Resend's free tier has a **100 emails/day** cap [93].
- **Alternatives:** Neon (100 CU-hours, 0.5 GB per project) [94]. Convex (1M function calls/month; medium confidence) [95].
- **Python path:** `uv add "fastapi[standard]"` + `fastapi dev`. FastAPI is at 0.141.1 [85].

Not researched: webhook signature verification, Supabase signed upload URLs, Stripe sandboxes, Firebase/Cloudflare free tiers, CORS (see open questions).

## 5. Frontend practices

**Currency check:**

| Cheat-sheet item | Verdict |
| --- | --- |
| Tailwind v4 `@theme` | ✅ v4.3.3, no v5 [98]. Tailwind Labs joined Shopify 2026-09-09. It stays MIT and "nothing changes"; Tailwind Plus and ui.sh are closed to new sign-ups [97] |
| shadcn: Base UI default (Jul 2026) | ✅ Radix is still supported [99]. ⚠️ The CLI is **v4** with `--base`, not 3.x [100]. React Aria is now a third option. Chat components (Jun), Human-in-the-Loop AI SDK helpers (Aug), and `cn` in its own package (Sep) [101] |
| Next.js / React Compiler | 16.3 (2026-08-03). The React Compiler is stable but opt-in. `next dev` writes an `AGENTS.md` for coding agents [70] |
| Impeccable | ✅ `npx impeccable install`, 24 commands, a no-LLM detector CLI, Apache-2.0 [103] |
| Anthropic frontend-design skill | ✅ still present. Make deliberate, brief-specific choices and avoid AI-default clusters [123] |
| Stitch MCP | ✅ an official Google codelab exists (API key, Antigravity MCP store) [113]. The `npx @google/stitch-mcp` command comes from blogs only (low confidence) |
| WCAG 2.2 / Core Web Vitals | not re-checked this run. They're stable standards verified in the 2026-09-21 run |

**Missing practices worth adding:**

- **AI-feature UI.**
  - Libraries: AI SDK UI (`useChat`, generative UI mapping tool results to components) [105], **AI Elements** (shadcn-based conversation, streaming, tool-call and reasoning components) [104], and shadcn's own chat and approval helpers [101].
  - AG-UI / CopilotKit are for a backend running a separate agent framework [106].
  - Make streaming states, tool-call progress cards, approval prompts, and error or empty states explicit requirements.
- **2026 defaults** (npm-verified): TanStack Query 5.103 [116], Zustand 5.0 [117], React Hook Form 7.88 + resolvers 5.9 [118], TanStack Form 1.33 stable [119], Motion 13.4 [114]. Zod v4 support in the form libraries is inferred, not verified.
- **Motion accessibility:** use `<MotionConfig reducedMotion="user">` [115]. Same-document View Transitions are Baseline. Cross-document ones don't work in Firefox [107].
- **Accessibility test:** `@axe-core/playwright` 4.13 in a smoke test [120]. Lighthouse CI hasn't had a release since 2025-06, so it's stale [121].
- **The EAA** covers commercial products and services such as e-commerce and banking [122]. Microenterprises providing services are exempt (law-firm summary). Hackathon prototypes are practically out of scope (inference).
- **AI app-builder free tiers are tight** (vendor pages, medium confidence), so spread your prompts across tools and teammates' accounts:
  - v0: $5/month plus 7 messages a day [108]
  - Lovable: 5 credits a day, 30 a month [109]
  - Bolt: 300K tokens a day [110]
  - Figma: 500 AI credits a month, and one Make generation can use 100+ [111]
  - 21st.dev Hobby: 2 copies a day, with AI features from $15 a month [112]
- **Judges:** one working flow, clean rather than elaborate [69]. A single-reviewer post says elaborate UI makes judges "wonder where the backend time went" [124] (low confidence).

---

## Cross-dimension insights

1. **Version drift is the single biggest risk for beginners, and it cuts across all five topics.**
   - AI SDK v6→v7 renames [9]
   - MCP 2025→2026 spec [37]
   - `computer_20251124` rejected on Opus 5.5 [44]
   - shadcn CLI 3→4 [100]
   - Supabase anon→publishable keys [75]
   - LangChain `langchain-mcp-adapters` → `MCPAdapter` [13]

   Every guide file should carry a short "if a tutorial says X, use Y" table and a "check the date on the tutorial" rule.
2. **"Deterministic demos" has to move from model settings to the app.** Temperature is gone [66][67] and agents are nondeterministic [64]. So demo safety now comes from backend and frontend engineering: cached or golden responses, seeded data, a recorded video [68], and error/loading states in the UI [70].
3. **Vercel's platform limits shape agent design.** The 300 s Hobby cap [61] means any agent loop longer than a few tool calls needs streaming plus Workflows [86]. That ties the agents doc to the deployment cheat sheet.
4. **Approval UIs are now a standard feature across the stack.** OpenAI MCP approval defaults to on [41], AI SDK v7 has `toolApproval` [9], and shadcn ships Human-in-the-Loop helpers [101]. The security advice (a human approves destructive actions) now costs almost nothing to build.

## Recommendations

| # | Recommendation | Feeds | Confidence basis |
| --- | --- | --- | --- |
| R1 | Create `04-ai-and-rag/docs/agents-and-tool-use.md`: pattern ladder, one-agent default, selection matrix (§1), tool design rules, MCP 2026-07-28 notes, reliability table, lethal trifecta, v6→v7 rename table | new doc | high: primary docs, two-source on spec and deprecations |
| R2 | Create `skills/hackathon-ai/SKILL.md`: a one-page version of R1 plus "don't use outdated patterns" (Assistants API, temperature 0, `stepCountIs`, `computer_20251124`, `FastMCP`, Helicone) | new skill | high |
| R3 | Backend skill: add the GRANT block, `sb_publishable_` keys, `next ≥ 16.3.6` pin, t3-env, pooler :6543, Upstash 500K/**month**, Resend 100/day, Workflows for long jobs, Better Auth alternative | `skills/hackathon-backend` + `03-backend/docs` | high: primary docs plus a two-source security advisory |
| R4 | Frontend skill: fix the shadcn CLI v4 line; add an "AI UI" block (AI Elements, streaming, tool cards, approvals); add Motion reduced-motion, axe-playwright, the free-tier budget note, and the Tailwind/Shopify "no action needed" note | `skills/hackathon-frontend` + `02-frontend/docs` | high on versions; medium on free tiers (vendor-only) |
| R5 | Add PROMPTS-ML macros: "scaffold ToolLoopAgent with cap + approval", "wrap tool errors", "demo fallback cache" | `04-ai-and-rag/PROMPTS-ML.md` | medium: synthesis of the above |
| R6 | Search the whole guide for "temperature 0", `langchain-mcp-adapters`, `stepCountIs`, `_ANON_KEY` and "shadcn CLI 3", and replace them | all folders | high |

## Open questions

- **Hackathon-specific framework evidence:** which frameworks 2026 winning projects actually use. Would need a Devpost gallery crawl.
- **Stability of MCP TS SDK v2:** check the GitHub releases.
- **Unresearched backend topics:** webhook verification (Stripe, Clerk/svix), Supabase signed upload URLs, Stripe sandboxes, Firebase and Cloudflare free tiers, CORS. One more backend round would cover them.
- **Unresearched tools:** Arize Phoenix, W&B Weave, Letta, Zep, and OTel GenAI stability.
- **Unverified numbers:** browser-agent benchmarks (OSWorld/WebArena) and the A2A organisation count.
- **Framework defaults:** the default `stopWhen` for bare `generateText` in AI SDK v7, and confirmation of Zod v4 support in React Hook Form and TanStack Form.

---

## Source appendix

| # | Supports | Publisher | Pub date | Accessed | Confidence |
| --- | --- | --- | --- | --- | --- |
| [1] | Claude Agent SDK TS 0.3.280; MCP features | [Anthropic GitHub](https://github.com/anthropics/claude-agent-sdk-typescript/releases) | 2026-09-22 | 2026-09-23 | high |
| [2] | Agent SDK = Claude Code as a library; SDK comparison | [Anthropic docs](https://code.claude.com/docs/en/agent-sdk/overview) | live | 2026-09-23 | high |
| [3] | Claude Managed Agents beta | [Anthropic docs](https://platform.claude.com/docs/en/managed-agents/overview) | live | 2026-09-23 | high |
| [4] | Managed Agents $0.08/session-hr | [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing) | live | 2026-09-23 | high |
| [5] | OpenAI Agents SDK Py 0.22.3 | [OpenAI GitHub](https://github.com/openai/openai-agents-python/releases) | 2026-09-17 | 2026-09-23 | high |
| [6] | Assistants shutdown; Agent Builder; Agents API beta | [OpenAI changelog](https://developers.openai.com/api/docs/changelog) | 2026-06 to 09 | 2026-09-23 | high |
| [7] | AI SDK 7.0.111 | [Vercel GitHub](https://github.com/vercel/ai/releases) | 2026-09-22 | 2026-09-23 | high |
| [8] | ToolLoopAgent, 20-step default, HarnessAgent | [AI SDK docs](https://ai-sdk.dev/docs/agents/loop-control) | live | 2026-09-23 | high |
| [9] | v6→v7 renames, Node 22, ESM, toolApproval | [AI SDK migration guide](https://ai-sdk.dev/docs/migration-guides/migration-guide-7-0) | undated | 2026-09-23 | high |
| [10] | AI SDK MCP client | [AI SDK docs](https://ai-sdk.dev/docs/ai-sdk-core/mcp-tools) | live | 2026-09-23 | high |
| [11] | LangGraph 1.2.12 | [PyPI](https://pypi.org/project/langgraph/) | 2026-09-21 | 2026-09-23 | high |
| [12] | LangChain v1 create_agent on LangGraph | [LangChain docs](https://docs.langchain.com/oss/python/langchain/agents) | live | 2026-09-23 | high |
| [13] | LangChain built-in MCPAdapter from v1.4 | [LangChain docs](https://docs.langchain.com/oss/python/langchain/mcp) | live | 2026-09-23 | medium (single source) |
| [14] | Pydantic AI 2.48.0, MCP, model-agnostic | [PyPI](https://pypi.org/project/pydantic-ai/) | 2026-09-23 | 2026-09-23 | high |
| [15] | CrewAI 1.15.22 | [PyPI](https://pypi.org/project/crewai/) | 2026-09-16 | 2026-09-23 | high |
| [16] | CrewAI MCP support | [CrewAI docs](https://docs.crewai.com/en/mcp/overview) | live | 2026-09-23 | high |
| [17] | Google ADK 2.9.2 | [PyPI](https://pypi.org/project/google-adk/) | 2026-09-18 | 2026-09-23 | high |
| [18] | MS Agent Framework 1.19.0 | [PyPI](https://pypi.org/project/agent-framework/) | 2026-09-18 | 2026-09-23 | high |
| [19] | MS Agent Framework MCP | [Microsoft Learn](https://learn.microsoft.com/en-us/agent-framework/agents/tools/local-mcp-tools) | 2026-09-16 | 2026-09-23 | high |
| [20] | AutoGen/SK maintenance mode | [Microsoft GitHub](https://github.com/microsoft/autogen) · [VentureBeat](https://venturebeat.com/ai/microsoft-retires-autogen-and-debuts-agent-framework-to-unify-and-govern) | 2025-10 | 2026-09-23 | high |
| [21] | smolagents 1.26.0, release pace | [PyPI](https://pypi.org/project/smolagents/) | 2026-05-29 | 2026-09-23 | high / medium |
| [22] | Mastra 1.67.0, licence | [Mastra GitHub](https://github.com/mastra-ai/mastra) | 2026-09-15 | 2026-09-23 | high |
| [23] | Mastra MCP | [Mastra docs](https://mastra.ai/docs/mcp/overview) | live | 2026-09-23 | high |
| [24] | HN practitioner sentiment | [Hacker News (Algolia)](https://hn.algolia.com/api/v1/search?query=langchain&tags=comment) | 2026-02 to 09 | 2026-09-23 | medium |
| [25] | OpenAI Agents SDK TS features | [OpenAI GitHub](https://github.com/openai/openai-agents-js) | live | 2026-09-23 | high |
| [26] | Claude client vs server tools, parallel calls | [Anthropic docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) | live | 2026-09-23 | high |
| [27] | strict, tool search, server tools | [Anthropic docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference) | live | 2026-09-23 | high |
| [28] | OpenAI strict mode, fewer than 20 tools | [OpenAI docs](https://developers.openai.com/api/docs/guides/function-calling) | live | 2026-09-23 | medium |
| [29] | Gemini function-calling modes | [Google AI docs](https://ai.google.dev/gemini-api/docs/function-calling) | live | 2026-09-23 | medium |
| [30] | Tool design rules | [Anthropic Engineering](https://www.anthropic.com/engineering/writing-tools-for-agents) | 2025-09-11 | 2026-09-23 | high |
| [31] | Six patterns; start simple | [Anthropic Engineering](https://www.anthropic.com/engineering/building-effective-agents) | 2024-12-19 | 2026-09-23 | high |
| [32] | Multi-agent 90.2%, 15× tokens, poor fit | [Anthropic Engineering](https://www.anthropic.com/engineering/multi-agent-research-system) | 2025-06-13 | 2026-09-23 | medium / high |
| [33] | Don't build multi-agents | [Cognition](https://cognition.com/blog/dont-build-multi-agents) | 2025-06-12 | 2026-09-23 | high |
| [34] | Context engineering | [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | 2025-09-29 | 2026-09-23 | high |
| [35] | MCP spec 2026-07-28; annotations untrusted | [MCP spec](https://modelcontextprotocol.io/specification/) | 2026-07-28 | 2026-09-23 | high |
| [36] | MCP 2026-07-28 release post | [MCP blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/) | 2026-07-28 | 2026-09-23 | high |
| [37] | MCP changelog, deprecations, back-compat | [MCP spec changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) | 2026-07-28 | 2026-09-23 | high |
| [38] | MCP TS SDK v2 beta | [MCP GitHub](https://github.com/modelcontextprotocol/typescript-sdk/releases) | 2026-07-27 | 2026-09-23 | medium |
| [39] | MCP Python SDK v2 stable | [MCP GitHub](https://github.com/modelcontextprotocol/python-sdk/releases) | ~2026-09 | 2026-09-23 | medium-high |
| [40] | Anthropic MCP connector beta | [Anthropic docs](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector) | live | 2026-09-23 | high |
| [41] | OpenAI remote MCP, approval default | [OpenAI docs](https://developers.openai.com/api/docs/guides/tools-connectors-mcp) | live | 2026-09-23 | high |
| [42] | MCP security best practices | [MCP docs](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) | live | 2026-09-23 | high |
| [43] | Tool poisoning | [Invariant Labs](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) | 2025-04-01 | 2026-09-23 | high |
| [44] | computer_toolset_20260801 GA | [Anthropic docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) | live | 2026-09-23 | high |
| [45] | OpenAI computer use GA | [OpenAI docs](https://developers.openai.com/api/docs/guides/tools-computer-use) | live | 2026-09-23 | medium |
| [46] | Browserbase free tier | [Browserbase](https://www.browserbase.com/pricing) | live | 2026-09-23 | medium-high |
| [47] | Stagehand 3.7.3 | [Browserbase GitHub](https://github.com/browserbase/stagehand/releases) | ~2026-08 | 2026-09-23 | medium |
| [48] | A2A under LF, v1.0 | [A2A project](https://a2a-protocol.org/latest/) | live | 2026-09-23 | medium-high |
| [49] | Langfuse free tier | [Langfuse](https://langfuse.com/pricing) | live | 2026-09-23 | high (vendor) |
| [50] | ClickHouse acquires Langfuse | [ClickHouse](https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability) | 2026-01-16 | 2026-09-23 | high |
| [51] | Langfuse acquisition (independent) | [InfoWorld](https://www.infoworld.com/article/4118621/clickhouse-buys-langfuse-as-data-platforms-race-to-own-the-ai-feedback-loop.html) | 2026-01 | 2026-09-23 | high |
| [52] | LangSmith free tier | [LangChain](https://www.langchain.com/pricing) | live | 2026-09-23 | high (vendor) |
| [53] | Braintrust free tier | [Braintrust](https://www.braintrust.dev/pricing) | live | 2026-09-23 | high (vendor) |
| [54] | Helicone acquired, maintenance mode | [Mintlify](https://www.mintlify.com/blog/mintlify-acquires-helicone) | 2026-03-03 | 2026-09-23 | high |
| [55] | Anthropic memory tool; max_iterations | [Anthropic docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) | live | 2026-09-23 | high |
| [56] | OpenAI Agents memory modes; max_turns handler | [OpenAI docs](https://openai.github.io/openai-agents-python/running_agents/) | live | 2026-09-23 | high |
| [57] | DEFAULT_MAX_TURNS = 10 | [OpenAI source](https://raw.githubusercontent.com/openai/openai-agents-python/main/src/agents/run_config.py) | main | 2026-09-23 | high |
| [58] | 429/529, retries, spend cap, streaming | [Anthropic docs](https://platform.claude.com/docs/en/api/errors) | live | 2026-09-23 | high |
| [59] | Anthropic prompt caching prices/TTL | [Anthropic docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) | live | 2026-09-23 | high |
| [60] | OpenAI prompt caching | [OpenAI docs](https://developers.openai.com/api/docs/guides/prompt-caching) | live | 2026-09-23 | high |
| [61] | Vercel 300 s / 4.5 MB | [Vercel docs](https://vercel.com/docs/functions/limitations) | 2026-08-24 | 2026-09-23 | high |
| [62] | Lethal trifecta | [Simon Willison](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) | 2025-06-16 | 2026-09-23 | high |
| [63] | OWASP Agentic Top 10 2026 | [OWASP GenAI](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | 2025-12-09 | 2026-09-23 | medium |
| [64] | Agent eval practice | [Anthropic Engineering](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | 2026-01-09 | 2026-09-23 | high |
| [65] | Evals FAQ | [Hamel Husain](https://hamel.dev/blog/posts/evals-faq/) | 2026-09-18 | 2026-09-23 | high |
| [66] | Temperature 400 on Opus 4.7+ / Sonnet 5 | [Anthropic docs](https://platform.claude.com/docs/en/models/opus-5/migration-guide) | live | 2026-09-23 | high |
| [67] | GPT-6 remove temperature with reasoning | [OpenAI docs](https://developers.openai.com/api/docs/guides/latest-model) | live | 2026-09-23 | high |
| [68] | Backup demo video | [Devpost](https://info.devpost.com/blog/how-to-present-a-successful-hackathon-demo) | undated | 2026-09-23 | medium |
| [69] | Judges: 90 s, one flow, mock everything | [JetBrains Blog](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/) | 2026-06 | 2026-09-23 | high |
| [70] | Next.js 16.3 features; security history | [Next.js blog](https://nextjs.org/blog/next-16-3) | 2026-08-03 | 2026-09-23 | high |
| [71] | 16.3.6 out-of-band release | [Next.js blog](https://nextjs.org/blog/nextjs-security-update-september-22-2026) | 2026-09-22 | 2026-09-23 | high |
| [72] | GHSA-vcvr-r3jv-pc5j / CVE-2026-94545 | [GitHub Advisory](https://github.com/vercel/next.js/security/advisories/GHSA-vcvr-r3jv-pc5j) | 2026-09-22 | 2026-09-23 | high |
| [73] | Same advisory (independent) | [Netlify changelog](https://www.netlify.com/changelog/2026-09-22-nextjs-imageresponse-vulnerability/) | 2026-09-22 | 2026-09-23 | high |
| [74] | Supabase explicit GRANT breaking change | [Supabase changelog](https://supabase.com/changelog/45329-breaking-change-tables-not-exposed-to-data-and-graphql-api-automatically) | 2026-04/05 | 2026-09-23 | high |
| [75] | anon/service_role deprecation | [Supabase docs](https://supabase.com/docs/guides/getting-started/migrating-to-new-api-keys) | live | 2026-09-23 | high |
| [76] | getClaims(); publishable env var | [Supabase docs](https://supabase.com/docs/guides/auth/server-side/nextjs) | live | 2026-09-23 | high |
| [77] | Clerk native Supabase integration | [Clerk docs](https://clerk.com/docs/integrations/databases/supabase) | live | 2026-09-23 | high |
| [78] | Supabase free tier | [Supabase](https://supabase.com/pricing) | live | 2026-09-23 | high (vendor) |
| [79] | Clerk free tier | [Clerk](https://clerk.com/pricing) | live | 2026-09-23 | high (vendor) |
| [80] | Pooler :6543, prepared statements | [Supabase docs](https://supabase.com/docs/guides/database/connecting-to-postgres) | live | 2026-09-23 | high |
| [81] | Better Auth joins Vercel | [Better Auth](https://better-auth.com/blog/better-auth-joins-vercel) | 2026-07-07 | 2026-09-23 | high |
| [82] | Vercel acquires Better Auth | [Vercel](https://vercel.com/blog/vercel-acquires-better-auth) | 2026-07-07 | 2026-09-23 | high |
| [83] | Auth.js maintained by Better Auth | [Better Auth](https://better-auth.com/blog/authjs-joins-better-auth) | 2025 | 2026-09-23 | high |
| [84] | Prisma 7 Rust-free | [Prisma changelog](https://www.prisma.io/changelog/2025-11-19) | 2025-11-19 | 2026-09-23 | high |
| [85] | FastAPI 0.141.1 | [PyPI](https://pypi.org/project/fastapi/) | 2026-07-29 | 2026-09-23 | high |
| [86] | Vercel Workflows GA | [Vercel docs](https://vercel.com/docs/workflows) | 2026-09-04 | 2026-09-23 | high |
| [87] | Workflows Hobby limits | [Vercel docs](https://vercel.com/docs/workflows/pricing) | 2026-09-16 | 2026-09-23 | high |
| [88] | Vercel Queues beta | [Vercel docs](https://vercel.com/docs/queues) | 2026-09-03 | 2026-09-23 | high |
| [89] | Inngest free tier | [Inngest](https://www.inngest.com/pricing) | live | 2026-09-23 | high (vendor) |
| [90] | Trigger.dev free tier, v4 | [Trigger.dev](https://trigger.dev/pricing) | live | 2026-09-23 | medium-high |
| [91] | t3-env build-time validation | [T3 OSS](https://env.t3.gg/docs/nextjs) | live | 2026-09-23 | high |
| [92] | Upstash 500K/month | [Upstash](https://upstash.com/pricing/redis) | live | 2026-09-23 | high (vendor) |
| [93] | Resend 3K/month, 100/day | [Resend](https://resend.com/pricing) | live | 2026-09-23 | high (vendor) |
| [94] | Neon free tier | [Neon](https://neon.com/pricing) | live | 2026-09-23 | high (vendor) |
| [95] | Convex free tier | [Convex](https://www.convex.dev/pricing) | live | 2026-09-23 | medium |
| [96] | Zod 4.6.5 | [npm](https://registry.npmjs.org/zod) | 2026-09-13 | 2026-09-23 | high |
| [97] | Tailwind joins Shopify, MIT forever | [Tailwind Labs](https://tailwindcss.com/blog/tailwind-is-joining-shopify) | 2026-09-09 | 2026-09-23 | high |
| [98] | Tailwind v4.3.3 | [Tailwind blog](https://tailwindcss.com/blog) | 2026-07 | 2026-09-23 | medium-high |
| [99] | shadcn Base UI default | [shadcn changelog](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default) | 2026-07 | 2026-09-23 | high |
| [100] | shadcn CLI v4 | [shadcn changelog](https://ui.shadcn.com/docs/changelog/2026-03-cli-v4) | 2026-03 | 2026-09-23 | high |
| [101] | shadcn chat, HITL helpers, cn package | [shadcn changelog](https://ui.shadcn.com/docs/changelog) | 2026-09 | 2026-09-23 | high |
| [103] | Impeccable | [GitHub pbakaus](https://github.com/pbakaus/impeccable) | live | 2026-09-23 | high |
| [104] | AI Elements | [Vercel](https://elements.ai-sdk.dev/) | live | 2026-09-23 | high |
| [105] | AI SDK UI generative UI | [AI SDK docs](https://ai-sdk.dev/docs/ai-sdk-ui/generative-user-interfaces) | live | 2026-09-23 | high |
| [106] | AG-UI protocol | [AG-UI docs](https://docs.ag-ui.com/) | 2026 | 2026-09-23 | medium-high |
| [107] | View Transitions Baseline | [web.dev](https://web.dev/blog/same-document-view-transitions-are-now-baseline-newly-available) | 2025-10 | 2026-09-23 | high |
| [108] | v0 free tier | [v0](https://v0.app/pricing) | live | 2026-09-23 | high |
| [109] | Lovable free tier | [Lovable](https://lovable.dev/pricing) | live | 2026-09-23 | medium |
| [110] | Bolt free tier | [Bolt](https://bolt.new/pricing) | live | 2026-09-23 | medium |
| [111] | Figma AI credits | [Figma Help](https://help.figma.com/hc/en-us/articles/35865276858647-Manage-AI-credits) | undated | 2026-09-23 | medium |
| [112] | 21st.dev pricing | [21st.dev](https://21st.dev/pricing) | live | 2026-09-23 | medium |
| [113] | Stitch MCP codelab | [Google Codelabs](https://codelabs.developers.google.com/design-to-code-with-antigravity-stitch) | undated | 2026-09-23 | medium |
| [114] | motion 13.4.1 | [npm](https://registry.npmjs.org/motion) | 2026-09-22 | 2026-09-23 | high |
| [115] | Motion reduced motion | [Motion docs](https://motion.dev/docs/react-accessibility) | undated | 2026-09-23 | high |
| [116] | TanStack Query 5.103.2 | [npm](https://registry.npmjs.org/@tanstack/react-query) | 2026-09-21 | 2026-09-23 | high |
| [117] | Zustand 5.0.15 | [npm](https://registry.npmjs.org/zustand) | 2026-08-13 | 2026-09-23 | high |
| [118] | React Hook Form 7.88.0 | [npm](https://registry.npmjs.org/react-hook-form) | 2026-09-11 | 2026-09-23 | high |
| [119] | TanStack Form 1.33.5 | [npm](https://registry.npmjs.org/@tanstack/react-form) | 2026-08-11 | 2026-09-23 | high |
| [120] | @axe-core/playwright 4.13.0 | [npm](https://registry.npmjs.org/@axe-core/playwright) | 2026-08-11 | 2026-09-23 | high |
| [121] | Lighthouse CI stale | [npm](https://registry.npmjs.org/@lhci/cli) | 2025-06-25 | 2026-09-23 | high |
| [122] | EAA scope | [European Commission](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en) | undated | 2026-09-23 | high |
| [123] | Anthropic frontend-design skill | [Anthropic GitHub](https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md) | live | 2026-09-23 | high |
| [124] | Judge: elaborate UI adds nothing | [DEV Community](https://dev.to/kurbaitaev/what-judges-actually-score-notes-from-a-year-of-hackathon-judging-3p4l) | 2026 | 2026-09-23 | low |

## Staleness map

Computed with `recon_kit.py staleness` (`imports/claims.json` → `imports/staleness.json`). Windows in months: version 1 · status 3 · pricing 3 · ecosystem 6 · pattern and performance 24.

> The script flags 10 claims as "stale", but all 10 are **dated events** (for example "Helicone was acquired on 2026-03-03" or "Lighthouse CI's last release was 2025-06"). They were re-confirmed live on 2026-09-23, so the old date is part of the fact, not a sign the claim is out of date. Their real re-check date is the access date plus the window.

| Re-check by | Claims |
| --- | --- |
| **2026-10-23** (version, 1 mo) | AI SDK v7 version, renames and the 20-step default [7][8][9] · Pydantic AI [14] · MCP spec, SDK status and connector beta [36][37][38][40] · computer_toolset [44] · max_turns default [57] · temperature rules [66][67] · Next.js CVE and patch [72] · Supabase GRANT and keys [74][75][76] · Vercel Workflows GA [86] · shadcn CLI and Base UI [99][100] |
| **2026-12-23** (pricing and status, 3 mo) | every free tier: Langfuse, LangSmith, Braintrust, Upstash, Resend, v0, Lovable, Bolt [49][52][53][92][93][108][109][110] · Managed Agents price [4] · cache pricing [59] · Vercel limits [61] · Assistants and AutoGen status [6][20] |
| **2027-03-23** (ecosystem, 6 mo) | acquisitions: Langfuse, Helicone, Better Auth, Tailwind [51][54][82][97] · Lighthouse CI staleness [121] |
| **2028-09** (patterns, 24 mo) | multi-agent evidence [32][33] |

**Earliest re-check: 2026-10-23.** That falls one day after the toolkit's existing re-check date (2026-10-22), so run both refreshes together.
