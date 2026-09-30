# Frontend standards & tooling: digest (r1-1)

Dimension: Frontend standards & tooling. 20 tool calls, ~17 sources. All accessed 2026-09-21.

## Findings

1. Core Web Vitals "good" thresholds are LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1, measured at the 75th percentile of page loads, split by mobile and desktop. | https://web.dev/articles/vitals | web.dev (Google) | 2024-10 | accessed 2026-09-21 | high | standard
2. INP replaced FID and became a stable Core Web Vital in 2024. The page was last updated Oct 2024 and says nothing of threshold changes in 2025–2026. I did not find any change, but I only checked this page. | https://web.dev/articles/vitals | web.dev | 2024-10 | accessed 2026-09-21 | med (for "no change since") | standard
3. web.dev's performance budget examples: under 170 KB of critical-path resources, compressed and minified (the same 170 KB figure also appears as a JS-on-mobile example); images under 2 MB; TTI under 5 s on slow 3G; Lighthouse performance score above 80. Budgets come in three types: quantity, milestone timing and rule-based. The article is from 2018 and uses TTI, which has been deprecated, so treat these numbers as heuristics and not current guidance. | https://web.dev/articles/performance-budgets-101 | web.dev | 2018-11 | accessed 2026-09-21 | med | pattern
4. WCAG 2.2 has been a W3C Recommendation since 12 Dec 2024 (current version). It adds nine criteria: 2.4.11, 2.4.12, 2.4.13, 2.5.7, 2.5.8, 3.2.6, 3.3.7, 3.3.8 and 3.3.9. It removes 4.1.1 Parsing as obsolete. | https://www.w3.org/TR/WCAG22/ | W3C | 2024-12 | accessed 2026-09-21 | high | standard
5. 1.4.3 Contrast (AA) requires 4.5:1 for text, or 3:1 for large text. 1.4.11 Non-text Contrast (AA) requires 3:1 for UI components, their states, and graphics needed to understand content. | https://www.w3.org/TR/WCAG22/ | W3C | 2024-12 | accessed 2026-09-21 | high | standard
6. 2.4.7 Focus Visible (AA) requires a visible keyboard focus indicator. 2.4.11 Focus Not Obscured (Minimum, AA) requires that a focused component is not *entirely* hidden by author content, such as sticky headers or footers. | https://www.w3.org/TR/WCAG22/ | W3C | 2024-12 | accessed 2026-09-21 | high | standard
7. 2.5.8 Target Size (Minimum, AA) requires pointer targets of at least 24×24 CSS px. There are five exceptions: spacing (a 24 px circle around the target does not intersect other targets), equivalent control, inline, user-agent control, and essential. | https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html | W3C WAI | undated | accessed 2026-09-21 | high | standard
8. WCAG 3.0 is still a Working Draft. The latest draft was published 10 Sep 2026, after a March 2026 draft. Secondary sources say a Candidate Recommendation is targeted for about Q4 2027 and a final Recommendation no earlier than 2028. It replaces A/AA/AAA with core and supplemental requirements. Build to WCAG 2.2 AA. | https://www.w3.org/WAI/news/2026-09-10/wcag3/ (W3C, title seen in search); timeline from https://abilitynet.org.uk/resources/digital-accessibility/what-expect-wcag-30-web-content-accessibility-guidelines (via search snippet) | W3C WAI / AbilityNet | 2026-09 | accessed 2026-09-21 | med (timeline is secondary, and I did not fetch the W3C page) | standard
9. The DTCG Design Tokens Specification reached its first stable version, 2025.10, on 28 Oct 2025. The format is JSON; each token has a required `$value` and an optional `$type`, and aliases, theming/multi-brand, and Display P3/OKLCH colour are supported. | https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/ (via search snippet) | W3C DTCG | 2025-10 | accessed 2026-09-21 | high | standard
10. In Tailwind v4, `@theme` defines tokens that emit CSS variables *and* generate utilities, while `:root` only emits variables. Namespaces include `--color-*`, `--font-*`, `--text-*`, `--font-weight-*`, `--spacing`, `--breakpoint-*`, `--radius-*` and `--shadow-*`. A single `--spacing: 0.25rem` base drives utilities such as `p-4` (= 1rem). Use `@theme inline` when a token references another variable. | https://tailwindcss.com/docs/theme | Tailwind Labs | undated | accessed 2026-09-21 | high | standard
11. Atlassian's spacing scale uses an 8 px base (`space.100`). The steps are 0, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64 and 80 px. Guidance: 0–8 px for icon gaps and input padding, 12–24 px for buttons and card internals, 32–80 px for page layout. | https://atlassian.design/foundations/spacing | Atlassian | undated | accessed 2026-09-21 | high | pattern
12. Impeccable (pbakaus/impeccable, Apache-2.0) describes itself as "1 skill, 24 commands, live browser iteration, and 61 deterministic detector rules". It builds on Anthropic's frontend-design skill. Install with `npx impeccable install`, then `/impeccable init`. It supports 17 harnesses, including Claude Code, Cursor, Codex CLI and Gemini CLI. | https://github.com/pbakaus/impeccable | pbakaus (GitHub README) | 2026-09 (pushed 2026-09-21) | accessed 2026-09-21 | high | tooling
13. Impeccable's 24 commands are: init (writes PRODUCT.md), craft, shape, critique, audit, polish, document (writes DESIGN.md), extract, bolder, quieter, distill, harden, onboard, animate, colorize, typeset, layout, delight, overdrive, clarify, adapt, optimize, live and generate. Its detector flags overused fonts (Inter/Arial), purple-to-blue gradients, bounce easing, side-tab borders, dark glows, grey text on colour, pure black/grey, nested cards, small touch targets, skipped heading levels, line length and cramped padding. The rules run without an LLM. | https://github.com/pbakaus/impeccable | pbakaus | 2026-09 | accessed 2026-09-21 | high | tooling
14. Anthropic's frontend-design skill (anthropics/skills) has four steps: ground the design in the subject; plan a compact token system (4–6 named hex colours, typeface roles, ASCII wireframes); review each choice against the brief; build and critique with screenshots. It says to keep 1–2 type families, lines under 80 characters, and "spend your boldness in one place". It names defaults to avoid: cream #F4F1EA with terracotta #D97757, dark backgrounds with acid-green or vermilion accents, SaaS card kits, and template chrome (all-caps eyebrows, middle-dot metadata, monospace labels). | https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md | Anthropic | 2026 (repo pushed 2026-09-10) | accessed 2026-09-21 | high | tooling
15. Google Stitch (Google Labs) was relaunched at I/O on 19 May 2026. It has a "Stitch Agent" that designs in real time on an infinite canvas, accepts voice input, gives design critiques, and runs parallel ideas through an agent manager. It can take existing codebases or design files as input. Exports go to Google Antigravity and publish to Netlify, and designs can be shared via AI Studio. The post does not mention Figma or code-zip export. | https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-updates/ | Google (blog.google) | 2026-05 | accessed 2026-09-21 | high | tooling
16. Stitch reaches Figma through copy-paste plus the official "Stitch to Figma" plugin, which keeps layers and Auto Layout, one screen at a time. Secondary sources say code export covers HTML/CSS/Tailwind and other frameworks as a .zip. Google has also published a Stitch MCP codelab with Antigravity and open-sourced Stitch's DESIGN.md format. | https://www.figma.com/community/plugin/1577379704241183556/stitch-to-figma ; https://justinmckelvey.com/blog/google-stitch-vs-figma ; https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/ (all via search snippets, not fetched) | Figma / blogs / Google | 2026 | accessed 2026-09-21 | low–med | tooling
17. 21st.dev's "21st AI" (formerly Magic Chat) generates multiple variants of React/shadcn components from text. It works on the web, through an MCP `generate` tool (Cursor, Claude Code, Windsurf) that returns a URL rather than inline code, and through the CLI (`npx @21st-dev/cli@latest`). It has a `code` mode (default) and a lightweight `sketch` HTML/Tailwind mode. The free tier is a daily allowance and then a paywall. | https://21st.dev/magic | 21st.dev | undated (current) | accessed 2026-09-21 | med | tooling
18. shadcn/ui is actively evolving. September 2026: components import `cn` from a `cn` package. August 2026: private GitHub registries. July 2026: server-side registry search, and Base UI became the default primitive layer. It has had an MCP server since Aug 2025, supported Tailwind v4 since Feb 2025, and documents `npx shadcn create`. | https://ui.shadcn.com/docs/changelog | shadcn | 2026-09 | accessed 2026-09-21 | med (summarised by a fetch model; check before quoting exact details) | version
19. Impeccable's own numbers don't agree across sources. Search snippets and blogs say "18 skills / 23 commands / 58 rules / ~50k stars"; the current README says 1 skill, 24 commands and 61 rules; the GitHub API reports 69,490 stars. Use the README and API figures. A look-alike repo, gessniio/impeccable_SKILL_CLAUDE, also exists; use the pbakaus original. | https://github.com/pbakaus/impeccable ; https://api.github.com/repos/pbakaus/impeccable | GitHub | 2026-09 | accessed 2026-09-21 | high | repo

