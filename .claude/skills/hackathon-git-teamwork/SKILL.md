---
name: hackathon-git-teamwork
description: Git workflow for 2–4 person hackathon teams covering kickoff repo setup, secrets hygiene, folder ownership, the pull-branch-commit-push loop, resolving merge conflicts, and safe recovery commands. Use when setting up a team repo, resolving a merge conflict, recovering from a git mistake, or when the user asks how to work on code with teammates.
---

# Git Teamwork Runbook

<!-- markdownlint-disable MD013 -->

> Condensed rules. Full beginner walkthrough: `../../01-hackathon-playbook/docs/git-for-teams.md`.

## Rules for the assistant

1. **Never** `git push --force` to `main`, and never rewrite shared history, without the user explicitly asking.
2. Before any command that discards work (`git restore`, `git reset --hard`, `git clean`), **say what will be lost** and confirm.
3. When resolving conflicts, **keep both teammates' intent** where possible and explain what was kept. Run the build afterwards.
4. Commit small and often with clear messages. Some events (ETHGlobal) may disqualify a single giant commit or missing history.
5. Never commit `.env*` files. If a secret was committed, tell the user to **rotate it first**.

## Kickoff setup (one person)

```text
GitHub → New repo → Add README → .gitignore: Node → invite collaborators
```

`.gitignore` must include `.env`, `.env.local`, `.env*.local`, `node_modules/`. Commit `.env.example` with key **names** only; share values privately.

**Split ownership by folder** (e.g. `features/<name>/` per person). Same-file edits are the main source of conflicts.

## The loop

```bash
git switch main && git pull              # start fresh
git switch -c feat/<task>                # one branch per task
git add . && git commit -m "<what works now>"   # repeat often
git pull origin main                     # bring in teammates' work; resolve conflicts here
npm run build                            # never merge something that doesn't build
git push -u origin feat/<task>           # then open PR → merge; Vercel auto-deploys main
```

Two people, separate folders? It's fine to skip branches: `pull → commit → push` on `main`, always pulling first.

## Resolving a conflict

1. `git status` → files marked "both modified".
2. In each file, edit the `<<<<<<<` / `=======` / `>>>>>>>` block to the final version; delete all markers.
3. `npm run build` to check.
4. `git add . && git commit` → `git push`.
5. Bail out: `git merge --abort` returns to the pre-merge state.

## Recovery

| Situation | Command |
| --- | --- |
| Committed on `main` by mistake | `git switch -c <branch>` (commits come with you) |
| Undo last unpushed commit, keep changes | `git reset --soft HEAD~1` |
| Discard uncommitted changes to one file | `git restore <file>` ⚠️ irreversible |
| Switch branch mid-change | `git stash` → switch → `git stash pop` |
| Push rejected ("fetch first") | `git pull`, resolve, push again |
| Deployed site broke after merge | Vercel → Deployments → promote last good deploy |
| Secret pushed | Rotate key now; then remove from code |

## Team rules

Pull before you start and before you push · one owner per folder · `main` always builds (it's what judges see) · one person owns deployment and production env vars · freeze `main` ~3 h before the deadline.
