# Import log: maxi-cmyk/help-me-papi

<!-- markdownlint-disable MD013 -->

> What was merged into this toolkit from [github.com/maxi-cmyk/help-me-papi](https://github.com/maxi-cmyk/help-me-papi), what was corrected, and what was left out. Import date: 2026-09-21.

## Source snapshot

| | |
| --- | --- |
| Repo | `maxi-cmyk/help-me-papi`, "prompts, skills, resources (websites) for wtv we need" |
| Last push | 2026-08-16 · ⭐ 0 · ~100 Markdown files + `organiser.py` |
| **License** | ⚠️ **None.** By default the author keeps all rights. Content was **adapted, attributed and linked**, not copied wholesale. `organiser.py` was **not** copied, only linked. Ask the author before redistributing their files as-is. |
| Nature | A personal agentic-development toolkit built by one author from their own hackathons (it'sPEAK, Echo, Epicenter, an NFC portfolio). Its folder layout is the one this toolkit already mirrors. |

## What was merged, and where

| From help-me-papi | Into this toolkit |
| --- | --- |
| `hackathons/PROMPTS.md` (6 chained macros) | `../01-hackathon-playbook/PROMPTS.md` C1–C6 (improved: non-goals, mock list, cut line, service layer, AI_USAGE, human-voice script) |
| `hackathons/templates/` (PRD, design, techStack) + the `docs/Research.md` convention | `../01-hackathon-playbook/templates/` (4 templates; techStack updated to Sep 2026 models) |
| `hackathons/file-structure.md` (feature-first) | `../01-hackathon-playbook/docs/project-structure.md` (Next.js 16 `proxy.ts`, service layer, Python variant) |
| `hackathons/skills/deployment.md` | `../skills/hackathon-deployment/SKILL.md` (**commands re-verified; 5 corrections**) |
| `hackathons/strategy-and-resources.md` (warm-up, docs-as-code, 50% rule, harvest) | `../01-hackathon-playbook/battle-plan.md` (with an MLH prior-code caveat) |
| `README.md` agentic workflow, CLAUDE.md, sub-agents, skills; `agents/README.md` | `../01-hackathon-playbook/docs/agent-context.md` |
| `frontend/docs/taste-skill.md` | `../02-frontend/docs/taste-skill.md` (re-verified: 88.9k stars, MIT, install commands) |
| `frontend/docs/impeccable-skill.md` (install options, detector CLI) | `../02-frontend/docs/impeccable.md` (merged) |
| `frontend/docs/design-resources.md`, `skills/styling-tokens.md` | `../02-frontend/docs/aesthetics-directory.md` |
| `frontend/skills/` clarity-first, layout-and-interaction, rendering-and-loading; `REVIEW_UX_HEURISTICS` | `../02-frontend/docs/ux-heuristics.md` + `../02-frontend/PROMPTS.md` F10–F13 |
| `hackathons/skills/backend.md`, `backend/standards.md`, `backend/docs/*-decisions.md` | `../03-backend/docs/hackathon-patterns.md` + `../03-backend/PROMPTS.md` B10–B13 |
| `AI/skills/modeling.md` (it'sPEAK pipeline, Echo lesson) | `../04-ai-and-rag/docs/multimodal-pipelines.md` |
| `AI/skills/chunking.md`, `retrieval.md`, `evaluation.md`; `ADD_GUARDRAILS` | `../04-ai-and-rag/docs/rag-architecture.md` (refinements + failure triage) + `PROMPTS-RAG.md` R9–R10 |
| `AI/PROMPTS-ML.md`, `data-analysis/prompts/scaffolds.md` | `../04-ai-and-rag/PROMPTS-ML.md` ML8–ML11 |
| `tools/PROMPTS.md`, `tools/good-to-know/*` | `../05-tools-and-mcp/PROMPTS.md` T1–T4, `../01-hackathon-playbook/docs/agent-context.md` (graphify) |

## Corrections (checked against official sources on 2026-09-21)

| help-me-papi says | Correct (source) |
| --- | --- |
| `claude mcp add 21st-dev npx -y @21st-dev/mcp` | 21st MCP via the plugin marketplace or `npx @21st-dev/cli@latest init --client claude`; old keys reset ([21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp)) |
| `claude mcp add stitch npx -y @_davideast/stitch-mcp proxy` | Needs `--` before the command ([Claude Code MCP docs](https://code.claude.com/docs/en/mcp)) |
| `middleware.ts` for route protection | `proxy.ts` on Next.js 16+ ([Supabase SSR guide](https://supabase.com/docs/guides/auth/server-side/nextjs), [Clerk quickstart](https://clerk.com/docs/nextjs/getting-started/quickstart)) |
| Supabase Auth: "always use `getUser()`" | Supabase now recommends **`getClaims()`**; never trust `getSession()` in server code ([Supabase SSR guide](https://supabase.com/docs/guides/auth/server-side/nextjs)) |
| `railway add --plugin postgres` | `railway add --database postgres` ([Railway CLI](https://docs.railway.com/reference/cli-api)) |
| `railway variables set KEY=…` | `railway variable set KEY=value` ([Railway CLI](https://docs.railway.com/reference/cli-api)) |
| Vercel "function > 10 s on free plan" times out | Hobby with Fluid compute: **300 s** default and max; 4.5 MB body limit ([Vercel limits](https://vercel.com/docs/functions/limitations), updated 2026-08-24) |
| `supabase db seed` | No such command. `seed.sql` runs on `db reset` or `db push --include-seed`; `supabase seed buckets` only seeds Storage ([Supabase CLI](https://supabase.com/docs/reference/cli/supabase-seed)) |
| techStack template: "Claude 3.5 Sonnet / GPT-4o" | Sonnet 5 / Haiku 4.5 / Opus 5 (Sep 2026) ([Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing)) |
| Impeccable "23 commands / 60 rules" | 24 commands / 61 rules (README, 2026-09-21) |
| "Railroad" deployment | Typo for Railway |
| `tools/guidelines.md` MCP repo links (`supabase/community-mcp`, `vercel/mcp-server`, `21st-dev/21st-mcp`) | See `../05-tools-and-mcp/docs/mcp-setup.md` §6 |

## Conflicts resolved (both views kept, with guidance)

| Topic | help-me-papi | This toolkit | Resolution |
| --- | --- | --- | --- |
| Pre-built boilerplate | Have a boilerplate and seed script ready before the event | MLH bans code written before the event | Prepare tools, accounts and commands; write code after kickoff (public starters are OK) |
| Language / validation | JavaScript, no Zod, for speed | TypeScript + Zod | Two explicit "speed modes"; pick one per project (`../03-backend/docs/hackathon-patterns.md`) |
| Error envelope | Three different shapes in different files | RFC 9457 | Pick one shape per project; RFC 9457 recommended |
| Aesthetics | Glassmorphism and gradients "wow judges" | Anti-slop rules flag default gradients and glows | A deliberate, domain-fitting aesthetic, recorded in `design.md` with reasoned Impeccable ignores |
| Rerank depth | Down to top 3–8 | Top 20 (Anthropic) | Start at 20; reduce for latency or cost |

## Not verified in this import (flagged in the docs)

- 21st.dev registry install via `npx shadcn@latest add "https://21st.dev/r/…"`
- Impeccable Option D (`npx skills add pbakaus/impeccable`) and the Node 22.12+ requirement
- The Clerk Python SDK snippet (`clerk_backend_api`)
- Rate-limit numbers in `security-standards.md` (100/min, 10/15 min, 3/hour)
- Chunking and retrieval heuristics (practitioner guidance)

## Deliberately not imported

- **`hardware/`** (embedded C++, firmware, sensor fusion, signal maths): out of scope for a software-hackathon toolkit. Worth reading directly for hardware hackathons.
- **`data-analysis/`** statistics standards (non-parametric defaults, bootstrap CIs): only the ML scaffolds were adapted.
- **Production-only backend material** (N+1 queries, indexing, caching, k6, BullMQ): summarised with a link in `../03-backend/docs/hackathon-patterns.md`.
- **`organiser.py`** inbox/catalogue tool: no license, so it's linked rather than copied. See help-me-papi's [CONTRIBUTING.md](https://github.com/maxi-cmyk/help-me-papi/blob/main/CONTRIBUTING.md) for how the `#domain/topic` inbox tagging works.
- Empty placeholder files and READMEs that point to folders that don't exist.
