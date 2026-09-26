# 🔧 Tools & MCP Macros

<!-- markdownlint-disable MD013 -->

> Build your own MCP servers and CLIs when off-the-shelf tools aren't enough. This is useful for sponsor-API hackathons ("give the agent hands on our API") and for automating repetitive setup. Adapted from [help-me-papi](https://github.com/maxi-cmyk/help-me-papi) `tools/PROMPTS.md` and `tools/good-to-know/`.

---

## Contents

| Code | Macro | When |
| --- | --- | --- |
| [T1](#t1--scaffold-an-mcp-server) | Scaffold an MCP server | Sponsor API / internal data |
| [T2](#t2--expose-it-remotely) | Expose it remotely | Judges or other tools need it |
| [T3](#t3--automation-cli) | Automation CLI | Repeated setup tasks |
| [T4](#t4--test-the-tool) | Test the tool | Before relying on it |

---

## When to build an MCP server

If you keep copy-pasting data from a dashboard, a sponsor API, a proprietary database or a CMS into prompts, **wrap it in an MCP server**. An MCP server can expose three kinds of thing:

| Primitive | Example |
| --- | --- |
| **Resources** | Static context: "here is the sponsor's API schema" |
| **Tools** | Executable functions: "create a row in the dev DB", "call the sponsor API" |
| **Prompts** | Reusable prompt templates |

**Transports:** `stdio` for local development (easiest), or **Streamable HTTP** for remote servers. SSE is deprecated in Claude Code ([Claude Code MCP docs](https://code.claude.com/docs/en/mcp)).

**Hackathon angle:** "We built an MCP server for `<sponsor>`'s API, so any AI agent can use it" is a strong, sponsor-friendly demo. Keep the business logic in your backend and make the MCP server a **thin adapter** over it, as in help-me-papi's Epicenter lesson.

---

### T1 · Scaffold an MCP server

```text
[ROLE] MCP specialist. [CONTEXT] Data source / API: <docs or schema>. Stack: <TypeScript | Python>.
Build an MCP server with the official SDK (@modelcontextprotocol/sdk for TS, or the official Python SDK):
- 3–5 tools max, each with a precise description (when to use / when NOT to use) and strict input validation (zod / pydantic).
- Read-only tools first; any write tool requires an explicit confirm parameter.
- Errors returned as short, LLM-readable messages (what failed + how to fix), never stack traces.
- Transport: stdio for local dev.
Output: server code, the `claude mcp add <name> -- <command>` line, a .mcp.json snippet using ${VAR} for secrets, and 3 example prompts that exercise the tools.
```

### T2 · Expose it remotely

```text
Convert the MCP server to Streamable HTTP so judges/other clients can connect:
- Deploy on <Railway | Vercel>; HTTPS only.
- Auth via bearer token header (read from env), rejected with a clear error if missing.
- Keep business logic in our backend; the MCP layer only adapts.
- Verification checklist: tool discovery works, one read-only call succeeds from `claude mcp add --transport http <name> <url> --header "Authorization: Bearer $TOKEN"`.
```

### T3 · Automation CLI

```text
[ROLE] DevTools engineer. Automate: <repetitive task, e.g. reset DB + seed + create demo user + open URLs>.
Requirements:
- --help and --version; clear, colour-coded errors; correct exit codes.
- --dry-run for anything that mutates files, DBs or APIs (default to dry-run if destructive).
- Idempotent: running twice is safe or warns ("already done").
- Core logic in importable functions; CLI layer only parses args and prints.
- Python: argparse (simple) or Typer/Click (multi-command). Node: Commander.js.
Output the script + a sample invocation.
```

### T4 · Test the tool

```text
Test <CLI or MCP server>: empty/missing inputs, missing files, permission errors, network failure, running twice (idempotency), and — for MCP — a malicious-looking tool input (prompt-injection text inside data).
Output the test commands and a list of unhandled cases with fixes.
```

---

## Related

- MCP servers worth installing: `docs/mcp-setup.md`
- Security rules (prompt injection, read-only, scoping): `docs/mcp-setup.md` §5
- Knowledge-graph navigation for big repos: `graphify claude install` → `/graphify` (see `../01-hackathon-playbook/docs/agent-context.md`)
