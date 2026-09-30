# 🧪 Worked Example: One Project, Start to Finish

<!-- markdownlint-disable MD013 -->

> **In plain English:** follow one made-up team through a 24-hour hackathon run with the **BMad Method**. At every step you'll see **which BMad skill they ran**, **what file it produced**, and **what the humans decided**. The **↩** notes show the copy-paste prompt that does the same job without Claude Code.
>
> ⚠️ The team, event and project are **fictional**. They exist to show how the toolkit's pieces fit together. Timings follow [`battle-plan.md`](battle-plan.md).

---

## The setup

| | |
| --- | --- |
| **Event** | "Sustain Hack", 24 hours, in person. Theme: *reduce waste* |
| **Sponsor track** | Best use of an AI model API |
| **Team** | **Ana** (frontend), **Ben** (backend + deployment owner), **Chi** (design + pitch). Two have done a hackathon before; one hasn't |
| **Rules they found** | No code written before the event. Must disclose AI use. Video ≤ 3 minutes |
| **Tools** | Claude Code with BMad on all three laptops |

## The week before

| They did | Using |
| --- | --- |
| Installed Node, git, VS Code and the GitHub CLI; checked everything with the test app | [`docs/setup-your-laptop.md`](docs/setup-your-laptop.md) |
| Installed Claude Code; **rehearsed BMad on a throwaway folder** with a made-up theme | [`docs/setup-bmad.md`](docs/setup-bmad.md) → Part A |
| Made GitHub, Vercel and Supabase accounts; Chi claimed the Student Pack | [`first-hackathon.md`](first-hackathon.md) → "Before the event" |
| Agreed roles: **Ben owns deployment**, Chi leads product and pitch | [`battle-plan.md`](battle-plan.md) → "Team roles" |
| Wrote **no project code** (the rules ban it) | — |

---

## H+0:00 → 0:15 · Kickoff setup

Ben created the repo, ran `npx bmad-method install` **inside it**, then the toolkit's `install.sh` from Git Bash ([`docs/setup-bmad.md`](docs/setup-bmad.md) → Part B).

Chi filled in `project-context.md` while Ben installed: the event name and deadline, **the rubric pasted word for word**, the sponsor track, the rules, and the stack (Next.js + Supabase + shadcn/ui, one pinned AI model). Theme and sponsor notes went into `docs/research.md`.

Ben committed and pushed. Everyone pulled.

## H+0:15 → 1:30 · Clarify: pick the idea

**Step 1. `/bmad-brainstorming`** (Chi, fresh chat). It read the rubric and sponsor track from `project-context.md` and produced ideas that each started from a real frustration. The team shortlisted 3. *↩ Prompt I1.*

