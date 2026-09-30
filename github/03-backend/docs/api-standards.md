# 🔌 API Standards: REST / GraphQL / Server Actions

<!-- markdownlint-disable MD013 -->

> How to shape endpoints, layers and errors for a Next.js 16 + Supabase hackathon app. Verified 2026-09-21.

---

## 1 · Which API style?

| Use | Style | Why |
| --- | --- | --- |
| Reading data in pages | **Server Components → Data Access Layer** | Next.js recommends the DAL for new projects; don't fetch your own Route Handlers from Server Components (extra round trip, breaks at build time) ([Next.js data security](https://nextjs.org/docs/app/guides/data-security), [BFF guide](https://nextjs.org/docs/app/guides/backend-for-frontend)) |
| Mutations from your UI | **Server Actions** (thin → service) | Built-in CSRF (Origin vs Host). They run sequentially, so use them for mutations, not fetching (same sources) |
| Webhooks, external callers, mobile clients | **REST Route Handlers** (`app/api/**/route.ts`) | Public contract; return RFC 9457 errors |
| Typed client ↔ server in a TypeScript-only monorepo | tRPC (optional) | End-to-end types; no non-TypeScript clients ([trpc/trpc](https://github.com/trpc/trpc), ⭐ 40.6k) |
| Many clients needing different data shapes | GraphQL | Usually overkill in 24–48 h; Supabase already has a Data API |

> [!NOTE]
> The REST vs GraphQL vs tRPC comparison rests on vendor blogs (low confidence). The first three rows are an **inference** from official Next.js guidance, not a published hackathon recommendation.

---

## 2 · Layered structure (route/action → service → repository)

```text
app/
  api/webhooks/<svc>/route.ts  # REST for external callers: parse → service → problem()
  (app)/tasks/actions.ts       # 'use server'; zod.parse → service. Re-check auth HERE.
lib/
  env.ts                       # server-only; zod-validated process.env
  errors.ts                    # AppError classes + problem() (RFC 9457)
  validation/                  # zod schemas shared by actions & handlers
server/                        # every file starts with: import 'server-only'
  auth.ts                      # cached getCurrentUser() via Clerk auth()
  services/tasks.service.ts    # authorization (ownership), business rules → returns DTOs
  repositories/tasks.repo.ts   # Supabase queries only, no business logic
proxy.ts                       # clerkMiddleware (Next 16+). NOT the only auth check.
supabase/migrations/ · supabase/seed.sql · supabase/tests/*_rls.test.sql
```

**Rules** ([Next.js data security](https://nextjs.org/docs/app/guides/data-security)):

1. Pick **one** data-access approach (DAL for new projects) and don't mix them.
2. The DAL is `server-only`, does the authorisation checks, and returns **minimal DTOs**, not raw rows.
3. Only the DAL and services read `process.env`.
4. **Server Actions are public endpoints.** Anyone can POST to them, so re-check auth and ownership inside every action.
5. Proxy (formerly middleware) is not an authorisation layer on its own.

---

## 3 · Error envelope: RFC 9457 Problem Details

RFC 9457 (July 2023) **obsoletes RFC 7807** ([RFC Editor](https://www.rfc-editor.org/rfc/rfc9457.html)).

| Member | Meaning |
| --- | --- |
| `type` | URI identifying the problem type (default `about:blank`) |
| `title` | Short human-readable summary of the type |
| `status` | HTTP status (advisory; the real status code wins) |
| `detail` | This occurrence, written to help the client *fix* it, not to debug the server |
| `instance` | URI for this specific occurrence |
| *extensions* | Any extra top-level members, e.g. `errors[]`, `traceId` |

Header: `Content-Type: application/problem+json`

```json
{
  "type": "https://example.com/problems/validation-error",
  "title": "Your request is not valid.",
  "status": 422,
  "detail": "2 fields failed validation.",
  "instance": "/api/tasks/req-7f3a",
  "errors": [
    { "detail": "must be a non-empty string", "pointer": "#/name" },
    { "detail": "must be one of: low, med, high", "pointer": "#/priority" }
  ]
}
```

### Helper (`lib/errors.ts`)

```ts
import { ZodError } from 'zod';

export function problem(status: number, title: string, extra: Record<string, unknown> = {}) {
  return Response.json(
    { type: 'about:blank', title, status, ...extra },
    { status, headers: { 'Content-Type': 'application/problem+json' } },
  );
}

export function fromZod(err: ZodError) {
  return problem(422, 'Validation failed', {
    errors: err.issues.map((i) => ({ detail: i.message, pointer: '#/' + i.path.join('/') })),
  });
}
```

**Never** put stack traces, SQL or internal IDs in `detail`. RFC 9457's security section and the Next.js docs both warn against exposing internals.

### Status code cheat sheet

| Code | When |
| --- | --- |
| 400 | Malformed body |
| 401 | Not signed in |
| 403 | Signed in but not allowed (ownership) |
| 404 | Not found, or hidden for authorisation reasons |
| 409 | Conflict (duplicate) |
| 422 | Validation failed (`errors[]`) |
| 429 | Rate limited (add `Retry-After`) |
| 500 | Unexpected error; generic `detail`, log the rest server-side |

---

## 4 · Route Handler checklist

From the [Next.js BFF guide](https://nextjs.org/docs/app/guides/backend-for-frontend):

- [ ] Validate content type and body size
- [ ] Zod-validate body, params and searchParams
- [ ] Rate-limit in code (**429**) *and* turn on host-level limits
- [ ] Timeouts on outbound calls
- [ ] Same-origin check on redirects (no open redirects)
- [ ] Strip sensitive fields from responses and logs
- [ ] Sanitise any input that ends up in markup

---

## Repos

| Repo | Why | Status |
| --- | --- | --- |
| [colinhacks/zod](https://github.com/colinhacks/zod) | Validation at every boundary | ⭐ 44k · pushed 2026-09 |
| [upstash/ratelimit-js](https://github.com/upstash/ratelimit-js) | Serverless rate limiting for `checkRateLimit()` | ⭐ 2k · pushed 2026-09 |
| [trpc/trpc](https://github.com/trpc/trpc) | Optional typed API layer | ⭐ 40.6k · pushed 2026-09 |
| [nextjs/saas-starter](https://github.com/nextjs/saas-starter) | Reference service-layer structure (Postgres + Stripe) | ⭐ 16k · ⚠️ last push 2025-12, check Next 16 support |
| [t3-oss/create-t3-app](https://github.com/t3-oss/create-t3-app) | Typesafe scaffold (tRPC + Prisma/Drizzle) | ⭐ 29k · ⚠️ last push 2025-12 |
| ~~vercel/nextjs-subscription-payments~~ | **Archived**, so don't use it | ❌ |
