# 🚀 Put Your App Online: A Step-by-Step Manual

<!-- markdownlint-disable MD013 -->

> **In plain English:** your first deploy, using only the website (no command line). You'll end up with a real link like `https://your-app.vercel.app` that judges can open on their phones, and it **updates by itself every time you push to GitHub**.
>
> **When:** in the **first hour** of the event, while the app still only says "hello". **Time needed:** 10 minutes.
>
> Using a Python backend, the CLI, or a different host? Use the full runbook: [`../../skills/hackathon-deployment/SKILL.md`](../../skills/hackathon-deployment/SKILL.md).

---

## Before you start

- [ ] Your Next.js app runs on your laptop (`npm run dev` works)
- [ ] It's pushed to a GitHub repo ([`../../01-hackathon-playbook/docs/git-for-teams.md`](../../01-hackathon-playbook/docs/git-for-teams.md))
- [ ] You have a Vercel account created **with "Continue with GitHub"**

## Step 1 · Check it builds

On your laptop, run:

```bash
npm run build
```

If this fails, the deploy will fail too. Fix the error first (see [`troubleshooting.md`](troubleshooting.md)).

## Step 2 · Import the repo into Vercel

1. Go to [vercel.com](https://vercel.com) → **Add New…** → **Project**.
2. Find your repo in the list → **Import**. (Can't see it? Click **Adjust GitHub App Permissions** and allow that repo.)
3. Leave the framework as **Next.js** and the other settings as they are.

## Step 3 · Add your secrets (environment variables)

Still on the import screen, open **Environment Variables**. Copy each line from your `.env.local`, **one key per row**:

| Key | Value |
| --- | --- |
| `NEXT_PUBLIC_SUPABASE_URL` | `https://xxxx.supabase.co` |
| `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY` | `sb_publishable_…` (older projects: the legacy `anon` key, deprecated by end of 2026) |
| `ANTHROPIC_API_KEY` *(or your model's key)* | `sk-…` |

> ⚠️ Only keys that are safe for anyone to see may start with `NEXT_PUBLIC_`. Secret keys must **not** have that prefix, or they get sent to every visitor's browser. See [`security.md`](security.md).

No database or AI yet? Skip this step and add the keys later (Step 6).

## Step 4 · Deploy

Click **Deploy**. Wait 1–2 minutes. When the confetti appears, click the preview image to open your live site.

**Copy the URL and post it in your team chat right away.**

## Step 5 · Test it like a judge

- [ ] Open the URL on your **phone, using mobile data** (not the venue Wi-Fi)
- [ ] Click through the main feature
- [ ] If anything is blank or broken, go to [`troubleshooting.md`](troubleshooting.md) → "Deploy problems"

## Step 6 · From now on, it's automatic

| You do | Vercel does |
| --- | --- |
| Push or merge to `main` | Rebuilds and updates your **production** URL |
| Push a branch or open a PR | Makes a separate **preview** URL, so you can test before merging |
| Add or change an env var (Project → **Settings** → **Environment Variables**) | **Nothing yet.** You must **redeploy**: Deployments → ⋯ → **Redeploy** |

## Step 7 · Add the production URL everywhere it's needed

Once you have a live URL, add it to:

- [ ] **Clerk / OAuth** allowed redirect URLs (logins break without this) → [`auth-clerk.md`](auth-clerk.md)
- [ ] **Supabase** → Authentication → URL Configuration, if you use Supabase Auth
- [ ] Your project README (`../../01-hackathon-playbook/templates/project-readme.md`)

## If the demo breaks after a merge

Vercel → **Deployments** → find the last one that worked → ⋯ → **Promote to Production**. Your site goes back to that version in seconds. Fix the bug calmly, then push again.

---

## Before you present

Run the **pre-pitch checklist** at the bottom of [`../../skills/hackathon-deployment/SKILL.md`](../../skills/hackathon-deployment/SKILL.md), and open the live URL **5–10 minutes before** you present so nothing is asleep.
