# Digest: backend practices — round 1, assistant 1
Accessed: 2026-09-23 · Tool calls used: 20 (1 ToolSearch + 19 web)

## Claims
| # | Claim | Source URL | Publisher | Pub date | Confidence (high/med/low) | Class |
|---|---|---|---|---|---|---|
| 1 | Next.js 16 released 2025-10-21; middleware.ts renamed proxy.ts; proxy runs on Node.js runtime | https://nextjs.org/blog/next-16 (via search summary); https://nextjs.org/docs/app/getting-started/proxy | Vercel / Next.js | 2025-10-21 | high | version |
| 2 | Latest stable minor is Next.js 16.3 (2026-08-03), with "Instant Navigations", Partial Prefetching, Cache Components (PPR + `use cache`) | https://nextjs.org/blog | Vercel / Next.js | 2026-08-03 | high | version |
| 3 | Current patch: 16.3.6 (Active LTS) / 15.5.26 (Maintenance LTS), out-of-band release 2026-09-22 | https://nextjs.org/blog/nextjs-security-update-september-22-2026 | Vercel / Next.js | 2026-09-22 | high | version |
| 4 | Critical RCE GHSA-vcvr-r3jv-pc5j in Node.js `ImageResponse` (`next/og`, via Satori): affects >=16.2.0 <16.3.6; Edge ImageResponse unaffected | same as #3 | Vercel / Next.js | 2026-09-22 | high | deprecation |
| 5 | August 2026 security release fixed two Critical vulns (16.3.3 / 15.5.24); earlier RSC CVEs include CVE-2025-66478 (Critical RCE), CVE-2025-55184 (DoS), CVE-2025-55183 (source exposure) | https://nextjs.org/blog | Vercel / Next.js | 2026-08-25 | high | practice |
| 6 | Supabase legacy `anon`/`service_role` keys are deprecated "by the end of 2026"; replaced by `sb_publishable_...` and `sb_secret_...`; both systems work at once until legacy is disabled | https://supabase.com/docs/guides/getting-started/api-keys ; https://supabase.com/docs/guides/getting-started/migrating-to-new-api-keys | Supabase | current docs | high | deprecation |
| 7 | Secret keys return HTTP 401 when used from a browser (User-Agent match); secret key bypasses RLS | https://www.guardlayer.io/blog/supabase-publishable-secret-api-keys (search summary; secondary) | GuardLayer | n/d | med | practice |
| 8 | Breaking change: new public-schema tables NOT auto-exposed to Data API/GraphQL. Opt-in 2026-04-28; default for new projects 2026-05-30; enforced on all existing projects 2026-10-30 | https://supabase.com/changelog/45329-breaking-change-tables-not-exposed-to-data-and-graphql-api-automatically ; https://github.com/orgs/supabase/discussions/45329 | Supabase | 2026-04/05 | high | deprecation |
| 9 | Required pattern per table: `grant select ... to anon; grant select, insert, update, delete ... to authenticated; ... to service_role;` plus RLS + policies. Forgetting yields PostgREST "permission denied for table X. Grant the required privileges ..." | same as #8 | Supabase | 2026 | high | practice |
| 10 | Supabase Free: 2 active projects, 500 MB DB, 50,000 MAU, 1 GB file storage, 5 GB egress + 5 GB cached egress, unlimited API requests, paused after 1 week inactivity. Pro $25/mo | https://supabase.com/pricing | Supabase | accessed 2026-09-23 | high (single primary source) | free-tier |
| 11 | Clerk Hobby (free): 50,000 MRU per app (1-month grace), unlimited apps, 3 dashboard seats, up to 3 social providers, webhooks, bot protection; excludes MFA, passkeys, SMS, custom-domain branding removal, enterprise SSO; "First Day Free" (users not counted until they return after 24h) | https://clerk.com/pricing | Clerk | accessed 2026-09-23 | high (single primary source) | free-tier |
| 12 | OWASP API Security Top 10 2023 is still the latest edition; the "2025" Top 10 is the separate web-app list | https://nordicapis.com/owasp-top-ten-2025-key-security-risks-for-apis-and-applications/ ; https://owasp.org/Top10/2025/0x00_2025-Introduction/ (search summaries; primary OWASP API page redirected, not read) | Nordic APIs / OWASP | 2025 | med | version |
| 13 | Zod 4 is stable; latest npm reported as 4.6.5 | https://www.npmjs.com/package/zod (search summary); https://zod.dev/v4 | Zod / npm | ~2026-09 | med (version number single-sourced via search snippet) | version |
| 14 | Auth.js (NextAuth) is now maintained by Better Auth team (security patches only); new projects are told to use Better Auth | https://better-auth.com/blog/authjs-joins-better-auth ; https://github.com/nextauthjs/next-auth/discussions/13252 | Better Auth / Auth.js | 2025 | high | alternative |
| 15 | Better Auth joined Vercel (announced 2026-07-07); remains open-source and framework-agnostic; continues maintaining Auth.js; adds Agent Auth Protocol focus | https://better-auth.com/blog/better-auth-joins-vercel | Better Auth | 2026-07-07 | high | alternative |
| 16 | Prisma ORM 7.0 (changelog 2025-11-19): Rust-free TS client is default, generated code out of node_modules, new config file, provider `prisma-client` replaces `prisma-client-js` | https://www.prisma.io/changelog/2025-11-19 ; https://www.infoq.com/news/2026/01/prisma-7-performance/ | Prisma / InfoQ | 2025-11 / 2026-01 | high | version |
| 17 | FastAPI latest 0.141.1 (2026-07-29); install via `uv add "fastapi[standard]"`; `fastapi dev` hot-reload; Python >=3.10 (to 3.14); FastAPI Cloud one-command deploy | https://pypi.org/project/fastapi/ | PyPI | 2026-07-29 | high (single primary) | version |
| 18 | Vercel Workflow DevKit (`"use workflow"`, durable `sleep`) announced public beta Oct 2025; GA status not confirmed in retrieved sources | https://vercel.com/changelog/open-source-workflow-dev-kit-is-now-in-public-beta ; https://vercel.com/docs/workflows | Vercel | 2025-10 | low (for current status) | practice |
| 19 | Supabase serverless: use shared pooler transaction mode (port 6543); transaction mode does not support prepared statements (disable in driver); direct connections are IPv6 by default (IPv4 add-on needed); session pooler 5432 is IPv4 | https://supabase.com/docs/guides/database/connecting-to-postgres | Supabase | current docs | high | failure-mode |

