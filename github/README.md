# 🧰 Hackathon Toolkit

<!-- markdownlint-disable MD013 -->

> **A guide to building something impressive at a hackathon with AI coding tools**, even if you're new to this.
> It runs the whole event on the **BMad Method**: step-by-step skills for Claude Code that take you from idea → plan → build → check → pitch. Every step also has a copy-paste prompt if you don't have Claude Code.

---

## 👋 New here? Start with these steps

| Step | Open this | Time |
| --- | --- | --- |
| **1. Understand the event** | [`01-hackathon-playbook/first-hackathon.md`](01-hackathon-playbook/first-hackathon.md): your first hackathon in plain English, and how BMad guides each step | 10 min |
| **2. Set up BMad** | [`01-hackathon-playbook/docs/setup-bmad.md`](01-hackathon-playbook/docs/setup-bmad.md): install Claude Code and practise once, the week before | 45 min |
| **3. See it done** | [`01-hackathon-playbook/worked-example.md`](01-hackathon-playbook/worked-example.md): one team's whole hackathon, skill by skill | 10 min |
| **📊 Entering a Datathon / ML Track?** | [`08-datathon-handbook/first-datathon.md`](08-datathon-handbook/first-datathon.md): The beginner's guide to data hackathons, 1-click starter & ML solutions | 10 min |

Words you don't know? [`GLOSSARY.md`](GLOSSARY.md). On the day, follow [`battle-plan.md`](01-hackathon-playbook/battle-plan.md) hour by hour.

That's enough to get started. Everything else is here for when you need it.

---

## 🗺️ What's in each folder

The folders are numbered in the order you'll need them.

| Folder | In plain English | Level |
| --- | --- | --- |
| 📘 [`01-hackathon-playbook/`](01-hackathon-playbook/README.md) | **The game plan.** The BMad workflow hour by hour: setup, idea, plan, build, pitch, after | 🟢 Start here |
| 🎨 [`02-frontend/`](02-frontend/README.md) | **What people see.** Making the app look good and work on phones | 🟢/🟡 |
| ⚙️ [`03-backend/`](03-backend/README.md) | **The engine behind the scenes.** Database, logins, keeping it secure, putting it online | 🟡 |
| 🤖 [`04-ai-and-rag/`](04-ai-and-rag/README.md) | **Adding AI to your app.** Choosing a model, writing prompts, agents and tools, chatbots over your own documents, voice | 🟡 |
| 🔧 [`05-tools-and-mcp/`](05-tools-and-mcp/README.md) | **Supercharging your AI assistant.** Plug-ins (MCP servers), free tools, staying safe | 🟡 |
| ⭐ [`06-repo-catalog/`](06-repo-catalog/README.md) | **The shopping list.** Recommended free libraries, and ones to avoid | 🟢 |
| 🧠 [`07-bmad-workflow/`](07-bmad-workflow/README.md) | **The BMad engine room.** The config pack that wires this toolkit into BMad, a verdict on every BMad skill, and how the wiring works. Open it when setup asks you to, or to customise | 🟡 |
| 📊 [`08-datathon-handbook/`](08-datathon-handbook/README.md) | **The Datathon Playbook.** For data science & ML competitions: dirty data wrangling (Polars/DuckDB), rapid ML baselines (LightGBM/CatBoost/AutoGluon), leak-free CV, What-If simulators, and winning pitch decks | 🟢/🟡 |
| 📄 [`skills/`](skills/README.md) | **One-page cheat sheets** you can load into Claude Code | 🟢 |
| 🔬 [`_research/`](_research/README.md) | **The proof.** Where every fact came from. You never need to open this | 📚 Reference |

**Level key:** 🟢 beginner-friendly · 🟡 read it when you need it · 🔴 advanced · 📚 reference only

### How the pieces fit

```text
01 playbook ── tells you WHICH BMad skill to run, and when (Software hackathons)
08 datathon handbook ── guides data wrangling, ML modeling & interactive UI (Datathons)
   │
   ▼
BMad skills in Claude Code ── do the work, one fresh chat per step
   │ (the config pack in 07 makes them load…)
   ▼
02–05 knowledge + skills/ cheat sheets ── HOW to do each thing well
06 repo catalog ── WHAT libraries to build with
```

### Inside every folder

```text
README.md     ← start here: explains the folder and what to read first
PROMPTS.md    ← copy-paste prompts: the fallback if you don't have Claude Code, or extras to paste into a BMad session
docs/         ← the detailed guides
  repos.md      ← recommended libraries for this topic
  evidence.md   ← sources (you can ignore this)
```

---

## 🙋 "I want to…"

