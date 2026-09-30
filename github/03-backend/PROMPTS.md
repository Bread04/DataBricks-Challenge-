# ⚙️ Backend / System Design Macros

<!-- markdownlint-disable MD013 -->

> Copy-paste prompts for Claude Code. They assume: Next.js 16 (`proxy.ts`), Supabase, Clerk via Third-Party Auth, Zod, and the layout in `docs/api-standards.md`.

---

## Contents

| Code | Macro | When |
| --- | --- | --- |
| [B1](#b1--system-design-in-10-minutes) | System design in 10 minutes | Plan |
| [B2](#b2--project-skeleton) | Project skeleton | Story 1 |
| [B3](#b3--scaffold-a-resource) | Scaffold a resource | Every entity |
| [B4](#b4--webhook-endpoint) | Webhook endpoint | Integrations |
| [B5](#b5--error-envelope-retrofit) | Error envelope retrofit | Cleanup |
| [B6](#b6--rls-audit) | RLS audit | Before demo |
| [B7](#b7--owasp-pass) | OWASP pass | Feature freeze |
| [B8](#b8--seed-data) | Seed data | Demo prep |
| [B9](#b9--free-tier-guard) | Free-tier guard | Day before judging |
| [B10](#b10--architect-the-database) | Architect the database (+ ERD) | Plan |
| [B11](#b11--debug-a-runtime-error) | Debug a runtime error | Any time |
| [B12](#b12--llm-through-the-backend) | LLM through the backend | AI features |
| [B13](#b13--python-worker-service) | Python worker service | Heavy processing |

> B10–B13 are adapted from [help-me-papi](https://github.com/maxi-cmyk/help-me-papi) `backend/PROMPTS.md` (`ARCHITECT_DATABASE`, `DEBUG_RUNTIME_ERROR`) and its Epicenter / it'sPEAK lessons. See `docs/hackathon-patterns.md`.

---

### B1 · System design in 10 minutes

```text
Design the backend for <idea> as a hackathon spine (one page):
1. Entities + relationships (table list with key columns; Clerk user ids are text).
2. Data access: Server Components + DAL for reads, Server Actions for mutations, REST route handlers ONLY for <webhooks/external>.
3. External APIs and what we mock for the demo.
4. Folder ownership if teammates build in parallel.
5. The 3 riskiest integration points and a fallback for each.
Keep it minimal: no queues, microservices, or GraphQL unless the demo needs it.
```

### B2 · Project skeleton

```text
Create the backend skeleton for Next.js 16:
- lib/env.ts (zod-validated env, server-only), lib/errors.ts (AppError + problem() + fromZod() per RFC 9457), lib/validation/.
- server/auth.ts (cached getCurrentUser via await auth()), server/supabase.ts (createClient with accessToken() from Clerk — Supabase Third-Party Auth, NOT the deprecated JWT template).
- proxy.ts with clerkMiddleware + createRouteMatcher protecting <routes>.
- supabase/ initialised with migrations/, seed.sql, tests/.
All server files import 'server-only'. No NEXT_PUBLIC_ server keys.
```

*Grounded in:* [Clerk quickstart](https://clerk.com/docs/nextjs/getting-started/quickstart), [Supabase third-party Clerk](https://supabase.com/docs/guides/auth/third-party/clerk), [Next.js data security](https://nextjs.org/docs/app/guides/data-security)

### B3 · Scaffold a resource

```text
Scaffold the <entity> resource end-to-end with fields: <fields>.
1. Migration: table (user_id text default auth.jwt()->>'sub'), index on user_id, RLS enabled, 4 policies (one per op, `to authenticated`, `(select auth.jwt()->>'sub')`), explicit grants.
2. pgTAP test: owner can CRUD, other user cannot, anon cannot.
3. Zod schemas (create/update) in lib/validation/.
4. server/repositories/<entity>.repo.ts — Supabase queries only.
5. server/services/<entity>.service.ts — ownership checks, business rules, returns DTOs.
6. app/.../actions.ts — 'use server', await auth(), zod.parse, call service, revalidatePath.
7. Errors mapped to RFC 9457 problem details.
Show the migration first and wait for my OK before the rest.
```

### B4 · Webhook endpoint

```text
Create a REST route handler app/api/webhooks/<service>/route.ts:
- Verify the provider signature before parsing (use the provider SDK).
- Check content-type and size; zod-validate the payload.
- Idempotency: ignore already-processed event ids.
- Call a service function; respond 2xx fast.
- Errors as application/problem+json (no internals in detail).
```

### B5 · Error envelope retrofit

```text
Find every place we return ad-hoc errors ({error: "..."}, thrown strings, bare 500s).
Convert them to RFC 9457 problem details via lib/errors.ts: correct status, title, safe detail, errors[] with JSON pointers for validation, Content-Type application/problem+json.
List each change as file:line → new status/title.
```

*Spec:* [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html)

### B6 · RLS audit

```text
Audit the Supabase schema (use the Supabase MCP in read-only mode):
- Tables in exposed schemas without RLS.
- Tables with default anon/authenticated grants still present.
- Policies missing `to <role>`, using auth.uid() without (select …), or filtering on unindexed columns.
- Operations with no policy (e.g. UPDATE without with check).
Output a fix migration + pgTAP tests for allowed and denied cases.
```

*Rules:* [Supabase RLS](https://supabase.com/docs/guides/database/postgres/row-level-security), [Securing your API](https://supabase.com/docs/guides/api/securing-your-api)

### B7 · OWASP pass

```text
Review the current diff against docs/security.md and the OWASP API Top 10 (2023).
For each finding: API1–API10 category, file:line, exploit in one sentence, fix. Prioritise anything reachable in the demo path and any secrets exposure. Then apply fixes for Critical/High only.
```

### B8 · Seed data

```text
Write supabase/seed.sql with realistic demo data for <story>: <n> records that make the demo look alive (real-sounding names, varied states, recent timestamps).
Include one demo user row matching Clerk user id <id>. `supabase db reset` must produce a demo-ready state.
```

### B9 · Free-tier guard

```text
Check our setup against free-tier limits and demo-day risks:
Supabase free (pauses after 1 week idle, 500 MB DB, 5 GB egress), Clerk Hobby (50k MRU, fixed 7-day sessions), our LLM API spend at <expected calls>.
Tell me what to do the day before judging (wake project, re-login demo user, cap generation endpoints).
```

*Limits:* [Supabase pricing](https://supabase.com/pricing), [Clerk pricing](https://clerk.com/pricing)

### B10 · Architect the database

```text
[ROLE] Senior database architect. [CONTEXT] docs/PRD.md, docs/techStack.md.
Design the MVP schema on Supabase Postgres:
- 2–3 tables max (users/profile, main entity, optional join). Flat; JSONB for uncertain shapes; status as text; created_at everywhere.
- Clerk ids as text (auth.jwt()->>'sub') or Supabase Auth uuid (auth.uid()).
Output: 1) CREATE TABLE + indexes as a migration, 2) RLS: one policy per operation, `to authenticated`, `(select …)` wrapped, 3) supabase/seed.sql with realistic demo data, 4) a mermaid erDiagram.
```

### B11 · Debug a runtime error

```text
[ROLE] Debugging specialist. Here are the logs <Vercel/Railway/terminal> and the failing code <paste>.
Check in this order and tell me which one it is before changing code:
1. ENV: missing/misnamed secret in this environment (Vercel vs Railway vs local), NEXT_PUBLIC_ vs server-only.
2. RUNTIME: Edge vs Node mismatch (Node-only import in proxy/edge code).
3. NETWORK: hard-coded localhost URL, CORS origin, OAuth redirect missing the production domain.
4. DATABASE: RLS denying the operation, missing grant, pooled vs direct connection, paused free project.
5. LIMITS: Vercel 300s timeout / 4.5 MB body, model rate limits.
Then give the minimal fix and one log line that would have caught it.
```

### B12 · LLM through the backend

```text
Wire <feature> to call <pinned model id> ONLY from the server (server action / route handler / FastAPI):
- Key in server env only; no NEXT_PUBLIC_ secrets.
- Per-user rate limit + max tokens; timeout; stream the response to the UI.
- Graceful degradation: if the model errors or times out, return a cached/rule-based fallback and a toast — the core flow must still work.
- Validate structured output before it touches the DB or renders as HTML.
- Log model id + token usage per call.
```

### B13 · Python worker service

```text
Add a FastAPI + worker service on Railway for <heavy job: video/audio/doc analysis>:
- POST /jobs → validate → enqueue (Redis) → return job id; worker processes one job at a time.
- Deterministic pre-checks first (file type/size/duration/quality) — reject bad input before spending tokens.
- Results → Supabase table + Storage; frontend polls or subscribes (Realtime) and reads via signed URL.
- CORS only for FRONTEND_ORIGIN; Clerk token verified on every request.
- railway.toml start commands for api + worker; restart worker after each heavy job.
```

*Deploy commands:* `../skills/hackathon-deployment/SKILL.md` · *Pattern:* `../04-ai-and-rag/docs/multimodal-pipelines.md`
