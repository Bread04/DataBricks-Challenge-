# Project context: [PROJECT NAME]

<!-- markdownlint-disable MD013 MD033 -->

<!--
Copy to <your-repo>/project-context.md and fill the <placeholders> at kickoff.
Almost every BMad skill loads this file automatically (default persistent_facts: **/project-context.md;
bmad-spec reads only the repo-root copy, so keep it at the root). This file is the hub that connects BMad to the toolkit.
Keep it under ~60 lines; point to toolkit docs instead of copying them.
-->

## Event

- Hackathon: <name> · Ends: <YYYY-MM-DD HH:MM TZ> · Team: <n> · Demo: <3-min live / video ≤2 min>
- Rubric (verbatim, with weights): <paste>
- Sponsor tech / prize tracks we target: <list>
- Rules: code written before the event <allowed?> · AI disclosure <required?> · video <length, name the event?>

## Hard constraints (apply to every workflow)

- Optimise for a working 3-minute demo, not production quality. Show it working within ~90 s.
- Stack is fixed: Next.js 16 (`proxy.ts`), Tailwind v4 + shadcn/ui, Supabase (RLS on), <Clerk via Third-Party Auth | Supabase Auth with getClaims()>, Vercel AI SDK, <model id, pinned>. Do not add frameworks.
- Speed mode: <⚡ JS + simple validators + {data}/{error} | 🛡️ TS + Zod + RFC 9457>. Use it consistently.
- Feature-first layout: `features/<name>/{actions,service,types}.ts`; services are server-only; every Server Action re-checks auth.
- Demo-safe: toasts not crashes; loading/empty/error states; seed data for every feature; mock slow or flaky APIs; `DEMO_MODE` fallback.
- Log every AI-generated file in `AI_USAGE.md`. Commit at the end of every story.
- UI: tokens only (`app/globals.css` @theme), one deliberate aesthetic from `docs/design.md`, WCAG 2.2 AA, no default "AI slop" tells.

## Where the rules live (toolkit vendored at `.toolkit/`)

- Strategy and timeline: `.toolkit/01-hackathon-playbook/battle-plan.md` · prompts: `.toolkit/01-hackathon-playbook/PROMPTS.md`
- Frontend: `.toolkit/skills/hackathon-frontend/SKILL.md` → details in `.toolkit/02-frontend/docs/`
- Backend: `.toolkit/skills/hackathon-backend/SKILL.md` → details in `.toolkit/03-backend/docs/`
- AI/RAG: `.toolkit/04-ai-and-rag/docs/` · Deploy: `.toolkit/skills/hackathon-deployment/SKILL.md`
- Libraries (use these first, avoid the avoid list): `.toolkit/06-repo-catalog/README.md`

## Project docs (docs-as-code)

- `docs/research.md` · `docs/prd.md` · `docs/tech-stack.md` · `docs/design.md` · `docs/pitch/`

## Commands

- dev `npm run dev` · build `npm run build` (before every push) · db `supabase db reset` · deploy: push to `main`

## Pitfalls seen (add as they happen, or via bmad-project-context record)

- (none yet)
