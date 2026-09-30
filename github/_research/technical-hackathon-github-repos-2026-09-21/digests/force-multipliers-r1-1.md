# Force-multiplier repos — digest r1-1 (accessed 2026-09-21)

Tool calls used: 20 (18 web, 4 github.com page fetches incl. none to api.github.com). Two fetches failed (pinggy ECONNRESET, morphllm HTTP 429); claims from those come only via search-result snippets and are marked lower confidence.

Legend for notes: **EV** = slug/status evidenced this run; **UNV** = slug proposed from prior knowledge, NOT evidenced this run (lead must verify). Star counts are as reported by the cited source, not verified via API.

## Candidates

| category | owner/repo (exact slug) | one-line hackathon use | evidence URL | notes |
|---|---|---|---|---|
| AI coding agents | anomalyco/opencode | Terminal coding agent, 75+ providers, plan/build agents | https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md | EV. Renamed from sst/opencode (old slug redirects). ~208.9k stars, commit 2026-09-21 |
| AI coding agents | openai/codex | Codex CLI terminal agent | https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md | EV. ~125.6k stars, active 2026-09-21 |
| AI coding agents | anthropics/claude-code | Claude Code CLI (repo = issues/plugins, product itself not fully OSS) | https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md | EV. ~147.2k stars |
| AI coding agents | OpenHands/OpenHands | Sandboxed autonomous agent, headless in CI | https://pinggy.io/blog/best_open_source_cli_coding_agents/ (snippet only) | UNV slug (formerly All-Hands-AI/OpenHands). ~85k per search snippet |
| AI coding agents | cline/cline | Model-agnostic agent (IDE, CLI, SDK) | https://github.com/RooCodeInc/Roo-Code | UNV slug; Roo archive notice recommends Cline. ~67k per snippet |
| AI coding agents | aaif-goose/goose | General MCP agent, desktop+CLI | https://goose-docs.ai/blog/2026/04/07/goose-moves-to-aaif/ | EV. MOVED from block/goose to AAIF (Linux Foundation) Apr 2026. ~54k |
| AI coding agents | Aider-AI/aider | Git-native pair programmer | https://www.morphllm.com/comparisons/cline-alternatives (snippet) | UNV slug. RISK: no commits since 2026-05-22 per snippet |
| AI coding agents | Kilo-Org/kilocode | BYOK VS Code agent (Roo/Cline lineage) | https://www.morphllm.com/comparisons/cline-alternatives (snippet) | UNV slug; mentioned as BYOK alternative only |
| AI coding agents — AVOID | continuedev/continue | (avoid) IDE assistant | https://github.com/continuedev/continue | EV. ARCHIVED, read-only, "no longer actively maintained"; final 2.0.0; ~36k stars |
| AI coding agents — AVOID | RooCodeInc/Roo-Code | (avoid) VS Code agent | https://github.com/RooCodeInc/Roo-Code | EV. ARCHIVED 2026-05-15; ~24.3k; points to ZooCode fork and Cline |
| AI coding agents — AVOID | google-gemini/gemini-cli | (avoid) Gemini CLI | https://www.techtimes.com/articles/318660/20260618/gemini-cli-shutdown-takes-effect-ci-cd-pipelines-break-go-based-antigravity-cli-arrives.htm | Service stopped 2026-06-18 for free/Pro/Ultra; replaced by closed-source Antigravity CLI (`agy`). Repo archival status not checked |
| AI coding agents (riser) | "DeepSeek Harness" (slug unknown) | Coding agent, ~203k stars in 2 weeks | https://www.morphllm.com/best-ai-coding-agents-2026 (snippet) | NOT verified; single snippet; slug not found |
| AI coding agents (riser) | "Pi" coding agent (slug unknown) | CLI agent ~98k | same snippet | Slug not found; possibly badlogic/pi-mono (UNV) |
| Claude skills/plugins | anthropics/skills | Official Agent Skills (docx/pdf/pptx/xlsx, etc.) | https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md | EV. ~177.4k, commit 2026-09-10 |
| Claude skills/plugins | obra/superpowers | Brainstorm→plan→TDD→subagent workflow skills | https://www.firecrawl.dev/blog/best-claude-code-skills (search snippet) | EV-ish (snippet). ">94k", in Anthropic marketplace |
| Claude skills/plugins | multica-ai/andrej-karpathy-skills | Single SKILL.md of 4 anti-failure coding rules | Medium/All About Claude via search snippet | Snippet says 156k; slug as quoted by snippet — verify |
| Claude skills/plugins | affaan-m/ECC | Mega Claude Code config/skills bundle | https://githublb.vercel.app/topic/claude-code | EV (leaderboard). ~263k |
| Claude skills/plugins | addyosmani/agent-skills | Engineering agent skills pack | https://githublb.vercel.app/topic/claude-code | EV. ~97.1k |
| Claude skills/plugins | nextlevelbuilder/ui-ux-pro-max-skill | UI/UX design skill for fast polished frontends | https://githublb.vercel.app/topic/claude-code | EV. ~129.1k |
| Claude skills/plugins | Leonxlnx/taste-skill | Design-taste skill for frontend output | https://githublb.vercel.app/topic/claude-code | EV. ~88.5k |
| Claude skills/plugins | thedotmack/claude-mem | Persistent memory across Claude Code sessions | https://githublb.vercel.app/topic/claude-code | EV. ~94.3k |
| Claude skills/plugins | Graphify-Labs/graphify | Codebase/docs → knowledge graph for agents | https://githublb.vercel.app/topic/claude-code | EV. ~119.7k |
| Claude skills/plugins | gsd-build/get-shit-done | Spec-driven build workflow for Claude Code | https://githublb.vercel.app/topic/claude-code | EV. ~64.5k |
| Claude skills/plugins | rtk-ai/rtk | Token-reduction proxy for CLI agent output | https://githublb.vercel.app/topic/claude-code | EV. ~81k; use unverified from description (none on page) |
| Claude skills/plugins | farion1231/cc-switch | Switch providers/configs for Claude Code/Codex | https://githublb.vercel.app/topic/claude-code | EV. ~133.7k |
| Skills registries/lists | ComposioHQ/awesome-claude-skills | Curated skills index | https://githublb.vercel.app/topic/claude-code | EV. ~75.3k |
| Skills registries/lists | hesreallyhim/awesome-claude-code | Curated Claude Code commands/hooks/plugins | https://githublb.vercel.app/topic/claude-code | EV. ~54.3k |
| Skills registries/lists | shanraisshan/claude-code-best-practice | Practices reference | https://githublb.vercel.app/topic/claude-code | EV. ~66.1k |
| Skills registries/lists | sickn33/agentic-awesome-skills | Large skills collection | https://githublb.vercel.app/topic/claude-code | EV. ~46.6k |
| Local models | ollama/ollama | Run local LLMs offline (bad venue Wi-Fi, no API credits) | https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md | EV. ~181.3k |
| Public data & APIs | public-apis/public-apis | Pick a free API for your idea in minutes | https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md | EV. ~481.9k, commit 2026-09-20 |
| Public data & APIs | ripienaar/free-for-dev | Free-tier SaaS/PaaS/IaaS for hosting, DBs, auth | https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md | EV. ~137.9k, commit 2026-09-20 |
| Public data & APIs | awesomedata/awesome-public-datasets | Topic-organised open datasets | — | UNV slug; not in Top-100; not evidenced this run |
| Public data & APIs | APIs-guru/openapi-directory | Machine-readable OpenAPI specs for many APIs | — | UNV |
| Mega lists | sindresorhus/awesome | Index of awesome lists | https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md | EV. ~508.3k |
| Mega lists | awesome-selfhosted/awesome-selfhosted | Self-hostable backends/services to bolt on | https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md | EV. ~320.6k |
| Mega lists | punkpeye/awesome-mcp-servers | Find an MCP server for any integration | https://www.star-history.com/punkpeye/awesome-mcp-servers/ | EV. ~93.9k (2026-09-04); growth has plateaued (+4/wk) |
| Mega lists | codecrafters-io/build-your-own-x | Learning, low hackathon utility | https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md | EV. #1, ~548.5k. Include only as "not a force-multiplier" |
| Mega lists | nilbuild/developer-roadmap | Learning; low direct hackathon utility | https://github.com/nilbuild/developer-roadmap | EV. RENAMED from kamranahmedse/developer-roadmap |
| Mega lists | donnemartin/system-design-primer | Pitch-architecture talking points; low utility | https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md | EV. ~371k |
| Mega lists — AVOID/stale | trimstray/the-book-of-secret-knowledge | CLI/ops cheat sheets | https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md | EV. Last commit 2024-11-19 (stale) |
| Mega lists — AVOID/stale | jlevy/the-art-of-command-line | CLI tips | same | EV. Last commit 2024-06-25 (stale) |
| Mock data & testing | typicode/json-server | Fake REST API from a JSON file in 30s | https://www.star-history.com/typicode/json-server/ | EV. ~75.7k; v1.0.0-beta.15 published ~6 months ago (slowing) |
| Mock data & testing | mswjs/msw | Intercept requests to mock REST/GraphQL in browser/Node | https://github.com/mswjs/msw | EV. ~18.1k per search summary; active |
| Mock data & testing | mockoon/mockoon | GUI local mock API server, Faker templating | https://www.star-history.com/mockoon/mockoon/ | EV. ~8.4k; monthly/bimonthly releases |
| Mock data & testing | faker-js/faker | Realistic seed/demo data (JS) | https://github.com/faker-js/faker/releases | EV. ~15k per search summary |
| Mock data & testing | joke2k/faker | Realistic seed data (Python) | — | UNV |
| Mock data & testing / scraping | microsoft/playwright | E2E tests + deterministic browser automation | https://www.nxcode.io/resources/news/stagehand-vs-browser-use-vs-playwright-ai-browser-automation-2026 | Slug UNV; 70k+ per search summary |
| Scraping/automation | microsoft/playwright-mcp | Give agents a browser via MCP | https://fastcrw.com/blog/browser-automation-ai-agents | Slug UNV; ~36.7k per summary |
| Scraping/automation | browser-use/browser-use | LLM-driven autonomous browser agent | https://www.nxcode.io/resources/news/stagehand-vs-browser-use-vs-playwright-ai-browser-automation-2026 | Slug UNV; ~112.2k per summary |
| Scraping/automation | browserbase/stagehand | act/extract/observe AI primitives over Playwright | same | Slug UNV; 50k+ per summary |
| Scraping/automation | apify/crawlee | JS/Python crawling library | https://www.firecrawl.dev/blog/best-open-source-web-crawler | Slug UNV; ~25.7k |
| Scraping/automation | firecrawl/firecrawl | URL → LLM-ready markdown | https://www.firecrawl.dev/blog/best-open-source-web-crawler | Slug UNV (formerly mendableai/firecrawl) |
| Scraping/automation | unclecode/crawl4ai | Open-source LLM-friendly crawler | same | Slug UNV |
| Scraping/automation | puppeteer/puppeteer; scrapy/scrapy | Classic headless Chrome / Python crawling | — | UNV, not researched this run |
| Diagram/docs/pitch | excalidraw/excalidraw | Hand-drawn architecture diagrams for pitch | https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md | EV. ~132.6k, commit 2026-09-20 |
| Diagram/docs/pitch | mermaid-js/mermaid | Diagrams-as-code in README/slides | https://www.pkgpulse.com/guides/slidev-vs-marp-vs-revealjs-code-first-presentations-2026 | Slug UNV; Slidev embeds Mermaid |
| Diagram/docs/pitch | slidevjs/slidev | Markdown+Vue dev slides, best DX | https://github.com/slidevjs/slidev/blob/main/docs/guide/why.md | EV slug |
| Diagram/docs/pitch | marp-team/marp | Simplest Markdown→slides, VS Code ext | https://dasroot.net/posts/2026/04/markdown-presentation-tools-marp-slidev-reveal-js/ | Slug UNV |
| Diagram/docs/pitch | hakimel/reveal.js | Most flexible HTML slides | same | Slug UNV |
| Diagram/docs/pitch | charmbracelet/vhs; asciinema/asciinema; obsproject/obs-studio | Scripted terminal GIFs / terminal recording / demo video | — | UNV; star data not found this run |
| Productivity/self-host | n8n-io/n8n | Glue integrations/webhooks/AI flows without code | https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md | EV. ~205.5k, commit 2026-09-21 |
| Productivity/self-host | appsmithorg/appsmith; ToolJet/ToolJet; calcom/cal.com; umami-software/umami | Internal admin UIs / scheduling / analytics | — | UNV; not researched this run |
| Hackathon-specific | sahat/hackathon-starter | Node/Express boilerplate w/ OAuth (8 providers) + LangChain ReAct agent | https://github.com/sahat/hackathon-starter | EV. v9/v10 with AI features — actively updated |
| Hackathon-specific | anishathalye/gavel | Pairwise-comparison expo judging system (organizers) | https://github.com/anishathalye/gavel | EV. Not archived; 489 stars; "stable software" |
| Hackathon-specific | HackMIT/gavel | HackMIT fork of Gavel | https://github.com/HackMIT/gavel | EV exists; activity unchecked |

