# 🗂️ MCP Server Catalog (cost-tagged)

<!-- markdownlint-disable MD013 -->

> MCP servers worth knowing for a hackathon, each with its install command, auth and **cost tag**. From the MCP & tools research run (2026-09-22); sources are in [`evidence.md`](evidence.md). Setup basics and the core five are in [`mcp-setup.md`](mcp-setup.md); security rules are in [`mcp-security.md`](mcp-security.md).

**Cost tags:** 🆓 free / open source, no account · 🆓* free tier (account or limits) · 💳 trial credits only · 💰 paid.
**Confidence:** H = official page fetched · M = official source via search snippet · L = third-party snippet only. Re-check M and L rows before relying on them.

> [!WARNING]
> **The official reference repo archived most of its servers.** `modelcontextprotocol/servers` now keeps only **7**: Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking and Time. The **Postgres, SQLite, GitHub, Brave Search, Redis, Sentry, Slack, Puppeteer, Google Drive/Maps, GitLab and AWS KB** servers moved to `servers-archived`. Use the vendor's own server instead (rows below). Old tutorials that say `npx @modelcontextprotocol/server-postgres` are out of date. (H)

---

## Start here: the easiest path is plugins

The official Claude Code marketplace **`claude-plugins-official`** bundles pre-configured MCP servers for **github, gitlab, atlassian, asana, linear, notion, figma, vercel, firebase, supabase, slack, sentry**. One command per integration, no JSON editing (H):

```bash
/plugin install supabase@claude-plugins-official
/plugin install vercel@claude-plugins-official
```

Use `claude mcp add` (below) for anything the marketplace doesn't cover.

---

## Browser & debugging

| Server | Install (Claude Code) | Auth | Cost | Conf |
| --- | --- | --- | --- | --- |
| **Chrome DevTools MCP** | `claude mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest` | None (Node LTS + Chrome) | 🆓 | H |
| Playwright MCP | `claude mcp add playwright -- npx @playwright/mcp@latest` | None | 🆓 | H |
| ~~Browserbase (Stagehand)~~ | ❌ **Repo `browserbase/mcp-server-browserbase` is archived** (GitHub API, 2026-09-22) | Browserbase key + LLM key | — | H |
| Browser MCP (extension) | `claude mcp add --scope user browsermcp npx @browsermcp/mcp@latest` | Browser extension | 🆓 (unverified) | L |

Chrome DevTools MCP exposes the **whole browser** to the model. It sends **usage statistics by default** (opt out with `--no-usage-statistics`), and its performance tools may send trace URLs to Google's CrUX API (`--no-performance-crux`).

## Docs, search & scraping

| Server | Install / endpoint | Auth | Cost | Conf |
| --- | --- | --- | --- | --- |
| **DeepWiki** (Cognition) | `claude mcp add -s user -t http deepwiki https://mcp.deepwiki.com/mcp` | **None** (public repos) | 🆓 | M |
| Context7 | See [`mcp-setup.md`](mcp-setup.md) | Optional free key | 🆓* | H |
| Exa | `claude mcp add exa -e EXA_API_KEY=KEY -- npx -y exa-mcp-server`, or remote `https://mcp.exa.ai/mcp` | Key optional (keyless free tier, rate-limited) | 🆓* | L |
| Tavily | `claude mcp add --transport http tavily https://mcp.tavily.com/mcp` | OAuth / key | 🆓* (~1K queries/mo) | L |
| Firecrawl | `claude mcp add firecrawl -e FIRECRAWL_API_KEY=KEY -- npx -y firecrawl-mcp` | Key | 🆓* | M |
| Ref | `claude mcp add --transport http Ref https://api.ref.tools/mcp --header "x-ref-api-key: KEY"` | Key | 🆓* (pricing not verified) | M |
| Brave Search | Brave's own server (the reference one is archived) | Key | 🆓* ($5 credit/mo, third party) | L |
| Perplexity | `claude mcp add --transport http perplexity https://api.perplexity.ai/mcp --header "Authorization: Bearer KEY"` | Key | 💰 | M |

## Databases

