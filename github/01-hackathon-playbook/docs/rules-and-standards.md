# 📏 Hackathon Standards

<!-- markdownlint-disable MD013 -->

> The rules you must not break, and the quality bar you hold yourself to. Verified 2026-09-21.

---

## 1 · Compliance: read these before writing code

| Rule | MLH | ETHGlobal | Devpost (typical) |
| --- | --- | --- | --- |
| **Code written before the event** | ❌ Not allowed. An idea from before is fine, but not code or materials. Existing public libraries and open-source code are allowed; pre-open-sourcing your own code to reuse it isn't | ❌ Not allowed in the Classic track | Check the event rules |
| **AI tools** | ✅ Allowed (completion, generation, images); be transparent | ✅ Assist only; **disclose where and how, down to files and assets**. Fully AI-built projects may lose eligibility | Check the event rules |
| **Git history** | — | ⚠️ A single large commit or missing history **may be disqualified** | — |
| **Video** | Digital events: ≤ 2 min, **names the hackathon at the start** | 2–4 min, ≥720p, intro ≤20 s, **no TTS or AI voiceover**, no phone recording, no sped-up footage | Usually < 3 min |
| **Live judging** | Science fair, ~3 min including questions | Finals: 4 min demo + 3 min Q&A | Varies |

Sources: [MLH standard rules](https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md) · [ETHGlobal](https://ethglobal.com/events/tokyo2026/info/details) · [Devpost video tips](https://info.devpost.com/blog/6-tips-for-making-a-hackathon-demo-video) · [MLH judging plan](https://guide.mlh.com/general-information/judging-and-submissions/judging-plan)

> [!IMPORTANT]
> **Always read the specific event's rules.** These are defaults, not guarantees. Rubrics differ a lot between learning-first student events and sponsor or prize events.

---

## 2 · Repo hygiene standard

- [ ] Commit at the end of every story, with messages that say what changed
- [ ] `AI_USAGE.md` at the repo root, updated as you go (tool · purpose · files · generated assets)
- [ ] `README.md` with a one-line pitch, screenshot/GIF, live demo URL, tech stack (sponsor tools named), how to run, and team
- [ ] `.env.example` with names only. **No secrets in git, ever.** Check `NEXT_PUBLIC_*` for leaked server keys
- [ ] License file if the event requires open source
- [ ] Remove dead code, test routes and unused starter pages. Judges penalise barely changed templates ([Devpost](https://info.devpost.com/blog/hackathon-judging-tips))

### `AI_USAGE.md` template

```markdown
# AI Usage Disclosure

| When | Tool | What for | Files / assets | Human edits |
| --- | --- | --- | --- | --- |
| H+3 | Claude Code | Scaffolded Supabase schema + RLS | supabase/migrations/001_init.sql | Reviewed, changed policy on tasks |
| H+6 | 21st MCP | Generated pricing card variant | components/pricing-card.tsx | Restyled to tokens |
| H+20 | — | Demo video script & narration | — | 100% human-written, human voice |
```

---

## 3 · Demo quality bar

| Check | Standard |
| --- | --- |
| Time to "it works" | Live functionality visible **within ~90 s** of starting ([JetBrains](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/)) |
| Scope | One core feature done well, not five done halfway |
| UI | A visible, designed UI. No backend-only demos |
| Resilience | Slow and flaky calls mocked; forms pre-filled; seed data loaded |
| Fallback | A backup video recorded and uploaded **before** the live demo |
| Network | Tested on a different network (phone hotspot) |
| Free tiers | Supabase project woken up (it pauses after 7 days idle); Clerk demo session fresh (fixed 7-day sessions) ([Supabase](https://supabase.com/pricing), [Clerk](https://clerk.com/pricing)) |

---

## 4 · Judging criteria reference

| Common criterion | What judges look for | How to show it |
| --- | --- | --- |
| Technological implementation | Real use of the required tech; not a thin wrapper | Name the sponsor APIs on a slide and show them in the demo |
| Ease of use / Usability | "Would I want to use it?" | Clean single journey; no dead ends |
| Demonstration | It works, live | Rehearsed, timed, mocked where needed |
| Potential impact / Practicality | Who has this problem and how much it hurts | Real user quote in the first 20 s |
| Quality of idea / Originality | Not rehashed or overly simple | A one-line "why not X?" answer ready |
| Design / WOW | Visual appeal is often the first thing judges see | One bold moment; run a `/impeccable audit` pass |

Sources: [Devpost criteria](https://info.devpost.com/blog/understanding-hackathon-submission-and-judging-criteria) · [ETHGlobal](https://ethglobal.com/events/tokyo2026/info/details) · [Devpost judges](https://info.devpost.com/blog/hackathon-judging-tips)
