# ⚙️ BMad Config Pack

<!-- markdownlint-disable MD013 -->

> Drop-in files that wire the whole toolkit into BMad. Checked on 2026-09-22 with BMad's own `resolve_customization.py`: the overrides merge on top of the shipped defaults.

## Install

```bash
# in your hackathon repo, first:
npx bmad-method install                 # BMad MUST live in the repo (see "Gotcha" below)

# then, from this toolkit:
bash 07-bmad-workflow/config-pack/install.sh /path/to/your-hackathon-repo --dry-run   # preview
bash 07-bmad-workflow/config-pack/install.sh /path/to/your-hackathon-repo             # apply (never overwrites)
```

## What it puts in your repo

| Path in your repo | From | Why |
| --- | --- | --- |
| `.toolkit/` | this toolkit (folders 00–06 + `skills/`) | The knowledge BMad skills load via `file:` facts |
| `_bmad/custom/*.toml` | `_bmad/custom/` (16 files) | Per-skill overrides: facts, review layers, lenses, judges |
| `project-context.md` | `project-context.template.md` | **The hub.** Almost every BMad skill loads it by default (`bmad-spec` needs it at the repo root) |
| `docs/research.md`, `prd.md`, `tech-stack.md`, `design.md` | `01-hackathon-playbook/templates/` | Docs-as-code inputs |
| `AI_USAGE.md` | generated | AI disclosure log (ETHGlobal/MLH) |
| `.claude/skills/hackathon-*/` | `skills/` | Project-scoped Claude Code skills |

## The 16 overrides

| File | Adds |
| --- | --- |
| `bmad-brainstorming.toml` | Event context + "real frustration, AHA, sponsor API, score vs rubric" |
| `bmad-forge-idea.toml` | Rubric + clock pressure; KEEP / RESHAPE / KILL |
| `bmad-deep-recon.toml` | `quick` preset, 15-minute hackathon framing, official sources first |
| `bmad-spec.toml` | Hackathon kernel rules, `mock-list.md` companion, story slicing with a cut line |
| `bmad-architecture.toml` | Quick one-page spine, feature-first structure |
| `bmad-ux.toml` | One demo journey, one deliberate aesthetic, token-first |
| `bmad-build.toml` | Frontend/backend/troubleshooting cheat sheets, repo catalogue, ≤500-line stories + **demo-safety review layer** |
| `bmad-build-auto.toml` | Same, for overnight `bmad-loop` runs |
| `bmad-code-review.toml` | **OWASP API**, **a11y + Core Web Vitals** and **Impeccable anti-slop** review layers |
| `bmad-qa-generate-e2e-tests.toml` | One Playwright test of the exact demo script |
| `bmad-correct-course.toml` | The 50% rule and a feature freeze ≥3 h before the deadline |
| `bmad-party-mode.toml` | 5 personas (tech, business and sponsor judges, target user, demo skeptic) + `judges-panel` and `build-crew` rooms |
| `bmad-review.toml` | A `hackathon-pitch` lens for scripts and Devpost write-ups |
| `bmad-cis-storytelling.toml` | 3-minute arc, human-voice rule |
| `bmad-project-context.toml` | Toolkit cheat sheets as standing sources for AGENTS.md |
| `bmad-retrospective.toml` | Post-event harvest into toolkit files |

## ⚠️ Gotcha: install BMad inside the repo

BMad finds the project root by walking up from where it runs. If your hackathon repo has no `_bmad/` but your home folder does (yours currently has `C:\Users\braed\_bmad`), the resolver uses the home one and **silently ignores these overrides**. That's what happened during verification until an explicit `--project-root` was passed. Always run `npx bmad-method install` in the hackathon repo.

## Verify it worked

```bash
uv run _bmad/scripts/resolve_customization.py --skill ~/.claude/skills/bmad-party-mode --project-root . --key workflow
# expect party_groups to include "judges-panel"; code-review layers to include owasp-api, a11y-cwv, anti-slop
```

## Tuning

- **Context budget:** every `file:` fact is loaded in full. The pack points at the one-page `SKILL.md` cheat sheets, not whole doc folders. Add big docs only where they earn their tokens.
- **Personal tweaks:** put them in `_bmad/custom/<skill>.user.toml`, which is merged after the team file.
- **Changing things conversationally:** `/bmad-customize` edits these files for you and checks the merge.
