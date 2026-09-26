# 🧠 Hackathon Strategy Macros

<!-- markdownlint-disable MD013 -->

> Copy-paste prompts for ideation, scaffolding and pitching. Replace anything in `<angle brackets>`.
> **On the BMad path these are the fallback:** use them if you don't have Claude Code, or paste one into a BMad session for extra focus. [`battle-plan.md`](battle-plan.md) lists which prompt matches each BMad skill.
> Each macro links to the evidence it's built on. See `battle-plan.md` for when to use each one.

---

## Contents

| Code | Macro | Phase |
| --- | --- | --- |
| [I1](#i1--theme--3-ideas) | Theme → 3 ideas | Ideate |
| [I2](#i2--pressure-test) | Pressure-test | Ideate |
| [R1](#r1--rubric-self-check) | Rubric self-check | Ideate / midpoint |
| [S1](#s1--one-page-spec) | One-page spec | Scaffold |
| [S2](#s2--story-slicer) | Story slicer | Scaffold |
| [S3](#s3--walking-skeleton) | Walking skeleton | Scaffold |
| [M1](#m1--midpoint-cut) | Midpoint cut | Build |
| [M2](#m2--demo-hardening) | Demo hardening | Harden |
| [P1](#p1--180-second-script) | 180-second script | Pitch |
| [P2](#p2--judge-qa-drill) | Judge Q&A drill | Pitch |
| [P3](#p3--devpost-write-up) | Devpost write-up | Pitch |
| [P4](#p4--ai-usage-disclosure) | AI-usage disclosure | Submit |
| [C1–C6](#-chained-pipeline-research--pitch) | **Chained pipeline:** research → persona → ideas → docs → feature → pitch | Whole event |

> **Two ways to use this file.** *Quick mode* uses the standalone macros I1–P4 on their own. *Chain mode* (C1–C6, adapted from [help-me-papi](https://github.com/maxi-cmyk/help-me-papi)) runs them in order, where each output becomes the next input and everything lands in `docs/`.

---

## Ideate

### I1 · Theme → 3 ideas

```text
Hackathon theme: <theme>. Sponsor APIs / prize tracks: <list>. Judging rubric: <paste>.
Team: <n> people, skills <skills>. Time: <h> hours. Stack we already know: <stack>.

Generate 8 ideas. Each must start from a REAL frustration a specific person has (not "a cool use of <tool>").
For each: the person, their frustration in one sentence, the one-feature solution, the "wow" moment a judge sees in the demo, and which sponsor API it uses meaningfully.
Then score all 8 against the rubric (1–5 per criterion) and return the top 3 with the single biggest risk for each.
```

*Why:* judges reward real frustrations and meaningful use of required tech, and punish rehashed or overly simple ideas ([JetBrains](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/), [Devpost](https://info.devpost.com/blog/hackathon-judging-tips)).

### I2 · Pressure-test

```text
Pressure-test this idea as three judges: a technical judge, a business judge and a sponsor judge.
Idea: <one paragraph>. We have <h> hours to a LIVE demo.
Ask me one hard question at a time (max 6). Focus on: can we show it working within 90 seconds? What must be mocked? What would make a judge say "I've seen this before"?
End with: KEEP / RESHAPE / KILL and why.
```

### R1 · Rubric self-check

```text
Here is the event rubric: <paste>. Here is our project right now: <description / repo summary / demo URL notes>.
Score it 1–5 on each criterion. Tell me which criterion we are over-indexing on, and name the single change that raises our weakest score within <n> hours.
```

*Why:* over-indexing on one criterion is a named submission killer ([Devpost](https://info.devpost.com/blog/hackathon-judging-tips)).

---

## Scaffold

### S1 · One-page spec

```text
Write a one-page hackathon spec from this idea: <idea>.
Sections:
- WHY: one sentence a judge can repeat.
- CAPABILITIES: only what appears in a 3-minute demo.
- CONSTRAINTS: deadline <time>, stack <stack>, required sponsor tech <tech>, must run live on venue Wi-Fi.
- NON-GOALS: be aggressive (auth → hardcoded demo user, payments, admin, multi-tenant, mobile unless judged).
- SUCCESS SIGNAL: "a judge completes <core action> in under 60 seconds".
- MOCK LIST: every slow/flaky dependency we will fake for the demo.
```

### S2 · Story slicer

```text
Slice this spec into stories for AI-assisted building: <paste spec>.
Rules: Story 1 = deployed walking skeleton (end-to-end, hardcoded data, live URL).
Order by DEMO VALUE, not technical layer. Each story ≤ ~500 changed lines in a handful of files.
Each story: title, acceptance check a human can do in 30s, files likely touched.
Mark a CUT LINE: everything below is stretch.
```

### S3 · Walking skeleton

```text
Scaffold a walking skeleton for <idea> using <Next.js 16 + Supabase + Tailwind v4 + shadcn>.
One page that performs the core action end-to-end with hardcoded/seed data, deployable to <Vercel> right now.
Include: README with run/deploy steps, .env.example (no real keys), seed script, and an AI_USAGE.md log file.
Do not add auth, settings, or any page not in the demo path.
```

---

## Build and harden

### M1 · Midpoint cut

```text
Status: <h> hours left. Done: <stories>. Remaining: <stories>. Problems: <blockers>.
Protect the demo. Which stories do we cut, which do we mock, and what is the new order?
Output a revised list with hours per story and a hard feature-freeze time (≥3h before deadline).
```

### M2 · Demo hardening

```text
Here is our demo script: <steps>. Walk the codebase and list everything that could crash, hang, or look broken during a live demo:
slow API calls without loading states, missing seed data, empty states, expired sessions, rate limits, cold starts, console errors, secrets in the repo.
For each: severity, a one-line fix, and whether to mock it instead.
```

*Why:* "Mock everything you can and make sure all your forms are filled" ([JetBrains](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/)).

---

## Pitch and submit

### P1 · 180-second script

```text
Write a 180-second demo script for <project> from this spec: <paste>.
Structure: hook + problem (≤20s, make the judge feel the frustration) → one-sentence solution → LIVE demo working by 0:90 → how it works + sponsor tech (≤4 bullets) → impact / who uses it → close.
Write it in MY voice from these notes: <notes>. Mark [CUT IF LONG] lines. Add stage directions for what's on screen.
```

*Why:* this follows the judge advice on working within 90 seconds, ETHGlobal's ≤20 s intro and ≤4 bullets per slide, and Devpost's "write your own script" ([JetBrains](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/), [ETHGlobal](https://ethglobal.com/events/tokyo2026/info/details), [Devpost](https://info.devpost.com/blog/6-tips-for-making-a-hackathon-demo-video)). Rewrite the draft in your own words, and **record your own voice**, because ETHGlobal bans AI voiceover.

### P2 · Judge Q&A drill

```text
You are a panel: technical judge, business judge, sponsor judge from <sponsor>, and a target user.
Here is our pitch: <script>. Each of you ask your 2 hardest questions. Then tell me the 3 answers I must have memorised and a 15-second answer for each.
```

### P3 · Devpost write-up

```text
Draft our Devpost submission from: spec <paste>, README <paste>, AI usage log <paste>.
Sections: Inspiration · What it does · How we built it (name every sponsor tool) · Challenges · Accomplishments · What we learned · What's next.
Plain, specific, no hype words. Include 1 screenshot placeholder per section where useful.
```

### P4 · AI-usage disclosure

```text
From this AI usage log <paste AI_USAGE.md> and git log <paste>, draft the AI disclosure section:
which tools were used, for which files/assets, and what was human-written.
Be specific and honest. Follow <event> rules: <paste rule text>.
```

*Why:* ETHGlobal requires file-level disclosure, and MLH requires transparency about AI tools ([ETHGlobal](https://ethglobal.com/events/tokyo2026/info/details), [MLH](https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md)).

---

## 🔗 Chained pipeline: research → pitch

> Adapted from [maxi-cmyk/help-me-papi](https://github.com/maxi-cmyk/help-me-papi) `hackathons/PROMPTS.md` (`[ROLE] / [TASK] / [OUTPUT]` format).
>
> **Rules:**
>
> 1. Paste one macro at a time. Never paste them all at once.
> 2. Each output is the source of truth for the next macro.
> 3. **Human pivot:** after C3 you tell the agent which idea you chose.
> 4. **Prerequisite:** fill in `docs/Research.md` first (template: `templates/research.md`).

### C1 · STRATEGIC_ANALYSIS

```markdown
[ROLE] You are an expert Hackathon Strategist. Find the highest-leverage angle for a winning project.
[INPUT] Hackathon: <name> · Theme: <statement> · Sponsors: <list> · Prizes/Tracks: <list> · Team/Stack: <details> · Rubric: <paste>
[CONTEXT] Read docs/Research.md.
[TASK]
1. SPONSOR AUDIT: search the web for each sponsor's current priorities and recent launches. What do they actually want built?
2. JUDGE PERSONAS: infer judge profiles (VC, CTO, domain, sponsor) and what impresses vs. bores each.
3. TRAP DETECTION: predict the 3 most common "default" projects other teams will build and why they are traps.
4. SWEET SPOT: intersect sponsor needs, judge novelty, and our team's technical edge.
[OUTPUT] 3 Strategic Positioning Statements: "Build for [user] in [sponsor domain] to solve [specific pain] using [technical edge]." Cite sources.
```

### C2 · PERSONA_BUILDER

```markdown
[ROLE] You are a Lead User Researcher.
[CONTEXT] The strategic analysis above + my observations: <notes>.
[TASK] Build one specific persona that validates the chosen angle:
1. WHO: name, role, daily context (specific, not a demographic).
2. DAY IN THE LIFE: the workflow where the friction happens.
3. CORE FRUSTRATION: exactly where they get stuck, give up, or waste time.
4. EXISTING WORKAROUNDS: why current solutions haven't fixed it.
5. THE WIN: what "solved" looks like.
[VALIDATION] Find real statistics or reports proving the problem exists at scale. Cite every source; flag anything you couldn't verify.
```

### C3 · IDEATE_PROJECT

```markdown
[ROLE] You are an expert Product Strategist.
[CONTEXT] Strategic analysis + persona above.
[TASK] Propose 3 distinct ideas. For each:
1. THE HOOK: one-sentence pitch opener.
2. USER STORY: "[Persona] needs to [action] because [pain], but currently [what's broken]."
3. USER FLOW: ≤4 steps from opening the app to problem solved.
4. AHA MOMENT: the exact 30-second interaction that makes a judge lean in.
5. SPONSOR FIT: which API/track, used meaningfully (not a thin wrapper).
6. RANKING: feasibility in <h> hours (1–5), flow clarity, judge appeal.
[OUTPUT] Recommend the "Winning Bet" and why. Then STOP and wait for me to choose.
```

### C4 · GENERATE_STRATEGY_SUITE

```markdown
[ROLE] You are a Technical Product Manager.
[CONTEXT] The idea I chose: <idea>. docs/Research.md.
[TASK] Fill these templates (templates/) into docs/:
- docs/PRD.md: why, persona, AHA feature, flow, constraints, NON-GOALS, mock list, demo metrics, stories ordered by demo value with a cut line.
- docs/techStack.md: stack + why + how the pieces connect.
- docs/design.md: flow, ONE deliberate aesthetic direction, tokens with contrast ratios, component sources (shadcn / 21st.dev), states checklist.
[CONSTRAINTS] No generic filler. Only the demoable MVP path. Story 1 = deployed walking skeleton.
```

### C5 · SCAFFOLD_FEATURE

```markdown
[ROLE] You are a Senior Fullstack Engineer using Claude Code.
[CONTEXT] docs/PRD.md story <n>, docs/design.md, docs/project-structure.md.
[TOOLS] shadcn MCP + 21st MCP for UI; Stitch MCP if a Stitch design exists; Supabase MCP (read-only) for schema.
[TASK] Scaffold feature <name> in features/<name>/:
1. types.ts — domain interfaces.
2. service.ts — server-only; ownership checks; returns DTOs.
3. actions.ts — 'use server'; auth check → validate → service.
4. components/ — UI from tokens + shadcn only.
5. Demo-safe error handling: toasts (sonner), not crashes; loading/empty/error states.
6. Seed data for this feature in scripts/seed.ts.
[OUTPUT] Files created, how to see it working on the deployed URL, and one line to add to AI_USAGE.md.
```

### C6 · PITCH_GENESIS

```markdown
[ROLE] You are a Pitch Coach.
[CONTEXT] docs/PRD.md, docs/design.md, the deployed demo flow.
[TASK] Create docs/pitch/:
1. outline.md: 7 slides (problem-first, Airbnb/Dropbox style):
   S1 Hook (the persona's pain) · S2 Persona · S3 Solution (the AHA) · S4 Live demo flow · S5 Tech stack (reliability + sponsor tech) · S6 Impact · S7 Team & vision
2. script.md: 3 minutes, ~70% on the live walkthrough, working by 0:90, memorable differentiation line at the close. Mark [CUT IF LONG] lines.
[CONSTRAINTS] Draft only — I will rewrite it in my own words and record my own voice (ETHGlobal bans AI voiceover; Devpost advises writing your own script).
```

*Changed from the original:* C5 adds `service.ts`, seed data and the AI_USAGE line. C6 adds the rule to write the final script and record the narration yourself. C4 adds non-goals, a mock list and a cut line.
