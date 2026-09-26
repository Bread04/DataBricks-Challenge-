# 🧭 Set Up BMad: A Step-by-Step Manual

<!-- markdownlint-disable MD013 -->

> **In plain English:** this toolkit runs your hackathon with the **BMad Method**, a free, open-source set of skills for Claude Code that walks you through each step: pick an idea → plan it → build it story by story → check it → pitch it. You type a command like `/bmad-spec`, and it asks the right questions and writes the right files.
>
> This page gets you ready in two parts: **Part A the week before** (about 45 minutes, once) and **Part B at kickoff** (10 minutes, in the new repo).
>
> **Do first:** [`setup-your-laptop.md`](setup-your-laptop.md) (Node, git, VS Code, GitHub login).

> [!NOTE]
> **Cost:** BMad is 🆓, but it runs inside **Claude Code, which is 💳 (Pro plan or higher) or 💰 (API key)**. No Claude Code? You can still follow every step using the copy-paste prompts in [`../PROMPTS.md`](../PROMPTS.md) with any AI tool, including free ones ([`../../05-tools-and-mcp/docs/free-ai-dev-tools.md`](../../05-tools-and-mcp/docs/free-ai-dev-tools.md)). Every step in this playbook lists its **fallback prompt**.

---

## How BMad works (2-minute version)

| Idea | What it means for you |
| --- | --- |
| **Skills are commands** | Type `/bmad-brainstorming`, `/bmad-spec`, `/bmad-build`… in Claude Code. Each one runs one job |
| **One skill per fresh chat** | Start a **new** Claude Code session for each skill. The files on disk carry the context, not the chat history |
| **Files are the memory** | Each skill writes a file the next one reads: idea → `SPEC.md` → `stories.yaml` → code |
| **`project-context.md` is the hub** | One file at your repo root with the event rules and your stack. Almost every BMad skill reads it automatically |
| **The config pack loads this toolkit** | `install.sh` wires the toolkit's rules (deploy, security, design, demo safety) into the BMad skills, so you don't paste them in |
| **Lost?** | Type `/bmad-help`. It looks at your files and tells you the next step |

The whole flow:

```text
CLARIFY  /bmad-brainstorming → /bmad-forge-idea → /bmad-party-mode (judges)
PLAN     /bmad-spec → "break this into stories"
BUILD    /bmad-build story 1, 2, 3… (fresh chat each) · /bmad-correct-course at halfway
HARDEN   /bmad-code-review · /bmad-qa-generate-e2e-tests
PITCH    /bmad-cis-storytelling · /bmad-party-mode (judges) · /bmad-review
LEARN    /bmad-retrospective
```

---

## Part A · The week before (once, ~45 minutes)

### A1. Install Claude Code

Follow the official install page: [code.claude.com/docs](https://code.claude.com/docs). The npm route works on every OS:

```bash
npm install -g @anthropic-ai/claude-code
```

Then, in any folder:

```bash
claude            # log in when prompted (Pro plan or API key)
```

Type `/exit` to leave.

### A2. Know the BMad installer

You don't install BMad globally. It goes **inside each hackathon repo** (Part B). Just check the installer runs:

```bash
npx bmad-method --help
```

> [!WARNING]
> **Don't rely on a BMad install in your home folder.** BMad finds the project by walking up the folder tree. If the hackathon repo has no `_bmad/` folder but your home folder does, every skill silently uses the home one and **ignores the toolkit's hackathon rules**. Always install inside the repo (Part B, step 3).

### A3. Rehearse on a throwaway repo (recommended, 20 minutes)

Do Part B once on a practice folder called `bmad-practice`. Run `/bmad-brainstorming` with a made-up theme and `/bmad-spec` on the result, so nothing is new on the night. Then delete the folder.

### A4. The rest of the pre-event list

Accounts, CLIs, MCP servers and design skills: [`../battle-plan.md`](../battle-plan.md) → "Days before". **Write no project code**: MLH bans code written before the event. Installing tools and rehearsing on a throwaway repo is fine.

---

## Part B · At kickoff, in the new repo (10 minutes)

One person (the **deployment owner**) does this, then everyone pulls.

### B1. Create the repo

Follow [`git-for-teams.md`](git-for-teams.md) → Part 1: create it on GitHub with a README and Node `.gitignore`, invite the team, and clone it.

### B2. Get a copy of this toolkit on your laptop

If you haven't already, download or clone this toolkit anywhere, for example `C:\dev\hackathon-toolkit` or `~/dev/hackathon-toolkit`.

### B3. Install BMad inside the repo

```bash
cd <your-repo>
npx bmad-method install
```

When asked, choose the **BMad Method** module plus **Creative Intelligence Suite** (for pitch storytelling). Skip the test and game modules unless you need them.

### B4. Install the toolkit's config pack

Run this from the repo. **On Windows, use Git Bash**, because it's a bash script:

```bash
bash <path-to-toolkit>/07-bmad-workflow/config-pack/install.sh . --dry-run   # preview
bash <path-to-toolkit>/07-bmad-workflow/config-pack/install.sh .             # apply
```

It never overwrites existing files. It adds:

| Added | What it's for |
| --- | --- |
| `project-context.md` | **The hub.** You fill it in next |
| `_bmad/custom/*.toml` | Loads the toolkit's rules into 16 BMad skills, adds review checks and a **judges panel** |
| `.toolkit/` | A copy of this toolkit that the skills read |
| `docs/research.md`, `prd.md`, `tech-stack.md`, `design.md` | Planning docs |
| `AI_USAGE.md` | Your AI disclosure log |
| `.claude/skills/hackathon-*` | The six cheat-sheet skills, for this project only |

### B5. Fill in the hub (5 minutes)

Open `project-context.md` and replace every `<placeholder>`: event name and deadline, the **rubric pasted word for word**, sponsor tracks, rules (prior code, AI disclosure, video), and your stack choices. Paste the theme, rubric and sponsor details into `docs/research.md` too.

### B6. Check it worked

```bash
uv run _bmad/scripts/resolve_customization.py --skill ~/.claude/skills/bmad-party-mode --project-root . --key workflow
```

The output should include `judges-panel`. No `uv`? Skip this and just check that `/bmad-party-mode` offers a **judges-panel** option in the next step.

### B7. Commit and start

```bash
git add . && git commit -m "Set up BMad and toolkit" && git push
```

Open Claude Code in the repo (`claude`) and run your first skill: `/bmad-brainstorming`. Next steps: [`../battle-plan.md`](../battle-plan.md) → H+0:15.

---

## If something's off

| Symptom | Fix |
| --- | --- |
| `No _bmad/ in …: run 'npx bmad-method install' there first` | Do B3 before B4 |
| No judges panel, and skills ignore hackathon rules | BMad is using a home-folder install. Make sure `_bmad/` exists **in the repo** and you started `claude` from the repo folder |
| `bash: command not found` (Windows) | Use Git Bash, not PowerShell, for `install.sh` |
| A skill mixes up earlier work | You reused a chat. Start a fresh session for every skill |
| Not sure what to run next | `/bmad-help` |

More detail on how the wiring works: [`../../07-bmad-workflow/README.md`](../../07-bmad-workflow/README.md).
