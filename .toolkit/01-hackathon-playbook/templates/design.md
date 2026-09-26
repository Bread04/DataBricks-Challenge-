# Design: [Project Name]

<!-- markdownlint-disable MD013 -->

> Adapted from help-me-papi's design template, plus the token and anti-slop rules from `../../02-frontend/docs/`.

## 1. User flow

1. **Landing:** what they see first (70% of the visual effort goes here)
2. **Primary action:** upload, input, choose
3. **Core loop:** result, dashboard, interaction
4. **Final state:** share, export, done

## 2. Aesthetic direction (pick ONE, deliberately)

- **Direction:** e.g. Apple-like clarity / editorial minimal / data-dense / retro terminal / neo-brutalist (see `../../02-frontend/docs/aesthetics-directory.md`)
- **Why it fits the domain:**
- **The one bold moment:**
- **Anti-references:** what it must NOT look like

## 3. Reference links

- [Link 1]: what we're taking from it
- [Link 2]: what we're taking from it

## 4. Tokens

| Token | Value | Contrast vs surface |
| --- | --- | --- |
| surface | | — |
| fg | | ≥ 4.5:1 |
| muted | | ≥ 4.5:1 if it's text |
| accent | | ≥ 3:1 |
| danger | | ≥ 3:1 |

Type: display = `____` · body = `____` · Spacing: 4 px base · Radius: `____`

## 5. Components (shadcn / 21st.dev)

| Slot | Source | Link |
| --- | --- | --- |
| Header / nav | shadcn | |
| Hero / AHA component | 21st.dev | |
| Stats / cards | shadcn | |

## 6. States checklist (per screen)

- [ ] Loading (skeleton, no layout shift)
- [ ] Empty (explains the situation and gives one CTA)
- [ ] Error (plain language, how to fix, retry)
- [ ] Success (feedback near the action)
