# 🧩 21st.dev MCP Manual (Component Sourcing)

<!-- markdownlint-disable MD013 -->

Search, retrieve and generate React/Tailwind components from Claude Code. Verified 2026-09-21.

> [!IMPORTANT]
> **"Magic MCP is now the 21st MCP."** The tools were renamed and **old Magic API keys were reset**, so create a new key even if you used Magic before ([21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp)).

---

## At a glance

| | |
| --- | --- |
| Repo | [21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp): ⭐ 5.9k · pushed 2026-09-09 · not archived |
| Catalogue | 10,000+ React/Tailwind components, themes and templates |
| Key | Free key at [21st.dev/mcp](https://21st.dev/mcp) → env var `API_KEY_21ST` |
| Pricing ([21st.dev/pricing](https://21st.dev/pricing), 2026-09-22) | **Free:** browsing, unlimited inspirations and logo search, **2 component copies/day**, 5 design-bug reviews, **no AI credits**. **Builder** $6–8/mo. **Builder + AI** $15–80/mo for 500–2,000 AI credits/mo; +100 credits for $5 |

---

## Install (two official routes that don't match; pick one)

### Route 1: README (Claude Code plugin marketplace)

```bash
claude plugin marketplace add 21st-dev/magic-mcp
# then inside Claude Code:
/plugin install 21st
```

### Route 2: 21st.dev/mcp page (CLI)

```bash
npx @21st-dev/cli@latest init --client claude
```

Set the key with `export API_KEY_21ST=...`. On Windows PowerShell: `$env:API_KEY_21ST="..."`.

---

## Tools

| Tool | What it does | Cost |
| --- | --- | --- |
| `search` | Search the catalogue of components, themes and templates (metadata only) | Free |
| `get_component` | Retrieve a component's code | **Paid retrieval** |
| `get_inspiration` | Design references for a component idea | — |
| `search_logo` | Brand logo SVGs | Free, "no retrieval limit" |
| `generate` | AI UI generation (multiple variants) | **Paid on the free tier** |

Sources: [21st.dev/mcp](https://21st.dev/mcp) (the page says the list is "a representative slice") · [magic-mcp README](https://github.com/21st-dev/magic-mcp)

- `generate` **only appears when AI access is enabled** on your account. Builder-component access "does not enable hosted 21st AI".
- Legacy names such as `21st_magic_component_builder` are still accepted and map to the new tools, so old `/ui …` prompts still work.
- The web `generate` flow returns a **URL** rather than inline code in some clients ([21st.dev/magic](https://21st.dev/magic)).
- Modes: `code` (default, React/shadcn) and `sketch` (lightweight HTML/Tailwind).

---

## Hackathon workflow

```text
1. search            "pricing table with toggle", "animated hero", "command palette"   (free)
2. get_inspiration   3 references for the one "bold moment" component
3. get_component     retrieve ONE winner (paid) — or generate if AI access is on
4. adapt             replace colours/spacing with our @theme tokens; swap primitives to shadcn
5. audit             /impeccable audit → remove gradients/glows/bounce easing
6. search_logo       sponsor & integration logos for the "how it works" slide   (free)
```

> [!TIP]
> Use 21st for **one or two distinctive components**, not the whole UI. Base components come from shadcn (free, accessible). A page built entirely from marketplace components looks like a template, and judges penalise barely changed templates.

---

## Prompts

```text
Using the 21st MCP, search for "<component>" and show the top 5 results with their names and what makes each distinct. Don't retrieve code yet.
```

```text
Retrieve "<chosen component>" via 21st. Adapt it: use our semantic tokens (no raw hex/px), shadcn primitives where equivalent, semantic HTML, focus-visible ring ≥3:1, targets ≥24px, and remove bounce easing and decorative gradients.
```

```text
Use search_logo to fetch SVG logos for: <Supabase, Clerk, Vercel, Anthropic, sponsor>. Save to public/logos/ with consistent sizing.
```

---

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Auth error with an old key | Keys were reset, so generate a new one at 21st.dev/mcp |
| No `generate` tool | Enable AI access on your 21st account |
| Out of quota | Switch to `search` + shadcn, or build it yourself with Frontend PROMPTS F3 |
| Install command doesn't work | Try the other route (plugin vs CLI) |
