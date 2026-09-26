# 🧯 It Broke: Troubleshooting Manual

<!-- markdownlint-disable MD013 -->

> **In plain English:** something isn't working and the clock is ticking. Follow **"The 5-minute method"** first, then find your symptom in the tables. Every fix here comes from pages already in this toolkit, linked in the last column.

---

## The 5-minute method

**Step 1. Stop and read the actual error.** Scroll to the **first** red line, not the last one. Copy it.

**Step 2. Find where it's happening.**

| Where you see it | Where the real error is |
| --- | --- |
| Terminal running `npm run dev` | That terminal |
| Browser page is blank or broken | Browser → right-click → **Inspect** → **Console** tab |
| Only on the live site | Vercel → your project → **Logs** (or the failed deployment's **Build Logs**) |
| Python / worker backend | `railway logs` |

**Step 3. Check the usual suspects, in this order.** Most hackathon bugs are one of these five:

1. **Env vars:** a key is missing, misspelled, or set locally but not on Vercel.
2. **Runtime:** Node-only code running in the Edge runtime (`proxy.ts` / middleware).
3. **URLs:** a hard-coded `localhost`, a CORS origin, or a login redirect missing the live domain.
4. **Database:** RLS blocking the query, or the free Supabase project is paused.
5. **Limits:** a timeout, a file too large, or the AI model's rate limit.

**Step 4. Ask your AI assistant properly.** Paste prompt **B11** from [`../PROMPTS.md`](../PROMPTS.md#b11--debug-a-runtime-error) with the error, the file and the logs. It checks these same five suspects **before** changing code.

**Step 5. Timebox it.** Stuck for **20 minutes**? Tell your team, then either ask a mentor or **fake it** for the demo (hardcode the result, see [`hackathon-patterns.md`](hackathon-patterns.md)). A working fake beats a broken real feature.

---

## Won't install or start on my laptop

| Symptom | Fix | More |
| --- | --- | --- |
| `'node'` or `'git'` is not recognized | Open a new terminal. Still broken? Reinstall | [`setup-your-laptop.md`](../../01-hackathon-playbook/docs/setup-your-laptop.md) |
| `running scripts is disabled` (Windows) | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` | same |
| `EPERM` / `EBUSY` (Windows) | Move the project out of OneDrive | same |
| `Module not found: Can't resolve 'x'` | `npm install x`, or check the import path's spelling and capitals | — |
| `Port 3000 is already in use` | Another `npm run dev` is still running. Close it, or use the port Next.js suggests | — |
| Weird errors after pulling teammates' code | `npm install` (they added a package), then restart `npm run dev` | [`git-for-teams.md`](../../01-hackathon-playbook/docs/git-for-teams.md) |
| Merge conflict markers (`<<<<<<<`) in a file | Resolve the conflict | [`git-for-teams.md`](../../01-hackathon-playbook/docs/git-for-teams.md) → Part 4 |

## Build fails (`npm run build` or on Vercel)

| Symptom | Fix | More |
| --- | --- | --- |
| Type error on a line | Fix it, or ask the AI to fix **only that error**. Don't let it rewrite the file | — |
| Works locally, fails on Vercel | Case-sensitive file names (`Button.tsx` vs `button.tsx`) or a missing env var at build time | [`deploy-step-by-step.md`](deploy-step-by-step.md) |
| Stale build | Redeploy with the build cache off | [deployment skill](../../skills/hackathon-deployment/SKILL.md) |
| Railway build fails | `package.json` / `requirements.txt` isn't at the root, or set the root directory | [deployment skill](../../skills/hackathon-deployment/SKILL.md) |

## Deploy problems (works locally, broken online)

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Blank page or `undefined` values | Missing env vars on Vercel | Settings → Environment Variables → add → **Redeploy** |
| Proxy/middleware crashes | Node-only import in the Edge runtime | Move the logic out, or use the Node runtime |
| `FUNCTION_INVOCATION_TIMEOUT` (504) | Long AI or processing call | Stream the response; move heavy work to a worker |
| `413 FUNCTION_PAYLOAD_TOO_LARGE` | Upload over 4.5 MB | Upload straight to Supabase Storage with a signed URL |
| CORS error in the console | Split frontend/backend | Backend allows **only** your Vercel URL (`FRONTEND_ORIGIN`), never `*` |
| Fetch goes to `localhost` | Hard-coded URL | Use a relative path (`/api/...`) or an env var |
| Site takes ~1 minute to load | Free host went to sleep | Open it 5–10 minutes before presenting |

Source for all of the above: [`../../skills/hackathon-deployment/SKILL.md`](../../skills/hackathon-deployment/SKILL.md).

## Database (Supabase)

| Symptom | Fix | More |
| --- | --- | --- |
| Query returns an empty list but the data exists | RLS is blocking it. Add a policy for that operation | [`database-supabase.md`](database-supabase.md) |
| `permission denied for table` | Missing GRANT (see the 2026-10-30 Supabase change) | [`database-supabase.md`](database-supabase.md) |
| Connection refused from serverless | Use the **pooled** connection string | [deployment skill](../../skills/hackathon-deployment/SKILL.md) |
| Project unreachable | **Free projects pause after 7 days idle.** Restore it in the dashboard | same |
| Migration fails | Someone edited tables in the dashboard. Run `supabase db diff` first | same |

## Logins (Clerk / OAuth)

| Symptom | Fix | More |
| --- | --- | --- |
| Login works locally, fails live | Add the production URL to the allowed redirect URLs | [`auth-clerk.md`](auth-clerk.md) |
| Route protection does nothing (Next.js 16+) | The file must be `proxy.ts`, not `middleware.ts` | [`auth-clerk.md`](auth-clerk.md) |
| Supabase rejects the Clerk user | Use Supabase **Third-Party Auth**, not the old JWT template | [`auth-clerk.md`](auth-clerk.md) |

## AI feature

| Symptom | Fix | More |
| --- | --- | --- |
| `401` / `invalid api key` | Key missing on the server, or it has a `NEXT_PUBLIC_` prefix it shouldn't have | [`security.md`](security.md) |
| `429` / rate limit | Slow down, cache answers, or use a cached or rule-based fallback for the demo | [`hackathon-patterns.md`](hackathon-patterns.md) → "Graceful degradation" |
| `model not found` | Model id retired or misspelled. Use a pinned current id | [`../../04-ai-and-rag/docs/model-selection.md`](../../04-ai-and-rag/docs/model-selection.md) |
| Answers are wrong or made up | Tighten the prompt; ask for structured output | [`../../04-ai-and-rag/docs/prompt-engineering.md`](../../04-ai-and-rag/docs/prompt-engineering.md) |
| Too slow for the demo | Stream the response, and seed the demo with a cached result | [`hackathon-patterns.md`](hackathon-patterns.md) |

## Git

See [`git-for-teams.md`](../../01-hackathon-playbook/docs/git-for-teams.md) → Part 5, "Oh no" fixes. **Pushed a secret? Rotate the key first**, then clean up.

## During the live demo

| It breaks | Do this |
| --- | --- |
| Anything, live on stage | Don't debug in front of the judges. Say "let me show you the recording" and **play the backup video** |
| Venue Wi-Fi is down | Switch to your phone's hotspot (you tested this, right?) |
| Logged out | Use the pre-seeded demo account |
