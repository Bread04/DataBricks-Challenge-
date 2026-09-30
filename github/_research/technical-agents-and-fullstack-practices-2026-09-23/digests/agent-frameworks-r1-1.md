# Digest: agent frameworks — round 1, assistant 1
Accessed: 2026-09-23 · Tool calls used: 20

## Claims
| # | Claim | Source URL | Publisher | Pub date | Confidence (high/med/low) | Class |
|---|---|---|---|---|---|---|
| 1 | Claude Agent SDK (TypeScript) latest is v0.3.280 (Sep 22 2026), kept in parity with Claude Code v2.1.280; still 0.x versioning | https://github.com/anthropics/claude-agent-sdk-typescript/releases | Anthropic (GitHub) | 2026-09-22 | high | version |
| 2 | Recent Claude Agent SDK releases add MCP features: `mcpServerStatus()` with MCP Apps UI metadata, alpha `readMcpResource()`, so MCP is supported natively | https://github.com/anthropics/claude-agent-sdk-typescript/releases | Anthropic (GitHub) | 2026-09-22 | high | feature |
| 3 | Claude Code SDK was renamed Claude Agent SDK. The secondary source gives two different dates for the rename (Sep 2025 and "early 2026"). Its "1.0 stable on 29 Sep 2025" claim conflicts with the 0.3.x npm versions in #1 | https://www.morphllm.com/ai-agent-framework | Morph (vendor blog) | ~2026 (undated in snippet) | low | status |
| 4 | Anthropic announced that Agent SDK / `claude -p` usage on subscription plans would move to a separate monthly credit from Jun 15 2026, then paused the change the same day | https://www.morphllm.com/ai-agent-framework (search snippet; also releasebot.io aggregator) | Morph / Releasebot | 2026 | low | pricing |
| 5 | Claude Managed Agents is a beta, Anthropic-hosted agent harness (beta header `managed-agents-2026-04-01`). It is enabled by default for all API accounts and includes Bash, file ops, web search/fetch, MCP servers, skills, cloud or self-hosted sandboxes, and cron-scheduled deployments. It is not eligible for ZDR or HIPAA | https://platform.claude.com/docs/en/managed-agents/overview | Anthropic docs | fetched 2026-09-23 | high | feature |
| 6 | Managed Agents pricing or free tier not stated on the overview page | https://platform.claude.com/docs/en/managed-agents/overview | Anthropic docs | fetched 2026-09-23 | high (absence) | pricing |
| 7 | OpenAI Agents SDK (Python) latest is v0.22.3 (Sep 17 2026). v0.22.1 (Sep 8) added server-wide MCP guardrails, Unix-local isolation, and Docker sandbox labels. Still 0.x | https://github.com/openai/openai-agents-python/releases | OpenAI (GitHub) | 2026-09-17 | high | version |
| 8 | The OpenAI Agents SDK's new harness and sandbox capabilities shipped first in Python, with TypeScript to follow later | https://openai.com/index/the-next-evolution-of-the-agents-sdk/ (search snippet); TechCrunch 2026-04-15 | OpenAI / TechCrunch | 2026-04 | med (possibly stale) | feature |
| 9 | OpenAI announced the Agent Builder discontinuation on Jun 3 2026. The search snippet says Agent Builder and Evals shut down Nov 30 2026, with the Agents SDK recommended for code workflows | https://developers.openai.com/api/docs/changelog ; https://openai.com/index/introducing-agentkit/ | OpenAI | 2026-06-03 | med (Nov 30 date only from a snippet) | status |
| 10 | OpenAI Assistants API shut down completely on Aug 26 2026; migrate to Responses and Conversations APIs | https://developers.openai.com/api/docs/changelog | OpenAI | 2026-08-26 | high | status |
| 11 | OpenAI "Agents API" (a managed Codex harness where OpenAI handles session orchestration, compaction and recovery) entered public beta on Sep 10 2026 | https://developers.openai.com/api/docs/changelog | OpenAI | 2026-09-10 | high | feature |
| 12 | Vercel AI SDK's current major is v7 (ai@7.0.111, Sep 22 2026). v6 (6.0.288) and v5 (5.0.263) still get patches | https://github.com/vercel/ai/releases | Vercel (GitHub) | 2026-09-22 | high | version |
| 13 | AI SDK 6 added the Agent interface and `ToolLoopAgent` default, human-in-the-loop via `needsApproval`, MCP support, structured tool output and DevTools. v7 changes were not examined | https://vercel.com/blog/ai-sdk-6 | Vercel | late 2025 | med (v6-era; v7 may change APIs) | feature |
| 14 | LangGraph (Python) latest is 1.2.12 (Sep 21 2026), MIT. Described as "low-level orchestration" for long-running stateful agents; LangChain agents are built on LangGraph | https://pypi.org/project/langgraph/ | PyPI / LangChain Inc | 2026-09-21 | high | version |
| 15 | Pydantic AI latest is 2.48.0 (Sep 23 2026), MIT. It is model-agnostic ("every model a string swap away"), supports MCP, has typed tools and structured output, and offers durable execution via Temporal/DBOS/Prefect | https://pypi.org/project/pydantic-ai/ | PyPI / Pydantic | 2026-09-23 | high | version |
| 16 | CrewAI latest is 1.15.22 (Sep 16 2026), MIT, standalone (no LangChain dependency). It has Crews (autonomous) and Flows (event-driven), supports many LLMs including Ollama, and requires Python 3.10–3.13. MCP was not confirmed on the page | https://pypi.org/project/crewai/ | PyPI / CrewAI | 2026-09-16 | high | version |
| 17 | Google ADK (Python) latest is 2.9.2 (Sep 18 2026), Apache-2.0. Described as "model-agnostic" but optimized for Gemini. It supports MCP tools and has a built-in dev UI. v2.0 broke the agent API and session schema | https://pypi.org/project/google-adk/ | PyPI / Google | 2026-09-18 | high | version |
| 18 | Microsoft Agent Framework (Python `agent-framework`) latest is 1.19.0 (Sep 18 2026), MIT, "Production/Stable", with Python and .NET versions | https://pypi.org/project/agent-framework/ | PyPI / Microsoft | 2026-09-18 | high | version |
| 19 | AutoGen and Semantic Kernel are in maintenance mode (bug and security fixes only). Microsoft Agent Framework (Oct 2025) is their successor for new projects. The community fork AG2 continues separately | https://github.com/microsoft/autogen ; https://venturebeat.com/ai/microsoft-retires-autogen-and-debuts-agent-framework-to-unify-and-govern | Microsoft / VentureBeat | 2025-10 onward | high (two sources) | status |
| 20 | smolagents latest is 1.26.0 (May 29 2026). Earlier releases: 1.25 on May 14, 1.24 on Jan 16. The release pace has slowed, with none in about 4 months. It has a ~1,000-LOC core, code-writing agents, any LLM via LiteLLM, and MCP support | https://pypi.org/project/smolagents/ | PyPI / Hugging Face | 2026-05-29 | high (version); med (status inference) | status |
| 21 | Agno latest is 3.0.10 (Sep 16 2026), Apache-2.0. It is now positioned as an "agent platform" (production API, storage, RBAC, 100+ integrations, Slack/Discord interfaces, cron). Heavier than a hackathon needs | https://pypi.org/project/agno/ | PyPI / Agno | 2026-09-16 | high (version); med (fit judgment) | version |
| 22 | Mastra: @mastra/core 1.67.0 (Sep 15 2026), TypeScript. The GitHub repo has ~28.3k stars and very frequent releases (workflows, memory, sandbox, Studio). License not confirmed | https://github.com/mastra-ai/mastra/releases | Mastra (GitHub) | 2026-09-15 | high (version); low (license) | version |
| 23 | Practitioner rule of thumb: "if you can describe your agent's control flow in five bullet points or fewer, you probably do not need a framework"; a model + tools + loop covers most cases | https://ai-tldr.dev/learn/agent-frameworks/choosing-a-framework/agent-without-framework/ ; several dev.to posts | AI/TLDR, dev.to | 2026 | med (blog register, multiple independent authors) | practitioner-sentiment |
| 24 | Practitioner claims: Pydantic AI agents run about 60 LOC vs about 200 for LangChain, and LangChain's loose `Any` typing hurts IDE help. One team post-mortem: "Why We Ditched LangChain for Pydantic AI" | https://jiminsf.com/langchain-to-pydantic-ai/ ; https://www.kunalganglani.com/blog/pydantic-ai-vs-langchain | Individual blogs | 2025–26 | low-med (seen only in snippets; LangChain v1 may have addressed some complaints) | practitioner-sentiment |
| 25 | OpenAI's own "practical guide to building agents" and LangChain's "How to think about agent frameworks" both discuss when frameworks help vs a plain loop (vendor sources) | https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf ; https://www.langchain.com/blog/how-to-think-about-agent-frameworks | OpenAI / LangChain | 2025 | low (not read, lead only) | practitioner-sentiment |

