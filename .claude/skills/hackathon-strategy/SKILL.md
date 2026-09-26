---
name: hackathon-strategy
description: Hackathon strategy toolkit for a BMad-driven event covering prep, the phase-by-phase BMad skill sequence, scope, timeline, judging, pitch, video, compliance rules (MLH/ETHGlobal/Devpost), the submission README, and post-event wrap-up. Use when planning a hackathon, deciding which BMad skill to run next, cutting scope, preparing a demo or pitch, writing a submission or README, or wrapping up after the event.
---

# Hackathon Strategy Toolkit

<!-- markdownlint-disable MD013 -->

> Condensed rules. Full detail: `../../01-hackathon-playbook/battle-plan.md` · `../../01-hackathon-playbook/docs/` · macros in `../../01-hackathon-playbook/PROMPTS.md` · a full fictional run-through in `../../01-hackathon-playbook/worked-example.md`. Verified 2026-09-21.

## The BMad sequence (one fresh chat per skill)

| Phase | Share | Run | Human decides | Fallback prompt |
| --- | --- | --- | --- | --- |
| Setup | 15 min | `npx bmad-method install` in the repo → config pack `install.sh` → fill `project-context.md` | Rubric, rules, stack | Copy `templates/` |
| Clarify | 5% | `bmad-brainstorming` → `bmad-forge-idea` → `bmad-party-mode` (judges-panel) | The one idea + one wow moment | I1, I2, R1 |
| Plan | 5–8% | `bmad-spec` → "break this into stories" (+ `bmad-architecture` for teams, `bmad-ux` if design is judged) | Non-goals and cut line | S1, S2 |
| Build | 60–65% | `bmad-build story <n>`; story 1 = deployed walking skeleton; `bmad-correct-course` at 50% | Commit/push each story | S3, C5 |
| Harden | 10% | `bmad-code-review` → `bmad-qa-generate-e2e-tests` | Fix Critical/High only | M2, B6, B7 |
| Pitch | 12–15% | `bmad-cis-storytelling` → `bmad-party-mode` rehearsal → `bmad-review` (pitch lens) | Rewrite script in own words | P1–P4 |
| Learn | after | `bmad-retrospective` → `bmad-project-context` | — | — |

Always install BMad **inside the repo**: a home-folder `_bmad/` silently wins and drops the toolkit overrides. Lost? `bmad-help`. Setup: `../../01-hackathon-playbook/docs/setup-bmad.md`.

## Week before

Install Node LTS, git, VS Code, GitHub CLI and test with `npx create-next-app@latest` (`../../01-hackathon-playbook/docs/setup-your-laptop.md`; on Windows keep projects out of OneDrive). Install Claude Code and rehearse BMad on a throwaway repo. Create GitHub, Vercel (via GitHub) and Supabase accounts. Agree roles, including **one deployment owner**. Write no project code if the rules ban prior work.

## Laws

1. **Clarity beats complexity.** One feature done well; the demo shows it working within ~90 s.
2. **Start from a real frustration**, not a cool tool. Picture the winning demo and work backwards from it.
3. **Mock anything slow or flaky**; pre-fill forms and seed data.
4. **Ship a visible, designed UI.** Backend-only projects and barely changed templates lose.
5. **Read the event rules first** (prior code, AI disclosure, video spec).

## Time split (scale to the event length)

| Phase | Share | Output |
| --- | --- | --- |
| Clarify | 5% | One idea scored against the rubric |
| Plan | 5–8% | One-page spec + ordered stories + cut line |
| Build | 60–65% | Walking skeleton by ~H+4, then stories by demo value |
| Harden | 10% | Feature freeze; one E2E of the demo script; secrets check |
| Pitch | 12–15% | Script, deck, video (start ≥2–3 h before the deadline) |

## Without Claude Code (fallback)

- **Quick mode:** standalone macros I1–P4 in `../../01-hackathon-playbook/PROMPTS.md`.
- **Chain mode:** fill `docs/Research.md`, then C1 strategy → C2 persona → C3 ideas (*you pick*) → C4 PRD/techStack/design docs → C5 feature-first scaffolding → C6 pitch. Templates are in `../../01-hackathon-playbook/templates/`; structure is in `../../01-hackathon-playbook/docs/project-structure.md`.
- **50% rule:** the core "wow" feature works end to end by the halfway mark, or you cut scope.

## Compliance defaults

| Rule | MLH | ETHGlobal |
| --- | --- | --- |
| Code written before the event | ❌ (an idea is OK) | ❌ Classic track |
| AI | ✅ with transparency | ✅ assist only; disclose files and assets |
| Git | — | A single giant commit or missing history may be disqualified |
| Video | ≤ 2 min, name the event | 2–4 min, ≥720p, intro ≤20 s, **no AI voiceover or TTS** |

Keep `AI_USAGE.md` and commit little and often from hour 0.

## Pitch (3 min)

Hook + problem (≤20 s) → one-sentence solution → **live demo working by 0:90** → how it works + sponsor tech (≤4 bullets) → impact → close. Write the script and record the narration yourself. Have the backup video uploaded before you go on stage.

## Judging criteria (common)

Implementation · Ease of use · Demo · Impact · Originality · Design (Devpost). Technicality · Originality · Practicality · Usability · WOW (ETHGlobal). **Always use the event's own rubric.**

## Demo-day checklist

- [ ] Supabase project woken up (pauses after 7 days idle); Clerk demo session fresh (fixed 7-day sessions)
- [ ] Demo tested on a phone hotspot
- [ ] Backup video on YouTube ("Not for Kids")
- [ ] README filled from `../../01-hackathon-playbook/templates/project-readme.md`: one-line pitch, live URL, video, screenshot/GIF, stack, **what's real vs mocked**, AI use, team
- [ ] Submit ≥1 h early

## After the event

1. **Same day:** rotate every API key; set spending limits or delete paid resources; revoke weekend-only access.
2. **Keep the demo alive:** Supabase free projects pause after 7 days idle; the video link is your permanent demo.
3. **Repo:** finish the README, add a `LICENSE` if wanted, pin it on GitHub.
4. **Share within 48 h:** update Devpost, post with a GIF tagging teammates and sponsors, thank judges and sponsor engineers.
5. **Harvest lessons:** `bmad-retrospective` (the config pack maps each lesson to a toolkit file), then `bmad-project-context` for agent pitfalls.

Full manual: `../../01-hackathon-playbook/docs/after-the-event.md`.

## Related skills

`hackathon-deployment` (get online) · `hackathon-troubleshooting` (something broke) · `hackathon-git-teamwork` (team repo, merge conflicts) · `hackathon-frontend` · `hackathon-backend`.

## Sources

[JetBrains judges (2026-06)](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/) · [Devpost judging tips](https://info.devpost.com/blog/hackathon-judging-tips) · [Devpost video tips](https://info.devpost.com/blog/6-tips-for-making-a-hackathon-demo-video) · [ETHGlobal](https://ethglobal.com/events/tokyo2026/info/details) · [MLH rules](https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md)
