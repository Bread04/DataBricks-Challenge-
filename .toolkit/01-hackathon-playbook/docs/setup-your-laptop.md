# 💻 Set Up Your Laptop: A Step-by-Step Manual

<!-- markdownlint-disable MD013 -->

> **In plain English:** install the tools once, **the week before the event**, so the first hour of the hackathon goes on building, not installing. Follow the section for your computer, then do **"Check it all works"** at the end.
>
> **Time needed:** 20–40 minutes.

---

## What you're installing

| Tool | What it's for |
| --- | --- |
| **Node.js (LTS)** | Runs JavaScript apps like Next.js. Includes `npm` and `npx` |
| **Git** | Saves versions of your code and uploads them to GitHub |
| **VS Code** + extensions | The code editor (or Cursor, which is based on it), plus a few free add-ons ([below](#everyone-add-vs-code-extensions)) |
| **GitHub CLI** (`gh`) | Logs git into GitHub without passwords. Optional but easier |
| **Claude Code** (for BMad) | The AI coding assistant this toolkit's BMad workflow runs in. Installed in [`setup-bmad.md`](setup-bmad.md). No Claude Code? Pick a fallback from [`../../05-tools-and-mcp/docs/free-ai-dev-tools.md`](../../05-tools-and-mcp/docs/free-ai-dev-tools.md) |

---

## 🪟 Windows

**Step 1. Open PowerShell** (Start menu → type "PowerShell" → open it).

**Step 2. Install everything with one command each** (`winget` comes with Windows 10 and 11):

```powershell
winget install OpenJS.NodeJS.LTS
winget install Git.Git
winget install Microsoft.VisualStudioCode
winget install GitHub.cli
```

**Step 3. Close PowerShell and open a new window**, so it picks up the new tools.

**Step 4. Fix the "running scripts is disabled" error before you hit it:**

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Without this, commands like `npm` or `npx` can fail in PowerShell with *"cannot be loaded because running scripts is disabled on this system"*.

**Step 5. Put your projects in a plain folder, not OneDrive, Desktop or Documents.**

```powershell
mkdir C:\dev
cd C:\dev
```

⚠️ OneDrive tries to sync `node_modules` (tens of thousands of files). That makes installs slow and can lock files mid-build, causing random `EPERM` or `EBUSY` errors. If your Desktop or Documents folder syncs to OneDrive, keep code out of it.

**Windows tips:**

- **Git Bash** is installed with Git. Use it when a guide shows Mac/Linux commands (`export`, `cp`, `rm -rf`). Some tools, such as Claude Code hooks, expect bash ([`../../05-tools-and-mcp/docs/claude-code-power-tools.md`](../../05-tools-and-mcp/docs/claude-code-power-tools.md)).
- Setting an environment variable for one session: bash uses `export KEY=value`, PowerShell uses `$env:KEY="value"`.

---

## 🍎 Mac

**Step 1. Open Terminal** (Cmd + Space → type "Terminal").

**Step 2. Install Apple's developer tools** (this includes git):

```bash
xcode-select --install
```

**Step 3. Install Homebrew** by following the one-line command on [brew.sh](https://brew.sh), then:

```bash
brew install node gh
brew install --cask visual-studio-code
```

**Step 4. Make a projects folder:**

```bash
mkdir ~/dev && cd ~/dev
```

---

## 🐧 Linux

Install Node LTS with [nvm](https://github.com/nvm-sh/nvm) (avoids permission problems with the system package), and `git` and `gh` with your package manager.

---

## Everyone: connect git to GitHub

**Step 1. Tell git who you are** (this name and email show on your commits):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

**Step 2. Log in to GitHub:**

```bash
gh auth login
```

Choose **GitHub.com** → **HTTPS** → **Yes** (authenticate git) → **Login with a web browser**, then follow the prompts.

---

## Everyone: add VS Code extensions

Extensions are free add-ons from the **VS Code Marketplace**. To install one, open VS Code, press `Ctrl + Shift + X` (Mac: `Cmd + Shift + X`), search for the name, and click **Install**. Or paste the install command into a terminal.

> Only install extensions from **verified publishers** (blue tick) or ones listed here. Extensions can read your code and keys. All the IDs below were checked on the Marketplace on 2026-09-23, and each one had an update within the last year (dates in [`../../_research/technical-agents-and-fullstack-practices-2026-09-23/imports/vscode-extensions-2026-09-23.json`](../../_research/technical-agents-and-fullstack-practices-2026-09-23/imports/vscode-extensions-2026-09-23.json)).

### 🟢 Everyone installs these (5 minutes)

| Extension | What it does for you | ID |
| --- | --- | --- |
| **ESLint** | Underlines bugs and bad patterns in JavaScript/TypeScript as you type | `dbaeumer.vscode-eslint` |
| **Prettier** | Tidies your code's formatting on save, so the team's code looks the same | `esbenp.prettier-vscode` |
| **Tailwind CSS IntelliSense** | Autocompletes Tailwind classes and shows the colour | `bradlc.vscode-tailwindcss` |
| **Error Lens** | Shows the error message right on the broken line, not just a red squiggle | `usernamehw.errorlens` |
| **Pretty TypeScript Errors** | Turns unreadable TypeScript errors into plain, formatted ones | `yoavbls.pretty-ts-errors` |
| **GitLens** | Shows who changed each line and when, and makes merge conflicts easier | `eamodio.gitlens` |
| **Live Share** | A teammate joins your editor live, like Google Docs for code. Great for pairing on a bug | `ms-vsliveshare.vsliveshare` |

```bash
code --install-extension dbaeumer.vscode-eslint
code --install-extension esbenp.prettier-vscode
code --install-extension bradlc.vscode-tailwindcss
code --install-extension usernamehw.errorlens
code --install-extension yoavbls.pretty-ts-errors
code --install-extension eamodio.gitlens
code --install-extension ms-vsliveshare.vsliveshare
```

> `code` not found? In VS Code press `Ctrl + Shift + P` → type **"Shell Command: Install 'code' command in PATH"** (Mac), or reopen the terminal (Windows).

### 🤖 Your AI assistant (pick one)

| Extension | Cost | ID |
| --- | --- | --- |
| **Claude Code for VS Code**: runs this toolkit's BMad workflow ([`setup-bmad.md`](setup-bmad.md)) | 💳 needs a Claude plan or API key | `anthropic.claude-code` |
| **GitHub Copilot Chat** | 🆓* Copilot Free (2,000 completions a month); students get the Copilot Student plan ([details](../../05-tools-and-mcp/docs/free-ai-dev-tools.md)) | `github.copilot-chat` |
| **Gemini Code Assist** | 🆓* has an individual free tier (limits not checked in this guide's research) | `google.geminicodeassist` |
| **Cline** (open source, bring your own model key, including free ones) | 🆓 + your model's cost | `saoudrizwan.claude-dev` |

Other options and the $0 route: [`../../05-tools-and-mcp/docs/free-ai-dev-tools.md`](../../05-tools-and-mcp/docs/free-ai-dev-tools.md).

### 🟡 Add the ones for your project

| If your project uses… | Install | ID |
| --- | --- | --- |
| **Python / FastAPI** | Python + Pylance (autocomplete, debugging) | `ms-python.python`, `ms-python.vscode-pylance` |
| | Ruff (fast linting and formatting for Python) | `charliermarsh.ruff` |
| **Data / ML notebooks** | Jupyter (run `.ipynb` notebooks inside VS Code) | `ms-toolsai.jupyter` |
| **Testing** | Playwright Test (run and record browser tests) | `ms-playwright.playwright` |
| | Vitest (run unit tests from the sidebar) | `vitest.explorer` |
| **Prisma ORM** | Prisma (schema highlighting and formatting) | `prisma.prisma` |
| **Testing your API** | Thunder Client (send requests to your API, like Postman) | `rangav.vscode-thunder-client` |
| **Plain HTML/CSS pages** | Live Preview (a preview of your page that reloads itself) | `ms-vscode.live-server` |
| **Docker** | Container Tools (the replacement for the old "Docker" extension) | `ms-azuretools.vscode-containers` |
| **Accessibility** | axe Accessibility Linter (flags accessibility mistakes in your markup) | `deque-systems.vscode-axe-linter` |
| **Writing the README / pitch** | markdownlint + Markdown Preview Mermaid Support (clean docs, diagrams in preview) | `davidanson.vscode-markdownlint`, `bierner.markdown-mermaid` |
| | Code Spell Checker (catches typos in code and text before the judges do) | `streetsidesoftware.code-spell-checker` |

### Share the list with your team

Commit a `.vscode/extensions.json` file to your repo. When a teammate opens the project, VS Code offers to install everything on it:

```json
{
  "recommendations": [
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "bradlc.vscode-tailwindcss",
    "usernamehw.errorlens",
    "eamodio.gitlens",
    "ms-vsliveshare.vsliveshare"
  ]
}
```

Then turn on **format on save** so Prettier runs automatically: `Ctrl + ,` → search **"format on save"** → tick it.

### ❌ Skip these (popular, but not updated in years)

| Instead of… | Use | Why |
| --- | --- | --- |
| Git Graph | **GitLens** (or VS Code's built-in Source Control graph) | Last updated 2021 |
| REST Client | **Thunder Client** | Last updated 2022 |
| DotENV | Nothing. VS Code highlights `.env` files well enough | Last updated 2018 |
| Auto Rename Tag | Nothing. VS Code has this built in: `Ctrl + ,` → search **"linked editing"** → tick it | Last updated 2022 |
| Import Cost | Check bundle size with `npx next build` output | Last updated 2022 |
| Docker (`ms-azuretools.vscode-docker`) | **Container Tools** | Replaced by Microsoft |

> Using **Cursor**? It's based on VS Code, so most of these install the same way from its own extension panel. A few Microsoft-only extensions (such as Pylance and Live Share) may be missing there. Use whatever Cursor offers instead.

---

## ✅ Check it all works

Run each line. Every one should print a version number or "Logged in", not an error.

```bash
node -v          # v22 or newer
npm -v
git --version
gh auth status
```

**Final test: make and run a real app** (this also downloads packages into your cache, which helps on slow venue Wi-Fi):

```bash
npx create-next-app@latest test-app --yes
cd test-app
npm run dev
```

Open <http://localhost:3000>. If you see the Next.js page, you're ready. Press `Ctrl + C` to stop it, then delete the `test-app` folder.

---

## ✅ Accounts to create before the event

Tick these off using [`../first-hackathon.md`](../first-hackathon.md) → "Before the event": **GitHub**, **Vercel** (sign up *with* GitHub), **Supabase**, and your AI tool. Students: claim the [GitHub Student Pack](free-credits.md).

## Next: set up BMad

Your laptop is ready. Now install Claude Code and practise BMad once: [`setup-bmad.md`](setup-bmad.md) → Part A.

## Common setup errors

| Error | Fix |
| --- | --- |
| `'node'` / `'git'` is not recognized | Close **all** terminal windows and open a new one. Still broken? Restart the computer |
| `running scripts is disabled on this system` | Windows Step 4 above |
| `EACCES` permission error on `npm install -g` (Mac/Linux) | Don't use `sudo`. Reinstall Node with nvm or Homebrew |
| `EPERM` / `EBUSY` during install (Windows) | Move the project out of OneDrive (Windows Step 5) and close VS Code's other windows |
| `gh: command not found` right after install | Open a new terminal window |
