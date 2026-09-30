# Deepen-2: MCP server catalog for hackathons (accessed 2026-09-22)

Method: 11 web calls this session (3 page fetches, 8 searches). **Confidence key:** H = official page fetched directly. M = official page came up in search results but only its snippet or summary was read. L = third-party snippet only, or sources conflict. The search tool summarises results, so anything rated M or L should be re-checked on the linked page before it goes into the guide.

## Catalog

| Category | Server | Install (Claude Code) / endpoint | Auth | Cost | Source | Conf |
|---|---|---|---|---|---|---|
| Browser/debug | Chrome DevTools MCP | `claude mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest` (the README gives the `npx -y chrome-devtools-mcp@latest` part; the `claude mcp add` wrapper is the standard form) | none. Needs Node LTS and Chrome stable | 🆓 | https://github.com/ChromeDevTools/chrome-devtools-mcp | H |
| Browser/debug | Browserbase MCP (Stagehand) | npm `@browserbasehq/mcp-server-browserbase` via npx. Snippets disagree on the package name (`@browserbasehq/mcp` vs `mcp-browserbase`) | BROWSERBASE_API_KEY + PROJECT_ID, plus an LLM key (snippet shows GEMINI_API_KEY) | 🆓* (Browserbase account; tier not verified) | https://github.com/browserbase/mcp-server-browserbase ; https://docs.stagehand.dev/v3/integrations/mcp/setup | L |
| Browser/debug | Browser MCP (browsermcp, not browser-use) | `claude mcp add --scope user browsermcp npx @browsermcp/mcp@latest` | browser extension | 🆓 (unverified) | search snippet (joeyyu23 handbook / pdenya blog) | L |
| Docs | Ref | `claude mcp add --transport http Ref https://api.ref.tools/mcp --header "x-ref-api-key: <KEY>"` | API key (ref.tools/keys) | 🆓* (pricing not verified) | https://docs.ref.tools/context/install/claude-code | M |
| Docs | DeepWiki (Cognition/Devin) | `claude mcp add -s user -t http deepwiki https://mcp.deepwiki.com/mcp` (SSE also at /sse) | none (public repos only) | 🆓 | https://docs.devin.ai/work-with-devin/deepwiki-mcp ; https://cognition.com/blog/deepwiki-mcp-server | M |
| Search | Exa | `claude mcp add exa -e EXA_API_KEY=KEY -- npx -y exa-mcp-server`, or remote `https://mcp.exa.ai/mcp` | key optional on remote: works keyless on the free tier, rate limited | 🆓* | firecrawl.dev/blog/best-web-search-mcp (third party) | L |
| Search | Tavily | `claude mcp add --transport http tavily https://mcp.tavily.com/mcp` | OAuth, or API key in the URL | 🆓* (about 1,000 queries/mo) | same third-party blog | L |
| Search | Brave Search | official Brave server (the reference server is archived, see Finding 1) | API key | 🆓* ($5 free credit/mo, then $5 per 1k requests, per third party) | firecrawl.dev blog | L |
| Search/scrape | Firecrawl | `claude mcp add firecrawl -e FIRECRAWL_API_KEY=KEY -- npx -y firecrawl-mcp` | API key | 🆓* (free prototyping tier) | https://github.com/firecrawl/firecrawl-mcp-server | M |
| Search | Perplexity | `claude mcp add --transport http perplexity https://api.perplexity.ai/mcp --header "Authorization: Bearer KEY"` (local npm `@perplexity-ai/mcp-server` also exists) | API key | 💰 (paid API, usage-based; free credit not verified) | https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server ; https://github.com/perplexityai/modelcontextprotocol | M |
| DB | Neon | `claude mcp add --transport http neon https://mcp.neon.tech/mcp` | OAuth | 🆓* (Neon free plan) | https://neon.com/guides/claude-code-mcp-neon | M |
| DB | Postgres (generic) | `claude mcp add --transport stdio db -- npx -y @bytebase/dbhub --dsn "postgresql://..."` | DSN | 🆓 | https://code.claude.com/docs/en/mcp | H |
| DB | MongoDB (official) | `claude mcp add mongodb -e MDB_MCP_CONNECTION_STRING=... -- npx -y mongodb-mcp-server@latest --readOnly` (or run `npx -y mongodb-mcp-server@latest setup`) | connection string / Atlas API creds | 🆓 (OSS; Atlas M0 is free) | https://github.com/mongodb-js/mongodb-mcp-server ; https://www.mongodb.com/docs/mcp-server/get-started/ | M |
| DB | Redis (official) | repo redis/mcp-redis; Docker image `mcp/redis` | Redis URL | 🆓 | https://github.com/redis/mcp-redis | M |
| DB | Prisma | remote `https://mcp.prisma.io/mcp` (manages Prisma Postgres) plus a local server (migrations, schema) | Prisma Console login | 🆓* | https://www.prisma.io/docs/postgres/integrations/mcp-server | M |
| Deploy | Netlify | `claude mcp add netlify -- npx -y @netlify/mcp` | Netlify login/PAT | 🆓* | https://docs.netlify.com/build/build-with-ai/netlify-mcp-server/ ; https://github.com/netlify/netlify-mcp | M |
| Deploy | Cloudflare | catalog of managed remote servers (OAuth). Claude Code plugin: `/plugin marketplace add cloudflare/skills` then `/plugin install cloudflare@cloudflare` | OAuth | 🆓* | https://developers.cloudflare.com/agent-setup/claude-code/ ; https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/ | M |
| Deploy | Railway | remote MCP, OAuth (endpoint not captured) | OAuth | 🆓* / 💳 (unverified) | top-mcps.com snippet | L |
| Deploy | Render | hosted OAuth MCP: services, logs, metrics, read-only Postgres (endpoint not captured) | OAuth | 🆓* (unverified) | top-mcps.com snippet | L |
| Infra | AWS (awslabs) | suite of Python servers (uvx, `awslabs.*` on PyPI), e.g. aws-documentation, aws-api, ccapi | AWS creds (the docs server likely needs none; unverified) | 🆓 OSS; AWS usage 💰 | https://awslabs.github.io/mcp/ ; https://github.com/awslabs/mcp | M |
| Productivity | Notion | `claude mcp add --transport http notion https://mcp.notion.com/mcp` | OAuth | 🆓* | https://code.claude.com/docs/en/mcp | H |
| Productivity | Sentry | `claude mcp add --transport http sentry https://mcp.sentry.dev/mcp` | OAuth | 🆓* | https://code.claude.com/docs/en/mcp | H |
| Productivity | Linear | `claude mcp add --transport sse linear https://mcp.linear.app/sse` | OAuth | 🆓* | search summary (mysecond.ai) | L |
| Productivity | Atlassian (Rovo MCP) | `claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse` (community alternative: sooperset/mcp-atlassian) | OAuth | 🆓* | https://www.atlassian.com/platform/rovo-mcp (snippet) | L |
| Productivity | Asana | `claude mcp add --transport sse asana https://mcp.asana.com/sse` | OAuth | 🆓* | https://code.claude.com/docs/en/mcp | H |
| Productivity | Slack | official Anthropic connector (claude.com/connectors). Claude Code endpoint not found | OAuth | 🆓* | https://claude.com/connectors (snippet) | L |
| Utility | Reference set: everything, fetch, filesystem, git, memory, sequential-thinking, time | e.g. `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem <dir>`; fetch, git, time are Python (`uvx mcp-server-fetch` etc.; package names not verified this run) | none | 🆓 | https://github.com/modelcontextprotocol/servers | H (list) / L (commands) |
| Design | Figma MCP (Dev Mode) | remote or desktop server | Figma login; Dev or Full seat on a paid plan | 🆓* very limited on Starter/View/Collab; 💰 for real use | https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/ (snippet) | M |
| Design | Canva | `claude mcp add --transport http canva https://mcp.canva.com/mcp` | OAuth | 🆓* | search summary | L |

