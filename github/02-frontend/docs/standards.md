# ✅ Frontend Standards: Accessibility and Performance

<!-- markdownlint-disable MD013 -->

> The non-negotiable quality gates. Verified 2026-09-21.

---

## Summary card

| Standard | Target | Source |
| --- | --- | --- |
| Whitespace-first | Spacing tokens only; section gaps ≥ 48 px | [Atlassian](https://atlassian.design/foundations/spacing) |
| Semantic HTML | Landmarks + ordered headings + native controls | [WCAG 2.2](https://www.w3.org/TR/WCAG22/) |
| Token-based CSS | Zero hard-coded hex/px in components | [Tailwind @theme](https://tailwindcss.com/docs/theme) |
| Accessibility | **WCAG 2.2 AA** | [W3C](https://www.w3.org/TR/WCAG22/) |
| Performance | **LCP ≤ 2.5 s · INP ≤ 200 ms · CLS ≤ 0.1** (p75, mobile) | [web.dev](https://web.dev/articles/vitals) |

---

## ♿ WCAG 2.2 AA fast-build checklist

WCAG 2.2 has been a W3C Recommendation since **12 Dec 2024**. It adds 9 criteria and removes 4.1.1 Parsing. **WCAG 3 is still a Working Draft** (latest 2026-09-10), and the final version isn't expected before about 2028, so build to 2.2 ([W3C](https://www.w3.org/TR/WCAG22/), [W3C WAI news](https://www.w3.org/WAI/news/2026-09-10/wcag3/)).

### Contrast

- [ ] Body text ≥ **4.5:1**; large text ≥ **3:1** (1.4.3)
- [ ] UI component borders, icons, focus rings, input outlines ≥ **3:1** against adjacent colours (1.4.11)

### Keyboard and focus

- [ ] Everything works with a keyboard alone
- [ ] Focus is always visible (2.4.7). **Never** write `outline: none` without a replacement:

  ```css
  :focus-visible { outline: 2px solid var(--color-accent); outline-offset: 2px; }
  ```

- [ ] A sticky header or footer never *fully* hides the focused element (2.4.11 Focus Not Obscured):

  ```css
  html { scroll-padding-top: var(--header-height); }
  ```

### Targets and input

- [ ] Pointer targets ≥ **24×24 CSS px**, or spaced so a 24 px circle doesn't overlap a neighbour (2.5.8). 44 px is a comfortable default ([W3C Understanding 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html))
- [ ] No drag-only interactions; offer a click alternative (2.5.7)
- [ ] Don't make users re-enter information they've already given (3.3.7)
- [ ] No cognitive-test logins; allow paste and password managers (3.3.8)

### Semantics

- [ ] One `<h1>`; no skipped heading levels
- [ ] `<header>`, `<nav>`, `<main>`, `<footer>` landmarks
- [ ] `<button>` for actions, `<a>` for navigation. Never use a `<div onClick>`
- [ ] Every input has a `<label>`; errors are linked with `aria-describedby`
- [ ] Images have meaningful `alt`; decorative images use `alt=""`

### Tooling

| Tool | Use | Status |
| --- | --- | --- |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated a11y engine (Playwright, Lighthouse) | ⭐ 7.5k · pushed 2026-09 |
| [eslint-plugin-jsx-a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y) | Static JSX lint | ⭐ 3.6k · pushed 2026-01 (slower cadence) |
| `/impeccable audit` | Flags small targets, skipped headings, grey-on-colour | See `impeccable.md` |

---

## ⚡ Performance budget

### Core Web Vitals (Google's "good" thresholds)

| Metric | Good | What it measures | Hackathon quick fix |
| --- | --- | --- | --- |
| **LCP** | ≤ 2.5 s | Largest content paint | `next/image` with `priority` on the hero image; preload the display font |
| **INP** | ≤ 200 ms | Interaction responsiveness (replaced FID in 2024) | No heavy work in click handlers; `useTransition` for slow updates |
| **CLS** | ≤ 0.1 | Layout shift | `width`/`height` or `aspect-ratio` on all media; reserve space for async content |

Measured at the **75th percentile**, mobile and desktop separately ([web.dev](https://web.dev/articles/vitals)). No threshold changes since the Oct 2024 page update were found.

### Resource budget (heuristic)

| Budget | Value |
| --- | --- |
| Critical-path JS (compressed) | ≤ ~170 KB |
| Images per page | ≤ ~2 MB total |
| Lighthouse Performance | ≥ 80 |

> [!CAUTION]
> These resource numbers come from a **2018** web.dev article ([source](https://web.dev/articles/performance-budgets-101)) and should be treated as rough rules of thumb.
>
> **Newer reference (Deepen run):** Alex Russell's *Performance Inequality Gap, 2026* models a 3-second load on 75th-percentile devices (Galaxy A24-class). It gives roughly **~1.5 MiB of critical-path bytes for JS-light pages vs ~935 KiB for JS-heavy pages** ([source](https://infrequently.org/2025/11/performance-inequality-gap-2026/)). Which figure belongs to which page type is inferred from a snippet and wasn't confirmed, so read the post before quoting numbers.

### Enforce it

- **[Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci)** (⭐ 7.1k): add budgets to CI. This is optional for a hackathon.
- Before judging, run Lighthouse on the deployed URL using mobile emulation.
