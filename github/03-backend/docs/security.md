# 🛡️ Security-First Checklist

<!-- markdownlint-disable MD013 -->

> Mapped to the **OWASP API Security Top 10 (2023)**, which is still the latest edition. Verified 2026-09-21.

---

## OWASP API Top 10 (2023) → what it means for your stack

| # | Risk | Next.js + Supabase control |
| --- | --- | --- |
| API1 | Broken Object Level Authorization | RLS on every table; services check ownership; never trust IDs from the client |
| API2 | Broken Authentication | Clerk/Supabase Auth only; no home-made auth; `await auth()` in every action |
| API3 | Broken Object Property Level Authorization | Return **DTOs**, not raw rows; Zod-whitelist writable fields |
| API4 | Unrestricted Resource Consumption | Rate-limit writes and LLM calls (429); body-size limits; timeouts |
| API5 | Broken Function Level Authorization | Role checks in services; admin actions behind explicit checks |
| API6 | Unrestricted Access to Sensitive Business Flows | Rate-limit sign-up, invites and AI generation |
| API7 | Server-Side Request Forgery | Allowlist any user-supplied URL before fetching |
| API8 | Security Misconfiguration | Revoke default grants; RLS on; no service key in the client; CORS tight |
| API9 | Improper Inventory Management | Delete demo and test routes; keep a list of endpoints |
| API10 | Unsafe Consumption of APIs | Treat third-party **and LLM output** as untrusted input; validate it |

Source: [OWASP API Security Top 10 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10) · [OWASP/API-Security](https://github.com/OWASP/API-Security)

---

## Pre-demo security checklist (15 minutes)

### Secrets

- [ ] `git log -p | grep -iE "sk_|secret|service_role|api[_-]?key"` returns nothing real
- [ ] No server key behind a `NEXT_PUBLIC_` prefix. The Supabase `service_role`/secret key must **never** reach browsers ([Supabase](https://supabase.com/docs/guides/api/securing-your-api))
- [ ] `.env*` is in `.gitignore`; `.env.example` has names only
- [ ] Keys you pasted into chats or screenshots have been rotated

### Authorization responses

- [ ] Return **404 (not 403)** when a user requests a resource they don't own, so you don't confirm it exists (from help-me-papi `security-decisions.md`)
- [ ] Generic login errors that never reveal whether an email exists

### Database

- [ ] RLS enabled on every exposed table, one policy per operation, `to authenticated`
- [ ] Default grants revoked and explicit grants added
- [ ] Policy columns indexed

### Server code

- [ ] Every Server Action re-checks auth and ownership. **Server Actions are public POST endpoints** ([Next.js](https://nextjs.org/docs/app/guides/data-security))
- [ ] DAL modules have `import 'server-only'`
- [ ] Zod validation on all inputs; content type and size checked
- [ ] Error bodies are RFC 9457 with **no** stack traces or internals
- [ ] Rate limit on expensive endpoints, especially **LLM calls**, which cost you money

### AI-specific

- [ ] The system prompt never contains secrets
- [ ] LLM output is validated (structured outputs plus a Zod parse) before it touches the DB or the UI as HTML
- [ ] Per-user or per-IP limits on generation endpoints

### Tooling

- [ ] Supabase MCP in **read-only** mode, scoped to the dev project, **never production** ([Supabase MCP](https://supabase.com/docs/guides/getting-started/mcp))
- [ ] The committed `.mcp.json` uses `${VAR}` placeholders, not literal keys

---

## Rate limiting notes

- Next.js recommends returning **429** from Route Handlers and also turning on host-level limits ([Next.js](https://nextjs.org/docs/app/guides/backend-for-frontend)).
- Supabase's own Data API rate-limit example (100 writes per IP per 5 min, via a pre-request function) returns a non-standard **420**. Change it to 429 if you copy it ([Supabase](https://supabase.com/docs/guides/api/securing-your-api)).
- For serverless apps, [upstash/ratelimit-js](https://github.com/upstash/ratelimit-js) is a drop-in.

This sketch follows the common `@upstash/ratelimit` usage but wasn't checked against the current README in this research:

```ts
// server/ratelimit.ts
import { Ratelimit } from '@upstash/ratelimit';
import { Redis } from '@upstash/redis';

export const aiLimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(10, '1 m'), // 10 generations / minute / key
});

// in a route/action:
// const { success } = await aiLimit.limit(userId ?? ip);
// if (!success) return problem(429, 'Too many requests', { detail: 'Try again in a minute.' });
```
