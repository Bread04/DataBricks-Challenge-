# 🔌 MCP Setup for Hackathons (Claude Code)

<!-- markdownlint-disable MD013 -->

> How MCP works in Claude Code, the recommended server set, exact install commands, and security rules. Verified 2026-09-21.

---

## 1 · Claude Code MCP essentials

From the [Claude Code MCP docs](https://code.claude.com/docs/en/mcp):

| Topic | Detail |
| --- | --- |
| Remote server | `claude mcp add --transport http <name> <url> [--header "K: V"]` |
| Local server | `claude mcp add [options] <name> -- <command> [args]` (the `--` is required) |
| Transports | `http` (recommended), `stdio` (local); SSE is **deprecated**; WebSocket only via `claude mcp add-json` |
| Scopes | `local` (default: this project, private, `~/.claude.json`) · `project` (`.mcp.json`, **committed to git**) · `user` (all projects, private) |
| Env expansion | `.mcp.json` supports `${VAR}` and `${VAR:-default}` in command, args, env, url and headers |
| OAuth | `/mcp` inside a session, or `claude mcp login <name>` (`--no-browser` for headless) |
| Manage | `claude mcp list` · `get` · `remove` · `add-from-claude-desktop` |
| Output limits | Warning at 10k tokens; **hard cap of 25k** (`MAX_MCP_OUTPUT_TOKENS`); overflow is saved to a file |

> [!CAUTION]
> Official warning: *"Verify you trust each server before connecting it. Servers that fetch external content can expose you to prompt injection risk."* Never put credentials in a project-scoped `.mcp.json`.

---

## 2 · Recommended hackathon set

**Cost tags:** 🆓 free / open source · 🆓* free tier (account or limits) · 💳 trial credits only · 💰 paid. Details and a full $0 stack: [`free-ai-dev-tools.md`](free-ai-dev-tools.md) · Full catalog: [`mcp-catalog.md`](mcp-catalog.md) · Security: [`mcp-security.md`](mcp-security.md)

> [!WARNING]
> Most `modelcontextprotocol/servers` reference servers (Postgres, SQLite, GitHub, Brave, Redis, Sentry, Slack, Puppeteer) are **archived**. Use vendor servers, see [`mcp-catalog.md`](mcp-catalog.md).

| Tier | Server | Why | Repo status |
| --- | --- | --- | --- |
| **Core** | **Context7** 🆓* | Up-to-date library docs, so fewer hallucinated APIs ("use context7") | [upstash/context7](https://github.com/upstash/context7) ⭐ 62k · 2026-09-21 |
| **Core** | **Supabase** 🆓* | Schema, SQL, migrations, logs, docs | [supabase/mcp](https://github.com/supabase/mcp) ⭐ 2.9k · 2026-09-19 |
| **Core** | **Playwright** 🆓 | Browser self-verification, screenshots, E2E | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) ⭐ 37k · 2026-09-18 |
| **Core** | **shadcn** 🆓 | Browse, search and install components | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) ⭐ 124k |
| UI | **21st** 🆓* | Distinctive components, logos | see `21st-dev-mcp.md` |
| UI | **Stitch** 🆓* | Design → DESIGN.md → code | see `stitch-mcp.md` |
| Deploy | **Vercel** 🆓* | Deployments, logs, docs | [docs](https://vercel.com/docs/agent-resources/vercel-mcp) (official beta) |
| Optional | **GitHub** 🆓* | Issues and PRs for team coordination | [github/github-mcp-server](https://github.com/github/github-mcp-server) ⭐ 33k · 2026-09-16 |
| Optional | **Stripe** 🆓* (sandbox) | Only if payments are in the demo | [docs](https://docs.stripe.com/mcp) |
| Optional | **Figma** 💰 (paid seat) | If the team designs in Figma | [docs](https://developers.figma.com/docs/figma-mcp-server/) |

**Keep the set small.** Every server adds tool schemas to context, and output is capped at 25k tokens.

---

## 3 · Install commands

```bash
# ── Core ────────────────────────────────────────────────────────────────
# Context7 (endpoint + header from the upstash README; command in Claude Code syntax)
claude mcp add --transport http context7 https://mcp.context7.com/mcp \
  --header "Authorization: Bearer $CONTEXT7_API_KEY"          # free key: context7.com/dashboard

# Supabase: scoped to ONE dev project, read-only, limited features
claude mcp add --scope project --transport http supabase \
  "https://mcp.supabase.com/mcp?project_ref=<ref>&read_only=true&features=database,docs"
# then run /mcp to authenticate

# Playwright
claude mcp add playwright -- npx @playwright/mcp@latest       # flags: --headless --isolated --caps vision,pdf,devtools

# shadcn (writes .mcp.json)
pnpm dlx shadcn@latest mcp init --client claude

# ── Deploy / optional ───────────────────────────────────────────────────
claude mcp add --transport http vercel https://mcp.vercel.com  # then /mcp (OAuth)
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ \
  --header "Authorization: Bearer $GITHUB_PAT"
claude mcp add --transport http stripe https://mcp.stripe.com/ # then /mcp; or: npm i -g @stripe/cli@latest && stripe agent setup
```

Sources: [Claude Code MCP](https://code.claude.com/docs/en/mcp) · [Context7](https://github.com/upstash/context7) · [Supabase MCP](https://supabase.com/docs/guides/getting-started/mcp) · [Playwright MCP](https://github.com/microsoft/playwright-mcp) · [shadcn MCP](https://ui.shadcn.com/docs/mcp) · [Vercel MCP](https://vercel.com/docs/agent-resources/vercel-mcp) · [Stripe MCP](https://docs.stripe.com/mcp)

> The Playwright README shows `claude mcp add playwright npx @playwright/mcp@latest` without `--`. Claude Code's docs require `--` before the command for stdio servers, so the form above follows the docs. Microsoft also says coding agents often do better with **Playwright CLI + skills**, which is more token-efficient than the MCP server.

---

## 4 · Team `.mcp.json` (commit this; no secrets)

```json
{
  "mcpServers": {
    "context7": {
      "type": "http",
      "url": "https://mcp.context7.com/mcp",
      "headers": { "Authorization": "Bearer ${CONTEXT7_API_KEY}" }
    },
    "supabase": {
      "type": "http",
      "url": "https://mcp.supabase.com/mcp?project_ref=${SUPABASE_PROJECT_REF}&read_only=true&features=database,docs"
    },
    "vercel": { "type": "http", "url": "https://mcp.vercel.com" },
    "playwright": { "type": "stdio", "command": "npx", "args": ["@playwright/mcp@latest", "--isolated"] },
    "shadcn": { "type": "stdio", "command": "npx", "args": ["shadcn@latest", "mcp"] }
  }
}
```

Each teammate sets `CONTEXT7_API_KEY` and `SUPABASE_PROJECT_REF` in their shell. Note from the docs: in remote `url`/`headers`, credential variables such as `ANTHROPIC_API_KEY` are **deliberately left empty** rather than expanded.

---

## 5 · Security rules (every vendor agrees)

| Server | Rule | Source |
| --- | --- | --- |
| All | Trust before connecting; external content is a prompt-injection vector; no credentials in `.mcp.json` | [Anthropic](https://code.claude.com/docs/en/mcp) |
| Supabase | `read_only=true` + `project_ref`; **never production**; enable only the feature groups you need; review tool calls manually | [Supabase](https://supabase.com/docs/guides/getting-started/mcp) |
| GitHub | `--read-only`; minimal `GITHUB_TOOLSETS`; least-privilege PAT | [GitHub](https://github.com/github/github-mcp-server) |
| Vercel | Has **your full account's power** (it can deploy and make purchases); check the domain is `mcp.vercel.com`; keep human confirmation on | [Vercel](https://vercel.com/docs/agent-resources/vercel-mcp) |
| Stripe | Sandbox and restricted keys; human confirmation; take care combining it with other servers | [Stripe](https://docs.stripe.com/mcp) |
| Playwright | "**Not** a security boundary"; use `--isolated` | [Microsoft](https://github.com/microsoft/playwright-mcp) |
| Context7 | Community-contributed docs, so accuracy and security aren't guaranteed | [Upstash](https://github.com/upstash/context7) |

---

## 6 · Outdated commands you'll see in older guides

These come from help-me-papi and similar older guides. Use the right-hand column.

| You'll see | Use instead | Why |
| --- | --- | --- |
| `claude mcp add 21st-dev npx -y @21st-dev/mcp` | `claude plugin marketplace add 21st-dev/magic-mcp` → `/plugin install 21st`, or `npx @21st-dev/cli@latest init --client claude` | Magic MCP became the 21st MCP; keys were reset (`21st-dev-mcp.md`) |
| `claude mcp add stitch npx -y @_davideast/stitch-mcp proxy` | `claude mcp add -s user stitch -- npx -y @_davideast/stitch-mcp proxy` (note the `--`), or the official remote endpoint | Claude Code needs `--` before stdio commands (`stitch-mcp.md`) |
| `github.com/supabase/community-mcp` | [supabase/mcp](https://github.com/supabase/mcp) with `read_only=true&project_ref=…` | The official server moved |
| `github.com/vercel/mcp-server` | Remote `https://mcp.vercel.com` (OAuth) | Official Vercel MCP is remote |
| `github.com/21st-dev/21st-mcp` | [21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp) | Current repo |
| Claude Desktop JSON config for Claude Code | `claude mcp add …` or a project `.mcp.json` | Different client |

---

## 7 · Pre-event checklist

- [ ] `claude mcp list` shows every server connected
- [ ] OAuth done for Supabase, Vercel and Stripe (`/mcp`)
- [ ] One test call per server (for example "use context7: Next.js 16 proxy.ts", "list Supabase tables")
- [ ] Stitch tested (see the issue #41664 warning in `stitch-mcp.md`)
- [ ] 21st key regenerated (old keys were reset)
- [ ] Env vars set in the shell profile, not in files

---

## 8 · Discover more servers

| List | Status |
| --- | --- |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | ⭐ 90.5k · pushed 2026-09-03 (reference servers) |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | ⭐ 95.4k · pushed 2026-09-21 (community list) |
