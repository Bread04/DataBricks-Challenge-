# Tech Stack: [Project Name]

<!-- markdownlint-disable MD013 -->

> Adapted from help-me-papi's techStack template. ✏️ Models, versions and auth wiring updated to September 2026 (see `../../04-ai-and-rag/docs/model-selection.md`).

Need an alternative for any row? `../../06-repo-catalog/README.md` has a verified default kit and 259 repos by category.

## Frontend

| Choice | Why |
| --- | --- |
| **Next.js 16 (App Router)** | UI and API in one deploy, no CORS; `proxy.ts` for route protection |
| **Tailwind v4 + shadcn/ui** | Token-driven styling (`@theme`) plus accessible copy-in components |
| **21st.dev** (via 21st MCP) | One or two distinctive components for the AHA moment |
| **sonner · lucide-react · Framer Motion** | Toasts ("toasts, not crashes"), icons, micro-interactions (check the animation library's current package name on npm) |

## Backend and data

| Choice | Why |
| --- | --- |
| **Supabase (Postgres + pgvector + Storage)** | DB, storage and vectors in one place; RLS for per-user data |
| **Clerk** (via Supabase Third-Party Auth) *or* Supabase Auth | Only if the demo needs accounts. Server checks: Clerk `await auth()` / Supabase `getClaims()` |
| **Zod** (TypeScript) *or* simple validators (JS speed mode) | Validate at every boundary |
| **Drizzle / Prisma** (optional) | Prisma is gentler for hackathons; Drizzle is lighter |

## AI

| Role | Model (Sep 2026) | Why |
| --- | --- | --- |
| Workhorse | **Claude Sonnet 5** ($2/$10 per MTok) | Quality at a sane cost |
| Bulk / cheap | **Claude Haiku 4.5** ($1/$5) | Classification, extraction, chunk context |
| Judged reasoning step | **Claude Opus 5** ($5/$25) | Only where it visibly wins |
| SDK | **Vercel AI SDK** | Streaming, tools, structured output |

**Pin the model ID** once you've tested it. "Latest" can silently change behaviour mid-hackathon.

## Infrastructure

| Choice | Why |
| --- | --- |
| **Vercel** | Push-to-deploy for Next.js; Hobby functions run up to 300 s |
| **Railway** (only if needed) | Python APIs, long-running workers, queues |

## How it fits together

```text
Browser → Next.js (Server Components / Server Actions) → service layer → Supabase (RLS)
                                                  └→ LLM API (key server-side only) → streamed to UI
```

(Replace this with your actual flow, e.g. "Supabase webhook → route handler → worker → Realtime → UI".)