## Repos

Stars and last push come from the GitHub API, fetched with curl this session (2026-09-21).

| repo | URL | stars | last push | why useful |
|---|---|---|---|---|
| pbakaus/impeccable | https://github.com/pbakaus/impeccable | 69,490 | 2026-09-21 | The /impeccable design-quality skill: 24 commands plus 61 deterministic anti-slop rules |
| anthropics/skills | https://github.com/anthropics/skills | 177,397 | 2026-09-10 | Official frontend-design SKILL.md, which impeccable builds on |
| shadcn-ui/ui | https://github.com/shadcn-ui/ui | 124,295 | 2026-09-21 | Copy-in accessible components, CLI, registry and MCP |
| 21st-dev/magic-mcp | https://github.com/21st-dev/magic-mcp | 5,906 | 2026-09-09 | 21st Magic MCP server for Claude Code and Cursor ("like v0 in your IDE") |
| serafimcloud/21st | https://github.com/serafimcloud/21st | 5,460 | 2025-05-28 | 21st.dev marketplace source. **Stale (no push for over a year)**; use the hosted site |
| vercel/next.js | https://github.com/vercel/next.js | 142,387 | 2026-09-21 | Default React framework for full-stack hackathon apps |
| vitejs/vite | https://github.com/vitejs/vite | 82,927 | 2026-09-21 | Fastest SPA scaffold (`npm create vite@latest`) |
| style-dictionary/style-dictionary | https://github.com/style-dictionary/style-dictionary | 4,820 | 2026-09-20 | Token build tool; has DTCG support (styledictionary.com/info/dtcg) |
| design-tokens/community-group | https://github.com/design-tokens/community-group | 2,126 | 2026-09-08 | DTCG spec source (stable 2025.10) |
| dequelabs/axe-core | https://github.com/dequelabs/axe-core | 7,537 | 2026-09-18 | Automated a11y engine (Lighthouse and Playwright integrations) |
| jsx-eslint/eslint-plugin-jsx-a11y | https://github.com/jsx-eslint/eslint-plugin-jsx-a11y | 3,618 | 2026-01-06 | Static JSX a11y lint. Slower cadence (last push 8 months ago) but not archived |
| GoogleChrome/lighthouse-ci | https://github.com/GoogleChrome/lighthouse-ci | 7,093 | 2026-03-27 | Enforce perf budgets in CI (last push 6 months ago) |