## Notes for synthesis
- **Landscape shape:** Every framework on the list shipped a release in the last ~10 days, except smolagents (last release May 29 2026). By version: LangGraph, CrewAI, Microsoft Agent Framework and Mastra are at 1.x. Pydantic AI, Google ADK, Vercel AI SDK (v7) and Agno (v3) are at 2.x or higher. Both vendor agent SDKs are still 0.x: Claude Agent SDK TS is 0.3.x and OpenAI Agents SDK Python is 0.22.x. Being 0.x does not mean immature here, since both release weekly, but breaking changes are possible.
- **Consolidations and deprecations in 2025–26:**
  - Microsoft moved AutoGen and Semantic Kernel into Microsoft Agent Framework; both old projects are in maintenance mode (two sources).
  - OpenAI shut down the Assistants API (Aug 26 2026) and is discontinuing Agent Builder (announced Jun 3 2026).
  - OpenAI launched a managed "Agents API" public beta (Sep 10 2026).
  - Claude Code SDK became Claude Agent SDK.
  - Vercel AI SDK moved to v7. Hackathon tutorials written for v5/v6 may mismatch the current API; this needs a v7 migration-guide check.
- **Vendor-tied vs model-agnostic:**
  - Vendor-leaning: Claude Agent SDK (Claude-specific harness), OpenAI Agents SDK (OpenAI-first; model-agnostic support not verified this run), Google ADK (says "model-agnostic" but optimized for Gemini), Microsoft Agent Framework (the page lists Azure OpenAI and OpenAI clients).
  - Model-agnostic: Vercel AI SDK, Pydantic AI, smolagents, CrewAI, Mastra, LangGraph.
