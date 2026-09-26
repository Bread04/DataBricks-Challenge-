# ✨ Clarity-First Design

<!-- markdownlint-disable MD013 -->

> Principles for UI that a judge understands in 5 seconds. Built on Anthropic's frontend-design skill and Impeccable's detector rules. Verified 2026-09-21.

---

## The five principles

| # | Principle | In practice |
| --- | --- | --- |
| 1 | **Ground the design in the subject** | Before any code, write down the product, audience and job to be done. The palette and type should *come from* the domain, not from a template ([Anthropic frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)) |
| 2 | **Whitespace first** | Space separates things before borders or colour do. Small gaps inside components, medium between them, large between sections ([Atlassian spacing](https://atlassian.design/foundations/spacing)) |
| 3 | **One bold moment** | "Spend your boldness in one place." Everything else stays quiet (Anthropic) |
| 4 | **Semantic before styled** | Use real `<button>`, `<nav>`, `<main>`, `<h1>`–`<h6>` in order. Styling comes second |
| 5 | **Tokens, never magic numbers** | Every colour, space, radius and font size comes from a token (see `design-system-variables.md`) |

---

## Pre-code design brief (5 minutes, mandatory)

Write this before generating any UI. Both the Anthropic skill and Impeccable (`/impeccable init` → `PRODUCT.md`) start this way.

```markdown
## Product
<what it is, one line> · Audience: <who> · Job: <what they're trying to get done>

## Tokens
Colors (4–6, named): surface #…, fg #…, muted #…, accent #…, danger #…
  → contrast vs surface: fg ≥ 4.5:1 ✅ · accent-on-surface ≥ 3:1 ✅
Type: display = <face>, body = <face>   (1–2 families max)
Spacing: 4px base → 4/8/12/16/24/32/48/64
Radius: <n>px · Shadow: <none | one level>

## Wireframe (ASCII)
┌───────────────────────────┐
│ Logo            [Action]  │
├───────────────────────────┤
│  H1 value prop            │
│  [Primary CTA]            │
│  ┌─────┐ ┌─────┐ ┌─────┐  │
└───────────────────────────┘

## The one bold moment
<e.g. the live result animating in>
```

---

## 🚫 Anti-"AI slop" list

These are what Impeccable's 61 deterministic rules and Anthropic's skill flag as tells of generic AI-made UI ([Impeccable](https://github.com/pbakaus/impeccable), [Anthropic](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)):

| Avoid | Do instead |
| --- | --- |
| Inter or Arial as an unexamined default | Pick a face that fits the domain; 1–2 families |
| Purple-to-blue gradients | A single accent from the domain palette |
| Dark background with glowing or acid-green accents | Tinted neutrals; glow only if it *means* something |
| Identical rounded card grids, nested cards | Vary density; flatten the hierarchy |
| Bounce or elastic easing | Short ease-out (150–250 ms) |
| All-caps eyebrow labels, middle-dot metadata, monospace labels everywhere | Plain sentence-case labels |
| Pure `#000` or pure grey | Neutrals tinted toward the brand hue |
| Grey text on coloured backgrounds | Check contrast; use a darker tint of the background hue |
| Side-tab accent borders | Whitespace and weight for emphasis |
| Cream `#F4F1EA` + terracotta `#D97757`, SaaS card kits, template chrome | Anthropic names these as its own overused defaults |
| Cramped padding, line length > 80 characters, skipped heading levels | Spacing tokens, `max-width: 65ch`, strict heading order |

---

## Copy rules

- Short, active voice. The button says what happens ("Create invoice", not "Submit").
- Error messages say what went wrong **and** how to fix it.
- Empty states tell the user the next action.
- No filler hero copy ("Revolutionize your workflow"). Say the concrete value.

---

## Clarity test (60 seconds)

Show the screen to someone for **5 seconds**, then hide it. Ask them:

1. What is this for?
2. What would you click first?
3. What stood out?

If answer 3 isn't your "one bold moment", or answer 1 is wrong, simplify.
