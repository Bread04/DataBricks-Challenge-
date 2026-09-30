# 🔐 Auth Standards: Clerk (+ Supabase)

<!-- markdownlint-disable MD013 -->

The **current** Clerk + Supabase integration and Next.js 16 setup. Verified 2026-09-21.

> [!WARNING]
> **Don't follow older tutorials.**
>
> 1. The Clerk "Supabase JWT template" has been **deprecated since 1 April 2025**. It meant sharing your Supabase JWT secret, and rotating that secret caused downtime. Both vendors say so ([Supabase](https://supabase.com/docs/guides/auth/third-party/clerk), [Clerk](https://clerk.com/docs/guides/development/integrations/databases/supabase)).
> 2. **Next.js 16 renamed `middleware.ts` to `proxy.ts`** ([Next.js](https://nextjs.org/docs/app/guides/backend-for-frontend), [Clerk quickstart](https://clerk.com/docs/nextjs/getting-started/quickstart)).

---

## Free tier (live pricing, 2026-09-21)

| Hobby plan | Value |
| --- | --- |
| Users | **50,000 MRU** per app (monthly *retained* users, not MAU) |
| Apps | Unlimited |
| Dashboard seats | 3 |
| Prebuilt UI | Sign-in, sign-up, user profile |
| Organizations | 100 MROs per app |
| Session lifetime | **Fixed 7 days**, so re-log the demo account before judging |
| Logs | 1-day retention |
| Pro | $25/mo ($20/mo billed annually) |

Source: [clerk.com/pricing](https://clerk.com/pricing)

---

## Setup: Next.js 16

```bash
npx -y clerk@latest init     # installs @clerk/nextjs, writes env + proxy.ts (Next 16+) / middleware.ts (≤15)
```

Environment variables:

```bash
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_...
CLERK_SECRET_KEY=sk_...                  # server only, never NEXT_PUBLIC_
```

Key points ([Clerk quickstart](https://clerk.com/docs/nextjs/getting-started/quickstart)):

- `clerkMiddleware()` lives in `proxy.ts` on Next.js 16+.
- `<ClerkProvider>` goes **inside `<body>`**.
- Protect routes with `createRouteMatcher` + `auth.protect()`.
- `auth()` is **async**, so always `await auth()`.
- Next.js warns **not** to rely on proxy alone for authorisation. Re-check in every Server Action and Route Handler ([Next.js](https://nextjs.org/docs/app/guides/backend-for-frontend)).

```ts
// proxy.ts (Next.js 16+)
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server';

const isProtected = createRouteMatcher(['/dashboard(.*)', '/api/private(.*)']);

export default clerkMiddleware(async (auth, req) => {
  if (isProtected(req)) await auth.protect();
});

export const config = {
  matcher: ['/((?!_next|.*\\..*).*)', '/(api|trpc)(.*)'], // verify against the current Clerk quickstart
};
```

> The matcher above is the common pattern. The research didn't extract Clerk's exact current regex, so copy the matcher from the quickstart page.

---

## Clerk → Supabase: the current method (Third-Party Auth)

### 1. Configure

1. **Clerk dashboard** → "Connect with Supabase". This adds the `role: authenticated` claim to session tokens.
2. **Supabase dashboard** → Authentication → Third-Party Auth → add Clerk (your `<x>.clerk.accounts.dev` domain).

   For the local CLI, in `supabase/config.toml`:

   ```toml
   [auth.third_party.clerk]
   enabled = true
   domain = "<your-instance>.clerk.accounts.dev"
   ```

### 2. Server client

```ts
// server/supabase.ts
import 'server-only';
import { auth } from '@clerk/nextjs/server';
import { createClient } from '@supabase/supabase-js';

export async function supabaseForUser() {
  return createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!, {
    async accessToken() {
      return (await auth()).getToken();
    },
  });
}
```

### 3. Browser client

```ts
'use client';
import { useSession } from '@clerk/nextjs';
import { createClient } from '@supabase/supabase-js';

export function useSupabase() {
  const { session } = useSession();
  return createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!, {
    async accessToken() {
      return session?.getToken() ?? null;
    },
  });
}
```

### 4. RLS

Match on `auth.jwt()->>'sub'` in a **`text`** `user_id` column. See the templates in `database-supabase.md`.

Clerk's docs now use a **publishable key** env name rather than the anon key ([Clerk](https://clerk.com/docs/guides/development/integrations/databases/supabase)).

---

## Using Supabase Auth instead of Clerk

If you don't need Clerk, Supabase Auth keeps everything in one platform:

- Create the server client per request with `@supabase/ssr`.
- ✏️ **Check the user on the server with `getClaims()`**, which verifies the JWT signature on every call. *"Never trust `supabase.auth.getSession()` inside server code such as Proxy"*, because it reads the cookie without revalidating ([Supabase Next.js guide](https://supabase.com/docs/guides/auth/server-side/nextjs)). Some older guides, including help-me-papi, recommend `getUser()`.
- Session refresh logic lives in `proxy.ts` on Next.js 16+.
- Add OAuth redirect URLs for **both** localhost and the production domain.

## Demo-day auth tips

- For a demo with no sign-up flow, pre-create a demo account and stay logged in, or add a "Continue as demo user" button that signs into it.
- Sessions are fixed at 7 days on Hobby, so sign in again the morning of judging.
- Auth is usually a **non-goal**. Add Clerk only if the demo needs per-user data, or if a sponsor prize requires it.

---

## Repos

| Repo | Why | Status |
| --- | --- | --- |
| [clerk/javascript](https://github.com/clerk/javascript) | Source of `@clerk/nextjs`; changelogs | ⭐ 1.8k · pushed 2026-09-21 |
| [clerk/nextjs-auth-starter-template](https://github.com/clerk/nextjs-auth-starter-template) | Official App Router starter | ⭐ 428 · pushed 2026-05 |
