# Digest: backend practices — round 2, assistant 1
Accessed: 2026-09-23 · Tool calls used: 20

## Claims
| # | Claim | Source URL | Publisher | Pub date | Confidence (high/med/low) | Class |
|---|---|---|---|---|---|---|
| 1 | next/og RCE is GHSA-vcvr-r3jv-pc5j / CVE-2026-94545, Critical (CVSS 9.5). Affected: `>= 16.2.0 < 16.3.6`; patched: 16.3.6. | https://github.com/vercel/next.js/security/advisories/GHSA-vcvr-r3jv-pc5j | Vercel (GitHub Security Advisory) | 2026-09-22 | high | security advisory |
| 2 | Root cause: the bundled upstream Satori does not escape generated SVG properly. Only the **Node.js** `ImageResponse` is affected, and only when attacker-controlled values go into SVG content, attributes or styles. The Edge `ImageResponse` is not affected. Workaround: keep untrusted input out of SVG content, attributes and styles. | same GHSA + web search summary of it | Vercel | 2026-09-22 | high | security advisory |
| 3 | Second source (Netlify) gives the same GHSA/CVE IDs. It says "prior to 15.5.26 and 16.3.6" are affected and patches are 15.5.26+ / 16.3.6+. On Netlify the impact is minimal: a crashed function does not affect other requests, but it can raise function costs. | https://www.netlify.com/changelog/2026-09-22-nextjs-imageresponse-vulnerability/ | Netlify changelog | 2026-09-22 | high (IDs); med (15.x scope) | security advisory |
| 4 | Vercel's release notes (seen through a search summary) call 15.5.26 "Maintenance LTS, hardening only". That supports the GHSA's range, which does not list 15.x as vulnerable. | web search summary (daily.dev / Vercel release) | — | 2026-09-22 | med | security advisory |
| 5 | Vercel is acquiring Better Auth (announced 2026-07-07). The founder and core team join Vercel. The library stays MIT, keeps its name and stays framework-agnostic. | https://vercel.com/blog/vercel-acquires-better-auth ; https://better-auth.com/blog/better-auth-joins-vercel | Vercel; Better Auth | 2026-07-07 | high | vendor news |
| 6 | Supabase is "deprecating the `anon` and `service_role` keys by the end of 2026". No exact removal date is given. The replacements are `sb_publishable_…` / `sb_secret_…`. | https://supabase.com/docs/guides/getting-started/migrating-to-new-api-keys | Supabase Docs | accessed 2026-09-23 | high | deprecation |
| 7 | Search summary (secondary sources plus Supabase GitHub discussions #29260 and #40300): new projects no longer get anon/service_role, and projects restored from 2025-11-01 do not get the legacy keys. | https://github.com/orgs/supabase/discussions/29260 (via search) | Supabase / secondary | — | med | deprecation |
| 8 | Supabase Next.js SSR guide: "Always use `supabase.auth.getClaims()` to protect pages and user data." "Never trust `supabase.auth.getSession()` inside server code such as Proxy." Env var: `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY`. | https://supabase.com/docs/guides/auth/server-side/nextjs | Supabase Docs | accessed 2026-09-23 | high | docs |
| 9 | Clerk: "the native Supabase integration is the recommended way". The Clerk Supabase JWT template has been deprecated since 2025-04-01. Pass Clerk's session token through the `accessToken()` option; the integration adds `role: authenticated`. | https://clerk.com/docs/integrations/databases/supabase | Clerk Docs | accessed 2026-09-23 | high | docs |
| 10 | Upstash Redis free tier: 500K commands **per month** (about 16.7K/day if averaged; that per-day figure is our own calculation), 256 MB storage, 10 GB bandwidth/month, up to 10 free databases, no credit card. | https://upstash.com/pricing/redis | Upstash | accessed 2026-09-23 | high | free tier |
| 11 | Vercel Workflows is **GA** (announced 2026-04-16). The Python SDK is in beta. Docs updated 2026-09-04. Package: `workflow`. Directives: `'use workflow'` / `'use step'`. | https://vercel.com/docs/workflows ; https://vercel.com/blog/a-new-programming-model-for-durable-execution (via search) | Vercel | 2026-04-16 / 2026-09-04 | high | version/status |
| 12 | Workflows on Hobby: 50,000 events/month and 1 GB data written included. Data Retained is not available on Hobby; run state is kept 1 day after completion. One step uses about 3 events (created/started/completed). Queues usage is billed separately. | https://vercel.com/docs/workflows/pricing | Vercel Docs | 2026-09-16 | high | free tier |
| 13 | Vercel Queues is still **Beta** ("public beta"; the consumer trigger type is `queue/v2beta`, under `experimentalTriggers`). Package: `@vercel/queue`. It is the primitive underneath Workflows. | https://vercel.com/docs/queues | Vercel Docs | 2026-09-03 | high | status |
| 14 | Inngest Free: 50,000 executions/month, 5 concurrent steps, 500K events/month, 24h trace history, no credit card. | https://www.inngest.com/pricing | Inngest | accessed 2026-09-23 | high | free tier |
| 15 | Trigger.dev Free: $5/month free credits, 20 concurrent runs, 10 schedules, 1-day log retention, 5 members. Current line is v4.x (the changelog mentions v4.6.4). | https://trigger.dev/pricing | Trigger.dev | accessed 2026-09-23 | med-high (version from a changelog reference) | free tier / version |
| 16 | t3-env: package `@t3-oss/env-nextjs`, function `createEnv`, with `server` / `client` (`NEXT_PUBLIC_`) sections. `experimental__runtimeEnv` works on Next ≥13.4.4. It accepts Zod or any Standard Schema validator. Importing the env file in `next.config.ts` validates variables at build time. | https://env.t3.gg/docs/nextjs | T3 OSS | accessed 2026-09-23 | high | docs |
| 17 | Resend Free: 3,000 emails/month, **100/day** cap, 3 domains. | https://resend.com/pricing | Resend | accessed 2026-09-23 | high | free tier |
| 18 | Neon Free: 100 CU-hours per project per month, 0.5 GB storage per project (writes blocked past that), up to 100 projects, 10 branches per project, scales to zero after 5 minutes, no credit card. | https://neon.com/pricing | Neon | accessed 2026-09-23 | high | free tier |
| 19 | Convex Free/Starter: 1M function calls/month, 0.5 GB database, 1 GB file storage, 1 GB egress, 1–6 developers, pay-as-you-go above the limits. | https://www.convex.dev/pricing | Convex | accessed 2026-09-23 | med (the fetch summary may have simplified the free vs. Starter split) | free tier |

## Verification of round-1 claims
- **Critical RCE in next/og ImageResponse affecting 16.2.0 up to 16.3.6** → **VERIFIED** (GHSA-vcvr-r3jv-pc5j, CVE-2026-94545, `>=16.2.0 <16.3.6`, fixed in 16.3.6, published 2026-09-22; Netlify is the second source). Correction: the round-1 wording "pin ≥16.3.6" is right. Add a note that it only affects the Node.js runtime `ImageResponse` fed untrusted input. 15.x users should move to 15.5.26 (Netlify lists it as a fix; Vercel calls it hardening).
- **Better Auth joined Vercel 2026-07-07** → **VERIFIED** (Vercel blog and Better Auth blog). Precise wording: Vercel *acquired* Better Auth; the library stays MIT.
- **anon/service_role keys deprecated end-2026** → **VERIFIED** (Supabase migration docs). No exact day-level removal date is published.
- **Supabase `getClaims()` recommended server-side** → **VERIFIED** (current Next.js SSR guide).
- **Clerk ↔ Supabase Third-Party Auth recommended** → **VERIFIED** (Clerk docs; the JWT template is deprecated).
- Next.js 16.3 current / Supabase GRANT dates / Prisma 7 / FastAPI 0.141.1 / Auth.js maintained by Better Auth → **not re-checked this round** (outside my question set or out of budget).

## Notes for synthesis
- Security box for the cheat sheet: "Run `next@16.3.6`+ (or `15.5.26`+ on 15.x). If you build OG images with `next/og` on the Node runtime, never put raw user input into it without escaping." Cite both the GHSA and the CVE.
- Upstash is a **monthly** quota (500K/month), not daily. If the cheat sheet says "10K/day", that is out of date.
- Resend's 100/day cap matters for hackathon demos that send many emails. Test with your own addresses.
- Background jobs, in order of simplicity for a Vercel-hosted hackathon app: Vercel Workflows (GA, 50K events/month on Hobby, no extra account) > Inngest (50K executions/month free) ≈ Trigger.dev v4 ($5 credit/month). Avoid using raw Vercel Queues in a beginner guide because it is still Beta.
- The Workflows Hobby tier keeps run state for only 1 day. That is fine for a hackathon but worth saying.
- t3-env: import `./env` in `next.config.ts` so builds fail fast when a variable is missing. This is the documented fix for "env var missing in production".
- Supabase's Next.js env var name is now `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY`. Update code snippets that still use `..._ANON_KEY`.

## Looked for but could not find
- An NVD entry for CVE-2026-94545 (not fetched, budget). The second source is Netlify instead.
- An exact removal day for the legacy Supabase keys; the docs only say "end of 2026".
- Q5 primary sources not fetched (budget): Stripe/Clerk (svix) webhook verification docs, Supabase Storage `createSignedUploadUrl`, Stripe Sandboxes.
- Q6 not fetched: Firebase Spark, Cloudflare Workers/D1 free tiers.
- Q7 (CORS in Route Handlers, serverless connection exhaustion/poolers): no sources retrieved; left for another round. Only the env-var-at-build fix is sourced (t3-env).
