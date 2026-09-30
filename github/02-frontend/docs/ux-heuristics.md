# 🧭 UX Heuristics and the Reduction Framework

<!-- markdownlint-disable MD013 -->

> What to show, what to hide, and how to check it. Adapted from [help-me-papi](https://github.com/maxi-cmyk/help-me-papi) (`frontend/skills/` clarity-first, layout-and-interaction and rendering-and-loading skills, plus the `REVIEW_UX_HEURISTICS` macro).

---

## Three questions before adding ANY element

1. Does the user need this to finish their main task? If not, remove it or hide it.
2. Can it be inferred or defaulted instead of asked?
3. Would a first-time user understand it in under 3 seconds?

---

## The Reduction Framework

| Tier | What | Treatment | Rule |
| --- | --- | --- | --- |
| **1 · Core actions** | The 1–3 things the user came to do | Primary weight, prominent, largest targets | "If this screen could have only one button, what is it?" Rarely more than 3 |
| **2 · Supporting** | Filters, settings, secondary navigation, metadata | Visible but subdued: secondary buttons, smaller type, muted colour | Supports the task but isn't the reason they came |
| **3 · Edge cases** | Advanced settings, bulk actions, export, admin | Hidden: overflow menu, "Advanced" toggle, expandable section | Power users and rare tasks |

If an element fits no tier, it doesn't belong on the screen.

**Responsive reduction:** desktop shows all tiers. Tablet folds Tier 3 into menus. Mobile shows Tier 1 only in the main view, with Tier 2 in tabs or sheets and Tier 3 in settings.

**For a hackathon demo:** the judge's journey should only ever touch Tier 1.

---

## Nielsen's 10 usability heuristics (checklist)

| # | Heuristic | Hackathon check |
| --- | --- | --- |
| 1 | Visibility of system status | Every async action shows loading and then a result |
| 2 | Match with the real world | The user's words, not developer jargon |
| 3 | User control and freedom | Clear back, cancel and undo; never trap the judge |
| 4 | Consistency and standards | Same word, same meaning, same place |
| 5 | Error prevention | Disable invalid actions; smart defaults |
| 6 | Recognition over recall | Show options; label icons |
| 7 | Flexibility and efficiency | Shortcuts are optional; guided flow first |
| 8 | Aesthetic and minimalist design | Every extra element competes with the core one |
| 9 | Help users recover from errors | Say what went wrong and how to fix it |
| 10 | Help and documentation | If it needs a manual, simplify it |

Reference: [Nielsen Norman Group articles](https://www.nngroup.com/articles/)

---

## Interaction states (every interactive element)

| State | Rule |
| --- | --- |
| Default | Clearly interactive |
| Hover | Subtle; **never** the only place critical info appears (touch screens have no hover) |
| Active / pressed | Immediate feedback |
| Disabled | Muted **and** says why (tooltip or adjacent text) |
| Loading | Skeleton or inline spinner, never a blank void |
| Success / error | Feedback **near the action**, not in a distant banner |
| Empty | Explains what's missing and gives **one** CTA ("Create your first project") |

---

## Typography and colour rules

- Body text ≥ 16 px (14–15 px for dense data UIs); line height 1.4–1.6; **50–75 characters per line**.
- Maximum 3 heading levels per view. Needing a fourth means the page is too complex.
- Label icons in primary navigation. Icon-only is acceptable only for universal symbols (close, search, menu) or with a tooltip.
- **Semantic colour:** red for destructive or error, green for success, blue for interactive or info, amber for warning. Never make a non-destructive primary button red.
- Palette: 1 primary, 1 accent, neutrals, plus semantic colours. **Never use colour alone** to convey status; pair it with text or an icon.
- Dark mode is **not an inversion**. It needs its own tokens.

---

## The 60 fps rule (motion and performance)

- Animate **only `transform` and `opacity`**, which run on the GPU.
- **Never animate** `width`, `height`, `top`, `left`, `margin`, `padding` or `box-shadow`, because they cause reflow.
- Fonts: `font-display: swap`; preload only the critical `.woff2`; use system fonts where custom type isn't needed.
- **Optimistic UI** for simple toggles and likes: update immediately, sync in the background, and revert only on failure.
- Respect `prefers-reduced-motion`.
- Fluid type without breakpoints: `font-size: clamp(1rem, 0.8rem + 1vw, 1.5rem);`

These add to the CWV budget in `standards.md` (LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1).

---

## Further reading

- [Nielsen Norman Group](https://www.nngroup.com/articles/): heuristics, F-pattern, cognitive load
- [Apple Human Interface Guidelines](https://developer.apple.com/design/): deference, clarity, depth
- [Material Design 3](https://m3.material.io): elevation and density (worth reading for the maths, not the look)
- Dieter Rams, *10 Principles of Good Design*: "as little design as possible"
