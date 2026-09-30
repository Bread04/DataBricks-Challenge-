# 🌐 MCP Ecosystem (Sep 2026): Spec, Registry, Plugins, Directories

<!-- markdownlint-disable MD013 -->

> What's changed in MCP and where to find servers you can trust. From the MCP & tools research run (2026-09-22); sources are in [`evidence.md`](evidence.md).

---

## The spec: 2026-07-28 is the current version

The biggest revision since launch (H):

- **Stateless core.** The `initialize` handshake and `Mcp-Session-Id` header are gone. State lives in explicit handles returned by tools, and list results can be cached (`ttlMs`, `cacheScope`).
- **Multi round-trip requests.** A server can return `resultType: "input_required"` to ask the user something mid-call.
- **Auth hardening.** RFC 9207 issuer validation is required, and clients move from Dynamic Client Registration to **Client ID Metadata Documents (CIMD)**.
- **Extensions framework:** Tasks, MCP Apps, Enterprise Managed Authorization.
- **Deprecated:** **Roots, Sampling, Logging** (removal after 12 months or more) and the **legacy HTTP+SSE transport**.
- Tier-1 SDKs (TypeScript, Python, Go, C#) are updated and backward-compatible; the Rust SDK is in beta.

The previous version, 2025-11-25, added URL-mode elicitation, CIMD (recommended), experimental tasks, icons and JSON Schema 2020-12.

**If you build an MCP server at the hackathon:** target 2026-07-28, keep it stateless, use Streamable HTTP rather than SSE, and don't rely on Sampling, Roots or Logging. See [`../PROMPTS.md`](../PROMPTS.md) T1–T2.

---

## Claude Code MCP features worth knowing

| Feature | Detail |
| --- | --- |
| **Tool search (deferred loading)** | **On by default.** Tools load only when needed, so many servers don't flood context. Disable with `ENABLE_TOOL_SEARCH=false` |
| Transports | `http` (recommended) · `stdio` (local) · SSE (**deprecated**) · WebSocket via `add-json` |
| Scopes | `local` (default) · `project` (`.mcp.json`, in git) · `user` |
| Project trust | `.mcp.json` servers connect only after the workspace trust dialog, but load **without a prompt** in `claude -p`, the Agent SDK and cloud sessions |
| Auth | OAuth via `/mcp` or `claude mcp login`; `headersHelper` script for dynamic headers (re-runs on 401/403) |
| Output | Warning at 10K tokens, cap 25K (`MAX_MCP_OUTPUT_TOKENS`); oversized results are saved to disk; long calls are auto-backgrounded after ~2 min |
| Timeouts | `MCP_TIMEOUT` (startup), `MCP_TOOL_TIMEOUT` |
| Import | `claude mcp add-from-claude-desktop` |

---

## Where to find servers, in order of trust

| # | Source | What it is | Trust | Cost |
| --- | --- | --- | --- | --- |
| 1 | **`claude-plugins-official`** (auto-added) + [claude.ai/directory](https://claude.ai/directory) | Anthropic-curated plugins that bundle MCP servers (github, supabase, vercel, sentry, linear, notion, figma, slack…) | Highest: reviewed against listing criteria (**not** security-audited) | 🆓 |
| 2 | `anthropics/claude-plugins-community` | Third-party plugins that passed automated screening, **pinned to a commit SHA** | Medium: Anthropic doesn't control the bundled MCP servers | 🆓 |
| 3 | [Official MCP Registry](https://registry.modelcontextprotocol.io) | Namespaced server metadata with an API; **in preview since 2025-09-08**; ~9.6K servers (third-party count, May 2026) | Metadata, **not a safety review** | 🆓 |
| 4 | Docker MCP Catalog | 300+ "verified" servers as container images (provenance, updates); Gateway is invite-only | Isolation helps with local servers | Pricing not found |
| 5 | Glama · Smithery · PulseMCP · mcp.so | Large third-party directories | **Discovery only.** Most listings are unmaintained or duplicates; one scan found SSRF issues in over a third of 8K+ servers (low confidence) | 🆓 |

**Rule:** prefer the **vendor's own server** (Supabase, Sentry, GitHub, Neon…) over community clones. The npm backdoor incident in [`mcp-security.md`](mcp-security.md) was a lookalike of an official server.

---

## Team setup through git

```jsonc
// .claude/settings.json (commit it)
{
  "extraKnownMarketplaces": { /* e.g. anthropics/claude-plugins-community */ },
  "enabledPlugins": { /* "supabase@claude-plugins-official": true */ }
}
```

- Commit `.mcp.json` with `${VAR}` placeholders, never literal keys.
- Since v2.1.195, plugins from external marketplaces still need each teammate to install them once.
- One-step add-and-install (v2.1.275+): `/plugin install <plugin> --marketplace owner/repo`.

## Other formats

- **MCPB (formerly DXT):** a one-click `.mcpb` bundle (a zip containing a local server and `manifest.json`) for **Claude Desktop**. Claude Code users just use `claude mcp add` or plugins.
