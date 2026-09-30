# ⚡ Claude Code Power Tools

<!-- markdownlint-disable MD013 -->

Plugins, skills, hooks, subagents, worktrees, headless mode and GitHub Actions, set up for a 24–48 hour build. From the MCP & tools research run (2026-09-22; official code.claude.com docs); sources are in [`evidence.md`](evidence.md).

> [!IMPORTANT]
> **Cost: 💳/💰. There is no free route to Claude Code.** The Free plan doesn't include it. You need **Pro** ($20/month, or $17/month billed annually), Max, Team, or a **pay-as-you-go API key** (required for `--bare` and CI). Everything below is free to *add*, but runs inside paid Claude Code. $0 alternatives are in [`free-ai-dev-tools.md`](free-ai-dev-tools.md).

---

## 1 · Plugins (the fastest setup)

| Marketplace | Add | Install example |
| --- | --- | --- |
| **`claude-plugins-official`** (auto-added) | `/plugin marketplace add anthropics/claude-plugins-official` if it's missing | `/plugin install github@claude-plugins-official` |
| Community (screened, SHA-pinned) | `/plugin marketplace add anthropics/claude-plugins-community` | `<name>@claude-community` |
| Demo | `/plugin marketplace add anthropics/claude-code` | `/plugin install commit-commands@claude-code-plugins` |

The official marketplace includes:

- **LSP plugins** such as `typescript-lsp` and `pyright-lsp`. Install the language server itself separately.
- **Integrations** that bundle MCP servers: github, gitlab, linear, notion, figma, vercel, firebase, supabase, slack, sentry.
- **Other plugins:** `security-guidance`, `commit-commands`, `pr-review-toolkit`, `plugin-dev`.

**Team-wide install:** `claude plugin install typescript-lsp@claude-plugins-official --scope project` writes it into `.claude/settings.json`.

⚠️ Plugins run arbitrary code with your privileges, so install only ones you trust.

## 2 · Skills

- **Locations:** personal skills in `~/.claude/skills/<name>/SKILL.md`, project skills in `.claude/skills/<name>/SKILL.md`, plugin skills in `<plugin>/skills/…`.
- **Invoke** with `/<name>`.
- **Frontmatter:** `name`, `description`, `allowed-tools`, `disable-model-invocation`, `context: fork`.
- **Bundled skills:** `/run`, `/verify`, `/debug`, `/code-review`, `/batch`, `/loop`, `/doctor` (medium confidence).
- **Hackathon use:** put your deploy steps in `.claude/skills/deploy/SKILL.md` with `disable-model-invocation: true`, so they run only when you type `/deploy`. This toolkit's own `skills/` folder is already in this format.

## 3 · Hooks (guardrails that run automatically)

Add these to `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      { "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write" }] }
    ],
    "PreToolUse": [
      { "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/protect-files.sh" }] }
    ]
  }
}
```

- **Auto-format after every edit** needs `jq`.
- **Block edits to `.env`, lockfiles and `.git/`:** `protect-files.sh` reads the path with `jq -r '.tool_input.file_path // empty'`, prints the reason to stderr, and exits with code **2** to block the edit.
- **Other events:** `Notification` (desktop alert when Claude needs you) and `SessionStart` with the `compact` matcher (re-inject context after compaction).
- *Running tests on `Stop`* is a common pattern, but no official example was found.
- **On Windows**, hooks need bash with `jq` installed (Git Bash).

## 4 · Parallel work

| Tool | How |
| --- | --- |
| **Worktrees** | `claude --worktree api` in one terminal, `claude --worktree ui` in another. Each gets its own branch. The repo needs at least one commit |
| **Subagents** | Put `.claude/agents/<name>.md` with `name`, `description`, `tools`, `model` (sonnet/opus/haiku/inherit). `background: true` runs it alongside you; `isolation: worktree` gives it a sandboxed branch |
| **Plan mode** | `claude --permission-mode plan` or Shift+Tab, before big changes |
| **Resume** | `claude --continue` / `--resume` |

## 5 · Automation

| Tool | Command | Use |
| --- | --- | --- |
| **Headless** | `claude -p "Run the tests and fix failures" --allowedTools "Bash,Read,Edit"` | Scripted fix loops; `--output-format json` includes `total_cost_usd` |
| Structured output | `claude -p "…" --output-format json --json-schema schema.json` | Machine-readable results |
| **GitHub Actions** | `/install-github-app`, or `anthropics/claude-code-action@v1` | Comment `@claude implement this` on issues or PRs |
| Subscription auth for CI | `claude setup-token` → secret `CLAUDE_CODE_OAUTH_TOKEN` | Bills to one teammate's **Pro/Max** plan instead of the API |
| **`/loop`** | Poll inside the session | "Check the deploy every 5 minutes" |
| Routines | claude.ai/code/routines (cloud; cron, GitHub or API triggers) | Jobs that must run with your laptop closed |

---

## Free community add-ons (🆓 to add, run in paid Claude Code)

| Add-on | What it does | Evidence |
| --- | --- | --- |
| [obra/superpowers](https://github.com/obra/superpowers) | Agentic skills framework: plan before code, TDD, debugging methodology | Repo confirmed |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Persistent memory across sessions (compresses and re-injects past context) | Repo confirmed |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic's first-party skills (for example frontend-design) | Confirmed in the earlier research run |
| [Leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) · [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Design-quality skills | See `../../02-frontend/docs/` |
| affaan-m/ECC ("Everything Claude Code") | Agent harness with skills, memory and security scanning | Secondary source only |

More are listed in [`repos.md`](repos.md) under Claude Code skills & plugins.

## 15-minute hackathon setup

```bash
git init && git commit --allow-empty -m "init"                 # worktrees need a commit
/plugin install github@claude-plugins-official
claude plugin install typescript-lsp@claude-plugins-official --scope project
# add the two hooks above to .claude/settings.json (+ protect-files.sh, chmod +x)
claude setup-token   # one teammate on Pro: store as CLAUDE_CODE_OAUTH_TOKEN for GitHub Actions
```
