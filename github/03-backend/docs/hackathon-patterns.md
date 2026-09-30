# ⚡ Hackathon Backend Patterns

<!-- markdownlint-disable MD013 -->

> Speed-first decisions, the "fake it" playbook, and lessons from real hackathon builds. Adapted from [help-me-papi](https://github.com/maxi-cmyk/help-me-papi) (`hackathons/skills/backend.md`, `backend/standards.md`, `backend/docs/*`), with corrections marked ✏️.

---

## Core principles

1. **Ship working software, not perfect architecture.** A clean happy path that demos well beats a thorough system that's half-finished.
2. **Pick boring tools.** Use what the team knows, unless a sponsor requires something else.
3. **Deploy in hour one, not the last hour.** Every feature goes live as it's built.
4. **Fake what you can't build.** Hardcode, mock, seed. Judges evaluate what they see.
5. **One repo, one deployment.** No microservices.

---

## Decision trees

### Stack

```text
Frontend is Next.js?          → Next.js route handlers / Server Actions + Supabase + Vercel   (DEFAULT)
Python needed (ML, sponsor SDK)?
  ├ shared DB needed          → FastAPI + Supabase + Railway   (+ Next.js on Vercel)
  └ local / simple data       → FastAPI or Flask + SQLite + Railway
Anything else                 → whatever the sponsor provides or the team knows
```

Don't let the team spend time choosing. If unsure, use the default.

### Auth

```text
Is auth essential to the demo?
  ├ No  → skip it. Hardcoded demo user.
  └ Yes
      ├ Next.js + Supabase only      → Supabase Auth
      ├ Sponsor provides auth (Clerk, Auth0) → use it (Clerk + Supabase: Third-Party Auth)
      └ Python backend               → verify the provider's JWT server-side
```

✏️ **Supabase Auth server check:** Supabase now recommends **`getClaims()`**, which verifies the token signature on every call. *"Never trust `supabase.auth.getSession()` inside server code such as Proxy."* help-me-papi's advice to use `getUser()` is outdated ([Supabase Next.js SSR guide](https://supabase.com/docs/guides/auth/server-side/nextjs)). The file is `proxy.ts` on Next.js 16+.

### Database

```text
Using Supabase already?   → Supabase Postgres
Deploying to Vercel?      → Supabase (the Vercel filesystem is ephemeral)
Railway / Render?         → Railway Postgres or SQLite
Local only?               → SQLite
```

---

## Schema rules for hackathons

- **2–3 tables maximum** for the MVP: users, the main entity, maybe one join table.
- UUID primary keys on Supabase (Clerk user IDs are `text`).
- **JSON(B) columns** for uncertain or flexible shapes.
- Don't over-normalise: a `status text` column beats a statuses table.
- Always add `created_at`.
- **RLS on**; users see and edit only their own rows (`database-supabase.md`).
- **Seed everything.** An empty app looks broken.

---

## Two speed modes (pick one per project)

| | ⚡ Speed mode (help-me-papi default) | 🛡️ Typed mode (this toolkit's default) |
| --- | --- | --- |
| Language | JavaScript, no type annotations | TypeScript |
| Validation | Small `validateX(body)` functions returning an error array | Zod schemas at every boundary |
| Error body | `{ "data": … }` / `{ "error": "message" }` | RFC 9457 `application/problem+json` |
| Best when | Solo builder, JS-first team, ≤24 h | Teams, AI-heavy codegen (types catch agent mistakes), 36 h+ |

**Pick one and use it everywhere.** help-me-papi itself mixes three error shapes across its files; inconsistency is worse than either choice.

Speed-mode validator:

```javascript
function validateProject(body) {
  const errors = [];
  if (!body.name || typeof body.name !== 'string') errors.push('name is required');
  if (body.name && body.name.length > 100) errors.push('name too long');
  return errors;
}
```

---

## What NOT to build at a hackathon

**Skip:** pagination, API versioning, GraphQL, microservices, WebSockets (unless real-time *is* the feature), caching (until you've measured a bottleneck), observability stacks.

**Build:** input validation, consistent errors, working auth on protected routes, **rate limits on LLM endpoints** (they cost you money), one clean happy path.

---

## Lessons from real builds (help-me-papi case studies)

### `DEMO_MODE` (Epicenter)

An explicit `DEMO_MODE=true` switches to synthetic users and data, so the whole app runs without live auth or providers. That's useful for tests and for a Wi-Fi failure on stage. **Label it honestly:** it proves the workflow, not real isolation, and must never be on in production.

### LLM calls go through the backend (Epicenter)

- **The key never reaches the browser.** Browser → your server → LLM API. No `NEXT_PUBLIC_*` secrets.
- **Pin the model ID** once you've tested it. "Latest" is a silent regression mid-hackathon.
- **Graceful degradation:** the core flow must still work when the LLM is down or slow. Have a cached or rule-based fallback (see `../../04-ai-and-rag/PROMPTS-ML.md` ML7).

### Contract-first for split stacks (Epicenter)

With a FastAPI backend and a TypeScript frontend, the **FastAPI schema is the contract**. Regenerate TypeScript types after every API change and commit them, so the two sides can't drift silently.

### Gated task flows (Epicenter)

For multi-step workflows, model **explicit gated steps** (a state machine with pre- and post-conditions), keep one persistent record through the whole flow, and use a deterministic simulator that never writes to real tables for replaying demo scenarios.

### Heavy processing → queue + worker (it'sPEAK)

Video, audio or document analysis doesn't fit in a request/response cycle, and Vercel functions cap at 300 s on Hobby. Use Upload → API → queue → worker → Supabase → signed URL → UI. Details are in `../../04-ai-and-rag/docs/multimodal-pipelines.md`.

---

## Security decisions worth copying (from help-me-papi `backend/docs/`)

| Decision | Why |
| --- | --- |
| **Return 404, not 403**, for resources a user doesn't own | A 403 confirms the resource exists, which lets attackers enumerate IDs |
| Generic auth errors | Never reveal whether an email is registered |
| Refresh tokens in **HttpOnly cookies**, never localStorage | Any XSS can read localStorage |
| **argon2id** (or bcrypt cost ≥12) if you ever hash passwords | OWASP recommendation; memory-hard |
| Redis-backed rate limiting (Upstash) on serverless | In-memory counters don't work across instances |
| `npm audit --audit-level=high` in CI | Automatic, not forgotten |
| Services own DB access; handlers stay thin | The service boundary is the security boundary |

Production reference limits (help-me-papi `security-standards.md`, not verified against an external standard): general API 100 req/min/IP · auth 10 req/15 min/IP · password reset 3/hour/IP.

---

## Production-grade reference (after the hackathon)

help-me-papi's `backend/skills/` also covers production topics you'll need if the project continues: REST conventions, cursor pagination, N+1 queries, Postgres indexing (composite and partial), cache-aside and stampede protection, connection pooling, BullMQ / Inngest / Trigger.dev / pg-boss background jobs, and k6 load testing. [Browse it on GitHub](https://github.com/maxi-cmyk/help-me-papi/tree/main/backend).

| Resource | Why |
| --- | --- |
| [explain.depesz.com](https://explain.depesz.com) | Visualise `EXPLAIN ANALYZE` output |
| [use-the-index-luke.com](https://use-the-index-luke.com) | Free book on SQL indexing |
| [Stripe API docs](https://stripe.com/docs/api) | A good model of REST API design |
| [pg-boss](https://github.com/timgit/pg-boss) | Postgres-backed job queue, no Redis needed |
| [Hono](https://hono.dev) | Fast, edge-compatible TypeScript API framework |
