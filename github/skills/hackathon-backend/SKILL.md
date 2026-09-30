---
name: hackathon-backend
description: Backend toolkit for hackathons covering Next.js 16 (proxy.ts) + Supabase (RLS, migrations) + Clerk (Third-Party Auth), RFC 9457 errors, service layers, OWASP API 2023, and AI/RAG on pgvector. Use when designing, scaffolding or reviewing a hackathon backend.
---

# Backend Toolkit

<!-- markdownlint-disable MD013 -->

> Condensed rules. Full detail: `../../03-backend/docs/` and `../../04-ai-and-rag/docs/` · macros in `../../03-backend/PROMPTS.md`. Verified 2026-09-21, updated 2026-09-23.

## Stack defaults

**Next.js 16.3.6+** · Supabase (Postgres + pgvector) · Clerk via **Supabase Third-Party Auth** · Zod · Vercel AI SDK · Upstash rate limiting.

## ⚠️ Don't use outdated patterns

| Outdated | Current |
| --- | --- |
| Clerk "Supabase JWT template" | **Deprecated since 2025-04-01.** Use Third-Party Auth: `role: authenticated` claim + supabase-js `accessToken()` |
| `middleware.ts` | **`proxy.ts`** on Next.js 16+ (and it's not your only auth check) |
| RFC 7807 | **RFC 9457** `application/problem+json` |
| Assistant prefill for JSON (Claude) | Returns 400 on 4.6+; use structured outputs or tools |
| Supabase Auth `getUser()` / `getSession()` on the server | **`getClaims()`** (verifies the signature on every call) |
| `railway add --plugin`, `supabase db seed`, "Vercel 10 s timeout" | `railway add --database`, `db reset` / `db push --include-seed`, Hobby 300 s (`../hackathon-deployment/SKILL.md`) |
| Next.js 16.2.0–16.3.5 | **Upgrade to ≥ 16.3.6** (15.x: ≥ 15.5.26). CVE-2026-94545 (CVSS 9.5): RCE in Node-runtime `next/og` `ImageResponse` when user input reaches the SVG |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` / `service_role` | **`sb_publishable_…` / `sb_secret_…`** (legacy keys deprecated by end of 2026). Env var: `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY` |
| Auth.js (NextAuth) for new projects | **Better Auth** (MIT, Vercel-owned since 2026-07; now maintains Auth.js) or Clerk |
| "Prisma is too heavy for serverless" | Outdated: Prisma 7 dropped the Rust engine |
| Relying on automatic table grants | **Explicit `GRANT` per table.** Supabase made exposure opt-in for new projects on 2026-05-30 and enforces it on all projects on **2026-10-30** |

## Speed modes

⚡ JavaScript + small validators + `{data}/{error}`, **or** 🛡️ TypeScript + Zod + RFC 9457. Pick one per project (`../../03-backend/docs/hackathon-patterns.md`). Use `DEMO_MODE` for synthetic data, keep LLM calls server-side with a pinned model, and always have a fallback.

## Architecture

- **Reads:** Server Components → server-only DAL → DTOs.
- **Mutations:** Server Actions (thin: `await auth()` → Zod → service). *Server Actions are public endpoints.*
- **REST:** Route Handlers only for webhooks and external callers.
- **Layers:** `app/` → `server/services` (authorisation, rules) → `server/repositories` (Supabase only).

## Build-safety quick wins

- **Env validation:** `@t3-oss/env-nextjs` `createEnv`, imported in `next.config.ts` so a missing variable **fails the build**, not the demo.
- **Serverless Postgres:** Supabase **transaction pooler :6543** with prepared statements off. Direct :5432 is IPv6-only.
- **Long jobs (> 300 s or retries):** **Vercel Workflows** (GA; `'use workflow'` / `'use step'`; Hobby includes 50k events a month and keeps run state 1 day) · Inngest (50k executions free) · Trigger.dev v4 ($5 credit). Vercel Queues is still beta.

## Database

**`GRANT` + RLS on every exposed table** (`grant select … to anon; grant select, insert, update, delete … to authenticated;`) · one policy per operation · `to authenticated` · `(select auth.jwt()->>'sub')` with a `text` `user_id` for Clerk · index policy columns · migrations only (`migration new` → `db reset` → `db push`) · pgTAP RLS tests.

## Security (OWASP API 2023)

Ownership checks (API1) · DTOs (API3) · rate limits with **429**, especially on LLM calls (API4/6) · allowlist fetched URLs (API7) · no `NEXT_PUBLIC_` server keys (API8) · delete test routes (API9) · treat LLM and third-party output as untrusted (API10).

## AI and RAG

Agents: see `../hackathon-ai/SKILL.md`. Sonnet 5 ($2/$10) as workhorse · Haiku 4.5 ($1/$5) for bulk · Opus 5 ($5/$25) for the judged step. RAG: ~800-token chunks + contextual prefix → pgvector **HNSW** + tsvector **hybrid (RRF k=50)** → rerank 150→20 → documents first, query last.

## Free tiers

Supabase: 2 projects, 500 MB, 50k MAU, **pauses after 7 days idle**. Clerk Hobby: 50k MRU, **fixed 7-day sessions, no MFA/passkeys**. Upstash: **500K commands a month** (not per day). Resend: 3k a month, **100 a day**. Neon: 100 CU-hours, 0.5 GB per project. Convex: 1M function calls a month.

## Related skills

AI features and agents: `../hackathon-ai/SKILL.md` · deploying: `../hackathon-deployment/SKILL.md` · something broke: `../hackathon-troubleshooting/SKILL.md` · team repo and conflicts: `../hackathon-git-teamwork/SKILL.md`.

## Sources

[Next.js GHSA-vcvr-r3jv-pc5j](https://github.com/vercel/next.js/security/advisories/GHSA-vcvr-r3jv-pc5j) · [Supabase API keys](https://supabase.com/docs/guides/getting-started/migrating-to-new-api-keys) · [t3-env](https://env.t3.gg/docs/nextjs) · [Vercel Workflows](https://vercel.com/docs/workflows) · [Upstash pricing](https://upstash.com/pricing/redis) · [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html) · [Supabase × Clerk](https://supabase.com/docs/guides/auth/third-party/clerk) · [Clerk quickstart](https://clerk.com/docs/nextjs/getting-started/quickstart) · [Next.js data security](https://nextjs.org/docs/app/guides/data-security) · [Supabase RLS](https://supabase.com/docs/guides/database/postgres/row-level-security) · [OWASP API 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10) · [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing) · [Supabase hybrid search](https://supabase.com/docs/guides/ai/hybrid-search)