## Findings

1. **Archived reference servers.** The modelcontextprotocol/servers repo has moved AWS KB Retrieval, Brave Search, EverArt, GitHub, GitLab, Google Drive, Google Maps, PostgreSQL, Puppeteer, Redis, Sentry, Slack and SQLite to `servers-archived`. For these, use the vendor's own server instead: github/github-mcp-server, mcp.sentry.dev, redis/mcp-redis, and DBHub or Neon for Postgres. Source: github.com/modelcontextprotocol/servers, MCP steering group, date not given, accessed 2026-09-22. Conf H.
2. **Maintained reference servers.** Only seven remain: Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking and Time. Same source. Conf H.
3. **Chrome DevTools MCP.** Apache-2.0, needs no auth. Three things to know:
   - It exposes the full browser contents to the MCP client.
   - Usage statistics are on by default. Opt out with `--no-usage-statistics` or `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS`.
   - Performance tools may send trace URLs to Google's CrUX API. Turn this off with `--no-performance-crux`.

   Source: github.com/ChromeDevTools/chrome-devtools-mcp, Google, accessed 2026-09-22. Conf H.
4. **Claude Code docs remote-server examples.** The official MCP page gives commands for Notion, Asana (SSE), GitHub (`https://api.githubcopilot.com/mcp/` with a PAT), Sentry, Stripe (`https://mcp.stripe.com`), HubSpot, Airtable and DBHub. Source: code.claude.com/docs/en/mcp, Anthropic, accessed 2026-09-22. Conf H.
5. **Figma seat requirement.** The Figma MCP server needs a Dev or Full seat on a paid plan. Limits:
   - Pro/Org Full or Dev seat: 200 tool calls per day.
   - Enterprise: 600 per day.
   - Education plans: same as Pro.
   - Starter, or View/Collab seats: roughly 6 tool calls per month. One snippet said 20 per month instead, so this figure is **conflicting**.

   Forum threads report limits not updating after a seat upgrade. Treat Figma as effectively paid for a hackathon. Source: developers.figma.com rate-limits page (search snippet) and forum.figma.com, accessed 2026-09-22. Conf M.