Count: 66 rows (~75 repos incl. grouped rows); ~40 with slug evidence this run.

## Findings

1. anomalyco/opencode is the most-starred OSS coding agent people run (~209k); repo moved from sst/opencode | https://github.com/anomalyco/opencode/issues/16440 ; https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md | GitHub / EvanLi | 2026-09-21 (auto-updated) | accessed 2026-09-21 | high | fact
2. Gemini CLI stopped serving free/Pro/Ultra users 2026-06-18, replaced by closed-source Go Antigravity CLI (`agy`); enterprise and paid API keys keep access | https://www.techtimes.com/articles/318660/20260618/gemini-cli-shutdown-takes-effect-ci-cd-pipelines-break-go-based-antigravity-cli-arrives.htm ; https://inventivehq.com/blog/gemini-cli-deprecated-antigravity-cli-migration | TechTimes; InventiveHQ | 2026-06-18 | accessed 2026-09-21 | high (multiple outlets, search snippets) | fact
3. continuedev/continue is archived/read-only, "no longer actively maintained", final 2.0.0 release; ~36k stars | https://github.com/continuedev/continue | GitHub | n/d | accessed 2026-09-21 | high | fact
4. RooCodeInc/Roo-Code archived 2026-05-15; recommends ZooCode fork or Cline | https://github.com/RooCodeInc/Roo-Code | GitHub | 2026-05-15 | accessed 2026-09-21 | high | fact
5. Aider has had no commits since 2026-05-22 | https://www.morphllm.com/comparisons/cline-alternatives | Morph | 2026 | accessed 2026-09-21 | low-medium (search snippet only; fetch not done) | claim
6. Goose moved from block/goose to aaif-goose/goose (Linux Foundation AAIF), contributed Dec 2025, transferred Apr 2026 | https://goose-docs.ai/blog/2026/04/07/goose-moves-to-aaif/ | goose project | 2026-04-07 | accessed 2026-09-21 | high | fact
7. Aug-2026 CLI agent star ranking: DeepSeek Harness ~203k, OpenCode ~202k, Codex ~119k, Pi ~98k, OpenHands ~85k, Cline ~67k, Goose ~54k, Aider ~48k | https://www.morphllm.com/best-ai-coding-agents-2026 | Morph | 2026-08-29 | accessed 2026-09-21 | low (snippet; fetch 429; DeepSeek Harness slug unlocated) | claim
8. anthropics/skills ~177k stars (#46 overall), obra/superpowers >94k and in Anthropic marketplace | EvanLi Top-100; https://www.firecrawl.dev/blog/best-claude-code-skills | EvanLi; Firecrawl | 2026 | accessed 2026-09-21 | high / medium | fact
9. Claude-code topic leaderboard (updated 2026-09-20) top entries: affaan-m/ECC 263k, NousResearch/hermes-agent 247k, farion1231/cc-switch 134k, nextlevelbuilder/ui-ux-pro-max-skill 129k, Graphify-Labs/graphify 120k, addyosmani/agent-skills 97k | https://githublb.vercel.app/topic/claude-code | GitHub Stars Leaderboard | 2026-09-20 | accessed 2026-09-21 | medium (third-party aggregator) | metric
10. public-apis/public-apis (~482k), free-for-dev (~138k), awesome-selfhosted (~321k), n8n (~205k), excalidraw (~133k) all committed within the last week | https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md | EvanLi | 2026-09-21 | accessed 2026-09-21 | high | metric
11. trimstray/the-book-of-secret-knowledge (last commit 2024-11-19) and jlevy/the-art-of-command-line (2024-06-25) are stale despite top-100 stars | same | EvanLi | 2026-09-21 | accessed 2026-09-21 | high | fact
12. developer-roadmap now lives at nilbuild/developer-roadmap (was kamranahmedse/developer-roadmap) | https://github.com/nilbuild/developer-roadmap | GitHub | n/d | accessed 2026-09-21 | high | fact
13. punkpeye/awesome-mcp-servers ~93.9k stars, 3.4k contributors, only +4 stars that week (plateau) | https://www.star-history.com/punkpeye/awesome-mcp-servers/ | star-history | 2026-09-04 | accessed 2026-09-21 | medium | metric
14. json-server ~75.7k but latest npm (1.0.0-beta.15) ~6 months old; MSW active; Mockoon ~8.4k moving to monthly/bimonthly releases | https://www.star-history.com/typicode/json-server/ ; https://www.star-history.com/mockoon/mockoon/ ; https://mockoon.com/blog/ | star-history; Mockoon | 2026-09 | accessed 2026-09-21 | medium (search summaries) | metric
15. Browser-automation stars: browser-use ~112k, Playwright 70k+, Stagehand 50k+, Playwright MCP ~36.7k, Crawlee ~25.7k; hybrid AI-over-Playwright is the trend | https://www.nxcode.io/resources/news/stagehand-vs-browser-use-vs-playwright-ai-browser-automation-2026 ; https://fastcrw.com/blog/browser-automation-ai-agents | NxCode; fastCRW | 2026 | accessed 2026-09-21 | medium (search summary) | metric
16. Slidev = best dev DX (embeds Mermaid, Vue); Marp = simplest/most mature, VS Code ext; reveal.js = most flexible | https://www.pkgpulse.com/guides/slidev-vs-marp-vs-revealjs-code-first-presentations-2026 ; https://htmldecks.com/blog/best-presentation-tools-developers.html | PkgPulse; HTMLDecks | 2026 | accessed 2026-09-21 | medium | opinion
17. sahat/hackathon-starter still maintained, now includes LangChain ReAct agent, 8 OAuth providers, prompt-injection guardrails (v10) | https://github.com/sahat/hackathon-starter | GitHub | n/d | accessed 2026-09-21 | medium (search snippet) | fact
18. anishathalye/gavel not archived, 489 stars, described as "stable software" | https://github.com/anishathalye/gavel | GitHub | n/d | accessed 2026-09-21 | high | fact

## Leads not chased / not found
- Slug + existence of "DeepSeek Harness" and "Pi" agent (possibly badlogic/pi-mono) — single-snippet claims, unverified.
- OpenHands current slug (OpenHands/OpenHands vs All-Hands-AI/OpenHands), cline/cline, Aider-AI/aider staleness (fetch morphllm/pinggy failed).
- google-gemini/gemini-cli GitHub archival status (service shutdown confirmed; repo state not).
- awesome-public-datasets, APIs-guru/openapi-directory activity; hackathon-specific public dataset lists.
- Stars/activity for Mermaid, Marp, reveal.js, VHS, asciinema, OBS, Appsmith, ToolJet, Cal.com, Umami, Plausible, Puppeteer, Scrapy, Faker (Python).
- Firecrawl slug rename (mendableai → firecrawl), browser-use/stagehand exact slugs.
- Hackathon organizer toolkits beyond Gavel (HELPq, Jury, Devpost galleries, MLH resources); no "awesome-hackathon" list evaluated.
- NousResearch/hermes-agent (247k) — high stars but role for hackathons unclear.
