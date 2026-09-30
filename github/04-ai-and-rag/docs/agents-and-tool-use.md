# 🤖 AI Agents and Tool Use (September 2026)

<!-- markdownlint-disable MD013 -->

> **In plain English:** an **agent** is an AI model that works in a loop. It decides to use a **tool** (search the web, query your database, send an email), reads the result, and repeats until the job is done. This guide covers which framework to use, how to design tools, which workflow pattern fits, and how to stop an agent from embarrassing you in front of the judges. Verified 2026-09-23. Sources: [`evidence.md`](evidence.md) (labels **A**).

---

## ⚡ The short version

1. **Start with the simplest thing that works.** Try one model call first, then a fixed workflow, and use an agent loop only if the number of steps really can't be predicted ([Anthropic](https://www.anthropic.com/engineering/building-effective-agents)).
2. **Use one agent, not a team of agents.** Multi-agent setups use about **15×** the tokens of a normal chat and break when the agents need shared context or are writing code ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system), [Cognition](https://cognition.com/blog/dont-build-multi-agents)).
3. **Always set a step limit yourself.** Don't rely on the defaults.
4. **Don't set `temperature`.** Current Claude and GPT-6 models reject it (see [Reliability](#-reliability-rules)).
5. **A human approves anything that writes, pays or sends.**
6. **Check the date on any tutorial.** Much of the 2025 agent code online no longer runs (see [Outdated patterns](#-dont-use-outdated-patterns)).

---

## 🪜 Pick a pattern (go down the ladder only when you need to)

| Step | Pattern | Use it when | Hackathon example |
| --- | --- | --- | --- |
| 1 | **Single call** + retrieval/examples | One input → one output | "Summarise this PDF" |
| 2 | **Prompt chain** | Fixed steps, each easier than the whole | outline → draft → polish |
| 3 | **Routing** | Different inputs need different handling | billing vs tech-support questions |
| 4 | **Parallelisation** | Independent sub-tasks, or voting for confidence | check 5 sources at once |
| 5 | **Orchestrator-workers** | Sub-tasks aren't known until runtime | "research this company" |
| 6 | **Evaluator-optimizer** | Clear quality criteria and iteration helps | draft → critique → revise |
| 7 | **Autonomous agent loop** | Open-ended, number of steps unknown | "plan my trip and book it" |

Steps 1–4 are **workflows**: you write the path in code, so they're predictable and cheap. Only step 7 lets the model choose its own path ([Anthropic](https://www.anthropic.com/engineering/building-effective-agents)).

**Multi-agent:** use subagents only for **independent, read-only fan-out**, such as several parallel searches that each return a short summary of about 1–2k tokens. Never split one piece of code between agents: they make conflicting assumptions ([Cognition](https://cognition.com/blog/dont-build-multi-agents), [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).

---

## 🧰 Pick a framework

| Your situation | Use | Why |
| --- | --- | --- |
| **Next.js / TypeScript web app** (most teams) | ⭐ **Vercel AI SDK v7**: `ToolLoopAgent` + AI SDK UI 🆓 | Works with any model; built-in 20-step cap, MCP client, tool approval, React chat hooks ([docs](https://ai-sdk.dev/docs/agents/overview)) |
| TypeScript, want memory + workflows built in | **Mastra** 🆓 | MCP client and server; Apache-2.0 core (the `ee/` folder needs a licence for production) ([GitHub](https://github.com/mastra-ai/mastra)) |
| **Python** | ⭐ **Pydantic AI** 🆓 | Typed tools, works with any model, MCP ([PyPI](https://pypi.org/project/pydantic-ai/)) |
| Agent that **edits files or runs code** | **Claude Agent SDK** 💰 (or OpenAI Agents SDK Sandbox Agents) | Claude Code as a library: file, bash and web tools, subagents, skills ([docs](https://code.claude.com/docs/en/agent-sdk/overview)) |
| **Simplest possible / flow fits in ~5 bullets** | **No framework:** the provider SDK plus a loop (Anthropic Tool Runner, OpenAI Responses) 🆓 | Nothing hidden, easiest to debug. Many 2026 practitioners prefer it |
| Already know LangChain | LangChain v1 `create_agent` (runs on LangGraph) 🆓 | Fine if you know it. Opinions are split, so don't learn it at the hackathon |
| Hosted, no server of your own | Claude Managed Agents 💰 (tokens + **$0.08 per running session-hour**) or the OpenAI Agents API (beta) | No infrastructure, but no free tier beyond starter credits ([Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing)) |

❌ **Don't start new projects on:** the OpenAI **Assistants API** (shut down 2026-08-26), OpenAI **Agent Builder** (being discontinued), or **AutoGen / Semantic Kernel** (maintenance mode; the replacement is Microsoft Agent Framework) ([OpenAI changelog](https://developers.openai.com/api/docs/changelog), [Microsoft](https://github.com/microsoft/autogen)).

Every framework above supports **MCP** now, so MCP doesn't separate them.

### Minimal AI SDK v7 agent (TypeScript)

```ts
import { ToolLoopAgent, tool, isStepCount } from "ai";
import { z } from "zod";

const agent = new ToolLoopAgent({
  model: "anthropic/claude-sonnet-5",
  instructions: "You help users find books. Use tools; never invent titles.",
  tools: {
    searchBooks: tool({
      description: "Search the library catalogue by keyword. Returns up to 5 books.",
      inputSchema: z.object({ query: z.string() }),
      execute: async ({ query }) => searchCatalogue(query), // your code
    }),
  },
  stopWhen: isStepCount(8), // set it yourself (default is 20)
});

const result = await agent.generate({ prompt: "Books like Dune?" });
```

> v7 needs **Node 22+** and is **ESM-only** ([migration guide](https://ai-sdk.dev/docs/migration-guides/migration-guide-7-0)). Treat the code as a sketch and check the exact names against the current docs.

---

## 🔧 Designing tools the model can actually use

From [Anthropic: Writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) and [OpenAI function calling](https://developers.openai.com/api/docs/guides/function-calling):

| Do | Don't |
| --- | --- |
| **A few well-chosen tools** (OpenAI suggests fewer than 20 per turn) | Wrap every API endpoint as its own tool |
| Namespace names: `books_search`, `books_reserve` | `search`, `do_action` |
| Clear parameter names: `user_id`, `isbn` | `id`, `data` |
| Describe tools as if to a new teammate: what it does, when to use it, what it returns | One-word descriptions |
| Return **short, readable** output: names instead of UUIDs, paginate, truncate | Dump 50 KB of JSON (Claude Code caps tool output at 25k tokens) |
| **Actionable errors:** `"No book with ISBN 123. Try books_search first."` | `"Error 400"` |
| Turn on **strict mode** (`strict: true`) so arguments always match your schema | Loose schemas that let the model invent fields |
| Use enums so invalid values can't be sent | Free-text "mode" fields |

**Server-side tools** (web search, web fetch, code execution) run on the provider's side, so you write no execution code ([Anthropic tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)). They can add per-use charges on top of tokens.

---

## 🔌 MCP as agent tools

**MCP** (Model Context Protocol) lets you plug ready-made tool servers into your agent. Details are in [`../../05-tools-and-mcp/`](../../05-tools-and-mcp/README.md).

- **Current spec: 2026-07-28.** It's stateless: sessions and the `initialize` handshake are gone, and Tasks and MCP Apps are now extensions. Old servers still work with the v2 SDKs, and deprecated features keep working for at least 12 months ([MCP changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)).
- **Building a server?** Use **Python SDK v2** (`MCPServer`, stable; formerly `FastMCP`) or **TypeScript SDK v2** (`@modelcontextprotocol/server`, beta as of July; check it's stable) ([MCP blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/)).
- **Fastest path:** point the model API at a public **remote** MCP server:
  - Anthropic `mcp_toolset` (beta header `mcp-client-2025-11-20`; tools only; no local servers) ([docs](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector))
  - OpenAI `type: "mcp"` (asks for approval before every call by default) ([docs](https://developers.openai.com/api/docs/guides/tools-connectors-mcp))
- **In your own code:** AI SDK `@ai-sdk/mcp` `createMCPClient`, Mastra `@mastra/mcp`, or Pydantic AI's MCP support.

---

## 🛡️ Security: the lethal trifecta

> If your agent has **(1) access to private data**, **(2) reads untrusted content** (web pages, emails, uploaded files) **and (3) can send data out** (email, HTTP, posting), one hidden instruction can leak your data. **Never give one agent all three.** ([Simon Willison](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/))

- **Tool poisoning:** a malicious MCP server can hide instructions in its tool descriptions ([Invariant Labs](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)). Only install servers you trust, and read the launch command first ([MCP security](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)).
- **A human approves** writes, payments and anything sent on the user's behalf. Use AI SDK v7 `toolApproval`, OpenAI MCP `require_approval`, or shadcn's Human-in-the-Loop UI helpers.
- **Least privilege:** give the agent a read-only database role unless it really needs write access.
- **Memory tool:** block paths outside `/memories` (path traversal) ([Anthropic](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)).
- Full list: [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/).

**Computer and browser use** (the agent clicks around a real screen) is now GA from Anthropic (`computer_toolset_20260801`) and OpenAI. It's still slow and fragile, so treat it as a **stretch goal**, and use an API or MCP server whenever one exists. Run it in a sandbox or VM with a domain allowlist ([Anthropic](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)). Browserbase's free tier is 1 browser-hour with 15-minute sessions ([pricing](https://www.browserbase.com/pricing)).

---

## 🧯 Reliability rules

| Risk | What to do |
| --- | --- |
| **Runaway loop** | Always set the cap: AI SDK `stopWhen: isStepCount(n)` (default 20; `WorkflowAgent` has **no** limit) · OpenAI `max_turns` (default 10; catch `MaxTurnsExceeded` or add a `"max_turns"` error handler that returns a friendly message) · Anthropic tool runner `max_iterations` |
| **Rate limits (429/529)** | The official SDKs retry twice with backoff. A **spend-cap 429 never recovers**, so set a low spend cap as your budget kill-switch ([Anthropic errors](https://platform.claude.com/docs/en/api/errors)) |
| **Vercel timeout** | Hobby functions stop at **300 s, including streaming** (504) ([Vercel](https://vercel.com/docs/functions/limitations)). For long runs, split into steps or use **Vercel Workflows** (GA) |
| **Cost** | Put the long, unchanging parts (system prompt, tool list) first so they get **cached**. Cached reads cost about 0.1× (Anthropic 5-minute cache by default; OpenAI automatic) |
| **Random outputs** | **Don't set `temperature`.** Claude Opus 4.7+ and Sonnet 5 return **400** for non-default values, and temperature 0 "never guaranteed identical outputs" ([Anthropic](https://platform.claude.com/docs/en/models/opus-5/migration-guide)). GPT-6 with reasoning on also rejects it ([OpenAI](https://developers.openai.com/api/docs/guides/latest-model)) |
| **Long requests** | Always stream. The SDKs refuse non-streaming calls expected to run past 10 minutes |
| **Wrong tool arguments** | Strict mode + actionable error messages. The model reads the error and tries again |

### 🎬 Demo-proofing (because you can't make the model deterministic)

1. **Golden inputs:** pick 3 demo inputs and run each 5 times beforehand.
2. **`DEMO_MODE=true` fallback:** return cached or recorded responses if the API is slow or down.
3. **Seeded data:** a fixed demo database, not live data.
4. **Show progress:** stream text and show a card for each tool call, so the judge sees movement within a second.
5. **Record a backup video early.** Uploads can take hours ([Devpost](https://info.devpost.com/blog/how-to-present-a-successful-hackathon-demo)).
6. One flow, working **within about 90 seconds** ([JetBrains judges](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/)).

Prompt: [`../PROMPTS-ML.md`](../PROMPTS-ML.md) → ML7, ML14.

---

## 🧠 Memory ($0 options)

| Need | Use |
| --- | --- |
| Remember this conversation | Keep the message list in your own state or database. It's free and has no dependency |
| Python, OpenAI Agents SDK | `SQLiteSession` (don't combine it with server-managed conversations in the same run) ([docs](https://openai.github.io/openai-agents-python/running_agents/)) |
| Claude remembers across sessions | Anthropic **memory tool**: files under `/memories` stored where you choose ([docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)) |
| Hosted memory | Mem0 free tier (1k retrievals a month, which is enough for a demo) |

---

## 📊 See what your agent did (tracing and evals)

| Tool | Free tier | Note |
| --- | --- | --- |
| ⭐ **Langfuse** 🆓* | 50k units a month, 2 users, 30 days | Open source and self-hostable. Owned by ClickHouse since Jan 2026 and still OSS ([pricing](https://langfuse.com/pricing)) |
| LangSmith 🆓* | 5k traces a month, **1 seat**, 14 days | The single seat is awkward for teams |
| Braintrust 🆓* | 1 GB a month, unlimited users, 14 days | |
| ~~Helicone~~ | — | Maintenance mode since the Mintlify acquisition (2026-03). Don't start new projects on it |

**Evals in a weekend** ([Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), [Hamel Husain](https://hamel.dev/blog/posts/evals-faq/)):

- Write **20–50 test cases** from real failures you've seen.
- Grade **pass/fail** on the outcome, not on which tools were called.
- **Read at least 30 traces** yourself before trusting any automatic score.
- If you use an LLM as a judge, check it against about 20 of your own labels.
- Run each case more than once, because agents vary between runs.

---

## 🕰️ Don't use outdated patterns

| If a tutorial says… | Use instead |
| --- | --- |
| OpenAI Assistants API / threads | **Responses + Conversations API** (Assistants shut down 2026-08-26) |
| AI SDK `stepCountIs`, `system:`, `onFinish`, `fullStream`, `maxSteps` | **v7:** `isStepCount`, `instructions:`, `onEnd`, `stream`, `stopWhen` |
| AI SDK `needsApproval` on `tool()` | **`toolApproval`** setting (v7) |
| `temperature: 0` "for determinism" | Leave sampling parameters out; use a demo fallback cache |
| MCP `FastMCP`, `@modelcontextprotocol/sdk`, `Mcp-Session-Id`, HTTP+SSE | **MCP SDK v2** (`MCPServer`, `@modelcontextprotocol/server`), spec 2026-07-28 |
| `langchain-mcp-adapters` | LangChain **v1.4+ built-in `MCPAdapter`** |
| Claude `computer_20251124` | **`computer_toolset_20260801`** (Opus 5.5 rejects the old one) |
| AutoGen / Semantic Kernel | **Microsoft Agent Framework** |
| Helicone for tracing | **Langfuse** |

---

**Related:** [`model-selection.md`](model-selection.md) (which model) · [`prompt-engineering.md`](prompt-engineering.md) (instructions) · [`rag-architecture.md`](rag-architecture.md) (agent over your documents) · [`../../02-frontend/docs/`](../../02-frontend/README.md) (chat and tool-call UI) · cheat sheet [`../../skills/hackathon-ai/SKILL.md`](../../skills/hackathon-ai/SKILL.md)
