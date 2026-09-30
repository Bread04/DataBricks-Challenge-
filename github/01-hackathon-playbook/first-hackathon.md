# 🌱 Your First Hackathon, in Plain English

<!-- markdownlint-disable MD013 -->

> No experience needed. This is the short version; the detailed hour-by-hour plan is in [`battle-plan.md`](battle-plan.md). Don't know a word? Check [`../GLOSSARY.md`](../GLOSSARY.md).
>
> You'll use the **BMad Method** in Claude Code to guide each step (explained below), with copy-paste prompts as a backup.

---

## What actually happens

1. **Kickoff:** organisers announce the theme, rules, prizes and judging criteria.
2. **You pick an idea** and build a small, working version of it.
3. **Judging:** you show it working (the *demo*) and explain it (the *pitch*), usually in 2–4 minutes.

Judges don't expect a finished product. They reward **a simple idea that clearly works** over a big idea that half-works.

---

## How you'll work: the BMad Method

This toolkit runs the whole hackathon with **BMad**, a free set of step-by-step skills for **Claude Code** (an AI coding assistant that runs in your terminal). Instead of working out what to ask the AI, you run one command per step and it asks *you* the right questions:

```text
/bmad-brainstorming  →  /bmad-spec  →  /bmad-build (one story at a time)  →  /bmad-code-review  →  /bmad-cis-storytelling
     pick an idea         plan it           build it                          check it                 pitch it
```

Three rules make it work:

1. **One command per fresh chat.** Each step saves a file; the next step reads it.
2. **You still make the decisions.** BMad suggests ideas and scope; your team picks.
3. **Lost? Type `/bmad-help`.** It reads your files and tells you the next step.

> **No Claude Code?** Claude Code is 💳 paid. Every step below has a **copy-paste prompt** in [`PROMPTS.md`](PROMPTS.md) that does the same job in any AI tool, including free ones ([options](../05-tools-and-mcp/docs/free-ai-dev-tools.md)).

---

## Before the event (the week before)

- [ ] Make free accounts: **GitHub**, **Vercel** (hosting) and **Supabase** (database). Students should also claim the free [GitHub Student Pack](docs/free-credits.md).
- [ ] Set up your laptop: Node.js, git and VS Code ([step by step](docs/setup-your-laptop.md)).
- [ ] **Install Claude Code and practise BMad once** on a throwaway folder ([step by step](docs/setup-bmad.md), Part A).
- [ ] Read the event's rules. Some events **don't allow code written before the event**, and many require you to **say how you used AI**.
- [ ] Skim the [default hackathon kit](../06-repo-catalog/README.md) so you know which tools you'll use.

## During the event: 5 phases

| Phase | What to do | Run this (BMad) | No Claude Code? |
| --- | --- | --- | --- |
| **0 · Set up** (first 15 min) | Create the repo, install BMad and the toolkit's config pack, fill in `project-context.md` with the rules and rubric | [`docs/setup-bmad.md`](docs/setup-bmad.md) Part B | Copy [`templates/`](templates/) into `docs/` |
| **1 · Idea** (first hour) | Pick a problem a *real person* has. Choose **one** main feature. | `/bmad-brainstorming` → `/bmad-forge-idea` | Prompt **I1**, then **I2** |
| **2 · Plan** (next hour) | Write down what it does, what you *won't* build, and what the demo will show. Split it into small stories. | `/bmad-spec`, then *"break this into stories"* | **S1** + [PRD template](templates/prd.md), then **S2** |
| **3 · Skeleton** (hours 2–4) | Get a basic page **online** with a working link, even if it only says "hello". | `/bmad-build story 1` + [deploy guide](../03-backend/docs/deploy-step-by-step.md) | **S3** + the deploy guide |
| **4 · Build** (most of the time) | Add features one story at a time. Save (commit) after each one. Check progress at halfway. | `/bmad-build story 2, 3…` (fresh chat each) · `/bmad-correct-course` at halfway | Folder `PROMPTS.md` files · **M1** at halfway |
| **5 · Finish** (last 3–4 hours) | **Stop adding features.** Check, fix, add example data, record a backup video, practise the pitch. | `/bmad-code-review` · `/bmad-cis-storytelling` · `/bmad-party-mode` (practice judges) | **M2**, **P1**, **P2** |

Submit **1 hour early**. The full hour-by-hour version is [`battle-plan.md`](battle-plan.md); a complete example is [`worked-example.md`](worked-example.md).

## The pitch (about 3 minutes)

1. **The problem** (20 seconds): who is struggling, and why.
2. **Your solution** (1 sentence).
3. **Live demo** (about 90 seconds): show it actually working.
4. **How it works** (30 seconds): mention the tools and sponsor products you used.
5. **Why it matters** (15 seconds): the impact, and what's next.

Write the script yourself and record your own voice. Some events ban AI voiceovers. More help: [`docs/pitch-and-demo.md`](docs/pitch-and-demo.md).

---

## Look after yourself (it affects your score)

Tired teams make careless mistakes in the last 3 hours, which is exactly when the pitch and the demo happen.

1. **Sleep at least 3–4 hours** on a 24-hour event. Take turns, so someone is always awake to watch the deploy.
2. **Eat proper meals** when the organisers serve them. Go easy on energy drinks after midnight.
3. **Drink water.** Keep a bottle at the desk.
4. **Take a 5-minute walk every 2 hours.** Being stuck on a bug is a good time to go.
5. **Pack:** laptop and phone chargers, an extension lead, headphones, a hoodie (venues get cold at night), toiletries, and any medication.
6. **The presenter sleeps before the pitch.** A rested speaker beats one extra feature.

---

## Beginner mistakes to avoid

| Mistake | Do this instead |
| --- | --- |
| Trying to build everything | Build **one** feature really well |
| Putting the app online at the very end | Get it online in the first few hours |
| Putting API keys or passwords in your code | Keep them in `.env`, which is never uploaded |
| An empty app during the demo | Load example data first ("seed data") |
| No plan if the Wi-Fi or demo fails | Record a **backup video** before you present |
| Coding until the last minute | Stop features 3 hours before, then polish and practise |

---

## Where to go next

- **See it all in action:** [`worked-example.md`](worked-example.md), one fictional team from idea to prize
- **Set up your laptop:** [`docs/setup-your-laptop.md`](docs/setup-your-laptop.md)
- **Set up BMad:** [`docs/setup-bmad.md`](docs/setup-bmad.md)
- **Working in a team:** [`docs/git-for-teams.md`](docs/git-for-teams.md)
- **Something broke:** [`../03-backend/docs/troubleshooting.md`](../03-backend/docs/troubleshooting.md)
- **The full plan:** [`battle-plan.md`](battle-plan.md)
- **Copy-paste prompts for your AI:** [`PROMPTS.md`](PROMPTS.md)
- **Making it look good:** [`../02-frontend/`](../02-frontend/README.md)
- **Spending nothing:** [`../05-tools-and-mcp/docs/free-ai-dev-tools.md`](../05-tools-and-mcp/docs/free-ai-dev-tools.md)