## Currency check results
- **Next.js 16 / proxy.ts replacing middleware.ts**: still-current. Update version guidance to "Next.js 16.3.x, pin >=16.3.6" (critical RCE in `next/og` ImageResponse <16.3.6). Cache Components / `use cache` are now the headline caching model in 16.x; 16.3 adds Instant Navigations / Partial Prefetching. Server Actions: blog references enhanced security in v15+, no new specifics retrieved — unverified beyond that.
- **Supabase RLS**: still-current, but CHANGED — RLS alone is no longer sufficient to make a table reachable. Explicit GRANTs required for new projects since 2026-05-30 and for all projects from 2026-10-30. Cheat sheet migrations template must include grants.
- **Supabase migrations**: still-current (not separately re-verified), but migration template needs grant statements (see above).
- **Supabase keys**: CHANGED — use `sb_publishable_` / `sb_secret_`; anon/service_role deprecated by end of 2026.
- **pgvector**: unverified this run.
- **getClaims()**: unverified this run (not mentioned on API keys page).
- **Clerk via Supabase Third-Party Auth**: unverified this run (only Clerk pricing checked). Free tier = 50k MRU.
- **Zod**: still-current as v4 (4.6.x reported; single-source).
- **RFC 9457**: unverified (stable RFC; not searched).
- **Upstash rate limiting**: unverified this run.
- **OWASP API Top 10 2023**: still-current (no API-specific 2025 edition found; don't confuse with OWASP Top 10:2025 web list). Medium confidence.

## Notes for synthesis
- The single most important cheat-sheet fix: Supabase grants. A beginner following an "enable RLS + write policy" recipe on a new project will get "permission denied for table" errors. Add the 3-line grant block to every table migration. Timing matters: 2026-10-30 enforcement lands during the hackathon season.
- Add a "pin versions" line: `next@16.3.6+`, and a habit of checking nextjs.org/blog security posts; Next.js has had multiple Critical advisories in the past year (RSC RCE 2025, two in Aug 2026, one Sep 2026).
- Auth landscape shift: Auth.js is effectively maintenance-only; Better Auth (now Vercel-owned, still OSS) is the recommended self-hosted option. Clerk free tier generous (50k MRU) but no MFA/passkeys on free.
- ORM: Prisma 7 removed the Rust engine, which removes the old serverless/edge bundle-size and cold-start complaints; old "Prisma is heavy on serverless" advice is outdated. Drizzle comparison not retrieved.
- Python path: `uv add "fastapi[standard]"` + `fastapi dev` is the current official quickstart; FastAPI still 0.x (0.141.1).
- Serverless Postgres failure mode: transaction pooler 6543 + disable prepared statements (e.g. Prisma/postgres.js settings); direct 5432 connection fails on IPv4-only networks/hosts.
- Background jobs: Vercel Workflow DevKit exists (`"use workflow"`) but its GA status is unconfirmed; treat as beta unless round 2 confirms.

## Leads worth chasing
- Next.js 16.3 release post (https://nextjs.org/blog) for Cache Components defaults and any Server Actions changes; August 2026 security release details.
- Supabase `getClaims()` docs and asymmetric JWT signing keys; Clerk Third-Party Auth integration page for current setup steps.
- https://supascale.app/blog/supabase-october-2026-breaking-change-data-api-grants-explai (secondary explainer).
- Neon pricing page (fetch failed to yield numbers) — also Neon/Databricks free tier changes.
- Vercel Workflow docs (https://vercel.com/docs/workflows) for GA/pricing; Inngest and Trigger.dev free tiers.
- Convex, Firebase, PocketBase, Cloudflare D1 free tiers; Resend free tier; Stripe test mode/sandboxes; t3-env status; tRPC vs oRPC vs Hono; Drizzle 1.0 status; SQLModel version.
- Primary OWASP API page: http://api-security.owasp.org/ (redirect target, not fetched).

## Looked for but could not find
- Neon free-tier numbers (pricing page fetch returned no content).
- Confirmation of Vercel Workflow GA (only 2025 beta sources surfaced).
- Primary OWASP confirmation of no API Top 10 2025 (redirect not followed within budget).
- Not researched within budget: getClaims, Clerk TPA, Upstash, RFC 9457, pgvector, Inngest/Trigger.dev, webhooks verification, signed-URL uploads, env validation, tRPC/oRPC/Hono, Drizzle, realtime, Stripe, Resend, health checks/logging, seed data, Convex/Firebase/PocketBase/Cloudflare free tiers, SQLModel, uv version, practitioner post-mortems (CORS, env vars on deploy, cold starts).
