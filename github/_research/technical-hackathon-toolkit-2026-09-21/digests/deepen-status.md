# Deepen: open status questions (accessed 2026-09-22)

Scope note: 14 tool calls, one round. Two fetches failed with ECONNREFUSED: supabase.com/changelog/45329 and github.com/anthropics/claude-code/issues/78534. Where a claim rests only on a search-engine summary, the class column says `search-snippet`, and it should be checked against the page itself before anything is published.

## Findings

1. Stitch MCP is a remote HTTP server at `https://stitch.googleapis.com/mcp`, and it authenticates with an API key in the `X-Goog-Api-Key` header. The documented Claude Code command is `claude mcp add stitch --transport http https://stitch.googleapis.com/mcp --header "X-Goog-Api-Key: YOUR-API-KEY" -s user`. | https://sotaaz.com/post/stitch-mcp-api-en ; https://felixschmidt.software/en/blog/google-stitch-mcp-claude-code | SOTAAZ Blog; Felix Schmidt (third-party) | 2026 | accessed 2026-09-22 | medium | search-snippet (secondary; the official stitch.withgoogle.com docs were not retrieved)
2. The community package `stitch-mcp` by David East offers a stdio proxy. It includes an init wizard (gcloud auth, project selection, IAM, MCP config) and refreshes tokens automatically. Direct HTTP with OAuth needs manual token handling. | https://sotaaz.com/post/stitch-mcp-guide-en ; https://mcpservers.org/servers/kargatharaakash/stitch-mcp | SOTAAZ; mcpservers.org | 2026 | accessed 2026-09-22 | medium-low | search-snippet
3. anthropics/claude-code #41664 ("Stitch MCP ... fails with 'Incompatible auth server: does not support dynamic client registration'") was opened 2026-03-31. It is Closed as not planned, with labels `duplicate`, `bug`, `area:auth`, `area:mcp`. The root cause given is that Claude Code ignores the configured `headers` and tries OAuth discovery. The fetched page did not show which issue it duplicates, and it listed no workaround. | https://github.com/anthropics/claude-code/issues/41664 | GitHub / Anthropic | 2026-03-31 | accessed 2026-09-22 | high | primary
4. Related issues exist: #7290 (HTTP/SSE transport ignores auth headers, v1.0.108), #52638 (HTTP MCP OAuth fails when the server lacks DCR) and #78534. The #78534 title reads "headersHelper on http transport still falls into 'Incompatible auth server...' on 2.1.211 (regression from #53267 persists)". Its snippet says that from v2.1.118, a 401 triggers OAuth discovery instead of re-running headersHelper, with no fallback. The bug therefore appears unfixed as of v2.1.211. | https://github.com/anthropics/claude-code/issues/78534 ; https://github.com/anthropics/claude-code/issues/7290 ; https://github.com/anthropics/claude-code/issues/52638 | GitHub / Anthropic | 2026 | accessed 2026-09-22 | medium | search-snippet (the #78534 fetch failed)
5. Supabase changelog "Breaking Change: Tables not exposed to Data and GraphQL API automatically" (discussion #45329): new public-schema tables need an explicit Postgres GRANT before the Data API can reach them. This is the default for new projects from **May 30, 2026** and is enforced on all existing projects from **October 30, 2026**. The temporary `auto_expose_new_tables = true` config.toml flag is deprecated and will be removed on 2026-10-30. | https://supabase.com/changelog/45329-breaking-change-tables-not-exposed-to-data-and-graphql-api-automatically ; https://github.com/orgs/supabase/discussions/45329 ; https://www.supascale.app/blog/supabase-october-2026-breaking-change-data-api-grants-explai | Supabase; Supascale | 2026 | accessed 2026-09-22 | medium-high | search-snippet (the changelog fetch failed; several sources agree)
6. The GSAP pricing page says: "GSAP is now 100% free for all users, thanks to Webflow's support." This covers all plugins, including SplitText, MorphSVG, DrawSVG, ScrollTrigger and Draggable. The page names no restrictions; the separate license terms were not checked. | https://gsap.com/pricing/ | GSAP / Webflow | undated | accessed 2026-09-22 | high | primary
7. The Chainlit README says the project moved to community maintenance on May 1, 2025, and that "the original Chainlit team has stepped back from active development". Community maintainers handle review, releases and security under a formal agreement, and "Chainlit SAS provides no warranties on future updates." The license is Apache 2.0. | https://github.com/Chainlit/chainlit | Chainlit | read 2026-09 | accessed 2026-09-22 | high | primary
8. Chainlit "ChainLeak" CVEs (found by Zafran Labs): CVE-2026-22218 is an arbitrary file read (CVSS 7.1) and CVE-2026-22219 is an SSRF in the SQLAlchemy data layer (CVSS 8.3). Both are fixed in Chainlit 2.9.4, released 2025-12-24. | https://github.com/advisories/GHSA-gm79-2pvc-wc75 ; https://thehackernews.com/2026/01/chainlit-ai-framework-flaws-enable-data.html ; https://www.zafran.io/resources/chainleak-critical-ai-framework-vulnerabilities-expose-data-enable-cloud-takeover | GitHub Advisory; The Hacker News; Zafran | 2026-01 | accessed 2026-09-22 | high | search-snippet (several agreeing sources)
9. oRPC: docs and README files live at github.com/unnoq/orpc. Search also shows github.com/middleapi/orpc and github.com/dinwwwh/orpc titled "Typesafe APIs Made Simple", which suggests the repo was renamed or transferred. The docs domains are orpc.unnoq.com and orpc.dev. v1.0 is stable (InfoQ, 2025-12). | https://github.com/unnoq/orpc ; https://github.com/middleapi/orpc ; https://orpc.dev/ ; https://infoq.com/news/2025/12/orpc-v1-typesafe/ | GitHub; InfoQ | 2025-12 | accessed 2026-09-22 | medium | search-snippet
10. DeepSeek Harness (`dsh`) is DeepSeek AI's open-source agent harness. Its tagline is "Everything is a Plugin" (built on Cordis), and it has subagent providers that delegate to Claude Code and Codex. It reportedly passed about 95k stars within about 2 days. | https://github.com/deepseek-ai/deepseek-harness ; https://thenewstack.io/deepseek-harness-open-source-plugins/ ; https://deepseek.com/harness/en/ | DeepSeek; The New Stack | 2026 | accessed 2026-09-22 | medium-high | search-snippet
11. Pi is Mario Zechner's (badlogic) agent toolkit: a unified LLM API, an agent loop, a TUI and a self-extensible coding-agent CLI (`@earendil-works/pi-coding-agent`). github.com/badlogic/pi-mono now shows the title "earendil-works/pi", so it has apparently moved to that org. | https://github.com/badlogic/pi-mono | GitHub | 2026 | accessed 2026-09-22 | medium | search-snippet
12. WCAG 3.0 is still a W3C Working Draft; the latest was reportedly published 2026-09-10. A Candidate Recommendation is projected around Q4 2027, and a Recommendation no earlier than 2028 (some estimates say late 2029). | https://www.webability.io/blog/wcag-3-0-explained ; https://abilitynet.org.uk/resources/digital-accessibility/what-expect-wcag-30-web-content-accessibility-guidelines | WebAbility; AbilityNet (secondary) | 2026 | accessed 2026-09-22 | medium-low | search-snippet (w3.org was not retrieved)
13. Alex Russell, "The Performance Inequality Gap, 2026" (Nov 2025). The baseline devices for the 75th-percentile user are the Samsung Galaxy A24 4G and HP 14. He models a 3-second budget for JS-light pages (15% JS) and JS-heavy pages (50% JS). The snippet gives a 3-second budget of about **1.5 MiB (JS-light) / 935 KiB (JS-heavy)** of critical-path bytes with four connections. The labels on those two figures are inferred and need checking. | https://infrequently.org/2025/11/performance-inequality-gap-2026/ | Infrequently Noted (Alex Russell) | 2025-11 | accessed 2026-09-22 | medium | search-snippet

## Answers

1. **Stitch MCP.** Use the endpoint `https://stitch.googleapis.com/mcp` with the header `X-Goog-Api-Key`; the setup is `claude mcp add ... --transport http --header` (F1). The official Google page was not retrieved. #41664 is closed as a duplicate / not planned, with no fix (F3). Related bugs were still open as of v2.1.211 (F4). The practical workaround is the `stitch-mcp` stdio proxy (F2); treat that as unverified until tested.
2. **Supabase.** New projects from 2026-05-30; all existing projects enforced from 2026-10-30 (F5).
3. **GSAP.** Yes, 100% free including all plugins, per gsap.com/pricing (F6). The license text was not checked.
4. **Chainlit.** Community-maintained since 2025-05-01, with the founders stepped back and no warranty from Chainlit SAS (F7). ChainLeak CVEs fixed in 2.9.4, so require 2.9.4 or later (F8).
5. **oRPC.** unnoq/orpc, with probable moves to middleapi/orpc or dinwwwh/orpc (F9). The canonical slug is unresolved.
6. **DeepSeek Harness** is deepseek-ai/deepseek-harness (F10). **Pi** is badlogic/pi-mono, now apparently earendil-works/pi (F11).
7. **WCAG 3.0.** Working Draft (2026-09-10); CR about Q4 2027; Recommendation 2028 or later (F12, secondary sources only).
8. **JS budget.** Russell 2026: about 1.5 MiB (JS-light) / about 935 KiB (JS-heavy) of critical-path bytes for 3 seconds on a Galaxy A24-class device (F13, figures need checking).
9. **Devpost judging criteria.** Unresolved; not searched because of the budget.

## Repo slugs found

- anthropics/claude-code (issues #41664, #7290, #52638, #78534, #53267, #38102, #26675, #3273)
- Chainlit/chainlit
- unnoq/orpc (also middleapi/orpc, dinwwwh/orpc)
- deepseek-ai/deepseek-harness
- Dominic789654/awesome-deepseek-harness
- badlogic/pi-mono (redirects to / titled earendil-works/pi)
- kargatharaakash/stitch-mcp (community Stitch MCP)
- gabelul/stitch-kit (per its LobeHub listing; slug not checked)
- supabase discussion #45329 (github.com/orgs/supabase)

## Not found

- The official Stitch setup page (stitch.withgoogle.com/docs/mcp/setup) and any Google blog or codelab.
- Which issue #41664 is a duplicate of. #7290 or #52638 are candidates, but this is not confirmed.
- The body of #78534 and the status of #53267 (fetch failed).
- A first-party read of the Supabase changelog (fetch failed).
- A w3.org/WAI primary source for the WCAG 3.0 timeline.
- The GSAP license terms page.
- The Devpost official judging criteria page.
- web.dev's current JS budget guidance.
