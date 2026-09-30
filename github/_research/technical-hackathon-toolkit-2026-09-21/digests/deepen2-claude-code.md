# Deepen 2: Claude Code features and community add-ons for a 24 to 48h hackathon

Decision: which Claude Code features and free community add-ons speed up a 24 to 48h hackathon the most (Sep 2026).
Method: 12 tool calls in one round (8 official doc fetches, 1 pricing fetch, 2 web searches, 1 write). Every source was accessed 2026-09-22. None of the code.claude.com pages showed a visible publish date, so they are dated "live docs, accessed 2026-09-22".
Classes: OFF = official vendor documentation. VEND = vendor pricing or marketing page. REPO = the GitHub repo page itself, taken from its search-result title. SEC = secondary source (blog or aggregator summary).

## Findings

1. The official Anthropic plugin marketplace is `claude-plugins-official`. Claude Code adds it automatically on the first interactive start. If that fails, add it with `/plugin marketplace add anthropics/claude-plugins-official`. Install a plugin with `/plugin install <name>@claude-plugins-official`, e.g. `/plugin install github@claude-plugins-official`. The catalog is at claude.com/plugins. | https://code.claude.com/docs/en/discover-plugins | Anthropic | live docs | accessed 2026-09-22 | high | OFF
2. The official marketplace covers LSP code-intelligence plugins (e.g. `typescript-lsp`, `pyright-lsp`; you install the language-server binary yourself), MCP integrations (`github`, `gitlab`, `linear`, `notion`, `figma`, `vercel`, `firebase`, `supabase`, `slack`, `sentry`), `security-guidance`, workflow plugins (`commit-commands`, `pr-review-toolkit`, `plugin-dev`) and output styles. | https://code.claude.com/docs/en/discover-plugins | Anthropic | live docs | accessed 2026-09-22 | high | OFF
3. Two more Anthropic marketplaces exist and must be added by hand. The community one is `/plugin marketplace add anthropics/claude-plugins-community` (install as `@claude-community`; plugins pass automated screening and are pinned to a commit SHA). The demo one is `/plugin marketplace add anthropics/claude-code` (named `claude-code-plugins`). Plugin skills are namespaced, e.g. `/commit-commands:commit`. | https://code.claude.com/docs/en/discover-plugins | Anthropic | live docs | accessed 2026-09-22 | high | OFF
4. Shell (non-interactive) plugin commands are `claude plugin install <plugin>@<marketplace> [--scope project]` and `claude plugin marketplace add ...`. Project scope writes the plugin into `.claude/settings.json`, so the whole team shares it. The docs warn that plugins run arbitrary code with your user privileges. | https://code.claude.com/docs/en/discover-plugins | Anthropic | live docs | accessed 2026-09-22 | high | OFF
5. Skill locations: personal `~/.claude/skills/<name>/SKILL.md`, project `.claude/skills/<name>/SKILL.md`, nested `<subdir>/.claude/skills/...`, plugin `<plugin>/skills/<name>/SKILL.md` (invoked as `/plugin:skill`). You invoke a skill with `/<dir-name>`. Frontmatter includes `name`, `description`, `disable-model-invocation`, `allowed-tools` and `context: fork`. | https://code.claude.com/docs/en/skills | Anthropic | live docs | accessed 2026-09-22 | high | OFF
6. Bundled skills include `/run`, `/verify`, `/debug`, `/code-review`, `/batch`, `/loop` and `/doctor`. (This list comes from the fetch tool's summary of the page.) | https://code.claude.com/docs/en/skills | Anthropic | live docs | accessed 2026-09-22 | medium | OFF
7. Hook: auto-format after edits. Use `PostToolUse` with matcher `Edit|Write` and command `jq -r '.tool_input.file_path' \| xargs npx prettier --write`, placed in project `.claude/settings.json`. It needs `jq`. | https://code.claude.com/docs/en/hooks-guide | Anthropic | live docs | accessed 2026-09-22 | high | OFF
8. Hook: block edits to protected files (`.env`, `package-lock.json`, `.git/`). Use `PreToolUse` with matcher `Edit\|Write` calling `"$CLAUDE_PROJECT_DIR"/.claude/hooks/protect-files.sh`. The script exits with code 2 to block the edit and gives Claude the stderr text as the reason. Other events on the page: `Notification` (desktop alert when Claude needs input, in `~/.claude/settings.json`), `SessionStart` with a `compact` matcher (re-injects context after compaction), `ConfigChange`. There are also prompt-based and agent-based hooks. | https://code.claude.com/docs/en/hooks-guide | Anthropic | live docs | accessed 2026-09-22 | high | OFF
9. Subagents live in `.claude/agents/` (project) or `~/.claude/agents/` (user), or come from the `--agents` CLI flag. Frontmatter: `name`, `description`, `tools`, `model` (sonnet/opus/haiku/inherit). `background: true` makes an agent run alongside you. `isolation: worktree` runs it in a temporary git worktree. As of v2.1.198, `/agents` no longer opens a wizard; you ask Claude to write the file or edit it yourself. | https://code.claude.com/docs/en/sub-agents | Anthropic | live docs | accessed 2026-09-22 | high (medium on wording; this is a fetch summary) | OFF
10. For parallel sessions, `claude --worktree <name>` gives each terminal its own worktree and branch. The repo needs at least one commit first. Plan mode is `claude --permission-mode plan` or Shift+Tab. Resume with `claude --continue` or `--resume`. Delegation example: "use a subagent to investigate ...". | https://code.claude.com/docs/en/common-workflows | Anthropic | live docs | accessed 2026-09-22 | high | OFF
11. Scheduling options: Routines (cloud, cron or GitHub or API triggers, set up at claude.ai/code/routines), Desktop scheduled tasks (run locally), GitHub Actions, and `/loop` (polls inside the current CLI session). | https://code.claude.com/docs/en/common-workflows | Anthropic | live docs | accessed 2026-09-22 | high | OFF
12. Headless mode: `claude -p "<prompt>" --allowedTools "Read,Edit,Bash"`. Output formats are `--output-format text\|json\|stream-json`, and `--json-schema` returns structured output. Other flags: `--permission-mode auto\|acceptEdits\|dontAsk` and `--permission-prompts none` (v2.1.259+). `--bare` is recommended for CI, but it needs `ANTHROPIC_API_KEY` and does not use your subscription login. The JSON output includes `total_cost_usd`. Background subagents keep `-p` open for up to a 10-minute idle ceiling. | https://code.claude.com/docs/en/headless | Anthropic | live docs | accessed 2026-09-22 | high | OFF
13. GitHub Actions: run `/install-github-app` for quick setup (needs `gh auth login` and repo admin rights), or install manually with `anthropics/claude-code-action@v1`. Auth is either `ANTHROPIC_API_KEY` or `CLAUDE_CODE_OAUTH_TOKEN`. The OAuth token comes from `claude setup-token`, works on Pro, Max, Team and Enterprise, and bills runs to the subscription instead of the API. Mentioning `@claude` in an issue or PR triggers interactive mode. | https://code.claude.com/docs/en/github-actions | Anthropic | live docs | accessed 2026-09-22 | high | OFF
14. Claude Code is not included on the Free plan. It is included on Pro ($17/mo billed annually, $20/mo monthly), Max 5x and Max 20x (from $100/mo), and Team. | https://claude.com/pricing | Anthropic | live page | accessed 2026-09-22 | high (fetch summary) | VEND
15. Pay-as-you-go API use is also possible: an API key from platform.claude.com, which `--bare` and CI runs require. | https://code.claude.com/docs/en/headless ; https://code.claude.com/docs/en/github-actions | Anthropic | live docs | accessed 2026-09-22 | high | OFF
16. obra/superpowers exists. Its repo title reads "An agentic skills framework & software development methodology that works." One blog puts it at about 270K stars and says it forces planning before coding and enforces TDD. Related repos: obra/superpowers-lab, obra/superpowers-skills. | https://github.com/obra/superpowers/ ; https://growthwithalex.substack.com/p/56-github-repos-that-pair-with-claude | obra (Jesse Vincent) / Substack | n.d. | accessed 2026-09-22 | high on existence, low on star count | REPO/SEC
17. thedotmack/claude-mem exists. Its repo title reads "Persistent Context Across Sessions for Every Agent". It captures session activity, compresses it with AI and re-injects it in later sessions. It works with Claude Code, Codex, Gemini, Copilot, OpenCode and others. | https://github.com/thedotmack/claude-mem | thedotmack | n.d. | accessed 2026-09-22 | high | REPO
18. anthropics/skills is described as Anthropic's official first-party skills collection and the reference for building your own. I did not fetch the repo page. | https://growthwithalex.substack.com/p/56-github-repos-that-pair-with-claude | Substack (secondary) | n.d. | accessed 2026-09-22 | medium | SEC
19. Everything Claude Code (ECC), at affaan-m/ECC per the search summary, is described as a "full agent harness bundling skills, memory, and security scanning". I did not fetch the repo page, and the exact slug may be `affaan-m/everything-claude-code`. | https://growthwithalex.substack.com/p/56-github-repos-that-pair-with-claude | Substack (secondary) | n.d. | accessed 2026-09-22 | low to medium | SEC

## Hackathon playbook (derived from the findings)

Cost tag: all of Claude Code is 💳, needing Pro at $20/mo or more, or 💰 API pay-as-you-go (F14, F15). There is no 🆓 route to Claude Code itself. The add-ons below are 🆓 open-source, but they only run inside paid Claude Code (🆓*).

**Hour 0: setup (about 15 min)**
- One teammate on Pro can cover the team's GitHub Actions through a subscription OAuth token (F13). Run `claude setup-token` and store the result as the `CLAUDE_CODE_OAUTH_TOKEN` secret.
- Make an initial commit right away. `--worktree` fails in a repo with no commits (F10).
- Install LSP and integration plugins with project scope so the whole team gets them (F2, F4):
  ```
  claude plugin install typescript-lsp@claude-plugins-official --scope project
  /plugin install github@claude-plugins-official
  /plugin install commit-commands@claude-code-plugins   # after: /plugin marketplace add anthropics/claude-code
  ```
  Install the language-server binary yourself, e.g. `typescript-language-server` (F2). `vercel`, `supabase` and `firebase` are also in the official marketplace if your stack uses them (F2).
- Optional: add `obra/superpowers` (F16) or `thedotmack/claude-mem` (F17) by following the install steps in each repo's README. I did not verify those steps this run.

**Guardrails in `.claude/settings.json` (F7, F8)**
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
`protect-files.sh` reads stdin JSON and gets the path with `jq -r '.tool_input.file_path // empty'`. It loops over patterns such as `.env`, `package-lock.json` and `.git/`, prints the reason to stderr and runs `exit 2` to block the edit. Mark it executable with `chmod +x`. This is how you stop a leaked `.env` during a rushed demo. On Windows the hook needs a bash with `jq` installed (inferred; the docs' examples are bash).

Tests-on-Stop: the docs list `Stop` as a hook event, but I did not retrieve an official Stop example this run. Treat "run tests on Stop" as an unverified pattern.

**Parallel build (F9, F10)**
- Give each person or workstream its own worktree: `claude --worktree api` in one terminal, `claude --worktree ui` in another.
- Keep throwaway research off the main context. Put an agent in `.claude/agents/researcher.md` with `tools: Read, Glob, Grep`, `model: sonnet`, `background: true`. For risky experiments, use `isolation: worktree`.
- Before large refactors, use plan mode (`claude --permission-mode plan` or Shift+Tab).

**Automation (F11, F12, F13)**
- Scripted review or lint: `git diff main | claude -p "you are a typo linter..."`. Structured output: `claude -p "..." --output-format json | jq -r '.result'`.
- Unattended fix loop: `claude -p "Run the test suite and fix any failures" --allowedTools "Bash,Read,Edit"`.
- In the repo, run `/install-github-app`, then assign work by commenting `@claude implement this feature based on the issue description` on issues.
- Use `/loop` to poll during the session (e.g. check the deploy every N minutes). Use Routines only for jobs that must run with your laptop closed.

**Custom skills (F5)**: put repeated demo or deploy steps in `.claude/skills/deploy/SKILL.md` with `disable-model-invocation: true` so it only runs when you call `/deploy`.

## Repo slugs
- anthropics/claude-plugins-official (official marketplace, F1)
- anthropics/claude-plugins-community (community marketplace, F3)
- anthropics/claude-code (demo marketplace `claude-code-plugins`, F3)
- anthropics/claude-code-action (GitHub Action, F13)
- obra/superpowers, obra/superpowers-skills, obra/superpowers-lab (F16)
- thedotmack/claude-mem (F17)
- anthropics/skills (F18, secondary evidence only)
- affaan-m/ECC (F19; slug unconfirmed, possibly affaan-m/everything-claude-code)

## Not found / unverified
- **ui-ux-pro-max-skill**: not found by the search. Existence, owner and slug unverified.
- **graphify**: not found by the search. Unverified as a public repo.
- **rtk** (reported as a token-reducing CLI): not found by the search. Unverified.
- **awesome-claude-code lists** (e.g. hesreallyhim/awesome-claude-code): not returned by the search. Unverified this run.
- **anthropics/skills and the ECC repo pages** were not fetched directly. Their descriptions come only from a secondary summary.
- **Official `Stop` hook example** (e.g. run tests before Claude finishes): not retrieved. The hooks reference at https://code.claude.com/docs/en/hooks is the next thing to fetch.
- **A free route to Claude Code**: no evidence of one. The pricing page marks Claude Code "No" on the Free plan. I did not check whether any hackathon or startup credit programs exist.
- **Publish dates** for the docs pages were not shown.
