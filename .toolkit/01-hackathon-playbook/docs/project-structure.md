# 📁 Hackathon Project Structure (Feature-First)

<!-- markdownlint-disable MD013 -->

> One Next.js 16 repo holds the UI, the API and the docs. Adapted from [help-me-papi](https://github.com/maxi-cmyk/help-me-papi) `hackathons/file-structure.md`, updated for Next.js 16 (`proxy.ts`) and merged with the server layering in `../../03-backend/docs/api-standards.md`.

---

## Tree

```text
src/
├── app/                        # Routing only: pages + route handlers
│   ├── (app)/dashboard/page.tsx
│   ├── api/webhooks/<svc>/route.ts   # REST only for external callers
│   ├── layout.tsx
│   └── globals.css             # @theme tokens (../../02-frontend/docs/design-system-variables.md)
├── components/
│   ├── ui/                     # shadcn primitives (generic, no business logic)
│   └── layout/                 # navbar, footer, sidebar
├── features/                   # ⭐ one folder per domain feature
│   └── <feature>/
│       ├── components/         # UI used only by this feature
│       ├── hooks/              # client data hooks
│       ├── actions.ts          # 'use server': await auth() → validate → service
│       ├── service.ts          # server-only: ownership checks, business rules, DTOs
│       ├── types.ts            # domain interfaces
│       └── constants.ts
├── lib/
│   ├── supabase/               # client singletons (server + browser)
│   ├── errors.ts               # error helper (RFC 9457 or {data}/{error}; pick one)
│   ├── env.ts                  # validated env, server-only
│   └── utils.ts
├── scripts/
│   └── seed.ts                 # hydrate the demo DB in seconds
proxy.ts                        # Next 16+ (was middleware.ts): route protection, not the only auth check
supabase/  migrations/ · seed.sql · tests/
docs/                           # ⭐ docs-as-code: the agent's source of truth
├── Research.md                 # raw research on the problem, sponsors, judges
├── PRD.md                      # ../templates/prd.md
├── techStack.md                # ../templates/tech-stack.md
├── design.md                   # ../templates/design.md
└── pitch/                      # outline.md, script.md, assets
AI_USAGE.md                     # AI disclosure log (rules-and-standards.md)
CLAUDE.md / AGENTS.md           # agent context (agent-context.md)
.env.example                    # every key name, no values
```

---

## Why feature-first?

| Reason | What it means |
| --- | --- |
| **Logic separation** | `components/` is how things *look*; `features/` is what they *do* |
| **AI efficiency** | The agent edits one feature folder instead of hunting through global `hooks/`, `utils/` and `components/` |
| **Encapsulation** | Types, hooks, UI and actions for a domain live and get deleted together, so there's no graveyard of one-off components |
| **Parallel builders** | Teammates or sub-agents take separate feature folders and don't conflict |

**Keep it flat.** More than two levels of nesting inside a feature is over-engineering for a hackathon.

---

## Three non-negotiables

1. **Docs as code.** `docs/` lives in the repo so the team and every agent session share the same plan.
2. **`scripts/seed.ts` + `.env.example` from hour one.** You can't afford to create test data by hand or debug a teammate's missing secret.
3. **Deploy the skeleton in hour one** (see `../../skills/hackathon-deployment/SKILL.md`).

---

## Python variant (FastAPI + Railway)

Use this when the sponsor SDK or the ML stack is Python-only:

```text
app/
├── main.py
├── core/          # config, auth (Clerk token verification), CORS
├── features/<feature>/
│   ├── router.py  # endpoints
│   ├── service.py # business logic
│   └── schemas.py # Pydantic models (the API contract)
└── lib/           # DB init, external API clients
requirements.txt · Dockerfile
```

Pair it with a Next.js frontend on Vercel. Set CORS to the Vercel origin only. If the frontend is TypeScript, generate TypeScript types from the FastAPI OpenAPI schema so the two sides can't drift.