| Server | Install / endpoint | Auth | Cost | Conf |
| --- | --- | --- | --- | --- |
| Supabase | See [`mcp-setup.md`](mcp-setup.md) (use `read_only=true`) | OAuth | 🆓* | H |
| **Postgres (any)** via DBHub | `claude mcp add --transport stdio db -- npx -y @bytebase/dbhub --dsn "postgresql://..."` | DSN | 🆓 | H |
| Neon | `claude mcp add --transport http neon https://mcp.neon.tech/mcp` | OAuth | 🆓* | M |
| MongoDB (official) | `claude mcp add mongodb -e MDB_MCP_CONNECTION_STRING=... -- npx -y mongodb-mcp-server@latest --readOnly` | Connection string | 🆓 (Atlas M0 free) | M |
| Redis (official) | `redis/mcp-redis` (Docker image `mcp/redis`) | Redis URL | 🆓 | M |
| Prisma | Remote `https://mcp.prisma.io/mcp` + a local server for migrations | Prisma login | 🆓* | M |

## Deploy & infrastructure

| Server | Install / endpoint | Auth | Cost | Conf |
| --- | --- | --- | --- | --- |
| Vercel | See [`mcp-setup.md`](mcp-setup.md) | OAuth | 🆓* | H |
| Netlify | `claude mcp add netlify -- npx -y @netlify/mcp` | Login / PAT | 🆓* | M |
| Cloudflare | Plugin: `/plugin marketplace add cloudflare/skills` → `/plugin install cloudflare@cloudflare` | OAuth | 🆓* | M |
| AWS (awslabs) | Python servers via `uvx awslabs.*` (for example aws-documentation) | AWS creds | 🆓 OSS · 💰 AWS usage | M |
| Railway / Render | Hosted OAuth MCPs (endpoints not captured) | OAuth | 🆓* (unverified) | L |

## Productivity & monitoring

| Server | Install / endpoint | Auth | Cost | Conf |
| --- | --- | --- | --- | --- |
| Notion | `claude mcp add --transport http notion https://mcp.notion.com/mcp` | OAuth | 🆓* | H |
| Sentry | `claude mcp add --transport http sentry https://mcp.sentry.dev/mcp` | OAuth | 🆓* | H |
| Asana | `claude mcp add --transport sse asana https://mcp.asana.com/sse` (SSE: deprecated transport) | OAuth | 🆓* | H |
| Linear | `claude mcp add --transport sse linear https://mcp.linear.app/sse`, or use the plugin | OAuth | 🆓* | L |
| Atlassian (Rovo) | `claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse`, or use the plugin | OAuth | 🆓* | L |
| Slack | Use the official plugin (no Claude Code endpoint found) | OAuth | 🆓* | L |

## Design & media

| Server | Install / endpoint | Auth | Cost | Conf |
| --- | --- | --- | --- | --- |
| shadcn | `pnpm dlx shadcn@latest mcp init --client claude` | None | 🆓 | H |
| 21st | See [`21st-dev-mcp.md`](21st-dev-mcp.md) | Key | 🆓* (2 copies/day free) | H |
| Stitch | See [`stitch-mcp.md`](stitch-mcp.md) (header bug still open) | Key | 🆓* (unverified) | M |
| **Figma** | Remote or desktop server | **Paid Dev/Full seat** | 💰 (Starter ≈ 6–20 calls/**month**, sources conflict) | M |
| Canva | `claude mcp add --transport http canva https://mcp.canva.com/mcp` | OAuth | 🆓* | L |

## Utility (maintained reference servers)

| Server | Install | Cost |
| --- | --- | --- |
| Filesystem | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem <dir>` | 🆓 |
| Memory, Sequential Thinking, Everything | npm `@modelcontextprotocol/server-*` | 🆓 |
| Fetch, Git, Time | Python via `uvx` (package names not verified this run) | 🆓 |

---

## A $0 hackathon MCP set

Every server here is 🆓 or has a free tier with no card:

```bash
claude mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest --no-usage-statistics
claude mcp add playwright -- npx @playwright/mcp@latest
claude mcp add -s user -t http deepwiki https://mcp.deepwiki.com/mcp
claude mcp add --transport http context7 https://mcp.context7.com/mcp   # add your free key header for higher limits
pnpm dlx shadcn@latest mcp init --client claude
/plugin install supabase@claude-plugins-official                        # then set read_only + project_ref
```

> [!TIP]
> For production use, **pin versions** (`chrome-devtools-mcp@X.Y.Z`) instead of `@latest`. See [`mcp-security.md`](mcp-security.md).