6. **DeepWiki.** Free, remote, no auth, public repos only. Tools: ask_question, read_wiki_structure, read_wiki_contents. Source: docs.devin.ai and cognition.com (snippet). Conf M.
7. **Exa and Tavily free access.** Exa's remote MCP reportedly works keyless on its free tier, which makes it the lowest-friction search option. Tavily's free tier is about 1,000 queries per month. Source: firecrawl.dev blog, which is a competitor's publication. Conf L.
8. **Prisma.** Prisma runs two servers: the remote `mcp.prisma.io/mcp` handles Postgres provisioning, and a local one handles migrations and schema. Source: prisma.io docs (snippet). Conf M.
9. **Cloudflare.** Cloudflare now points Claude Code users to a plugin (`cloudflare/skills`) rather than individual `claude mcp add` commands. Source: developers.cloudflare.com/agent-setup/claude-code (snippet). Conf M.

## Repo slugs

ChromeDevTools/chrome-devtools-mcp · browserbase/mcp-server-browserbase · ref-tools/ref-tools-mcp · firecrawl/firecrawl-mcp-server · perplexityai/modelcontextprotocol · neondatabase/mcp-server-neon · mongodb-js/mongodb-mcp-server · redis/mcp-redis · prisma/mcp · netlify/netlify-mcp · awslabs/mcp · sooperset/mcp-atlassian (community) · modelcontextprotocol/servers · modelcontextprotocol/servers-archived · figma/mcp-server-guide · github/github-mcp-server · bytebase/dbhub (npm @bytebase/dbhub) · regenrek/deepwiki-mcp (community; the official DeepWiki server is remote)

## Not found

- browser-use (browser-use/browser-use) MCP install command. The searches returned Browser MCP (browsermcp) instead.
- Railway and Render endpoint URLs and free-tier terms.
- Brave's new official MCP repo slug.
- Exa's official repo slug (exa-labs/exa-mcp-server is my assumption, not verified).
- A Slack MCP endpoint for Claude Code.
- Ref pricing.
- Canva MCP official docs page. The URL above comes from a search summary only.
- Exact uvx/npm package names for the fetch, git and time reference servers.
