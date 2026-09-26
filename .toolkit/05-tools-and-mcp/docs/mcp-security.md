# 🛡️ MCP Security for Hackathon Teams

<!-- markdownlint-disable MD013 -->

> MCP servers run with **your** privileges and feed text straight into the model. This covers the real incidents, the official guidance and a 10-point checklist. From the MCP & tools research run (2026-09-22); sources are in [`evidence.md`](evidence.md).

---

## Real attacks (not theoretical)

| Attack | What happened | Lesson |
| --- | --- | --- |
| **Tool poisoning** (Invariant Labs, Apr 2025) | Hidden instructions in a tool's *description*, which the model reads and you don't, caused it to exfiltrate SSH keys and config files | Read tool descriptions; scan servers |
| **Rug pull** | A server changes its tool descriptions **after** you approved it | Pin versions; re-scan on updates |
| **Shadowing** | One server's descriptions change how the agent uses a *different*, trusted server | Don't mix unknown servers with trusted ones |
| **GitHub "toxic agent flow"** (May 2025) | A malicious public issue prompt-injected the agent, which then leaked **private-repo** data using the same token. No server bug was needed | Don't give one session both untrusted input and private access |
| **postmark-mcp npm backdoor** (Sep 2025) | A lookalike of Postmark's official server. Versions 1–15 were clean, then **v1.0.16 silently BCC'd every email** to an attacker (~1.6K downloads) | Check the publisher is the real vendor; pin versions |
| **2026 supply-chain wave** | A malicious Cline plugin, hijacked axios, poisoned LiteLLM, and a worm across 160+ TanStack packages (search-summary evidence) | Your MCP server's dependencies can be compromised too |

---

## Official guidance, briefly

- **MCP spec (Security Best Practices):**
  - Servers **must not** accept tokens not issued for them (no token passthrough).
  - OAuth proxies must get consent per client.
  - Clients must show the exact local startup command and **should sandbox** local servers.
  - Request **minimal scopes** (no `admin:*`).
- **Claude Code:**
  - Manual mode starts read-only and asks before edits and risky Bash.
  - `/sandbox` isolates Bash's filesystem and network access.
  - New MCP servers need trust approval, **except under `claude -p`**.
  - Anthropic reviews Directory connectors but **"does not security-audit or manage any MCP server."**
  - Its advice is to write your own servers, or use servers from providers you trust.
- **GitHub MCP:**
  - `--read-only` / `GITHUB_READ_ONLY=1`, and `/readonly` toolset URLs.
  - **Lockdown mode** limits public-repo content to authors with push access, which reduces prompt-injection risk.
  - ⚠️ Open issue #2156: `--read-only` may not restrict write tools on the new HTTP command, so test it.

---

## ✅ The 10-point checklist

1. **Allowlist a handful of servers:** vendor-official, from `claude-plugins-official`, or your own. Never install lookalike npm packages; check the publisher.
2. **Pin exact versions** (`npx -y pkg@1.2.3`) in `.mcp.json`, not `@latest`. Rug pulls and version-16 backdoors both rely on auto-updates.
3. **Scan before first use and after every change:**

   ```bash
   SNYK_TOKEN=<token> uvx snyk-agent-scan@latest
   ```

   This is Snyk Agent Scan, formerly `mcp-scan`. It needs a Snyk account token and **sends tool descriptions and configs (secrets redacted) to Snyk**. Its free-tier status wasn't confirmed, so the cost is 🆓*. An open-source alternative is `eSentire-Labs/mcp-scanner` (unverified).
4. **Least-privilege tokens:** a fine-grained GitHub PAT for the hackathon repo only, short expiry. Use a **separate dev account**, not your work account.
5. **Read-only by default:** Supabase `read_only=true`; GitHub `--read-only` plus lockdown mode for public repos.
6. **Separate trust zones:** a server that reads **untrusted content** (web, public issues, email) and a server with **private data or write access** don't share a session. Use `--strict-mcp-config` to load an explicit set.
7. **Keep a human in the loop:** Manual mode with third-party servers. Put write tools in `permissions.deny`/`ask` (`mcp__<server>__<tool>`). No `bypassPermissions`.
8. **Sandbox:** `/sandbox`, a dev container or a VM, especially for local stdio servers.
9. **Review `.mcp.json` like code** in PRs. Remember that CI and `claude -p` load it without asking. Reset approvals with `claude mcp reset-project-choices`.
10. **No secrets in the repo.** Use `${VAR}` placeholders, and **rotate every token after the event**, or immediately if a package turns out to be compromised.

Related: the security section of [`mcp-setup.md`](mcp-setup.md) and [`../../03-backend/docs/security.md`](../../03-backend/docs/security.md).