- **MCP:** confirmed this run for Claude Agent SDK, OpenAI Agents SDK, Vercel AI SDK (v6), Pydantic AI, Google ADK and smolagents. Not confirmed for CrewAI, Microsoft Agent Framework, Agno's runtime (only its docs MCP server was seen), Mastra or LangGraph.
- **Contradiction:** the Morph blog says the Claude Agent SDK hit a "1.0 stable" release on 29 Sep 2025, but the official npm/GitHub versions are 0.3.x (Sep 2026). Trust GitHub. The same source also dates the rename both "Sep 2025" and "early 2026".
- **Tentative matrix (a hypothesis to validate, not yet a conclusion):**
  - TS/Next.js: Vercel AI SDK v7. It is model-agnostic, has built-in MCP support and UI hooks, and its versions were verified. Mastra is the option if you want batteries included (memory, workflows).
  - Python: Pydantic AI. It is model-agnostic, has typed tools, and practitioners report low overhead.
  - Fastest path: the provider SDK plus a hand-written loop (for a flow of five bullets or fewer), or a vendor agent SDK / managed agent (Claude Agent SDK or Managed Agents, OpenAI Agents SDK) if you are committed to one model vendor.
  - Avoid for new hackathon projects: AutoGen (maintenance mode), OpenAI Assistants API (shut down) and Agent Builder (being discontinued). Agno and Microsoft Agent Framework are likely overkill.
  - LangGraph is powerful but low-level. The learning-curve claim rests on practitioner blogs only.

## Leads worth chasing
- Vercel AI SDK v7 release notes and migration guide: what changed from v6's Agent/ToolLoopAgent API?
- LangChain v1 `create_agent` current version, and whether the typing and abstraction complaints were fixed.
- OpenAI Agents SDK TypeScript (`@openai/agents`) latest version, and whether it supports non-OpenAI models (LiteLLM / AI SDK adapter).
- Pricing for OpenAI Agents API beta, Claude Managed Agents and AWS Bedrock AgentCore, including free tiers and hackathon credits.
- Confirm the Agent Builder shutdown date (Nov 30 2026) on the OpenAI deprecations page.
- Mastra license (believed Apache-2.0 or Elastic, unverified), and Mastra MCP support.
- Read the jiminsf.com post-mortem and the HN threads for first-hand switching stories.
- GitHub star counts for the others (only Mastra's was captured).

## Looked for but could not find
- A free tier or pricing on the Claude Managed Agents overview page (not stated).
- The Claude Agent SDK license (not shown on the releases page).
- MCP support statements for CrewAI and Microsoft Agent Framework on their PyPI pages.
- AWS Bedrock AgentCore details and Google Vertex Agent Engine details: not searched (budget exhausted).
- First-hand HN/Reddit threads: only blog posts surfaced.
