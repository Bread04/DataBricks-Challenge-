---
name: hackathon-frontend
description: Frontend toolkit for hackathon UI covering clarity-first design, Tailwind v4 tokens, shadcn, WCAG 2.2 AA, Core Web Vitals budgets, anti-AI-slop rules, and the Stitch/21st/impeccable workflow, and UI for AI features (streaming, tool-call cards, approvals). Use when building or reviewing UI during a hackathon.
---

# Frontend Toolkit

<!-- markdownlint-disable MD013 -->

> Condensed rules. Full detail: `../../02-frontend/docs/` · macros in `../../02-frontend/PROMPTS.md`. Verified 2026-09-21, updated 2026-09-23.

## Before any UI code

Write a brief: product/audience/job · 4–6 named colour tokens with contrast ratios · 1–2 type roles · 4 px spacing scale · ASCII wireframe · **one bold moment**.

## Standards (quality gates)

| Area | Gate |
| --- | --- |
| Performance | **LCP ≤ 2.5 s · INP ≤ 200 ms · CLS ≤ 0.1** (p75, mobile). JS ≤ ~170 KB and Lighthouse ≥ 80 are *heuristics* (2018 source) |
| Accessibility | **WCAG 2.2 AA**: text 4.5:1 (large 3:1); UI and focus 3:1; `:focus-visible` always; focus not hidden by sticky UI; targets ≥ 24×24 px; no drag-only; allow paste in logins |
| Semantics | Landmarks; one h1; no skipped levels; `<button>` for actions, `<a>` for navigation; labelled inputs |
| Tokens | Tailwind v4 `@theme` primitives → `@theme inline` semantics → components use semantics only. No raw hex or px |
| Whitespace | 8 px system with half steps: 4/8/12/16/24/32/48/64/80. Section gaps ≥ 48 px; text ≤ 65ch |

## Anti-slop (Impeccable + Anthropic frontend-design)

Avoid: default Inter/Arial · purple-to-blue gradients · glows on dark · identical or nested card grids · bounce easing · all-caps eyebrows and middle-dot metadata · pure #000 or grey · grey text on colour · cramped padding.

## Hackathon priorities

- **Hero focus:** about 70% of visual effort goes on the first viewport the judge sees.
- **One deliberate aesthetic** (`../../02-frontend/docs/aesthetics-directory.md`), recorded in `design.md`.
- **Reduction Framework:** Tier 1 visible, Tier 2 subdued, Tier 3 hidden. The judge's path only touches Tier 1.
- **Fake data first:** build the UI on hardcoded JSON, then swap in the API when it's ready.
- **Animate only transform and opacity** (60 fps). Toasts, not crashes.

## AI feature UI (if your app has a chatbot or agent)

- **Build on:** AI SDK UI `useChat` + **AI Elements** (shadcn-based conversation, message, streaming, tool-call and reasoning components) or shadcn's own chat components. CopilotKit/AG-UI only if the agent runs on a separate backend framework.
- **Required states:** streaming text (the first token visible within about 1 s) · a **card per tool call** (running → done → failed) · an **approval prompt** before write, pay or send actions (shadcn Human-in-the-Loop helpers / AI SDK `toolApproval`) · empty, error and retry states (Next.js 16.3 `catchError` + `retry()`).
- **Generative UI:** map tool results to your own React components instead of dumping raw text.

## Defaults and polish (versions from npm, 2026-09)

- **Data and state:** TanStack Query 5 · Zustand 5 · forms: React Hook Form 7 + `@hookform/resolvers` 5 + Zod 4 (TanStack Form v1 is a stable alternative).
- **Motion 13** (`motion`): wrap the app in `<MotionConfig reducedMotion="user">`. Same-document View Transitions are Baseline; cross-document ones don't work in Firefox.
- **Accessibility check:** `@axe-core/playwright` in one smoke test, plus the Lighthouse panel in DevTools. Lighthouse CI hasn't had a release since 2025-06.
- **Judges:** one working flow within about 90 s, with everything mocked and pre-filled. Clean beats elaborate.

## Tool flow

```text
Stitch (directions) → Stitch MCP → DESIGN.md → @theme tokens
→ shadcn MCP (base components) → 21st MCP (1 distinctive component)
→ Taste Skill (generate) → Claude Code assembles → /impeccable audit → polish
→ npx impeccable detect <demo-url> → Playwright screenshots
```

## Key facts (2026-09)

- Impeccable (pbakaus): 1 skill, 24 commands, 61 rules. `npx impeccable install` → `/impeccable init`.
- shadcn: **CLI v4** (`npx shadcn init`; the `--base` flag picks Radix or Base UI). Base UI has been the default since Jul 2026, with Radix still supported and React Aria a third option. Chat components (Jun) and Human-in-the-Loop helpers (Aug). `cn` moved to its own package (Sep). MCP via `mcp init --client claude`.
- Tailwind **v4.3** (no v5). Tailwind Labs joined Shopify on 2026-09-09 and stays MIT, so no action is needed. Tailwind Plus is closed to new buyers.
- Next.js **16.3**: the React Compiler is stable but opt-in, and `next dev` writes an `AGENTS.md` for coding agents.
- AI app-builder free tiers are tight: v0 is $5 a month plus 7 messages a day, Lovable 5 credits a day, Bolt 300K tokens a day, Figma Make 500 credits a month (one generation can use 100+). Spread prompts across teammates' accounts.
- DTCG tokens spec stable (2025.10). Style Dictionary converts it.
- WCAG 3 is still a draft (not before ~2028), so build to 2.2.
- Stitch sync is one-way (Stitch → code).

## Sources

[web.dev vitals](https://web.dev/articles/vitals) · [WCAG 2.2](https://www.w3.org/TR/WCAG22/) · [Tailwind theme](https://tailwindcss.com/docs/theme) · [Atlassian spacing](https://atlassian.design/foundations/spacing) · [Impeccable](https://github.com/pbakaus/impeccable) · [Anthropic frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) · [shadcn changelog](https://ui.shadcn.com/docs/changelog) · [AI Elements](https://elements.ai-sdk.dev/) · [Next.js 16.3](https://nextjs.org/blog/next-16-3) · [Motion a11y](https://motion.dev/docs/react-accessibility) · [Tailwind × Shopify](https://tailwindcss.com/blog/tailwind-is-joining-shopify)
