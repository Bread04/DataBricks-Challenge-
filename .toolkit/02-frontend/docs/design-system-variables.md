# 🎨 Design System Variables

<!-- markdownlint-disable MD013 -->

> Token architecture for Tailwind v4 + shadcn, aligned with the stable W3C DTCG format. Verified 2026-09-21.

---

## Three-tier architecture

```text
PRIMITIVES  (raw values: what exists)      --color-ink-900, --color-brand-600, --spacing
   ↓ referenced by
SEMANTIC    (roles: what it's for)         --color-surface, --color-fg, --color-accent
   ↓ referenced by
COMPONENT   (local decisions)              .btn { padding: …; background: var(--color-accent) }
```

Rule: **components only reference semantic tokens.** Re-theming, including dark mode, then means changing the semantic layer only.

---

## Tailwind v4 implementation

Key facts ([Tailwind docs](https://tailwindcss.com/docs/theme)):

- `@theme` creates CSS variables **and** utility classes. `:root` creates variables only.
- Use `@theme inline` when a token references another variable.
- A single `--spacing` base drives every spacing utility: `p-4` = 4 × base.
- Namespaces: `--color-*`, `--font-*`, `--text-*`, `--font-weight-*`, `--spacing`, `--breakpoint-*`, `--radius-*`, `--shadow-*`.

```css
/* app/globals.css */
@import "tailwindcss";

/* ── 1. PRIMITIVES ─────────────────────────────── */
@theme {
  --color-ink-900: oklch(0.20 0.02 260);
  --color-ink-600: oklch(0.45 0.02 260);
  --color-paper-50: oklch(0.98 0.005 90);
  --color-paper-100: oklch(0.95 0.008 90);
  --color-brand-600: oklch(0.55 0.15 250);
  --color-brand-700: oklch(0.48 0.15 250);
  --color-red-600: oklch(0.55 0.20 25);

  --spacing: 0.25rem;                 /* 4px → p-2=8, p-4=16, p-6=24, p-8=32 */

  --font-sans: "YourBodyFace", system-ui, sans-serif;
  --font-display: "YourDisplayFace", var(--font-sans);

  --text-sm: 0.875rem;  --text-base: 1rem;  --text-lg: 1.25rem;
  --text-xl: 1.563rem;  --text-2xl: 1.953rem;  --text-3xl: 2.441rem;

  --radius-sm: 0.25rem;  --radius-md: 0.5rem;  --radius-lg: 1rem;
}

/* ── 2. SEMANTIC (reference primitives) ───────── */
@theme inline {
  --color-surface: var(--color-paper-50);
  --color-surface-raised: var(--color-paper-100);
  --color-fg: var(--color-ink-900);
  --color-fg-muted: var(--color-ink-600);
  --color-accent: var(--color-brand-600);
  --color-accent-hover: var(--color-brand-700);
  --color-danger: var(--color-red-600);
}

/* Dark mode: swap semantics only */
@media (prefers-color-scheme: dark) {
  :root {
    --color-surface: var(--color-ink-900);
    --color-fg: var(--color-paper-50);
  }
}
```

> [!NOTE]
> The 1.25 type-scale ratio above is an illustrative choice. The research found no authoritative source for a particular ratio.

---

## Spacing scale

Based on Atlassian's 8 px system, with 2/4/6 px half steps ([Atlassian](https://atlassian.design/foundations/spacing)):

| Token | px | Tailwind (4px base) | Use for |
| --- | --- | --- | --- |
| space-025 | 2 | `p-0.5` | Hairline gaps |
| space-050 | 4 | `p-1` | Icon ↔ label |
| space-100 | 8 | `p-2` | Input padding, tight groups |
| space-150 | 12 | `p-3` | Button padding (y) |
| space-200 | 16 | `p-4` | Card padding, form gaps |
| space-300 | 24 | `p-6` | Between components |
| space-400 | 32 | `p-8` | Section internals |
| space-600 | 48 | `p-12` | Between sections |
| space-800 | 64 | `p-16` | Page-level rhythm |
| space-1000 | 80 | `p-20` | Hero breathing room |

---

## Contrast requirements for tokens (WCAG 2.2 AA)

| Pair | Minimum |
| --- | --- |
| `fg` on `surface` (body text) | **4.5:1** |
| Large text (≥24 px, or ≥18.66 px bold) | **3:1** |
| `accent` borders, icons, focus ring vs neighbours | **3:1** |

Source: [WCAG 2.2](https://www.w3.org/TR/WCAG22/). Check every semantic pair when you define it, and write the ratio in a comment next to the token.

---

## DTCG JSON (when a tool needs it)

The W3C Design Tokens spec reached its **first stable version (2025.10)** in Oct 2025. Each token has a required `$value` and an optional `$type`, plus aliases and theming ([W3C DTCG](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/)).

```json
{
  "color": {
    "brand": { "600": { "$type": "color", "$value": "#2f5fd0" } },
    "accent": { "$type": "color", "$value": "{color.brand.600}" }
  },
  "space": { "200": { "$type": "dimension", "$value": "16px" } }
}
```

Convert it to CSS variables with **[Style Dictionary](https://github.com/style-dictionary/style-dictionary)** (⭐ 4.8k · pushed 2026-09), which supports DTCG. For a hackathon, write tokens straight into `@theme` and only use DTCG if Figma or Stitch hands you JSON.

---

## shadcn integration

- `npx shadcn@latest init` writes its own CSS variables. **Map them to your semantic tokens** instead of keeping the defaults, or it will look like every other shadcn app.
- As of Jul 2026, **Base UI** is the default primitive layer, and `cn` comes from the `cn` package (Sep 2026) ([shadcn changelog](https://ui.shadcn.com/docs/changelog)). Check the changelog before copying older tutorials.
