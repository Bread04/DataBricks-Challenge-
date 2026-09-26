# 🗄️ Database Standards: Supabase / Postgres

<!-- markdownlint-disable MD013 -->

> Schema, RLS, migrations and free-tier facts. Verified 2026-09-21.

---

## Free tier (live pricing page, 2026-09-21)

| Limit | Free | Hackathon impact |
| --- | --- | --- |
| Active projects | 2 | One for dev, one for demo |
| Database | 500 MB (shared CPU, 500 MB RAM) | Plenty; don't store blobs in rows |
| **Inactivity pause** | **After 1 week** | ⚠️ Wake the project up before judging day |
| Auth MAU | 50,000 | — |
| File storage | 1 GB | Compress uploads |
| Egress | 5 GB + 5 GB cached | Watch for large media in the demo |
| Edge Function invocations | 500,000 | — |
| Realtime concurrent connections | 200 | — |
| Pro | from $25/mo | — |

Source: [supabase.com/pricing](https://supabase.com/pricing)

---

## Row Level Security standard

Rules ([Supabase RLS docs](https://supabase.com/docs/guides/database/postgres/row-level-security)):

1. **Enable RLS on every table in an exposed schema.**
2. **One policy per operation:** SELECT → `using`; INSERT → `with check`; UPDATE → both; DELETE → `using`.
3. Always scope with `to authenticated` (or another role).
4. Wrap functions as `(select auth.uid())` so they run once per statement, not once per row.
5. **Index every column a policy filters on.**
6. `auth.uid()` is `null` when unauthenticated, so policies fail closed.

### Template: Clerk user IDs (text)

```sql
create table tasks (
  id bigint generated always as identity primary key,
  name text not null,
  priority text not null default 'med' check (priority in ('low','med','high')),
  user_id text not null default auth.jwt()->>'sub',   -- Clerk IDs are text
  created_at timestamptz not null default now()
);
alter table tasks enable row level security;
create index on tasks (user_id);

create policy "tasks: select own" on tasks for select to authenticated
  using ((select auth.jwt()->>'sub') = user_id);
create policy "tasks: insert own" on tasks for insert to authenticated
  with check ((select auth.jwt()->>'sub') = user_id);
create policy "tasks: update own" on tasks for update to authenticated
  using ((select auth.jwt()->>'sub') = user_id)
  with check ((select auth.jwt()->>'sub') = user_id);
create policy "tasks: delete own" on tasks for delete to authenticated
  using ((select auth.jwt()->>'sub') = user_id);
```

With **Supabase Auth** instead of Clerk, use `user_id uuid default auth.uid()` and `(select auth.uid())`.

---

## ⚠️ Default grants: opt-in exposure is here

> [!IMPORTANT]
> **Dates confirmed (Deepen run, 2026-09-22):** new public-schema tables need an **explicit `GRANT`** before the Data API or GraphQL can see them. This became the default for **new projects on 2026-05-30** and is **enforced on all existing projects on 2026-10-30**. The temporary `auto_expose_new_tables` flag is removed that day ([Supabase changelog](https://supabase.com/changelog/45329-breaking-change-tables-not-exposed-to-data-and-graphql-api-automatically)). If a table returns `permission denied` from the client, a missing grant is the likely cause.

Older projects gave new `public` tables SELECT/INSERT/UPDATE/DELETE grants for `anon`, `authenticated` and `service_role` automatically ([Securing your API](https://supabase.com/docs/guides/api/securing-your-api)).

Adding policies **doesn't remove** existing grants. Opt in explicitly:

```sql
alter default privileges for role postgres in schema public
  revoke select, insert, update, delete on tables from anon, authenticated, service_role;

grant select, insert, update, delete on tasks to authenticated;
```

Also recommended: expose a dedicated `api` schema so the public surface is easy to audit.

---

## Migrations workflow (Supabase CLI)

From [Supabase: database migrations](https://supabase.com/docs/guides/deployment/database-migrations):

```bash
supabase login
supabase init && supabase start          # local stack (Docker)
supabase migration new add_tasks         # write SQL in supabase/migrations/
supabase db diff -f add_tasks            # capture dashboard changes as a migration
supabase db reset                        # reapply migrations + supabase/seed.sql locally
supabase link --project-ref <ref>
supabase db push                         # apply to remote
```

Rule: **never change the remote database directly.** Everything goes through migrations. Also available: `db pull`, `migration list`, `migration repair`.

> Type generation (`supabase gen types typescript --local > types/db.ts`) is commonly used, but its flag syntax wasn't verified in this research.

---

## Testing RLS (pgTAP)

Put tests in `supabase/tests/<table>_rls.test.sql`. For each table, test that the owner can read and write, another user can't, and an anonymous user can't.

---

## pgvector (for AI features)

Enable the `vector` extension under Dashboard → Database → Extensions. HNSW indexes and hybrid search are covered in `../../04-ai-and-rag/docs/rag-architecture.md`. Using the same Postgres for app data and embeddings means you don't need a separate vector database.

---

## Repos

| Repo | Why | Status |
| --- | --- | --- |
| [supabase/supabase](https://github.com/supabase/supabase) | Official `examples/` (Next.js, auth, pgvector) | ⭐ 110k · pushed 2026-09-21 |
| [supabase/cli](https://github.com/supabase/cli) | Local stack, migrations, types, functions | ⭐ 2.4k · pushed 2026-09-21 |
| [supabase/mcp](https://github.com/supabase/mcp) | Official MCP server (see Tools & MCP) | ⭐ 2.9k · pushed 2026-09-19 |
