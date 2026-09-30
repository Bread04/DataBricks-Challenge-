# 🎤 Pitch Resources

<!-- markdownlint-disable MD013 -->

> Structures, timings, video specs and rehearsal drills. Verified 2026-09-21.

---

## The 3-minute pitch skeleton

| Segment | Time | Content | Evidence |
| --- | --- | --- | --- |
| 🪝 Hook + problem | 0:00–0:20 | Make the judge *feel* the frustration. A real user quote works well | [JetBrains](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/), [ETHGlobal](https://ethglobal.com/events/tokyo2026/info/details) (≤20 s intro) |
| 💡 One-sentence solution | 0:20–0:30 | `"<Product> lets <person> <do thing> in <time>."` | [Devpost](https://info.devpost.com/blog/6-tips-for-making-a-hackathon-demo-video) |
| 🖥️ Live demo | 0:30–2:00 | The success-signal journey. **Working by 0:90** | JetBrains |
| ⚙️ How it works | 2:00–2:30 | Architecture in ≤4 bullets; name the sponsor tech | ETHGlobal (≤4 bullets/slide), [Devpost criteria](https://info.devpost.com/blog/understanding-hackathon-submission-and-judging-criteria) |
| 🚀 Impact + close | 2:30–3:00 | Who uses it, what's next, a memorable last line | Devpost criteria (impact) |

**Variants:** MLH science fair is ~3 min including questions, so cut the demo to 60 s. ETHGlobal finals are 4 min + 3 min Q&A, so add depth to "how it works".

---

## Slide deck (5–7 slides max)

1. **Title:** name, one-line pitch, team
2. **Problem:** one image and one quote
3. **Demo:** switch to the live app, or embed the video as a fallback
4. **How it works:** a diagram and ≤4 bullets
5. **Sponsor tech:** logos plus exactly what each API does in your product
6. **Impact / next:** who, how many, what you'd build next
7. *(optional)* **Team**

Keep one idea per slide with large visuals and no walls of text.

---

## Demo video specification

| Spec | Value |
| --- | --- |
| Length | MLH digital ≤ 2 min · Devpost usually < 3 min · ETHGlobal 2–4 min |
| Resolution | ≥ 720p (ETHGlobal) |
| Intro | ≤ 20 s; **say the hackathon name** at the start (MLH) |
| Narration | **Your own voice.** No TTS or AI voiceover (ETHGlobal); write your own script (Devpost) |
| Footage | Screen recording (OBS, etc.); no phone recording; don't speed up; **cut out waiting** |
| Upload | YouTube (unlisted or public), marked "Not for Kids"; copy the link before the upload finishes |
| Timing | Start ≥ 2–3 h before the deadline |

Sources: [ETHGlobal](https://ethglobal.com/events/tokyo2026/info/details) · [MLH rules](https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md) · [Devpost](https://info.devpost.com/blog/6-tips-for-making-a-hackathon-demo-video)

### Recording workflow

1. Reset the demo state (fresh seed data, logged-in demo user).
2. Record the screen in one take per segment; retakes are cheap.
3. Record narration separately if that's easier, then line it up while editing.
4. Cut out every loading spinner and pause.
5. Add a title card (event name) and an end card (repo and demo URL).
6. Export at 1080p, upload, paste the link into the submission, and let it finish processing.

### Bonus: a 1-command launch video with `/brag`

[**latent-spaces/brag**](https://github.com/latent-spaces/brag) 🆓 (MIT, 6.9k ⭐, last push 2026-09-21) is a Claude Code skill that turns your project into a **short launch video with music, motion and share copy**. Run it inside your repo, and you get a `brag-output/` folder with the plan, a composition brief, share copy and `brag.mp4`. The rendering is done by [Hyperframes](https://hyperframes.heygen.com/).

```bash
# Claude Code
/plugin marketplace add latent-spaces/brag
/plugin install brag@brag
# any other agent (Cursor, Codex, Copilot, Gemini CLI, opencode…)
npx skills add https://github.com/latent-spaces/brag --skill brag
```

Then ask your agent `let's /brag`, or steer the tone: `/brag --tone "fake Series A launch from 2016"`.

**Needs:** Node.js 22+, **FFmpeg** on your `PATH`, and the Hyperframes CLI (`npx hyperframes doctor` checks it). **Install and test it the week before**, not at 3 a.m. On Windows, clone with `git clone -c core.symlinks=true`, or copy `skills/brag/` into `~/.claude/skills/` by hand.

> ⚠️ **It's a hype video, not your demo video.** Use it for the end card, a Devpost gallery clip, or your LinkedIn/X post after the event ([`after-the-event.md`](after-the-event.md)). The **judged** demo video still needs a real screen recording of your working app, in the format your event specifies (table above). Leave voiceover **off** (the default): `--voice` adds AI narration, which ETHGlobal bans. Mention it in your AI-use disclosure.

---

## Rehearsal drills

| Drill | How |
| --- | --- |
| **Timed run ×3** | Use a stopwatch. If you're over, cut the `[CUT IF LONG]` lines |
| **Cold judge** | Someone who hasn't seen the project watches once and explains it back. If they can't, clarify the pitch |
| **Q&A drill** | `PROMPTS.md` → P2; memorise 15 s answers to the top 5 questions |
| **Failure drill** | Practise switching to the backup video mid-demo in under 5 seconds |

---

## What kills pitches (named judges)

- **Ambiguity:** judges can't tell what the product does
- **A backend-heavy project with no UI**
- **A barely changed template**
- **A rehashed or overly simple idea**
- **Over-indexing on one criterion**
- **Big teams with unequal contribution**

Source: [Devpost: hackathon judging tips](https://info.devpost.com/blog/hackathon-judging-tips)

---

## Further reading

- [JetBrains: How to win a hackathon, notes from the judging table (2026-06)](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/)
- [Devpost: Understanding submission & judging criteria](https://info.devpost.com/blog/understanding-hackathon-submission-and-judging-criteria)
- [Devpost: 6 tips for making a hackathon demo video](https://info.devpost.com/blog/6-tips-for-making-a-hackathon-demo-video)
- [MLH Organizer Guide: Judging plan](https://guide.mlh.com/general-information/judging-and-submissions/judging-plan)
