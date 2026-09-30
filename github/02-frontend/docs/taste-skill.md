# 🎯 Taste Skill: Anti-Slop Generation

<!-- markdownlint-disable MD013 -->

Taste Skill improves AI-generated UI **as it's generated**. It pairs with `/impeccable`, which **audits** afterwards. Details were checked against the repo README on 2026-09-21. The skill list comes from help-me-papi `frontend/docs/taste-skill.md`.

---

## At a glance

| | |
| --- | --- |
| **Repo** | [Leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill): ⭐ 88.9k · MIT · pushed 2026-09-20 |
| **Site** | [tasteskill.dev](https://tasteskill.dev) · [changelog](https://www.tasteskill.dev/changelog) |
| **What** | Portable Agent Skills for stronger layout, typography, motion and spacing, plus image-generation skills for reference boards |
| **Works with** | Claude Code, Cursor, Codex (Agent Skills format) |

---

## Install (verified from the README)

```bash
# everything (code + image-generation skills)
npx skills add https://github.com/Leonxlnx/taste-skill

# just the default skill (install name = the SKILL frontmatter `name:`)
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"

# pin the original v1 behaviour
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend-v1"
```

The default `design-taste-frontend` is now **v2 (experimental)**, a substantial rewrite. Re-running the install upgrades it in place. You can also paste any `SKILL.md` straight into a session.

---

## Skills

From help-me-papi's catalogue. Check the repo's `skills/` folder for the current list.

| Skill | Use it for |
| --- | --- |
| `design-taste-frontend` (v2, default) | Reads the brief, infers a design language, tunes three dials |
| `design-taste-frontend-v1` | The original, pinned |
| `gpt-taste` | Stricter variant for GPT/Codex |
| `image-to-code` | Generate references → analyse → implement |
| `redesign-existing-projects` | Audit and fix an existing generic UI |
| `high-end-visual-design` | Calm, premium, soft contrast, spring motion |
| `minimalist-ui` | Editorial product UI (Notion/Linear feel) |
| `industrial-brutalist-ui` | Swiss type, hard contrast, experimental layout |
| `full-output-enforcement` | Stops the model shipping half-finished placeholder output |
| `stitch-design-taste` | Google Stitch-compatible rules; `DESIGN.md` export |
| `imagegen-frontend-web` / `-mobile` / `brandkit` | Image-only skills: site comps, mobile screens, logo and palette directions |

---

## The three dials (1–10)

| Dial | Low | High | Hackathon suggestion |
| --- | --- | --- | --- |
| **DESIGN_VARIANCE** | Centred, clean | Asymmetric, experimental | 5–7: memorable but not confusing |
| **MOTION_INTENSITY** | Hover only | Scroll and magnetic effects | 3–5: motion must not slow down the demo |
| **VISUAL_DENSITY** | Spacious | Dense dashboard | 3–4 for consumer apps, 6–7 for data tools |

Example prompt:

```text
Follow the Taste Skill v2 design language: brief inference → design-system map → generate.
DESIGN_VARIANCE=6, MOTION_INTENSITY=4, VISUAL_DENSITY=4. Use our @theme tokens and shadcn primitives.
```

---

## Taste + Impeccable workflow

```text
Taste Skill (generate)  →  /impeccable audit (detect slop)  →  /impeccable polish  →  Playwright screenshots
```

They complement each other: Taste pushes the agent away from the default "centred hero + cards + Inter" look while it builds, and Impeccable's deterministic rules catch whatever still slips through.
