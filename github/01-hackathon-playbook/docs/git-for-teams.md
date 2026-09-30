# 🤝 Git for Teams: A Step-by-Step Manual

<!-- markdownlint-disable MD013 -->

> **In plain English:** how 2–4 people can work on the same code at the same time without overwriting each other. Follow the steps in order. New words (commit, branch, PR) are in [`../../GLOSSARY.md`](../../GLOSSARY.md) → "Code and teamwork".
>
> **Time needed:** 15 minutes to set up at kickoff, then a few seconds per save.

---

## Part 1 · Set up once, at kickoff (one person does this)

**Step 1. Create the repo on GitHub.**
GitHub → **New repository** → name it → tick **Add a README** → choose the **Node** `.gitignore` → **Create**.

**Step 2. Invite your team.**
Repo → **Settings** → **Collaborators** → **Add people**. Each teammate accepts the email invite.

**Step 3. Make sure secrets can never be uploaded.**
Open `.gitignore` and check that these lines are in it. Add any that are missing:

```text
.env
.env.local
.env*.local
node_modules/
```

**Step 4. Share the secrets another way.**
Create `.env.example` with the **names** of every key and no values, and commit it. Send the real values to teammates in a private message, **never** in the repo.

**Step 5. Split the work by folder.**
Agree who owns which folder, for example Alex owns `features/upload/` and Sam owns `features/results/`. Two people editing the same file at the same time is the #1 cause of merge conflicts. See [`project-structure.md`](project-structure.md) for a feature-first layout that makes this easy.

## Part 2 · Everyone: get the code (once)

```bash
git clone https://github.com/<team>/<repo>.git
cd <repo>
npm install
cp .env.example .env.local    # then paste in the real values you were sent
```

> **On Windows?** Run these in **Git Bash** or PowerShell. See [`setup-your-laptop.md`](setup-your-laptop.md) if `git` isn't recognised.

## Part 3 · The loop you repeat all event

Do this for **every** small piece of work (about 30–90 minutes each):

**Step 1. Start from the latest code.**

```bash
git switch main
git pull
```

**Step 2. Make a branch for your task.**

```bash
git switch -c feat/upload-button     # name = what you're building
```

**Step 3. Build it. Save often.**

```bash
git add .
git commit -m "Add upload button to home page"
```

Commit every time something works. Small commits are easy to undo, and some events (ETHGlobal) check that your history isn't one giant commit ([`../battle-plan.md`](../battle-plan.md)).

**Step 4. Bring in your teammates' changes before you share yours.**

```bash
git pull origin main
```

If git says **CONFLICT**, go to Part 4. Otherwise, continue.

**Step 5. Upload and merge.**

```bash
git push -u origin feat/upload-button
```

Open the link git prints (or GitHub → **Compare & pull request**) → **Create pull request** → **Merge**. If Vercel is connected, main auto-deploys (see [`../../03-backend/docs/deploy-step-by-step.md`](../../03-backend/docs/deploy-step-by-step.md)).

**Step 6. Tell the team.** Post "merged upload button" in your team chat so everyone pulls.

> **Hackathon shortcut:** with 2 people who own separate folders, you can skip branches and PRs and just run `git pull` → `git commit` → `git push` on `main`. Always pull before you push. Switch to branches as soon as you start clashing.

## Part 4 · Fixing a merge conflict

A conflict means you and a teammate changed the **same lines**. Git doesn't guess, so it asks you.

**Step 1. Find the conflicted files.**

```bash
git status        # look for "both modified"
```

**Step 2. Open each file.** You'll see blocks like this:

```text
<<<<<<< HEAD
<h1>Welcome to ShelfLife</h1>          ← your version
=======
<h1>ShelfLife: cook before it spoils</h1>   ← their version
>>>>>>> main
```

**Step 3. Edit it to the version you want.** Keep one version, or combine them. **Delete all three marker lines** (`<<<<<<<`, `=======`, `>>>>>>>`). VS Code shows **Accept Current / Accept Incoming / Accept Both** buttons above each block, which does this for you.

**Step 4. Check that it still runs.**

```bash
npm run build
```

**Step 5. Finish the merge.**

```bash
git add .
git commit -m "Merge main into feat/upload-button"
git push
```

**Stuck or panicking?** Run `git merge --abort` to go back to how things were before the pull, then ask the teammate who wrote the other version to sit with you. You can also paste the conflicted file into your AI assistant and ask: *"Resolve this merge conflict. Keep both features working and explain what you kept."*

## Part 5 · "Oh no" fixes

| Problem | Fix |
| --- | --- |
| I committed to `main` by accident | `git switch -c my-branch`: your commits move with you to the new branch |
| I want to undo my last commit (not yet pushed) | `git reset --soft HEAD~1`: the changes stay in your files, the commit is gone |
| I want to throw away my uncommitted changes to one file | `git restore <file>` ⚠️ this can't be undone |
| I need to switch branches but I'm mid-change | `git stash`, switch, then `git stash pop` to get the changes back |
| **I pushed an API key** | **Rotate the key immediately** in the provider's dashboard. Deleting the commit isn't enough, because the key is already public. See [`../../03-backend/docs/security.md`](../../03-backend/docs/security.md) |
| `rejected … fetch first` when pushing | Someone pushed before you. Run `git pull`, fix any conflicts, then push again |
| The deployed site broke after a merge | Vercel → **Deployments** → promote the last working one, then fix calmly |

## Part 6 · Team rules (agree on these at kickoff)

1. **Pull before you start, pull before you push.**
2. **One owner per folder.** Ask before editing someone else's.
3. **Never push broken code to `main`.** Run `npm run build` first. `main` is what the judges see.
4. **One person owns deployment** and the production env vars.
5. **Freeze `main` about 3 hours before the deadline.** Only demo-path fixes after that.
