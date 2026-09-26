# 🎨 Frontend / UI-UX Macros

<!-- markdownlint-disable MD013 -->

> Copy-paste prompts for Claude Code. They assume tokens in `app/globals.css` (see `docs/design-system-variables.md`) and shadcn installed.
> Standards they enforce: `docs/standards.md` · Anti-slop rules: `docs/clarity-first-design.md`

---

## Contents

| Code | Macro | When |
| --- | --- | --- |
| [F1](#f1--design-brief-before-code) | Design brief before code | Start of UI work |
| [F2](#f2--tokens-from-a-brief-or-designmd) | Tokens from a brief or DESIGN.md | After F1 / Stitch |
| [F3](#f3--component-scaffold) | Component scaffold | Every component |
| [F4](#f4--page-assembly) | Page assembly | Every screen |
| [F5](#f5--source-a-distinctive-component) | Source a distinctive component | The "bold moment" |
| [F6](#f6--a11y--perf-audit) | A11y + perf audit | Before commit |
| [F7](#f7--de-slop-pass) | De-slop pass | Feature freeze |
| [F8](#f8--states-hardening) | States hardening | Before demo |
| [F9](#f9--responsive-check) | Responsive check | Before demo |
| [F10](#f10--ux-heuristics-review) | UX heuristics review | Polish |
| [F11](#f11--generate-with-taste) | Generate with taste | New screens |
| [F12](#f12--deployed-slop-gate) | Deployed slop gate | Before pitch |
| [F13](#f13--state-without-ceremony) | State without ceremony | Build |

> F10–F13 are adapted from [help-me-papi](https://github.com/maxi-cmyk/help-me-papi) `frontend/PROMPTS.md` (`REVIEW_UX_HEURISTICS`, `AUDIT_UI_CLARITY`, `IMPLEMENT_STATE_MANAGEMENT`) and its Taste Skill notes.

---

### F1 · Design brief before code

```text
Before writing any code, output a design brief for <product> (audience: <who>, job: <what>):
1. 5 named colour tokens (surface, fg, muted, accent, danger) as OKLCH + hex, with contrast ratio of each vs surface (fg must be ≥4.5:1, accent ≥3:1).
2. 2 type roles (display, body) — avoid Inter/Arial unless justified by the domain.
3. Spacing scale on a 4px base.
4. ASCII wireframe of the demo screen.
5. The ONE bold moment on this screen and why.
Ground every choice in the product domain, not generic SaaS defaults.
```

*Based on:* the Anthropic frontend-design four-step process and Impeccable's `init` ([Anthropic](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md), [Impeccable](https://github.com/pbakaus/impeccable)).

### F2 · Tokens from a brief or DESIGN.md

```text
Convert <this brief | DESIGN.md> into Tailwind v4 tokens in app/globals.css:
- @theme: primitives (colour ramps in oklch, --spacing: 0.25rem, font families, type scale, radii).
- @theme inline: semantic tokens (surface, surface-raised, fg, fg-muted, accent, accent-hover, danger) referencing primitives.
- Dark mode by redefining semantic tokens only.
- Map shadcn's CSS variables onto our semantic tokens.
Add a comment with the contrast ratio next to each semantic colour pair. No component may use raw hex/px after this.
```

### F3 · Component scaffold

```text
Scaffold <ComponentName> for <purpose>.
- Build on shadcn primitives (use the shadcn MCP to install anything missing).
- Styling: semantic tokens only; no hard-coded hex/px/arbitrary values.
- Semantic HTML: native <button>/<a>/<input>/<label>; correct heading level for context.
- A11y: visible :focus-visible ring (≥3:1), targets ≥24×24px (aim 44), aria-* for state (expanded, pressed, invalid), keyboard support.
- States: default, hover, focus, active, disabled, loading, error, empty.
- Props typed in TypeScript; export a usage example.
```

### F4 · Page assembly

```text
Assemble the <page> from existing components and tokens only. Layout from this wireframe: <ASCII>.
- Landmarks: header/nav/main/footer; one h1; no skipped levels.
- Whitespace first: section gaps ≥ p-12, component gaps p-6, internals p-4.
- Line length ≤ 65ch for text blocks.
- Media: next/image with width/height (no CLS); hero image priority.
- Seed with realistic demo data from <file>, not lorem ipsum.
```

### F5 · Source a distinctive component

```text
Use the 21st MCP: search for "<component idea>" and get_inspiration for 3 references.
Pick the one that best fits our DESIGN.md, then adapt it to our semantic tokens and shadcn primitives.
Remove anything that violates docs/clarity-first-design.md (gradients, glows, bounce easing, nested cards).
```

*Note:* `generate` needs AI access enabled on your 21st account, while `search` and `search_logo` are free ([21st.dev/mcp](https://21st.dev/mcp)).

### F6 · A11y + perf audit

```text
Audit <component/page> against WCAG 2.2 AA and Core Web Vitals:
- Contrast: text ≥4.5:1 (large 3:1); UI/focus/borders ≥3:1.
- Focus visible, not fully obscured by sticky header (scroll-padding-top).
- Targets ≥24×24 CSS px or spaced; no drag-only actions; labels on inputs; errors linked via aria-describedby.
- CLS: media dimensions set, space reserved for async content. INP: no heavy work in handlers. LCP: hero optimised.
Report violations as a table (criterion, element, fix), then apply the fixes.
```

*Thresholds:* [WCAG 2.2](https://www.w3.org/TR/WCAG22/) · [web.dev vitals](https://web.dev/articles/vitals)

### F7 · De-slop pass

```text
Run /impeccable audit on the app. Then fix every flag, prioritising: default fonts, purple/blue gradients, glows on dark, nested cards, grey-on-colour text, pure black/grey, bounce easing, cramped padding, skipped headings.
Then /impeccable polish. Show before/after screenshots via Playwright MCP.
```

### F8 · States hardening

```text
For every data-driven component on the demo path, add: loading skeleton (fixed size, no layout shift), empty state with next action, error state with a specific fix-it message and retry, and an optimistic update where the action is a mutation.
Then list any remaining path where a slow API would leave the judge staring at nothing.
```

### F9 · Responsive check

```text
Use Playwright MCP to screenshot <url> at 375px, 768px, 1280px. List overflow, overlap, tap targets <24px, and text >80ch. Fix with token-based responsive utilities only.
```

### F10 · UX heuristics review

```text
Review <page/flow> as a UX strategist against Nielsen's 10 heuristics and the Reduction Framework (docs/ux-heuristics.md):
1. Visibility of status: every async action has loading → result feedback.
2. The 5-second rule: is the Tier-1 action immediately obvious? Are Tier-2 items subdued and Tier-3 hidden?
3. Visual weight: secondary actions properly de-emphasised.
4. Breathing room around interactive targets; targets ≥24px (aim 44).
5. Empty / error / disabled states explain themselves.
Output: Must Fix / Should Fix / Nitpick, each with the fix. Then apply the Must Fixes.
```

### F11 · Generate with taste

```text
Using the Taste Skill (design-taste-frontend v2): brief inference → design-system map → generate <screen>.
Dials: DESIGN_VARIANCE=<5–7>, MOTION_INTENSITY=<3–5>, VISUAL_DENSITY=<3–7>.
Constraints: our @theme tokens only, shadcn primitives, semantic HTML, the ONE aesthetic direction in docs/design.md.
Then run /impeccable audit on the result and fix every flag that isn't a deliberate choice recorded in design.md.
```

*See:* `docs/taste-skill.md` · `docs/impeccable.md`

### F12 · Deployed slop gate

```text
Run `npx impeccable detect --json https://<demo-url>` and `npx impeccable detect --json src/`.
Group findings by rule, fix all that affect the demo path, and add reasoned ignores (npx impeccable ignores add-value …) only for deliberate brand choices in docs/design.md.
Re-run until clean, then screenshot the hero at 375px and 1280px with Playwright MCP.
```

### F13 · State without ceremony

```text
Add state for <feature> the hackathon way:
- Local component state first; pass props if ≤2 levels deep.
- Server state via Server Components or a data hook — not copied into a global store.
- Only truly global UI state (e.g. current workspace, player, map) goes in a tiny Zustand store.
- Optimistic updates for toggles/likes: update now, sync in background, revert on failure with a toast.
Output the store/hook and show one component consuming it.
```