**Step 2. `/bmad-forge-idea`** on the top 2 (fresh chat). One came back **KILL** (it needed data they couldn't get in 24 hours). The other came back **RESHAPE**: *"narrow it to students and fridges."* *↩ Prompt I2.*

**Step 3. ✋ The team decided: ShelfLife.**

> *"ShelfLife lets a student snap a photo of their fridge and get 3 recipes that use the food about to go off, in 10 seconds."*

**Step 4. `/bmad-party-mode` → judges-panel** (fresh chat). The sponsor judge persona liked the vision-model use; the demo skeptic asked, *"What if the photo is blurry?"* That question went on the risk list. *↩ Prompt R1.*

**Step 5. ✋ Real-world check.** Chi asked two students at the venue, *"How often do you throw food away?"* Both said weekly. That quote went straight into the pitch.

## H+1:30 → 2:30 · Plan: write it down

**Step 1. `/bmad-spec`** (Ana, fresh chat), then *"break this into stories"*. It produced:

- `SPEC.md`: **Why** (students waste food weekly) · **Capabilities** (photo → items + days left → 3 recipes) · **Constraints** (24 h, free tiers, venue Wi-Fi) · **Non-goals** (logins, shopping lists, a mobile app) · **Success signal** (a judge gets recipes from a photo in under 60 s)
- `mock-list.md`: if the AI is slow, show a cached result for the demo photo
- `stories.yaml`: 7 stories, **story 1 = deployed walking skeleton**, **cut line after story 5**

*↩ Prompts S1 + [`templates/prd.md`](templates/prd.md), then S2.*

**Step 2. `/bmad-architecture`** (Ben, fresh chat): a one-page spine with two tables (`scans`, `recipes`), one server route for the AI call, and **folder ownership**: Ana `features/scan/`, Ben `features/recipes/` and the API, Chi `app/` layout and styling. *↩ Prompts B1, B10.*

**Step 3. ✋ Scope contract.** The three of them read the Non-goals and cut line out loud and agreed. Ben filled `docs/tech-stack.md` by hand in 5 minutes.

## H+2:30 → 3:30 · Walking skeleton, online

**`/bmad-build story 1 from stories.yaml`** (Ben, fresh chat): a Next.js app with a page that said *"ShelfLife: coming soon"*. Ben ran `npm run build`, pushed, and deployed through the Vercel website ([`../03-backend/docs/deploy-step-by-step.md`](../03-backend/docs/deploy-step-by-step.md)). *↩ Prompt S3.*

Ben posted the live URL in the team chat **at H+3:10**. From here on, every merge to `main` updated it automatically.

## H+3:30 → ~17:00 · Build: the story loop

Each person: **fresh chat → `/bmad-build story <n>` → try it → `npm run build` → commit → push → next story.** Each run also added lines to `AI_USAGE.md` and ran the toolkit's demo-safety check.

| When | Who | What happened | BMad (↩ fallback) |
| --- | --- | --- | --- |
| H+4 | Chi | Design direction and colour/font tokens into `docs/design.md` | `/bmad-ux` (↩ F1, F2) |
| H+4–8 | Ana | Story 2: upload-photo screen with a preview | `/bmad-build story 2` (↩ F3, F4) |
| H+4–8 | Ben | Story 3: server route that sends the photo to the model and gets **structured JSON** back (items + days left) | `/bmad-build story 3` (↩ B12 + ML4) |
| H+9 | Ben | Deploy broke: blank page. The build session's troubleshooting rules pointed straight at env vars: the API key was set locally but not on Vercel | Troubleshooting skill (auto-loaded) · [`../03-backend/docs/troubleshooting.md`](../03-backend/docs/troubleshooting.md). Fixed in 4 minutes |
| H+10 | Ana | **Merge conflict** in `app/page.tsx`: Ana and Chi both edited the heading | [`docs/git-for-teams.md`](docs/git-for-teams.md) → Part 4 |
| H+10 | Ben | The agent kept importing a retired model id | `/bmad-project-context` → recorded as a pitfall, so no session repeated it |
| **H+12** | All | **Midpoint check.** Photo → recipes worked end to end. Stories 6–7 (sharing, history) moved below the cut line | `/bmad-correct-course` + `/bmad-checkpoint-preview` (↩ M1) |
| H+12–16 | Ben | Story 4: seeded the database with a demo fridge photo and its cached result | `/bmad-build story 4` (↩ B8, ML7) |
| H+14–16 | Chi | Story 5: loading, empty and error states; phone layout | `/bmad-build story 5` (↩ F8, F9) |

**Commits by H+17:** 41, all small. Nobody lost work.

## ~H+17 → 20 · Harden (feature freeze)

- [x] **`/bmad-code-review`** on the demo path. The toolkit's extra checks flagged one Critical finding: the Supabase service key had a `NEXT_PUBLIC_` prefix. It was fixed and the key was rotated. Two Low findings were left for later. *(↩ B6, B7)*
- [x] **`/bmad-qa-generate-e2e-tests`**: one Playwright test that runs the exact demo script. It went green on the live URL. *(↩ M2)*
- [x] Tested on a phone using mobile data. The recipe cards overflowed, so Ana fixed them
- [x] Ana filled the repo README from [`templates/project-readme.md`](templates/project-readme.md), including an honest **"What's real and what's mocked"** table

## H+20 → 23 · Pitch and submission

**Step 1. `/bmad-cis-storytelling`** (Chi): a 3-minute outline and script in `docs/pitch/`. **✋ Chi rewrote the script in their own words** (Devpost advises against AI-written scripts). *↩ C6, P1.*

**Step 2. `/bmad-cis-agent-presentation-master`**: five slides using the outline in [`docs/pitch-and-demo.md`](docs/pitch-and-demo.md).

**Step 3. `/bmad-party-mode` → judges-panel**: the **same judges from hour 1** remembered the blurry-photo objection and asked again, plus *"How is this different from asking ChatGPT?"* They practised 15-second answers. *↩ P2.*

**Step 4.** They recorded the backup video: one take per segment, spinners cut out, own voices, 2:48 long.

**Step 5. `/bmad-review`** with the pitch lens tightened the Devpost text; the AI disclosure was built from `AI_USAGE.md`. *↩ P3, P4.*

## H+23 · Submit

They submitted **at H+22:50**, over an hour early. The venue Wi-Fi dropped at H+23:40, and several teams missed the deadline.

## The demo

The live demo worked. A judge asked to try their own fridge photo. It took 9 seconds and got two of the items wrong, and **the team said so honestly**; they had rehearsed that exact question. They didn't win the main prize but **won the sponsor track**.

## After

Ben rotated all the keys that evening ([`docs/after-the-event.md`](docs/after-the-event.md)). Two days later they ran **`/bmad-retrospective`**, which turned their notes into 3 lessons and pointed each one at the toolkit file it belonged in:

1. Deploying at H+3 saved them at H+9.
2. Folder ownership from `bmad-architecture` kept merge conflicts to one.
3. Test with **real** fridge photos earlier; the model struggled with bad lighting.

---

## Your turn

Copy this path:

| Step | BMad | Guide |
| --- | --- | --- |
| Week before | — | [`docs/setup-your-laptop.md`](docs/setup-your-laptop.md) · [`docs/setup-bmad.md`](docs/setup-bmad.md) Part A |
| Kickoff | install + config pack + `project-context.md` | [`docs/setup-bmad.md`](docs/setup-bmad.md) Part B |
| Idea | `/bmad-brainstorming` → `/bmad-forge-idea` → `/bmad-party-mode` | [`battle-plan.md`](battle-plan.md) → Clarify |
| Plan | `/bmad-spec` → stories (+ `/bmad-architecture` for teams) | [`battle-plan.md`](battle-plan.md) → Plan |
| Skeleton | `/bmad-build story 1` | [`../03-backend/docs/deploy-step-by-step.md`](../03-backend/docs/deploy-step-by-step.md) |
| Build | `/bmad-build story n` · `/bmad-correct-course` at halfway | [`docs/git-for-teams.md`](docs/git-for-teams.md) · [`../03-backend/docs/troubleshooting.md`](../03-backend/docs/troubleshooting.md) |
| Harden | `/bmad-code-review` · `/bmad-qa-generate-e2e-tests` | [`templates/project-readme.md`](templates/project-readme.md) |
| Pitch | `/bmad-cis-storytelling` · `/bmad-party-mode` · `/bmad-review` | [`docs/pitch-and-demo.md`](docs/pitch-and-demo.md) |
| After | `/bmad-retrospective` | [`docs/after-the-event.md`](docs/after-the-event.md) |

Stuck at any point? `/bmad-help`.
