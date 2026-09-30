# 🖼️ Aesthetics Directory

<!-- markdownlint-disable MD013 -->

Pick **one** deliberate direction per project, then study what's listed for it. Adapted from [help-me-papi](https://github.com/maxi-cmyk/help-me-papi) `frontend/docs/design-resources.md` and `frontend/skills/styling-tokens.md`.

> [!NOTE]
> **Reconciling two schools of thought.** help-me-papi's hackathon notes say glassmorphism, gradients and dark mode "wow judges". The anti-slop tools (Impeccable, Anthropic frontend-design) flag *default* purple-to-blue gradients and glows as AI tells. Both can be true: **a deliberate, domain-fitting aesthetic wins, and an unexamined default loses.** Choose a direction from this list on purpose, write it in `design.md`, and run `/impeccable audit`, ignoring rules that conflict with the chosen direction (see `impeccable.md`).

---

## Default: Apple-like clarity

**Focus:** big typography, precise whitespace, translucent blur, one focal point.

| Study | What to take |
| --- | --- |
| apple.com | Scroll-driven product storytelling |
| linear.app | Dark hero, restrained single CTA, stark type |
| stripe.com | Dense technical copy, confident colour |
| raycast.com | Interactive, polished hero media |
| vercel.com | Sparse layouts, monochrome geometry, micro-borders |

**Tokens (from help-me-papi `styling-tokens.md`):**

- Mostly monochrome (whites, soft greys, off-blacks) with **one vibrant accent** used only for interaction.
- Glass surface:

  ```css
  .surface-glass {
    background-color: rgb(255 255 255 / 0.7);
    backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid rgb(255 255 255 / 0.3);
  }
  ```

- Soft elevation (never black or muddy):

  ```css
  .shadow-high { box-shadow: 0 10px 40px -10px rgb(0 0 0 / 0.08), 0 1px 3px rgb(0 0 0 / 0.04); }
  ```

- Type tracking: display (48 px+) `-0.04em` weight 600 · heading (24–40 px) `-0.02em` weight 600 · body 16 px, line height 1.5.

Check glass text contrast (WCAG 4.5:1) against the **worst-case background** behind the blur.

---

## Alternatives

| Direction | Study | Tools / references |
| --- | --- | --- |
| **Editorial minimal** | Notion, Linear docs | Taste Skill `minimalist-ui` |
| **Swiss / Bauhaus brutalism** | Gumroad redesign | Müller-Brockmann *Grid Systems*, [Typewolf](https://www.typewolf.com), Taste `industrial-brutalist-ui` |
| **Neo-brutalism** | Figma marketing pages | NeoBrutalism UI (thick borders, hard shadows) |
| **Data-dense / Bloomberg** | Bloomberg Terminal | AG Grid; Tufte, *The Visual Display of Quantitative Information* |
| **Hyper-playful (Gen-Z)** | Arc launch, Zenly, BeReal | LottieFiles, Spline, [Godly](https://godly.website/) |
| **Arcade / 8-bit** | Playdate, Stardew Valley | NES.css, RPGUI, [Lospec palettes](https://lospec.com/palette-list) |
| **Synthwave / cyberpunk** | Cyberpunk 2077 | Arwes, Three.js |
| **Skeuomorphic / Y2K Aero** | macOS Snow Leopard, Teenage Engineering | 98.css, XP.css, [skeuomorph.com](https://skeuomorph.com) |
| **Neumorphism** | Audio software | [neumorphism.io](https://neumorphism.io) ⚠️ often fails contrast, so check it |

---

## Two proven themes from real projects

### Retro terminal (from help-me-papi's NFC portfolio)

- **Palette:** cream `#f5f0e8` · navy text `#1a1a40` · gold interactive `#b8860b` / `#d4a017` · traffic-light status colours
- Monospace sections (JetBrains Mono / SF Mono), with a skippable typewriter boot sequence and command-router UI (`whoami`, `help`)
- **Why it works:** tiny payload (great Core Web Vitals on event Wi-Fi) and memorable
- **Pitfalls:** body text still ≥ 16 px; always offer visible navigation too; skip the animation on repeat visits and when `prefers-reduced-motion` is set

### Clinical / healthcare (from help-me-papi's Epicenter demo)

- **Palette:** white / `#f8f9fa` base · charcoal text · medical-blue primary · status green/amber/red/blue, **always with a text label**
- Gated task flow (Identity → Forms → Review → Billing → Summary), prominent queue number
- Touch targets 44 px+; full keyboard support; plain-language errors with recovery actions
- **Why it works:** trustworthy, accessible under stress, scales from patient view to staff dashboard

---

## Component libraries (hackathon-appropriate)

| Need | Pick |
| --- | --- |
| Accessible primitives | shadcn/ui (Base UI default as of Jul 2026), Radix, React Aria |
| Pre-styled, minimal | Radix Themes, Geist-style layouts |
| Motion | Framer Motion (springs), CSS transitions for simple states |
| Distinctive one-offs | 21st.dev (see `../../05-tools-and-mcp/docs/21st-dev-mcp.md`) |
| Avoid for consumer apps | Bootstrap, MUI, Ant Design: heavy, and they look generic unless you override heavily |
