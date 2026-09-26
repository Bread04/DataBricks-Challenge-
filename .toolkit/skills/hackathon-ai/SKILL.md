---
name: hackathon-ai
description: AI feature and agent toolkit for hackathons covering the workflow-before-agent ladder, framework choice (AI SDK v7 ToolLoopAgent, Pydantic AI, Claude Agent SDK, plain loop), tool design, MCP spec 2026-07-28, step limits, the lethal trifecta, demo-proofing without temperature, tracing and evals. Use when adding an LLM feature or agent to a hackathon app, or reviewing one.
---

# AI & Agents Toolkit

<!-- markdownlint-disable MD013 -->

> Condensed rules. Full detail: `../../04-ai-and-rag/docs/agents-and-tool-use.md`, `model-selection.md`, `rag-architecture.md` · macros in `../../04-ai-and-rag/PROMPTS-ML.md`. Verified 2026-09-23.

## Pattern ladder (stop at the first step that works)

Single call → prompt chain → routing → parallel → orchestrator-workers → evaluator-optimizer → autonomous agent. Use workflows when the path is known and agents only when the step count is unknown. **One agent by default.** Subagents only for independent, read-only fan-out: multi-agent costs about 15× chat tokens and breaks when agents need shared context or are writing code.

## Framework

| Situation | Pick |
| --- | --- |
| Next.js / TS | **AI SDK v7** `ToolLoopAgent` + AI SDK UI (Node 22+, ESM-only) |
| TS with memory and workflows | Mastra (Apache-2.0 core; `ee/` needs a licence for production) |
| Python | **Pydantic AI** |
| Agent edits files / runs bash | Claude Agent SDK |
| Flow fits in about 5 bullets | No framework: provider SDK + loop (Anthropic Tool Runner / OpenAI Responses) |
| Hosted | Claude Managed Agents (tokens + $0.08 per running session-hour) · OpenAI Agents API (beta) |

## ⚠️ Don't use outdated patterns

| Outdated | Current |
| --- | --- |
| OpenAI Assistants API | **Shut down 2026-08-26.** Use Responses + Conversations |
| AutoGen / Semantic Kernel / OpenAI Agent Builder | Microsoft Agent Framework / Agents SDK |
| AI SDK `stepCountIs`, `system`, `onFinish`, `fullStream`, `needsApproval` | v7: `isStepCount`, `instructions`, `onEnd`, `stream`, `toolApproval` |
| `temperature: 0` for determinism | **400 error** on Claude Opus 4.7+ / Sonnet 5, and rejected by GPT-6 with reasoning. Omit it and use a demo cache |
| MCP `FastMCP`, `@modelcontextprotocol/sdk`, sessions, HTTP+SSE | MCP spec **2026-07-28** (stateless) + SDK v2 (`MCPServer`, `@modelcontextprotocol/server`) |
| `langchain-mcp-adapters` | LangChain v1.4+ built-in `MCPAdapter` |
| Claude `computer_20251124` | `computer_toolset_20260801` (GA) |
| Helicone | Langfuse (Helicone is in maintenance mode) |

## Tool design

Few tools (fewer than about 20) · namespaced names (`books_search`) · clear parameter names · teammate-style descriptions · `strict: true` · enums · short readable output (no UUIDs, paginate) · **actionable error messages** · server tools (web search, code execution) when you can.

## Reliability

- **Always set the step cap yourself.** AI SDK `stopWhen: isStepCount(n)` (default 20; `WorkflowAgent` has none) · OpenAI `max_turns` (default 10; handle `MaxTurnsExceeded`) · Anthropic `max_iterations`.
- **Stream everything.** The Vercel Hobby limit is 300 s, streaming included. Use Vercel Workflows for longer runs.
- **Rate limits:** SDKs retry 429/529 twice with backoff. A spend-cap 429 never recovers, so a low spend cap is your budget kill-switch.
- **Cost:** put the unchanging system prompt and tools first to get prompt-cache reads at about 0.1×.

## Security

**Lethal trifecta:** private data + untrusted content + a way to send data out. Never give one agent all three. Human approval for write, pay and send actions · trusted MCP servers only (tool poisoning) · read-only database role · sandbox computer use · OWASP Agentic Top 10 (2026).

## Demo-proofing

3 golden inputs, each run 5 times · `DEMO_MODE` cached fallback · seeded data · stream text and show tool-call cards · backup video recorded early · one flow working within about 90 seconds.

## Observe and evaluate

Langfuse free tier (50k units, OSS) · 20–50 pass/fail cases from real failures · read at least 30 traces · check any LLM judge against your own labels.

## Related skills

Model prices: `../../04-ai-and-rag/docs/model-selection.md` · RAG: `../hackathon-backend/SKILL.md` → AI and RAG · chat UI: `../hackathon-frontend/SKILL.md` → AI UI · deploying: `../hackathon-deployment/SKILL.md`.

## Sources

[Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) · [Writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) · [Multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system) · [Cognition](https://cognition.com/blog/dont-build-multi-agents) · [AI SDK v7 migration](https://ai-sdk.dev/docs/migration-guides/migration-guide-7-0) · [MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/changelog) · [OpenAI changelog](https://developers.openai.com/api/docs/changelog) · [Opus 5 migration (temperature)](https://platform.claude.com/docs/en/models/opus-5/migration-guide) · [Lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) · [Agent evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) · [Vercel limits](https://vercel.com/docs/functions/limitations)
