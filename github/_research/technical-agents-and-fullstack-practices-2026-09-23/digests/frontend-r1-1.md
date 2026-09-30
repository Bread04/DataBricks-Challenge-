# Digest: frontend practices — round 1, assistant 1
Accessed: 2026-09-23 · Tool calls used: 20

## Claims
| # | Claim | Source URL | Publisher | Pub date | Confidence (high/med/low) | Class |
|---|---|---|---|---|---|---|
| 1 | Latest Tailwind CSS release is v4.3.3 (Jul 16 2026); v4.3.0 (May 8 2026) added container queries/scrollbar utilities; v4.3.1 Node 26+ compat. No v5 mentioned. | https://releases.sh/tailwind-css | releases.sh (aggregator of GitHub releases) | Aug 2026 | med (aggregator; corroborated by tailwindcss.com/blog v4.3 post) | version |
| 2 | Tailwind blog: "Tailwind CSS v4.3: Scrollbars, new colors, and more" (May 8 2026); "Tailwind Labs is joining Shopify" (Sep 9 2026). Excerpt did not state licensing/v5 implications. | https://tailwindcss.com/blog | Tailwind Labs | 2026-09-09 | high | version |
| 3 | v4 replaced JS config with CSS-native `@theme` directives (still the v4 model). | https://tailwindcss.com/blog/tailwindcss-v4 (via search snippet) | Tailwind Labs | 2025-01-22 | high | version |
| 4 | shadcn/ui: Base UI became the default for new projects in July 2026 (`npx shadcn init`); Radix NOT deprecated, every component ships for both. | https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default | shadcn/ui | 2026-07 | high | version |
| 5 | shadcn/cli v4 (Mar 2026) adds `--base` flag to pick Radix or Base UI. (Cheat sheet "CLI 3.x" is outdated.) | https://ui.shadcn.com/docs/changelog/2026-03-cli-v4 | shadcn/ui | 2026-03 | high | version |
| 6 | shadcn/ui 2026 changelog: Chat interface components + GitHub Registries (Jun); React Aria support, shadcn/typeset, @shadcn/helpers, registry dynamic search (Jul); Private GitHub registries, "Human in the Loop" helpers for AI SDK tool-approval flows, Questionnaire multi-step form (Aug); `cn` moved to a dedicated `cn` package (Sep). | https://ui.shadcn.com/docs/changelog | shadcn/ui | 2026-09 | high | version |
| 7 | Next.js 16.3 released Aug 3 2026: Instant Navigations (opt-in `cacheComponents` + `partialPrefetching`), up to 90% less dev memory, TS 7 type checking, `catchError` custom error boundaries with `retry()`, `@next/playwright` `instant()` test helper, experimental `useOffline`. | https://nextjs.org/blog/next-16-3 | Vercel/Next.js | 2026-08-03 | high | version |
| 8 | Next.js 16.3 `next dev` writes a version-matched AGENTS.md pointing coding agents at bundled docs; earlier next-skills retired. | https://nextjs.org/blog/next-16-3 | Vercel/Next.js | 2026-08-03 | high | tool |
| 9 | React Compiler support stable since Next.js 16 (after React Compiler 1.0), enabled via `reactCompiler: true`, not on by default; 16.3 adds experimental Rust compiler (`turbopackRustReactCompiler`). Turbopack default since 16. | https://nextjs.org/blog/next-16 ; https://nextjs.org/blog/next-16-3 | Vercel/Next.js | 2025-10 / 2026-08 | high | version |
| 10 | Impeccable (pbakaus): `npx impeccable install` then `/impeccable init`; 24 commands (audit, critique, animate, colorize, live browser iteration...); 61 deterministic detector rules + LLM critique; standalone no-LLM CLI detector scans dirs/HTML/live URLs; 17+ harnesses; Apache 2.0. | https://github.com/pbakaus/impeccable | GitHub (pbakaus) | accessed 2026-09 | high | tool |
| 11 | Impeccable 3.5 announced as "design in production: iterate on real UI with your AI agent, in the codebase you actually ship"; author claims popular design skills incl. Anthropic's frontend-design "weren't actually very good at...design". | https://x.com/pbakaus/status/2060208540992880794 | X (Paul Bakaus) | ~mid 2026 (date not retrieved) | med | tool |
| 12 | Google Stitch big update Mar 19 2026: infinite canvas, voice, design agent, DESIGN.md brand import, MCP server; setup `npx -y @google/stitch-mcp@latest` + Stitch API token. | https://sfailabs.com/guides/google-stitch-vs-figma ; https://justinmckelvey.com/blog/google-stitch-mcp | secondary blogs | 2026 | med (no Google primary fetched) | tool |
| 13 | Community stitch-mcp CLI by davideast exists for moving Stitch designs into dev workflow. | https://github.com/davideast/stitch-mcp | GitHub | accessed 2026-09 | med | tool |
| 14 | AI SDK UI: generative UI = connect tool-call results to React components; framework-agnostic hooks for chat/generative UI. | https://ai-sdk.dev/docs/ai-sdk-ui/generative-user-interfaces | Vercel | current | high | practice |
| 15 | AI Elements: shadcn/ui-based component library + registry for AI apps (conversation, message, streaming states, tool calls, reasoning, code/Sandbox), installed via CLI as source. | https://github.com/vercel/ai-elements ; https://elements.ai-sdk.dev/ | Vercel | current | high | tool |
| 16 | AG-UI is an event-based Agent-User Interaction protocol (runtime connection agent<->frontend), not a generative-UI spec; CopilotKit built on it; sits below A2UI / Open-JSON-UI / MCP Apps. AWS Bedrock AgentCore Runtime added AG-UI support Mar 2026. | https://docs.ag-ui.com/ ; https://www.copilotkit.ai/ag-ui-and-a2ui | AG-UI / CopilotKit | 2026 | med-high (vendor docs; AWS claim via vendor) | standard |
| 17 | Same-document View Transitions Baseline Newly available since Oct 14 2025 (Chrome/Edge 111, Firefox 144, Safari 18). Cross-document (`@view-transition`) not in Firefox → limited availability. | https://web.dev/blog/same-document-view-transitions-are-now-baseline-newly-available ; https://developer.mozilla.org/en-US/docs/Web/CSS/@view-transition | web.dev / MDN | 2025-10 | high | standard |
| 18 | v0 Free: $5 monthly credits, 7 messages/day; Premium $20 being phased out; Plus $30/user/mo; Business $100/user/mo; credits roll over, expire after 65 days. (Secondary source adds watermarked deploys on free, $2 daily login credits — unconfirmed on docs page; one secondary names the $30 tier "Team".) | https://v0.app/docs/pricing ; https://automationatlas.io/answers/v0-pricing-explained-2026/ | Vercel v0 docs + secondary | accessed 2026-09 | high (docs) | free-tier |
| 19 | Judges: "show something working within about 90 seconds" (Bacon); demo "should show what your app does in one flow" and "Mock everything you can and make sure all your forms are filled" (Lowenberg); "Shipping a good demo matters more than having the most reliable, highest-quality code" (Wortmann). | https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/ | JetBrains Blog (K. Druckman) | 2026-06 | high | practice |
| 20 | Judge write-up: clean readable UI helps, but elaborate UI adds no value and "past a point makes judges wonder where the backend time went". | https://dev.to/kurbaitaev/what-judges-actually-score-notes-from-a-year-of-hackathon-judging-3p4l | DEV Community (individual) | 2026 (approx) | low-med (single practitioner, snippet only) | practice |

