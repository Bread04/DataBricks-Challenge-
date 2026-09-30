# Digest: Backend standards & stack (backend-r1-1)

Dimension: Backend standards & stack for a personal hackathon toolkit (API, Supabase/Postgres, Clerk, security, service layers).
Run date: 2026-09-21. All sources fetched this session. Pricing pages carry no date; fetched live today, so they are current as of the access date.

## Findings

1. RFC 9457 "Problem Details for HTTP APIs" is a Standards Track RFC published July 2023 that obsoletes (supersedes) RFC 7807. | https://www.rfc-editor.org/rfc/rfc9457.html | IETF / RFC Editor | 2023-07 | accessed 2026-09-21 | high | standard
2. RFC 9457 defines media types `application/problem+json` and `application/problem+xml`, plus five standard members: `type` (URI, defaults to `about:blank`), `status` (advisory; the real HTTP status code wins), `title` (short human-readable summary of the problem type), `detail` (explanation of this occurrence, aimed at fixing it, not debugging), `instance` (URI for this specific occurrence). | https://www.rfc-editor.org/rfc/rfc9457.html | IETF | 2023-07 | accessed 2026-09-21 | high | standard
3. RFC 9457 allows extension members. Its example validation error adds an `errors` array whose entries carry `detail` and a JSON Pointer to the failing field. Changes from 7807: a registry of common problem type URIs, guidance for reporting multiple problems, and guidance for type URIs that don't resolve (such as tag: URIs). | https://www.rfc-editor.org/rfc/rfc9457.html | IETF | 2023-07 | accessed 2026-09-21 | high | standard
4. RFC 9457 security considerations: vet problem details carefully so they don't expose internals, attack vectors or sensitive data. Next.js docs say the same for Route Handlers ("Avoid exposing sensitive information in error messages"). | https://www.rfc-editor.org/rfc/rfc9457.html ; https://nextjs.org/docs/app/guides/backend-for-frontend | IETF; Vercel | 2023-07; 2026-06 | accessed 2026-09-21 | high | security
5. Supabase Free plan: 2 active projects, 500 MB database (shared CPU, 500 MB RAM), projects paused after 1 week of inactivity, 50,000 MAU, 1 GB file storage, 5 GB egress plus 5 GB cached egress, 500,000 Edge Function invocations, 200 concurrent Realtime connections. Pro starts at $25/month. | https://supabase.com/pricing | Supabase | undated (live page) | accessed 2026-09-21 | high | pricing
6. Clerk Hobby (free) plan: 50,000 MRU (monthly retained users, not MAU) per app, unlimited applications, up to 3 dashboard seats, prebuilt sign-in/sign-up/profile UIs, custom domain, 100 MROs (monthly retained organizations) per app, fixed 7-day session lifetime, 1-day log retention, API keys capped at 1,000 creations and 100,000 verifications a month. Pro is $25/month ($20/month billed annually). | https://clerk.com/pricing | Clerk | undated (live page) | accessed 2026-09-21 | high | pricing
7. The current official Clerk + Supabase method is Supabase Third-Party Auth. Enable it on Clerk's "Connect with Supabase" page, then add a Clerk integration in Supabase (dashboard, or `[auth.third_party.clerk] enabled = true, domain = "<x>.clerk.accounts.dev"` in `config.toml`). Clerk session tokens must carry a `role` claim, set to `authenticated` for end users. | https://supabase.com/docs/guides/auth/third-party/clerk | Supabase | undated | accessed 2026-09-21 | high | version
8. The old Clerk "Supabase JWT template" integration has been deprecated since April 1, 2025. Both vendors say so. The reasons given: it meant sharing the Supabase JWT secret with a third party, and rotating that secret caused downtime. The toolkit should not teach it. | https://supabase.com/docs/guides/auth/third-party/clerk ; https://clerk.com/docs/guides/development/integrations/databases/supabase | Supabase; Clerk | 2025-04 (deprecation date) | accessed 2026-09-21 | high | version
9. Client code for the native integration: supabase-js `createClient(url, NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY, { async accessToken() { return session?.getToken() ?? null } })` on the client, and `(await auth()).getToken()` on the server. Clerk's docs now use a "publishable key" env name rather than the anon key. RLS matches on `auth.jwt()->>'sub'` stored in a `text` user_id column. | https://clerk.com/docs/guides/development/integrations/databases/supabase | Clerk | undated | accessed 2026-09-21 | high | pattern
10. Clerk Next.js quickstart: package `@clerk/nextjs`, env vars `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` and `CLERK_SECRET_KEY`, bootstrap with `npx -y clerk@latest init`. `clerkMiddleware()` goes in `proxy.ts` on Next.js 16+ and `middleware.ts` on Next.js 15 and below. `<ClerkProvider>` goes inside `<body>`. Protect routes with `createRouteMatcher` + `auth.protect()`. `auth()` is async and must be awaited. | https://clerk.com/docs/nextjs/getting-started/quickstart | Clerk | undated | accessed 2026-09-21 | high | version
11. Next.js 16 renamed middleware to `proxy` (file `proxy.ts`, exported function `proxy`, one per project). Next.js docs warn not to rely on proxy alone for authentication and authorization, and note that third-party libraries may still call it "middleware". | https://nextjs.org/docs/app/guides/backend-for-frontend | Vercel (Next.js docs v16.3.5) | 2026-06 | accessed 2026-09-21 | high | version
12. Supabase RLS guidance: enable RLS, then (per the current page) revoke default grants from `anon`/`authenticated` and grant back only what's needed, because "adding policies doesn't remove" existing grants. Write one policy per operation: SELECT uses `using`, INSERT uses `with check`, UPDATE uses both, DELETE uses `using`. `auth.uid()` returns null when unauthenticated. Test policies with pgTAP files in `supabase/tests/<table>_rls.test.sql`. | https://supabase.com/docs/guides/database/postgres/row-level-security | Supabase | undated | accessed 2026-09-21 | high | security
13. RLS performance: index every column a policy filters on, wrap functions as `(select auth.uid())` so they're evaluated once per statement instead of per row, and always scope policies with `to authenticated` (or another role). | https://supabase.com/docs/guides/database/postgres/row-level-security | Supabase | undated | accessed 2026-09-21 | high | pattern
14. New `public` tables currently get SELECT/INSERT/UPDATE/DELETE grants for anon, authenticated and service_role automatically, and Supabase says it "is changing the platform default to revoke these automatic grants so that exposure becomes opt-in". The page gives no date for the switch. To opt in now: `alter default privileges for role postgres in schema public revoke select, insert, update, delete on tables from anon, authenticated, service_role;`. The service_role (secret) key must never reach browsers. A dedicated `api` schema is recommended to make the exposed surface easy to audit. | https://supabase.com/docs/guides/api/securing-your-api | Supabase | undated | accessed 2026-09-21 | high | security
15. Supabase's own Data API rate-limit example uses a pre-request function: 100 writes per IP per 5 minutes, returning HTTP 420 (non-standard; 429 is the usual code, and Next.js uses 429). | https://supabase.com/docs/guides/api/securing-your-api | Supabase | undated | accessed 2026-09-21 | med | security
16. Supabase CLI migration workflow: `supabase login` → `supabase init`/`start` → `supabase migration new <name>` → `supabase db diff -f <name>` (captures dashboard changes) → `supabase db reset` (reapplies migrations plus `supabase/seed.sql`) → `supabase link` → `supabase db push`. Also available: `db pull`, `migration list`, `migration repair`. Docs rule: "never change the remote database directly". | https://supabase.com/docs/guides/deployment/database-migrations | Supabase | undated | accessed 2026-09-21 | high | pattern
17. pgvector is available on Supabase as a Postgres extension: enable "vector" under Dashboard → Database → Extensions. Docs also cover vector columns, vector indexes and automatic embeddings. (Evidence comes from search-result snippets of official docs; the page itself wasn't fetched.) | https://supabase.com/docs/guides/database/extensions/pgvector | Supabase | undated | accessed 2026-09-21 | med | version
18. The Supabase MCP server is hosted at `https://mcp.supabase.com/mcp`, with a local CLI endpoint at `http://localhost:54321/mcp`. Add it to Claude Code with `claude mcp add --scope project --transport http supabase "https://mcp.supabase.com/mcp"`, then authenticate via `/mcp`. Official safety advice: use read-only mode, scope to one project, avoid production, enable only the tool groups you need, and review tool calls manually because of prompt-injection risk from database content. Tool groups: database, debugging, development, Edge Functions, account, docs, branching (experimental), storage (off by default). | https://supabase.com/docs/guides/getting-started/mcp | Supabase | undated | accessed 2026-09-21 | high | version
19. OWASP API Security Top 10 2023 is the latest edition. The site moved to api-security.owasp.org via a 308 redirect. Items: API1 Broken Object Level Authorization; API2 Broken Authentication; API3 Broken Object Property Level Authorization; API4 Unrestricted Resource Consumption; API5 Broken Function Level Authorization; API6 Unrestricted Access to Sensitive Business Flows; API7 SSRF; API8 Security Misconfiguration; API9 Improper Inventory Management; API10 Unsafe Consumption of APIs. | https://api-security.owasp.org/editions/2023/en/0x11-t10 | OWASP | 2023 | accessed 2026-09-21 | high | security
20. Next.js recommends three data-access approaches: external HTTP APIs for large existing organizations, a Data Access Layer for new projects, and component-level queries for prototypes only. Pick one and don't mix them. The DAL should run server-only (`import 'server-only'`), do the authorization checks and return minimal DTOs. Only the DAL should read `process.env`. | https://nextjs.org/docs/app/guides/data-security | Vercel (Next.js docs v16.3.5) | 2026-08 | accessed 2026-09-21 | high | pattern
21. Server Actions can be reached by direct POST, so treat them as public endpoints: re-check auth inside every action (a page-level check doesn't cover it), check ownership to prevent IDOR, validate arguments, return only what the UI needs, and keep actions thin by delegating to the DAL. Next.js compares Origin to Host for CSRF protection. Server Actions run sequentially (queued), so use them for mutations, not data fetching. | https://nextjs.org/docs/app/guides/data-security ; https://nextjs.org/docs/app/guides/backend-for-frontend | Vercel | 2026-08; 2026-06 | accessed 2026-09-21 | high | security
22. Route Handler security from the Next.js docs: rate-limit in code (return 429) and turn on your host's rate limiting too; validate content type and size; sanitize input used in markup; use timeouts; stop open redirects with same-origin checks; strip sensitive data from responses and logs; rotate keys. Server Components should read data from the source directly, not through your own Route Handlers, which add a round trip and break at build time. `create-next-app --api` scaffolds a sample `route.ts`. | https://nextjs.org/docs/app/guides/backend-for-frontend | Vercel | 2026-06 | accessed 2026-09-21 | high | security
23. REST vs GraphQL vs tRPC, per secondary sources: REST (plus OpenAPI) suits public, external or multi-language consumers and simple CRUD. GraphQL suits multiple clients with different data shapes and bigger teams. tRPC suits a single full-stack TypeScript app or monorepo that wants end-to-end types, and can't serve non-TypeScript clients. Many systems combine them. (Vendor and blog opinion; no primary standard.) | https://directus.io/blog/rest-graphql-tprc ; https://wundergraph.com/blog/graphql-vs-federation-vs-trpc-vs-rest-vs-grpc-vs-asyncapi-vs-webhooks | Directus; WunderGraph (search snippets) | undated | accessed 2026-09-21 | low | pattern
24. Inference, not a sourced claim: for a solo 24–48h Next.js + Supabase build, the official Next.js guidance points to Server Components with a DAL for reads, Server Actions for mutations and Route Handlers (REST) only for webhooks or external callers. This follows from findings 20–22. GraphQL isn't needed because Supabase already provides a Data API. | derived from nextjs.org data-security + backend-for-frontend | — | — | accessed 2026-09-21 | med | pattern

## Repos

Stars and last push come from the GitHub REST API (`api.github.com/repos/...`), queried 2026-09-21.

| repo | URL | stars | last push | why useful |
|---|---|---|---|---|
| supabase/supabase | https://github.com/supabase/supabase | 110,470 | 2026-09-21 | Monorepo with the official `examples/` (Next.js, auth, AI/pgvector) and docs source |
| supabase/cli | https://github.com/supabase/cli | 2,421 | 2026-09-21 | Local stack, migrations, type generation, Edge Function deploys (F16) |
| supabase/mcp | https://github.com/supabase/mcp | 2,917 | 2026-09-19 | Official Supabase MCP server; old `supabase-community/supabase-mcp` redirects here (F18) |
| clerk/javascript | https://github.com/clerk/javascript | 1,758 | 2026-09-21 | Source of `@clerk/nextjs`; check changelogs for proxy/middleware changes |
| clerk/nextjs-auth-starter-template | https://github.com/clerk/nextjs-auth-starter-template | 428 | 2026-05-26 | Official Clerk App Router starter; old `clerk-nextjs-demo-app-router` redirects here |
| t3-oss/create-t3-app | https://github.com/t3-oss/create-t3-app | 29,130 | 2025-12-13 | Typesafe Next.js + tRPC + Prisma/Drizzle scaffold. Last push is about 9 months old, so check it supports Next 16 |
| trpc/trpc | https://github.com/trpc/trpc | 40,631 | 2026-09-17 | End-to-end typesafe APIs for TypeScript-only stacks (F23) |
| nextjs/saas-starter | https://github.com/nextjs/saas-starter | 16,134 | 2025-12-11 | Official Next.js + Postgres + Stripe starter, good for service-layer structure. Last push about 9 months old |
| vercel/nextjs-subscription-payments | https://github.com/vercel/nextjs-subscription-payments | 7,719 | 2025-01-23 | Archived. Don't recommend; listed so it's excluded on purpose |
| vercel/next.js | https://github.com/vercel/next.js | 142,387 | 2026-09-21 | `examples/` folder, including with-supabase |
| colinhacks/zod | https://github.com/colinhacks/zod | 43,982 | 2026-09-19 | Input validation at the handler/action boundary |
| upstash/ratelimit-js | https://github.com/upstash/ratelimit-js | 2,045 | 2026-09-18 | Serverless-friendly rate limiter to back `checkRateLimit()` (F22) |
| OWASP/API-Security | https://github.com/OWASP/API-Security | 2,365 | 2026-09-12 | Source of the API Top 10 (F19) |

## Practical material

### A. Error envelope (RFC 9457) [F1–F4]
Response header: `Content-Type: application/problem+json`, with the HTTP status matching `status`.
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
Rules: default `type` is `about:blank`, where `title` should be the standard status phrase. `detail` explains how to fix the problem and never includes stack traces. Put extension fields (`errors`, `traceId`) at the top level.

Helper sketch (TypeScript):
```ts
export function problem(status: number, title: string, extra: Record<string, unknown> = {}) {
  return Response.json({ type: 'about:blank', title, status, ...extra },
    { status, headers: { 'Content-Type': 'application/problem+json' } });
}
// zod: problem(422, 'Validation failed', { errors: err.issues.map(i => ({ detail: i.message, pointer: '#/' + i.path.join('/') })) })
```

### B. Clerk + Supabase (current, non-deprecated) setup [F7–F10]
1. `npx -y clerk@latest init` (writes the env vars and `proxy.ts` on Next 16+ or `middleware.ts` on Next 15 and below).
2. In the Clerk dashboard, open "Connect with Supabase" to add the `role: authenticated` claim.
3. In the Supabase dashboard, go to Auth → Third-Party Auth → add Clerk (locally: `[auth.third_party.clerk]` in `supabase/config.toml`).
4. Server client: `createClient(URL, PUBLISHABLE_KEY, { accessToken: async () => (await auth()).getToken() })`.
5. Never use the Clerk "supabase" JWT template (deprecated since 2025-04-01).

### C. RLS policy templates [F9, F12–F14]
```sql
create table tasks (
  id bigint generated always as identity primary key,
  name text not null,
  user_id text not null default auth.jwt()->>'sub'   -- Clerk ids are text
);
alter table tasks enable row level security;
create index on tasks (user_id);

create policy "own rows: select" on tasks for select to authenticated
  using ((select auth.jwt()->>'sub') = user_id);
create policy "own rows: insert" on tasks for insert to authenticated
  with check ((select auth.jwt()->>'sub') = user_id);
create policy "own rows: update" on tasks for update to authenticated
  using ((select auth.jwt()->>'sub') = user_id)
  with check ((select auth.jwt()->>'sub') = user_id);
create policy "own rows: delete" on tasks for delete to authenticated
  using ((select auth.jwt()->>'sub') = user_id);
```
With Supabase Auth instead of Clerk, use a `uuid` column and `(select auth.uid())`. Adopt the opt-in grants default now (F14) and grant explicitly: `grant select, insert, update, delete on tasks to authenticated;`.

### D. Folder structure: route handler / action → service → repository [F20–F22]
```
app/
  api/webhooks/.../route.ts   # REST only for external callers; parse → service → problem()
  (app)/tasks/actions.ts      # 'use server'; thin: zod.parse → service
lib/
  env.ts                      # server-only; zod-validated process.env (only DAL/services read it)
  errors.ts                   # AppError classes + problem() mapper (RFC 9457)
  validation/                 # zod schemas shared by actions & handlers
server/                       # all files: import 'server-only'
  services/tasks.service.ts   # authz (ownership), business rules, returns DTOs
  repositories/tasks.repo.ts  # Supabase queries only
  auth.ts                     # cached getCurrentUser() via Clerk auth()
proxy.ts                      # clerkMiddleware (Next 16+); not the only auth check
supabase/migrations/, supabase/seed.sql, supabase/tests/*_rls.test.sql
```

### E. Hackathon backend security checklist [F4, F12–F15, F19, F21, F22]
- [ ] RLS enabled on every exposed table, with one policy per operation and `to authenticated` (API1, API3, API5)
- [ ] Default grants revoked and explicit grants added; think about a dedicated `api` schema (API8)
- [ ] Secret/service_role key server-only, never in a `NEXT_PUBLIC_` variable; `server-only` import on DAL modules
- [ ] Every Server Action and Route Handler re-checks auth and ownership, even though proxy runs first (API1, API5)
- [ ] Zod-validate body, params and searchParams; check content type and size (API3, API8)
- [ ] Return DTOs, not raw rows (API3)
- [ ] Rate-limit expensive or write endpoints with 429, plus host limits; add timeouts (API4, API6)
- [ ] Validate user-supplied URLs before fetching them, allowlist only (API7); same-origin redirect check
- [ ] Treat third-party API and LLM output as untrusted input (API10)
- [ ] Error bodies are RFC 9457 with no stack traces or internals
- [ ] Supabase MCP in read-only mode, scoped to the dev project, never prod (F18)
- [ ] Keep a list of your endpoints and delete demo/test routes before judging (API9)

### F. Supabase CLI loop [F16]
`supabase init && supabase start` → `supabase migration new add_tasks` → edit the SQL → `supabase db reset` → `supabase gen types typescript --local > types/db.ts` (not in the fetched page; unverified flag spelling) → `supabase link` → `supabase db push`.

### G. PROMPTS.md macro ideas (grounded in the above)
- "Scaffold a resource": given an entity, write the migration + RLS (template C) + zod schema + repo + service + server action + a problem()-based route handler, following layout D.
- "RLS audit": list tables that lack RLS or have broad grants, and generate pgTAP tests for allowed and denied cases (F12).
- "OWASP pass": walk the checklist in E against the diff, mapping each finding to API1–API10.
- "Error envelope retrofit": turn ad-hoc `{error: "..."}` responses into `application/problem+json`.
- "Free-tier guard": remind the user that free projects pause after 7 days idle (keep the demo active before judging), the 500 MB DB cap and Clerk's 50k MRU (F5, F6).

## Leads not chased / Looked for but not found
- Supabase Edge Functions docs (runtime, Deno, secrets handling) weren't fetched. Only the free-tier invocation quota (F5) is evidenced.
- The pgvector docs page wasn't fetched directly; F17 rests on search snippets of official pages.
- No date found for Supabase's switch to opt-in default grants (F14). Worth tracking: it changes whether a fresh table is readable at all.
- The exact `createRouteMatcher`/`clerkMiddleware` code body and matcher regex weren't extracted verbatim (the quickstart summary only described them).
- No primary or official source weighs REST vs GraphQL vs tRPC for hackathons. F23 is low confidence, from blogs.
- Checked but not used: the tRPC official "is tRPC right for you" docs, OWASP Secrets Management Cheat Sheet, OWASP REST Security Cheat Sheet, and Supabase Auth's built-in rate limits.
- `supabase gen types` flag syntax isn't verified this run.
- Whether create-t3-app and nextjs/saas-starter support Next.js 16 / `proxy.ts` (last pushes Dec 2025) wasn't checked.