## Practical material

**Performance budget card (hackathon default)** [F1, F2, F3]
- LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 at p75, checked on mobile.
- JS ≤ ~170 KB compressed on the critical path; hero and other images ≤ ~2 MB total per page; Lighthouse Performance ≥ 80. These are heuristics from a 2018 web.dev article. Say so in the doc.
- Prevent CLS by setting `width`/`height` or `aspect-ratio` on media and reserving space for async content.

**WCAG 2.2 AA fast-build checklist** [F4–F7]
- Body text contrast ≥ 4.5:1; large text ≥ 3:1; borders, icons, focus rings and input outlines ≥ 3:1 against adjacent colours.
- Never write `outline: none` without a replacement. Use `:focus-visible` with a ring of at least 3:1 contrast.
- Sticky headers and footers must not fully cover a focused element. Add `scroll-padding-top` equal to the header height.
- Pointer targets ≥ 24×24 CSS px, or spaced so a 24 px circle doesn't overlap a neighbour. 44 px is a comfortable default.
- No drag-only interactions (2.5.7). Don't make users re-enter information (3.3.7). No cognitive-test logins, so allow paste and password managers (3.3.8).
- Target WCAG 2.2 AA. WCAG 3 is years away [F8].

**Token architecture sketch (primitive → semantic → component)** [F9, F10, F11]
```css
@import "tailwindcss";
@theme {
  /* primitives */
  --color-ink-900: oklch(0.2 0.02 260);
  --color-paper-50: oklch(0.98 0.005 90);
  --color-brand-600: oklch(0.55 0.15 250);
  --spacing: 0.25rem;          /* 4px base → p-2=8px, p-4=16px, p-6=24px */
  --font-sans: "YourChosenFace", system-ui, sans-serif;
  --text-sm: 0.875rem; --text-base: 1rem; --text-lg: 1.25rem; --text-2xl: 1.953rem;
  --radius-md: 0.5rem;
}
@theme inline {
  /* semantic (reference primitives) */
  --color-surface: var(--color-paper-50);
  --color-fg: var(--color-ink-900);
  --color-accent: var(--color-brand-600);
}
/* component tokens in plain CSS */
.btn { padding: calc(var(--spacing) * 3) calc(var(--spacing) * 5); border-radius: var(--radius-md); }
```
- Spacing steps (Atlassian-style 8 px base with 2/4/6 px half steps): 0, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80 px. Small steps go inside components, medium around components, large between page sections [F11].
- DTCG JSON equivalent: `{ "color": { "brand": { "600": { "$type": "color", "$value": "#2f5fd0" } } } }`. Style Dictionary can transform it to CSS variables [F9, repos table].
- The type scale ratio above (1.25) is my own example; I did not find a source for it.