## Currency check results
- **Tailwind v4 @theme tokens** — still-current. Latest v4.3.3 (Jul 2026); no v5 found. New: Tailwind Labs joined Shopify (Sep 9 2026) — implications unknown.
- **shadcn/ui, Base UI default as of Jul 2026** — still-current (confirmed, primary). Change: CLI is v4 (Mar 2026), not 3.x; `--base` flag; React Aria is now a third option; chat components (Jun 2026) and Human-in-the-Loop AI SDK helpers (Aug 2026); `cn` now from `cn` package (Sep 2026) — older snippets importing from `@/lib/utils` may diverge.
- **Next.js / React Compiler** — changed: Next.js 16.3 (Aug 3 2026) current; React Compiler stable but opt-in. Exact React 19.x minor: unverified.
- **WCAG 2.2 AA** — unverified this run (not searched; no evidence of change retrieved).
- **Core Web Vitals thresholds (LCP ≤2.5s, INP ≤200ms, CLS ≤0.1)** — unverified this run.
- **Impeccable** — still-current, now 3.5-era with 24 commands, deterministic detector CLI. Install `npx impeccable install`.
- **Anthropic frontend-design skill** — unverified (only referenced second-hand in pbakaus post, which critiques it).
- **Stitch → Stitch MCP** — still-current per secondary sources (Mar 2026 update added official MCP). Google primary not fetched.
- **21st.dev MCP** — unverified this run.
- **v0** — free tier confirmed ($5/mo, 7 msgs/day). Lovable / Bolt / Figma MCP / Figma Make — unverified.

