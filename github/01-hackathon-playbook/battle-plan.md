# 🗺️ Battle Plan: The BMad Hackathon, Hour by Hour

<!-- markdownlint-disable MD013 -->

> From the week before to the moment you leave the stage, run with the **BMad Method** in Claude Code. Every step also lists a copy-paste fallback prompt for people without Claude Code.
> Evidence: `../_research/technical-hackathon-toolkit-2026-09-21/research.md` §1 · Verified 2026-09-21

---

## The four laws (from the judging table)

1. **Clarity beats complexity.** Judges prefer a simpler project they understand over a strong project with a confusing demo. Do one thing well rather than five things halfway. ([JetBrains, 2026-06](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/))
2. **Show it working within ~90 seconds.** Open with the problem so judges feel the frustration, then demo. (same source)
3. **Mock anything slow or flaky.** A working demo matters more than code quality: "Mock everything you can and make sure all your forms are filled." (same source)
4. **Ship a visible UI.** Devpost judges name backend-only projects and barely changed templates as submission killers. ([Devpost](https://info.devpost.com/blog/hackathon-judging-tips))

---

## 🧭 How to read this plan

This plan runs on the **BMad Method** inside Claude Code (setup: [`docs/setup-bmad.md`](docs/setup-bmad.md)). Each phase lists:

- **▶ BMad:** the skill to run. Start a **fresh Claude Code chat for every skill**; the files on disk carry the context.
- **✋ You:** the human decisions no skill makes for you.
- **↩ No Claude Code?** The copy-paste prompt from [`PROMPTS.md`](PROMPTS.md) that does the same job in any AI tool.

Lost at any point? Run `/bmad-help`. The skill-by-skill reference is in [`../07-bmad-workflow/`](../07-bmad-workflow/README.md).

| Phase | Share of the clock | Main BMad skill | Output on disk |
| --- | --- | --- | --- |
| 🔍 Clarify | 5% | `bmad-brainstorming` → `bmad-forge-idea` | `forged-idea.md` |
| 📐 Plan | 5–8% | `bmad-spec` | `SPEC.md`, `mock-list.md`, `stories.yaml` |
| 🔨 Build | 60–65% | `bmad-build` (one story per chat) | Working, deployed increments |
| 🛡️ Harden | 10% | `bmad-code-review`, `bmad-qa-generate-e2e-tests` | Locked demo path |
| 🎤 Pitch | 12–15% | `bmad-cis-storytelling`, `bmad-party-mode` | Script, slides, video, submission |
| 📈 Learn | after | `bmad-retrospective` | Lessons for next time |

---

## ⏱️ Timeline (24h event; for 48h, double the Build block, not the planning)

### Days before: prepare your tools, not your project

> [!WARNING]
> Some guides (including help-me-papi) say to have a finished boilerplate and seed script ready. **MLH bans code and materials written before the event.** Public open-source libraries and starters are allowed, but pre-writing your own project code isn't. Warm up your **tools and muscle memory**, not your repo.

- [ ] Laptop ready: [`docs/setup-your-laptop.md`](docs/setup-your-laptop.md)
- [ ] **Claude Code installed and logged in; BMad rehearsed on a throwaway repo:** [`docs/setup-bmad.md`](docs/setup-bmad.md) → Part A
- [ ] Accounts created: GitHub, Vercel (linked to GitHub), Supabase, Clerk, model API, Railway if you use Python
- [ ] CLIs installed and logged in: `vercel`, `supabase`, `railway` (see `../skills/hackathon-deployment/SKILL.md`)
- [ ] MCP servers configured and tested (`../05-tools-and-mcp/docs/mcp-setup.md`); design skills installed (`/impeccable`, Taste Skill)
- [ ] **Know your scaffold commands** (`npx create-next-app@latest`, `npx shadcn@latest init`), and the "demo-winner" packages you'll add at kickoff: `sonner` (toasts), `zod`, `clsx`, `lucide-react`
- [ ] Team roles agreed, including **one person who owns deployment** (see "Team roles" below)

### T-minus 2h: Setup (before kickoff)

- [ ] **Read the rules and rubric** for required tech, the prior-code policy, AI disclosure, video length, and whether the video must name the event. ([MLH rules](https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md), [ETHGlobal](https://ethglobal.com/events/tokyo2026/info/details))
- [ ] **Accounts are live and keys work:** Supabase, Clerk, model API, Vercel. Supabase free projects pause after 7 days idle, so wake yours up now. ([Supabase pricing](https://supabase.com/pricing))
- [ ] **MCP servers installed** (see `../05-tools-and-mcp/docs/`): Context7, Supabase (read-only, dev project), Playwright, shadcn, 21st Magic.
- [ ] **Empty repo only.** MLH allows an idea from before the event but not code or materials. Don't open-source code in advance so you can reuse it. (MLH rules)
- [ ] **Stack you already know.** Don't learn new video or editing tools during the event. ([Devpost video tips](https://info.devpost.com/blog/6-tips-for-making-a-hackathon-demo-video))

### H+0:00 → H+0:15: Kickoff setup

- **✋ You:** create the repo, install BMad **inside it**, run the config pack, fill `project-context.md` (event, rubric word for word, sponsors, rules, stack) and `docs/research.md`. Commit and push. [`docs/setup-bmad.md`](docs/setup-bmad.md) → Part B.
- The pack also creates `AI_USAGE.md`, the AI-usage log (ETHGlobal requires file-level disclosure). Every `bmad-build` appends to it.

### H+0:15 → H+1:30: Clarify

| When | ▶ BMad | What it does | ↩ No Claude Code? |
| --- | --- | --- | --- |
| 0:15 | `/bmad-brainstorming` | Ideas from real frustrations, scored against the rubric and sponsor tracks | C1 → C2 → C3, or I1 |
| 0:45 | `/bmad-forge-idea` on your top 1–2 | Pressure-tests each idea: **KEEP / RESHAPE / KILL** | I2 |
| 1:05 | `/bmad-party-mode` → **judges-panel** | 5 judge personas score the idea and raise the hardest objection. It remembers this for pitch rehearsal | R1 |
| 1:15 | `/bmad-deep-recon` *(optional, 15 min)* | Quick cited check: competitors, API limits | C2 (validation step) |

- **✋ You:** start from a **real frustration**, not "the coolest new tool" (Bonnie Xu, OpenAI; via [JetBrains](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/)). **Imagine the winning demo and work backwards** from it (JetBrains).
- **✋ You:** pick **one core feature and one "wow" moment**. Everything else becomes a non-goal. BMad suggests; the team decides.

### H+1:30 → H+2:30: Plan

| When | ▶ BMad | What it does | ↩ No Claude Code? |
| --- | --- | --- | --- |
| 1:30 | **`/bmad-spec`**, then say *"break this into stories"* | Writes `SPEC.md` (Why · Capabilities · Constraints · Non-goals · Success signal), `mock-list.md`, and `stories.yaml` with **story 1 = deployed walking skeleton**, ordered by demo value, with a **cut line** | S1 → S2, using `templates/prd.md` |
| 2:00 | `/bmad-architecture` *(teams of 2+)* | One-page spine: tables, contracts, **folder ownership** | B1, B10 |
| 2:00 | `/bmad-ux` *(if design is judged)* | Design direction and tokens → `docs/design.md` | F1, F2 |
| 2:20 | `/bmad-review` *(optional, 10 min)* | Adversarial check of the spec before any code | I2 on the spec |

- **✋ You:** read the spec's **Non-goals** and **cut line** together as a team. This is the scope contract.
- `SPEC.md` replaces `docs/prd.md` on this path. Fill `docs/tech-stack.md` by hand (5 minutes; BMad has no equivalent).

### H+2:30 → ~H+17: Build

**The story loop** (repeat for every story in `stories.yaml`):

1. **Fresh chat:** `/bmad-build story <n> from stories.yaml`
2. It builds, runs its own review checks (including the toolkit's **demo-safety** check), and appends to `AI_USAGE.md`.
3. **✋ You:** try it, `npm run build`, commit, push. Vercel auto-deploys `main`.
4. Next story.

↩ **No Claude Code?** S3 for the walking skeleton, then C5 per feature, with the folder prompts (F3/F4, B3/B12, ML4/ML5).

- [ ] **Story 1 is the walking skeleton, deployed by ~H+3.** [`../03-backend/docs/deploy-step-by-step.md`](../03-backend/docs/deploy-step-by-step.md)
- [ ] **Commit at the end of every story.** ETHGlobal may disqualify a single giant commit or missing git history.
- [ ] Teams: one story per person per chat, in separate branches. [`docs/git-for-teams.md`](docs/git-for-teams.md)
- [ ] Handle errors with **toasts, not crashes**. Pre-fill forms and seed data for every feature.
- [ ] **Midpoint check (~H+12): `/bmad-correct-course`** (↩ M1). The 50% rule: the core "wow" feature must work end to end by halfway. Fake or hardcode everything that isn't essential. Move stories below the cut line if needed.
- [ ] **`/bmad-checkpoint-preview`** at the midpoint: a guided human walkthrough of what's actually built.
- [ ] Something broke? The troubleshooting skill loads automatically in `bmad-build`; the manual is [`../03-backend/docs/troubleshooting.md`](../03-backend/docs/troubleshooting.md) (↩ B11).
- [ ] The agent keeps repeating a mistake? `/bmad-project-context` → record it as a pitfall.
- [ ] *Optional, overnight:* `bmad-build-auto` via `bmad-loop`, **on a branch only**. Review it in the morning with `/bmad-checkpoint-preview`. Rehearse this before the event, never for the first time on the night.
- [ ] Sanity checks: does it work on mobile? Are empty states handled? Can you explain the AHA moment in 30 seconds without touching a keyboard?

### ~H+17 → H+20: Harden (feature freeze)

| ▶ BMad | What it does | ↩ No Claude Code? |
| --- | --- | --- |
| **`/bmad-code-review`** on the demo-critical changes | Adds the toolkit's **OWASP API**, **accessibility + Core Web Vitals** and **anti-slop** checks. Fix Critical/High only | B6, B7, B9, F6 |
| **`/bmad-qa-generate-e2e-tests`** | One Playwright test that performs the exact demo script. **If it's red, don't deploy** | M2 |
| `/bmad-checkpoint-preview` | Human walkthrough of what's shipping | F9, F12 |

- [ ] No new features, only fixes on the demo path.
- [ ] Secrets check: nothing in git and no `NEXT_PUBLIC_` service keys.
- [ ] Delete demo and test routes you don't need.
- [ ] Fill the repo README from [`templates/project-readme.md`](templates/project-readme.md).

### H+20 → H+23: Pitch and submission

| ▶ BMad | What it does | ↩ No Claude Code? |
| --- | --- | --- |
| `/bmad-cis-storytelling` | 3-minute pitch outline and script (`docs/pitch/`) | C6, P1 |
| `/bmad-cis-agent-presentation-master` | 5–7 slides | [`docs/pitch-and-demo.md`](docs/pitch-and-demo.md) → "Slide deck" |
| `/bmad-party-mode` → **judges-panel** | Rehearsal with the same judges from hour 1: scores, the 5 hardest questions, 15-second answers | P2 |
| `/bmad-review` (pitch lens) | Tightens the Devpost text and AI disclosure | P3, P4 |

- [ ] **Leave at least 2–3 hours before the deadline** to script, record and upload the video. ([Devpost](https://info.devpost.com/blog/6-tips-for-making-a-hackathon-demo-video))
- [ ] **✋ Rewrite the script in your own words.** Devpost advises not relying on AI for it, and ETHGlobal **bans AI voiceover and TTS**.
- [ ] Record the backup video: ≥720p, no phone recording, no sped-up footage, cut out waiting time. (ETHGlobal)
- [ ] Upload to YouTube and mark it "Not for Kids". You can copy the link before the upload finishes. (Devpost)
- [ ] Finish the AI-usage disclosure from `AI_USAGE.md`.
- [ ] Test the demo URL on a **different network** (phone hotspot).

### H+23: Buffer, then submit

- [ ] Submit **at least 1 hour early**.

### After: Learn

- [ ] Same day: rotate every key ([`docs/after-the-event.md`](docs/after-the-event.md)).
- [ ] `/bmad-retrospective`, then `/bmad-project-context` to keep the pitfalls for next time. Details in the harvest table below.

---

## 👥 Team roles

| Role | Runs these BMad skills | Owns in the toolkit |
| --- | --- | --- |
| **Product / pitch lead** | brainstorming, forge-idea, spec, correct-course, storytelling, party-mode | `01-hackathon-playbook/`, `docs/research.md`, the pitch |
| **Frontend builder** | build (UI stories), ux | `02-frontend/` |
| **Backend / AI builder** | build (API/AI stories), architecture | `03-backend/`, `04-ai-and-rag/` |
| **Integrator / QA** (team of 4) | code-review, qa-e2e, checkpoint-preview, bmad-loop; **owns deployment** | deployment skill, `05-tools-and-mcp/` |

Solo? Run every skill yourself in the same order; skip `bmad-architecture`.

---

## 🌾 After the event: harvest the lessons

> From help-me-papi's post-hackathon practice. The author turned two hackathon projects (it'sPEAK, a video-analysis coach, and Echo, a dementia-therapy PWA) into reusable skills.

Every hackathon project is a **spike**, a high-speed experiment in what works. The code may be messy, but the patterns that worked under pressure are worth keeping. Within 48 hours of the event, extract:

| Extract | Example | Where it goes in this toolkit |
| --- | --- | --- |
| **Pipeline patterns** | Async queue + worker, deterministic pre-checks, LLM fallbacks | `../04-ai-and-rag/docs/multimodal-pipelines.md` |
| **Auth/DB scaffolding** | The Clerk + Supabase + RLS setup you debugged under pressure | `../03-backend/docs/` |
| **Deployment runbooks** | The exact Vercel + Railway flow you fixed at 3 a.m. | `../skills/hackathon-deployment/SKILL.md` |
| **Winning prompts** | Which prompts worked first time, and which needed 5 retries | `PROMPTS.md` and the domain `PROMPTS.md` files |
| **Agent mistakes** | Wrong imports, a stale API the agent kept using | Your project's `CLAUDE.md` / `AGENTS.md` pitfalls (`docs/agent-context.md`) |

`/bmad-retrospective` walks you through this table (the config pack tells it which toolkit file each lesson belongs in). Then run `/bmad-project-context` to record agent pitfalls, and add the project to your ideas list with a link to the repo.

---

## 🎤 Pitch formats by event

| Event type | Format | Source |
| --- | --- | --- |
| MLH science fair | ~3 min per team including questions; judges stack-rank their top 3 | [MLH organizer guide](https://guide.mlh.com/general-information/judging-and-submissions/judging-plan) |
| MLH digital event | Video ≤ 2 min that names the hackathon at the start | [MLH rules](https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md) |
| Devpost (typical) | Video usually < 3 min | [Devpost](https://info.devpost.com/blog/6-tips-for-making-a-hackathon-demo-video) |
| ETHGlobal finals | 4 min demo + 3 min Q&A; video 2–4 min, ≤20 s intro | [ETHGlobal](https://ethglobal.com/events/tokyo2026/info/details) |

---

## 🧭 Judging criteria you'll meet

| Source | Criteria |
| --- | --- |
| Devpost (common set, no weights) | Technological implementation · Ease of use · Demonstration · Potential impact · Quality of idea · Design |
| ETHGlobal | Technicality · Originality · Practicality · Usability (UI/UX/DX) · WOW factor |
| MLH (learning-first) | Stack-ranked, lighter rubric. **Contradiction:** one snippet says pitch and idea quality aren't judged at MLH events, while sponsor judges weight them heavily. Always read the event's own rubric |

---

## 📚 Resources

| Resource | Why | Status |
| --- | --- | --- |
| [sahat/hackathon-starter](https://github.com/sahat/hackathon-starter) | Node.js boilerplate with auth and APIs, built for hackathons | ⭐ 35.3k · pushed 2026-09-21 |
| [MLH/mlh-policies](https://github.com/MLH/mlh-policies) | The actual MLH rules (AI use, prior code, video) | pushed 2026-09-21 |
| [HappyHackingSpace/awesome-hackathon](https://github.com/HappyHackingSpace/awesome-hackathon) | Tools and resources for participants | ⭐ 90 · pushed 2026-05 |
| [dribdat/awesome-hackathon](https://github.com/dribdat/awesome-hackathon) | Aimed at organizers; useful for understanding formats and judging | ⭐ 301 · pushed 2026-05 |
| [Devpost judging tips](https://info.devpost.com/blog/hackathon-judging-tips) | Named judges on what kills submissions | undated |
| [JetBrains: notes from the judging table](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/) | 2026 judge quotes | 2026-06 |
| [maxi-cmyk/help-me-papi](https://github.com/maxi-cmyk/help-me-papi) | The personal toolkit this guide adapts chained prompts, templates and the deploy runbook from | pushed 2026-08 · ⚠️ no license |
| [Dropbox MVP demo video](https://techcrunch.com/2011/10/19/dropbox-minimal-viable-product/) | A classic, relatable demo-as-story | 2011 |
| ~~geekcamp-ph/awesome-hackathon-starters~~ | Stale (last push 2016), so skip it | ❌ |
