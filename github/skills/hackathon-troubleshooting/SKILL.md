---
name: hackathon-troubleshooting
description: Triage runbook for hackathon breakages covering local setup (Windows/Mac), build failures, Vercel deploys, Supabase, Clerk logins, AI API errors and live-demo failures, with a fixed check order (env → runtime → URLs → database → limits). Use when something breaks during a hackathon, an error appears, the deployed site differs from localhost, or the user says "it's broken".
---

# Troubleshooting Runbook

<!-- markdownlint-disable MD013 -->

> Condensed rules. Full detail: `../../03-backend/docs/troubleshooting.md` · deploy fixes in `../hackathon-deployment/SKILL.md` · macro **B11** in `../../03-backend/PROMPTS.md`. Built from facts verified 2026-09-21/22.

## Rules for the assistant

1. **Diagnose before editing.** Name which suspect it is (below) and why, *then* change code.
2. **Read the first error, not the last.** Ask for the full log if you only have the final line.
3. **Minimal fix only.** Don't rewrite files or "clean up" while debugging; the clock is running.
4. **Say how you'd have caught it:** one log line or check to add.
5. **Timebox 20 minutes.** Past that, propose a demo-safe fake (hardcoded result, cached response) and move on.

## Where the real error is

| Symptom location | Look at |
| --- | --- |
| Local dev | The terminal running `npm run dev` |
| Blank/broken page | Browser DevTools → Console and Network |
| Live site only | Vercel → project → Logs, or the deployment's Build Logs |
| Python/worker | `railway logs` (`--build` for build logs) |

## Check in this order

1. **ENV:** missing or misnamed var in *this* environment (local vs Vercel vs Railway). Changed a Vercel var? It needs a **redeploy**. Secrets must not start with `NEXT_PUBLIC_`.
2. **RUNTIME:** Node-only import in Edge code (`proxy.ts` on Next.js 16+, formerly `middleware.ts`).
3. **URLS:** hard-coded `localhost`; CORS origin (allow only the frontend URL, never `*` with credentials); OAuth/Clerk redirect missing the production domain.
4. **DATABASE:** RLS denying the operation (empty result, no error); missing per-table `GRANT` (`permission denied`; enforced on all Supabase projects from **2026-10-30**); direct instead of pooled connection from serverless; **free project paused after 7 days idle**.
5. **LIMITS:** Vercel Hobby 300 s function timeout (504), 4.5 MB body (413); model API 429 rate limit.

## Symptom → fix

| Symptom | Fix |
| --- | --- |
| `'node'`/`'git'` not recognized | New terminal window; else reinstall |
| `running scripts is disabled on this system` (PowerShell) | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| `EPERM`/`EBUSY` on install (Windows) | Project is in a OneDrive-synced folder; move it to e.g. `C:\dev` |
| `Module not found` | `npm install <pkg>` or fix path case |
| Errors right after `git pull` | `npm install`, restart dev server |
| Builds locally, fails on Vercel | File-name case mismatch, or env var missing at build time |
| Blank page / `undefined` in production | Missing Vercel env vars → add → redeploy |
| `FUNCTION_INVOCATION_TIMEOUT` | Stream the response; move heavy work to a worker |
| `413 FUNCTION_PAYLOAD_TOO_LARGE` | Upload directly to Supabase Storage via signed URL |
| Supabase query returns `[]` but rows exist | Add an RLS policy for that operation |
| Login works locally, not live | Add the production URL to allowed redirects |
| Next.js 16 route protection ignored | File must be `proxy.ts` |
| Clerk user rejected by Supabase | Use Supabase Third-Party Auth, not the deprecated JWT template |
| AI `401` | Key missing server-side, or wrongly `NEXT_PUBLIC_` |
| AI `429` | Back off, cache, or use a cached/rule-based fallback |
| AI `model not found` | Retired or misspelled id; pin a current one |
| Prefilled JSON returns 400 (Claude 4.6+) | Use structured outputs or a tool schema |
| Merge conflict markers `<<<<<<<` | See `../hackathon-git-teamwork/SKILL.md` |
| Site slow to load (~1 min) | Free host sleeping; warm it 5–10 min before demo |

## Broke after a merge?

Roll back first, debug second: Vercel → Deployments → last good one → **Promote to Production**.

## Live on stage

Don't debug in front of judges. Switch to the **backup video**. Wi-Fi down → phone hotspot. Logged out → seeded demo account.

## Pushed a secret?

**Rotate the key in the provider dashboard immediately.** Removing the commit is not enough.
