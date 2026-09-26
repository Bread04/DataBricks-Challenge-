# 🛠️ Frontend Tooling: Claude Code · Stitch · 21st.dev · shadcn

<!-- markdownlint-disable MD013 -->

> What each tool is for, and the fastest hackathon workflow that uses them together. Install commands and MCP details are in `../../05-tools-and-mcp/docs/`. Verified 2026-09-21.

---

## Which tool for which job

| Job | Tool | Why |
| --- | --- | --- |
| Explore visual directions fast | **Google Stitch** | Agent-driven infinite canvas, voice input, parallel ideas ([Google, 2026-05](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-updates/)) |
| Get production components | **shadcn/ui** (+ MCP) | Accessible copy-in components; agent can browse and install via MCP ([shadcn](https://ui.shadcn.com/docs/mcp)) |
| Get a *distinctive* component variant | **21st.dev** (21st MCP) | 10k+ React/Tailwind components plus AI variant generation ([21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp)) |
| Write and wire the app | **Claude Code** | Orchestrates the tools above via MCP |
| Generate with taste | **Taste Skill** | Pushes the agent away from default layouts as it generates (see `taste-skill.md`) |
| Quality gate | **/impeccable** | 61 deterministic anti-slop rules, plus a headless `detect` CLI (see `impeccable.md`) |
| Verify in a browser | **Playwright MCP** | Accessibility-tree snapshots, self-verification |

---

## Google Stitch

- **What:** Google Labs AI UI designer, **relaunched at I/O on 19 May 2026**. It has a Stitch Agent on an infinite canvas, voice input, design critiques, and parallel ideas via an agent manager. It accepts existing codebases or design files as input ([Google](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-updates/)).
- **Exports:**
  - Official: Google Antigravity, publish to Netlify, share via AI Studio (Google post).
  - Via plugin: Figma, one screen at a time, keeping layers and Auto Layout ([Figma plugin](https://www.figma.com/community/plugin/1577379704241183556/stitch-to-figma)).
  - HTML/CSS/Tailwind code export is reported by secondary sources only.
- **DESIGN.md:** Google open-sourced Stitch's DESIGN.md format, which carries palette, type and layout rules into a coding agent.
- **Into Claude Code:** Stitch MCP (see `../../05-tools-and-mcp/docs/stitch-mcp.md`). The sync is **one-way** (Stitch → code); re-pull after editing in Stitch.
- **Unknown:** pricing and quotas weren't found.

## 21st.dev

- **What:** a component registry plus **21st AI** (formerly Magic Chat), which generates several React/shadcn variants from text ([21st.dev/magic](https://21st.dev/magic)).
- **Modes:** `code` (default) and a lightweight `sketch` HTML/Tailwind mode.
- **Access:** the web app, the MCP (`generate`, `search`, `get_component`, `get_inspiration`, `search_logo`) and the CLI (`npx @21st-dev/cli@latest`).
- **Cost:** a daily free allowance, then a paywall. `search` and `search_logo` are free; `get_component` and `generate` are paid ([21st.dev/mcp](https://21st.dev/mcp)). Exact prices aren't published.
- **Install via the shadcn CLI:** help-me-papi uses `npx shadcn@latest add "https://21st.dev/r/<author>/<component>"` to pull a 21st component straight into the project. This wasn't confirmed on 21st.dev in this research, so check a component page's install snippet first.
- ⚠️ The marketplace source repo ([serafimcloud/21st](https://github.com/serafimcloud/21st)) hasn't been pushed since May 2025, so use the hosted site and MCP.

## shadcn/ui

- **What:** accessible components you copy into your repo, plus a CLI, registry and MCP server ([shadcn-ui/ui](https://github.com/shadcn-ui/ui), ⭐ 124k · pushed 2026-09-21).
- **Recent changes** ([changelog](https://ui.shadcn.com/docs/changelog)):
  - Sep 2026: `cn` comes from the `cn` package.
  - Aug 2026: private GitHub registries.
  - Jul 2026: server-side registry search, and **Base UI became the default primitives**.
  - MCP server since Aug 2025; Tailwind v4 support since Feb 2025.
- **Commands:** `npx shadcn@latest init` · `npx shadcn@latest add button` · `npx shadcn create`

## Claude Code

- Acts as the orchestrator. Connect the MCP servers above and give it `PRODUCT.md` / `DESIGN.md` as context.
- Load the **frontend-design** skill or **/impeccable**, so generated UI follows the token plan rather than defaults ([anthropics/skills](https://github.com/anthropics/skills), ⭐ 177k).

---

## 🏎️ Hackathon workflow: idea → polished UI in ~2 hours

```text
1. Stitch       Prompt/voice 3 directions for the demo screen → pick one        (20 min)
2. Stitch MCP   Claude pulls design context → writes DESIGN.md                  (10 min)
3. Tokens       Claude converts DESIGN.md → @theme primitives + semantics       (10 min)
4. shadcn MCP   Install the base components (button, input, card, dialog)       (10 min)
5. 21st MCP     Generate 1 distinctive component for the "bold moment"          (15 min)
6. Claude Code  Assemble the page from components + tokens only                 (30 min)
7. /impeccable  audit → polish  (+ Taste Skill if a screen still looks generic)  (15 min)
8. Playwright   Screenshot at mobile + desktop, fix, commit                     (10 min)
```

**No Stitch?** Skip steps 1–2 and run `/impeccable init` → `shape` instead.

---

## Starter scaffolds

| Starter | Command | Status |
| --- | --- | --- |
| Next.js (full-stack default) | `npx create-next-app@latest` (add `--api` for a sample route handler) | [vercel/next.js](https://github.com/vercel/next.js) ⭐ 142k · pushed 2026-09-21 |
| Vite (SPA) | `npm create vite@latest` | [vitejs/vite](https://github.com/vitejs/vite) ⭐ 83k · pushed 2026-09-21 |
| shadcn project | `npx shadcn create` | shadcn changelog |
