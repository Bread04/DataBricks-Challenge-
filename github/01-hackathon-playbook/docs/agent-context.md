# 🤖 Agent Context and the Agentic Workflow

<!-- markdownlint-disable MD013 -->

> How to set up Claude Code (or any agentic IDE) so each session starts with the right context, plus the phase loop for building with agents. Adapted from [help-me-papi](https://github.com/maxi-cmyk/help-me-papi) (`README.md`, `agents/README.md`).

---

## 1 · The agentic loop: chain macros, don't freestyle

| Phase | What happens | Use |
| --- | --- | --- |
| **Strategy** | Research, persona, idea | `../PROMPTS.md` C1–C3 |
| **Spec** | Write the plan and acceptance criteria **before** any code. Never let the agent start editing files from a one-line prompt | C4, `../templates/prd.md` |
| **Scaffold** | Feature-first scaffolding | C5, `../../02-frontend/PROMPTS.md`, `../../03-backend/PROMPTS.md` |
| **Verify** | Red → green → refactor where the stack allows: a failing test, then the smallest fix, then cleanup. It keeps agent code honest instead of "looks right, ships broken" | One Playwright demo test at minimum |
| **Polish** | UI clarity and UX heuristics pass | `/impeccable audit`, Frontend F10 |
| **Review** | Diff review, security check, test check **before merge**. Don't rely on "the agent said it's done" | `bmad-code-review` / `/code-review` |

---

## 2 · `CLAUDE.md` / `AGENTS.md`: the first file every agent reads

Keep one at the root of every hackathon repo. It holds the **hard-won, repo-specific context** a fresh session would otherwise have to rediscover.

### What belongs in it (each line should answer "would an agent likely get this wrong without help?")

- Exact commands: dev, build, single test, lint, typecheck, `supabase db reset`, deploy
- Required order when it matters (for example `lint → typecheck → test`)
- Architecture that isn't obvious from filenames: "features live in `features/<name>/`; services are server-only; proxy is NOT the auth boundary"
- Conventions that differ from defaults: "Clerk ids are text; use `auth.jwt()->>'sub'` in RLS"
- Env quirks: which keys are server-only, where `.env.example` lives
- **Pitfalls you've seen the agent make** (add them the moment they happen)
- Pointers to domain docs instead of copies: "UI rules: `../../02-frontend/docs/clarity-first-design.md`"

### What stays out

Generic advice, long tutorials, full file trees, anything speculative or unverified, and anything the agent can infer in seconds.

### Hackathon starter `CLAUDE.md`

```markdown
# <Project> — agent notes

## Commands
- dev: `npm run dev` · build: `npm run build` (run before every push)
- db: `supabase db reset` (re-seeds) · types: `supabase gen types typescript --local > types/db.ts`
- deploy: push to main (Vercel auto-deploy). Never deploy with failing build.

## Architecture
- Next.js 16: route protection in `proxy.ts` — but every Server Action re-checks auth.
- Feature-first: `features/<name>/{actions,service,types}.ts`. Services are `server-only`.
- Supabase + Clerk via Third-Party Auth (NOT the JWT template). RLS on every table.

## Rules
- Demo path first. Toasts, not crashes. Seed data for every feature.
- Tokens only (app/globals.css @theme); no raw hex/px.
- Log AI-generated files in AI_USAGE.md.

## Pitfalls seen
- (add as they happen)
```

### Generating or refreshing it

- **BMad:** `bmad-project-context` sets it up, refreshes it, and records observed mistakes as pitfall lines.
- **Plain prompt** (condensed from help-me-papi `agents/README.md`):

```text
Create or update AGENTS.md for this repo. Read README, manifests, lockfiles, build/test/lint config, CI, and any existing CLAUDE.md/AGENTS.md first; prefer executable sources over prose.
Include only high-signal, repo-specific facts: exact commands (incl. single-test), required command order, real entrypoints and boundaries, toolchain quirks (codegen, migrations, env loading), conventions that differ from defaults, testing prerequisites.
Exclude generic advice, tutorials, exhaustive trees, and anything you couldn't verify. If AGENTS.md exists, improve it in place. When in doubt, omit.
```

---

## 3 · Sub-agent delegation

- Split **independent workstreams** (for example "scaffold the API", "build the UI shell", "write the demo E2E test") across parallel sub-agents or separate sessions, then integrate.
- Only parallelise work that **doesn't share files**. Two agents editing the same component will fight each other. Feature-first folders make this split natural.
- Give each sub-agent the relevant docs (spec, `design.md`, the right domain `PROMPTS.md`), not the whole conversation.

---

## 4 · Skills over one-off prompts

If you use a workflow more than once (a debugging checklist, a design review, an install procedure), turn it into a **skill** instead of retyping the prompt. The `../../skills/*.md` files in this toolkit already have skill frontmatter; copy them to `~/.claude/skills/<name>/SKILL.md` to load them on demand.

---

## 5 · Token-saving tip: graphify

In larger repos, `graphify claude install` builds a knowledge graph and adds a hook, so Claude reads `graphify-out/GRAPH_REPORT.md` before grepping raw files. Run `/graphify` inside Claude Code to build it. (From help-me-papi `tools/good-to-know/graphify.md`. You already have the graphify skill installed.)