| I want to… | Open |
| --- | --- |
| Know what to do at my first hackathon | [`01-hackathon-playbook/first-hackathon.md`](01-hackathon-playbook/first-hackathon.md) |
| See a whole hackathon done start to finish | [`01-hackathon-playbook/worked-example.md`](01-hackathon-playbook/worked-example.md) |
| Set up my laptop (Windows, Mac, Linux) | [`01-hackathon-playbook/docs/setup-your-laptop.md`](01-hackathon-playbook/docs/setup-your-laptop.md) |
| Work with teammates without breaking each other's code | [`01-hackathon-playbook/docs/git-for-teams.md`](01-hackathon-playbook/docs/git-for-teams.md) |
| See the full hour-by-hour plan | [`01-hackathon-playbook/battle-plan.md`](01-hackathon-playbook/battle-plan.md) |
| Set up BMad | [`01-hackathon-playbook/docs/setup-bmad.md`](01-hackathon-playbook/docs/setup-bmad.md) |
| Come up with an idea | `/bmad-brainstorming` (↩ no Claude Code: [`PROMPTS.md`](01-hackathon-playbook/PROMPTS.md) → I1) |
| Know what to run next | `/bmad-help` in Claude Code |
| **Spend $0** | [`05-tools-and-mcp/docs/free-ai-dev-tools.md`](05-tools-and-mcp/docs/free-ai-dev-tools.md) → "The $0 stack" |
| Make my app look good | [`02-frontend/README.md`](02-frontend/README.md) |
| Get my app online | [`03-backend/docs/deploy-step-by-step.md`](03-backend/docs/deploy-step-by-step.md) (first time) · [`skills/hackathon-deployment/SKILL.md`](skills/hackathon-deployment/SKILL.md) (full runbook) |
| Add a chatbot or AI feature | [`04-ai-and-rag/README.md`](04-ai-and-rag/README.md) |
| Build an AI agent that uses tools | [`04-ai-and-rag/docs/agents-and-tool-use.md`](04-ai-and-rag/docs/agents-and-tool-use.md) · [`skills/hackathon-ai/SKILL.md`](skills/hackathon-ai/SKILL.md) |
| Build a mobile, voice or crypto app | [`mobile.md`](02-frontend/docs/mobile.md) · [`voice-and-realtime.md`](04-ai-and-rag/docs/voice-and-realtime.md) · [`web3.md`](03-backend/docs/web3.md) |
| **Win a Datathon / ML Challenge** | [`08-datathon-handbook/`](08-datathon-handbook/README.md) · [`skills/hackathon-datathon/SKILL.md`](skills/hackathon-datathon/SKILL.md) · Evidence: [`_research/`](_research/technical-datathons-and-ml-solutions-2026-09-23/research.md) |
| Give my AI assistant more abilities | [`05-tools-and-mcp/docs/mcp-catalog.md`](05-tools-and-mcp/docs/mcp-catalog.md) |
| Prepare the final pitch | [`01-hackathon-playbook/docs/pitch-and-demo.md`](01-hackathon-playbook/docs/pitch-and-demo.md) |
| Fix something that broke | [`03-backend/docs/troubleshooting.md`](03-backend/docs/troubleshooting.md) |
| Write the README judges will read | [`01-hackathon-playbook/templates/project-readme.md`](01-hackathon-playbook/templates/project-readme.md) |
| Know what to do after the event | [`01-hackathon-playbook/docs/after-the-event.md`](01-hackathon-playbook/docs/after-the-event.md) |

---

## 💰 What the price tags mean

You'll see these next to tools throughout the guide:

| Tag | Meaning |
| --- | --- |
| 🆓 | **Free.** Open source, no account needed |
| 🆓* | **Free tier.** Free with an account, up to a limit (usually plenty for a hackathon) |
| 💳 | **Trial only.** Some free credits, then you pay |
| 💰 | **Paid** |

---

## ⚠️ Three things that trip beginners up

1. **Get your app online in the first hour**, even if it only says "hello". Leaving deployment to the end is the most common way projects die. See [`03-backend/docs/deploy-step-by-step.md`](03-backend/docs/deploy-step-by-step.md).
2. **Never put passwords or API keys in your code.** Keep them in a `.env` file that isn't uploaded to GitHub. See [`GLOSSARY.md`](GLOSSARY.md) → "API key".
3. **Stop adding features about 3 hours before the deadline.** Use that time to fix bugs, record a backup video and practise the pitch.

The full list of "things that changed recently" (tools that were renamed, retired or changed price) is in [`06-repo-catalog/`](06-repo-catalog/README.md) → "What changed in 2025–26".

---

_Built from cited research (checked 2026-09-21 to 2026-09-22). Prices and tools change often; the next re-check is due **2026-10-22**. See [`_research/README.md`](_research/README.md) for how to refresh it._