## Notes for synthesis
- For AI-feature UIs, the lowest-friction beginner stack is now shadcn/ui + AI Elements + AI SDK UI (`useChat`), all shadcn-registry compatible; shadcn itself now ships chat components and human-in-the-loop tool-approval helpers. CopilotKit/AG-UI is the choice if the backend is a separate agent framework.
- Recommend "tool-call cards / approval prompts / streaming states / reasoning displays" as explicit UI requirements for AI hackathon projects (both AI Elements and shadcn helpers are designed around these).
- Next.js 16.3 `catchError` with `retry()` and Suspense-based loading shells give cheap error/loading states; `useOffline` is experimental — don't rely on it.
- Next.js 16.3 auto-writes AGENTS.md for coding agents — relevant to the Claude Code workflow section.
- View Transitions: safe to use same-document (Baseline); cross-document is Chromium/Safari only — progressive enhancement.
- Judge evidence favors one working flow in ≤90s, mocked/pre-filled demo data, and "clean not elaborate" UI — this tempers "impress with polish" framing: polish should serve the one demo flow.
- Impeccable's no-LLM detector CLI is a quick CI/pre-demo check for AI-slop patterns.

## Leads worth chasing
- Full text of https://tailwindcss.com/blog/tailwind-is-joining-shopify (licensing, roadmap).
- https://nextjs.org/blog/next-16-3-ai-improvements and /docs/app/guides/ai-agents (agent workflow details).
- shadcn changelog entries for Chat components (Jun 2026) and Human in the Loop (Aug 2026) — exact install commands.
- Google primary Stitch blog/docs for MCP and free-tier limits.
- assistant-ui current status; A2UI and MCP Apps specs.
- Motion (motion.dev) current version; TanStack Query v5/Form status; Zustand; React Hook Form vs TanStack Form.
- EAA scope for hackathon (likely low relevance), axe-core/Playwright CI; web.dev CWV threshold page; WCAG 3 draft status.
- Lovable, Bolt, Figma Make free tiers (two-source class required).

## Looked for but could not find
- Any Tailwind v5 announcement (none found in releases or blog).
- Primary Google source for Stitch MCP (only secondary blogs surfaced).
- Publication date of Impeccable 3.5 announcement and a tagged GitHub release version.
- Not searched due to budget: Motion, TanStack Query/Form, Zustand, forms, dark mode/next/font, axe/Lighthouse CI, EAA, Lovable/Bolt/Figma MCP/Make, 21st.dev, Anthropic frontend-design skill, WCAG/CWV threshold reconfirmation, mobile-responsiveness judge evidence.