**Anti-"AI slop" rules for PROMPTS.md / docs** [F13, F14]
- Ground the design in the product domain first. Write a mini token plan (4–6 named colours, 1–2 typefaces with roles, an ASCII wireframe) before any code.
- One bold moment per page. Everything else stays quiet.
- Avoid: Inter/Arial as the unexamined default, purple-to-blue gradients, glow-on-dark, identical rounded card grids, bounce easing, all-caps eyebrow labels, middle-dot metadata, nested cards, pure #000 or grey (tint neutrals instead), and grey text on coloured backgrounds.
- Line length ≤ 80 characters. Don't skip heading levels. Use real `<button>`, `<nav>`, `<main>`, `<h1>`–`<h6>`.
- Copy should be short and active-voiced, with specific error messages.

**Tool setup steps** [F12, F15–F18]
- Impeccable: `npx impeccable install`, then `/impeccable init`, which writes PRODUCT.md. The loop is `/impeccable shape` → `craft` → `critique` → `audit` → `polish`. `document` writes DESIGN.md.
- shadcn: `npx shadcn@latest init`, then `npx shadcn@latest add button`. The MCP server lets Claude Code browse and install from the registry. Base UI is the default as of Jul 2026.
- 21st: add the Magic MCP server (21st-dev/magic-mcp) to Claude Code, or run `npx @21st-dev/cli@latest`. It generates component variants; watch the daily free quota.
- Stitch: prompt or voice a design at stitch.withgoogle.com. To bring it into Figma, copy the screen and paste it via the Stitch to Figma plugin. To get code, use export options or Antigravity/Stitch MCP (not fully verified, F16). DESIGN.md can carry design context between Stitch and a coding agent.

**Prompt macro ideas** [F13, F14, F7, F5]
- "Before coding, output: product/audience/job, 5 named colour tokens (with contrast ratios vs surface), 2 type roles, spacing scale, ASCII wireframe. Then build using only those tokens."
- "Audit this component: semantic elements, focus-visible ring ≥3:1, targets ≥24px, contrast ≥4.5:1, no layout shift. Report violations, then fix."
- "Scaffold `<Component>` using shadcn primitives + project tokens only; no hard-coded hex/px; include aria states and keyboard handling."

## Leads not chased / Looked for but not found

- **No 2025–2026 Core Web Vitals threshold changes were found.** I only checked web.dev/articles/vitals (updated Oct 2024). I did not check the Chrome/web.dev blog for new metrics such as soft-navigation work.
- **I found no current authoritative JS budget.** The web.dev budget article dates from 2018. Alex Russell's "performance inequality gap" posts would give a more recent figure; I did not fetch them.
- **Carbon spacing page:** the fetch returned truncated content, so I have no Carbon token values. Material, Radix and shadcn spacing/type-scale docs were not fetched. I found no sourced typographic scale ratio.
- **Stitch:** I did not fetch or confirm its current code export formats, Figma export, the Stitch MCP codelab (codelabs.developers.google.com/design-to-code-with-antigravity-stitch) or the DESIGN.md open-source post. Pricing and quota are unknown.
- **v0 (Vercel):** not researched this round.
- **shadcn CLI:** exact current version number not retrieved. The npm page would give it.
- **The WCAG 3 W3C news page itself was not fetched.** The 10 Sep 2026 date comes from the search result title and snippet.
- **The DTCG announcement was not fetched directly.** The details come from search snippets, though it is the W3C community page.
- **Next.js/Vite starter templates:** I have repo stats but did not check the specific starters (create-next-app flags, shadcn Vite template).
