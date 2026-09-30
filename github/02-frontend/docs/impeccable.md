# 💎 /impeccable: Design-Quality Skill

<!-- markdownlint-disable MD013 -->

> Manual for [pbakaus/impeccable](https://github.com/pbakaus/impeccable): an anti-"AI slop" design skill for Claude Code and 16 other harnesses. Verified from the README, 2026-09-21.

---

## What it is

| | |
| --- | --- |
| **Repo** | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) · Apache-2.0 · ⭐ 69.5k · pushed 2026-09-21 |
| **Shape** | **1 skill, 24 commands**, live browser iteration, **61 deterministic detector rules** (no LLM needed for detection) |
| **Built on** | Anthropic's [frontend-design skill](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) |
| **Harnesses** | 17, including Claude Code, Cursor, Codex CLI, Gemini CLI |

> [!WARNING]
> Blogs and search snippets still say "18 skills / 23 commands / 58 rules / ~50k stars". Those figures are out of date; the README and GitHub API are correct. There is also a **look-alike repo** (`gessniio/impeccable_SKILL_CLAUDE`), so install from **pbakaus** only.

---

## Install

Options A–C are confirmed in the README (2026-09-21). Option D and the Node requirement come from help-me-papi.

| Option | Command | Best for |
| --- | --- | --- |
| **A · CLI installer** (recommended) | `npx impeccable install` (non-interactive: `npx impeccable install --providers=claude --scope=project`) | One project |
| **B · Git submodule** | `git submodule add https://github.com/pbakaus/impeccable .impeccable` then `npx impeccable link --source=.impeccable --providers=claude` | Teams who want it pinned |
| **C · Claude Code plugin** | `/plugin marketplace add pbakaus/impeccable`, then install it from `/plugin` | Plugin users |
| **D · Generic skills CLI** | `npx skills add pbakaus/impeccable` | Shared build for every harness |

Node 22.12+ is needed, according to help-me-papi. Update with `npx impeccable update`.

```text
/impeccable init    # asks: brand surface (landing, portfolio) or product surface (app, dashboard)?
                    # writes PRODUCT.md (+ optional DESIGN.md): audience, voice, anti-references, colours, type
```

**Design hook:** on Claude Code, `install`/`update` offers to add a hook that runs the detector on every UI file edit and reports findings back to the agent automatically. Skip it with `--no-hooks`. Your choice is remembered in the gitignored `.impeccable/config.local.json`.

---

## The 24 commands

| Group | Commands | Use |
| --- | --- | --- |
| **Set up** | `init` · `document` · `extract` | `init` writes PRODUCT.md; `document` writes DESIGN.md; `extract` pulls a system from existing UI |
| **Create** | `shape` · `craft` · `generate` | Plan the layout → build it → generate variants |
| **Review** | `critique` · `audit` | Design critique; deterministic rule audit |
| **Refine** | `polish` · `distill` · `clarify` · `harden` | Final pass; simplify; clarify copy and hierarchy; edge and error states |
| **Dial** | `bolder` · `quieter` · `overdrive` | Push or pull visual intensity |
| **Specialise** | `colorize` · `typeset` · `layout` · `animate` · `delight` · `onboard` · `adapt` · `optimize` | One design dimension at a time |
| **Iterate** | `live` | Live browser iteration |

---

## What the detector flags (sample of the 61 rules)

- Overused fonts (Inter, Arial)
- Purple-to-blue gradients
- Bounce easing
- Side-tab accent borders
- Dark glows
- Grey text on coloured backgrounds
- Pure black or pure grey
- Nested cards
- Small touch targets
- Skipped heading levels
- Line length and cramped padding

These overlap heavily with what hackathon judges penalise: "barely changed templates", and visual appeal being the first thing they look at ([Devpost judges](https://info.devpost.com/blog/hackathon-judging-tips)).

---

## Headless detector (a CI or pre-demo gate)

The deterministic rules also run without an agent:

```bash
npx impeccable detect src/                   # human-readable
npx impeccable detect --json src/            # CI-friendly
npx impeccable detect https://your-demo.app  # inspect the rendered production page
npx impeccable ignores add-value overused-font Inter --reason "Brand font"   # deliberate exceptions
npx impeccable ignores add-file "src/legacy/**"
```

- Config lives in `.impeccable/config.json`, under `detector.ignoreRules`, `ignoreFiles` and `ignoreValues`.
- To waive a rule for one file, add an inline comment: `<!-- impeccable-disable overused-font: brand doc -->`. The `-line` and `-next-line` variants also exist.
- **Deliberate aesthetic ≠ slop.** If `design.md` deliberately chooses glassmorphism or a gradient, record an ignore with a reason instead of fighting the rule (see `aesthetics-directory.md`).

Sources: [Impeccable README](https://github.com/pbakaus/impeccable) · help-me-papi `frontend/docs/impeccable-skill.md` · [detector docs](https://impeccable.style/docs/detector)

---

## Hackathon workflow

| When | Command | Why |
| --- | --- | --- |
| Hour 2 (plan) | `/impeccable init` | PRODUCT.md grounds every later UI generation |
| Story 1 (skeleton) | `/impeccable shape` → `craft` | Get a considered layout on the first pass |
| Each UI story | `/impeccable critique` | Quick check before committing |
| Feature freeze | `/impeccable audit` → `polish` | Run the deterministic rules and fix the flags |
| Before the pitch | `npx impeccable detect https://<demo-url>` | Check the deployed page, not just the source |
| Before the pitch | `/impeccable harden` | Empty, error and loading states for the live demo |
| If it looks flat | `/impeccable bolder` (once, on the hero only) | "One bold moment" |

---

## Pairs well with

- **Taste Skill:** generates with stronger taste, and Impeccable then audits (see `taste-skill.md`).
- **Anthropic frontend-design skill:** the four-step process (ground → token plan → review → build and critique) that Impeccable builds on.
- **shadcn MCP / 21st MCP:** source components, then run `/impeccable audit` so they don't look like stock kits.
- **Playwright MCP:** screenshot-based verification after `polish`.
