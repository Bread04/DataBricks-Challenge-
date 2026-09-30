# Backend & Infra: hackathon accelerator repos, round 1, digest 1
Accessed 2026-09-21. I did not call api.github.com. I fetched two github.com repo pages (better-auth, hackathon-starter). The lead should verify all star counts and push dates.
Slug confidence: **V** means the slug appears in a fetched or searched source this run. **P** means the slug is proposed from prior knowledge and the project name was evidenced this run, but the exact slug was not. The lead should verify every P slug.

## Candidates

| category | owner/repo (exact slug) | one-line hackathon use | evidence URL | notes |
|---|---|---|---|---|
| BaaS | supabase/supabase (P) | Postgres, auth, storage, realtime and instant APIs in one project | https://openalternative.co/alternatives/firebase | Called "the 2026 benchmark" (hafencity.dev via search) |
| BaaS | appwrite/appwrite (P) | Self-hosted BaaS with auth, DB, functions and storage, runs in Docker | https://encore.dev/articles/firebase-alternatives | Microservices stack, so heavier to run than PocketBase |
| BaaS | pocketbase/pocketbase (P) | Single-binary backend with SQLite, auth and an admin UI, ideal for a 24h prototype | https://developer.puter.com/blog/pocketbase-alternatives/ | Described as "lightest possible backend" |
| BaaS | get-convex/convex-backend (P) | Reactive TypeScript backend with built-in realtime sync, good for AI and collaborative apps | https://encore.dev/articles/firebase-alternatives | Check the self-host licence (not verified this run) |
| BaaS | nhost/nhost (P) | Postgres plus Hasura GraphQL BaaS | https://encore.dev/articles/supabase-alternatives | Named with Appwrite as the strongest OSS alternatives |
| BaaS/CMS | directus/directus (P) | Instant admin and REST/GraphQL API over an existing SQL DB | https://unfoldcms.com/blog/strapi-vs-directus-2026 | "Friendly database client" feel |
| BaaS/CMS | strapi/strapi (P) | Headless CMS with a large plugin ecosystem (v5) | https://unfoldcms.com/blog/strapi-vs-directus-2026 | Strapi 5 brought better TypeScript support |
| BaaS/CMS | payloadcms/payload (V) | Next.js-native headless CMS and app framework | https://github.com/payloadcms/payload/discussions/12843 | Acquired by Figma in June 2025. Stays open source, but Payload Cloud paused new sign-ups |
| Auth | better-auth/better-auth (V) | Full TypeScript auth: OAuth, 2FA, orgs and multi-tenant, via plugins | https://github.com/better-auth/better-auth | About 30k stars, not archived, 337 open issues (fetched). Recommended default |
| Auth | nextauthjs/next-auth (V) | Legacy Next.js auth | https://github.com/nextauthjs/next-auth/discussions/13252 | **Avoid for new projects.** Security patches only since joining Better Auth (Sep 2025) |
| Auth | lucia-auth/lucia (V) | Learning resource only | https://github.com/lucia-auth/lucia | **Avoid as a dependency.** Deprecated in March 2025 and now a learning guide |
| Auth | logto-io/logto (P) | Self-hosted OIDC auth with admin console | (not evidenced this run) | Unverified lead |
| Auth | keycloak/keycloak (P) | Enterprise SSO/IdP | (not evidenced this run) | Heavy for a hackathon. Unverified lead |
| Auth | supertokens/supertokens-core (P) | Self-hosted auth with prebuilt UI | (not evidenced this run) | Unverified lead |
| Auth | zitadel/zitadel (P) | OSS identity platform | https://openalternative.co/alternatives/firebase | Listed as a Firebase alternative |
| ORM | drizzle-team/drizzle-orm (P) | SQL-first TypeScript ORM, edge-friendly and tiny bundle | https://makerkit.dev/blog/tutorials/drizzle-vs-prisma | Leads new-project adoption. 0.45.2 stable, 1.0 in beta, team now at PlanetScale |
| ORM | prisma/prisma (P) | Schema-first ORM, fastest route to a working CRUD | https://www.prisma.io/docs/orm/v7/more/comparisons/prisma-and-drizzle | 7.10 stable and 8 in RC, per a search-result summary |
| ORM | kysely-org/kysely (P) | Type-safe SQL query builder | https://tomodahinata.com/en/blog/prisma-vs-drizzle-vs-typeorm-kysely-orm-comparison-guide | A query builder, not an ORM |
| ORM | typeorm/typeorm (P) | Decorator ORM, common with NestJS | https://tomodahinata.com/en/blog/prisma-vs-drizzle-vs-typeorm-kysely-orm-comparison-guide | Maintenance status not checked this run |
| ORM (Py) | fastapi/sqlmodel (P) | Pydantic plus SQLAlchemy models for FastAPI | (not evidenced this run) | Unverified |
| Local DB | tursodatabase/turso (V) | SQLite-compatible Rust rewrite with MVCC, vector search and an MCP mode | https://blog.openreplay.com/turso-rust-sqlite-evolution/ | 21k+ stars, v0.6.1 (May 2026), **beta** |
| Local DB | tursodatabase/libsql (P) | Production SQLite fork behind Turso Cloud | https://docs.turso.tech/libsql | Still maintained, but "the future is Turso" |
| Postgres ext | pgvector/pgvector (P) | Vector similarity in Postgres for RAG demos | (not evidenced this run) | Unverified slug |
| API | honojs/hono (P) | Web-standards framework that runs on Workers, Bun, Node and Deno | https://www.pkgpulse.com/guides/hono-vs-express-vs-fastify-vs-elysia-2026 | 28k+ stars and about 9.3M weekly downloads (early 2026) |
| API | elysiajs/elysia (P) | Bun-first, very fast, with Eden end-to-end types | https://encore.dev/articles/elysia-vs-hono | Loses its edge off Bun |
| API | fastify/fastify (P) | Fast Node framework with strong official plugins | https://kanopylabs.com/blog/hono-vs-express-vs-fastify | |
| API | expressjs/express (P) | Ubiquitous Node framework, v5 | https://www.pkgpulse.com/guides/hono-vs-express-vs-fastify-vs-elysia-2026 | Express 5 is a cleanup release, not a speed release |
| API | nestjs/nest (P) | Structured TypeScript backend with DI | (not evidenced this run) | Unverified |
| API | fastapi/fastapi (P) | Python API with auto OpenAPI docs, the default for ML hackathons | https://github.com/mjhea0/awesome-fastapi | |
| API | trpc/trpc (P) | End-to-end typed RPC for TypeScript monorepos | https://zenn.dev/m_noto/articles/92168c3fa006ed?locale=en | "Growth has leveled off" |
| API | unnoq/orpc (P) | tRPC-style RPC with OpenAPI output | (not evidenced this run) | Riser lead, unverified |
| Starter | t3-oss/create-t3-app (P) | Next.js, tRPC, Prisma/Drizzle and NextAuth scaffold | https://makerkit.dev/blog/saas/best-nextjs-saas-boilerplate | 28k+ stars. Defaults to NextAuth, so check the auth default |
| Starter | nextjs/saas-starter (V) | Official minimal SaaS starter with Postgres, Stripe and auth | https://makerkit.dev/blog/saas/best-nextjs-saas-boilerplate | About 16.1k stars |
| Starter | ixartz/SaaS-Boilerplate (V) | Next.js, Drizzle, Clerk and Stripe, with monthly updates | https://makerkit.dev/blog/saas/best-nextjs-saas-boilerplate | About 7.4k stars |
| Starter | wasp-lang/open-saas (P) | Free SaaS template on Wasp (React, Node, Prisma) | https://wasp.sh/resources/2026/09/09/redwoodjs-alternatives-2026 | 14k+ stars (vendor source). Wasp is beta, nearing 1.0 |
| Starter | wasp-lang/wasp (P) | Full-stack DSL framework | https://wasp.sh/resources/2026/09/09/redwoodjs-alternatives-2026 | Beta |
| Starter | sahat/hackathon-starter (V) | Express, MongoDB and Pug with many OAuth/API integrations plus LangChain/RAG examples | https://github.com/sahat/hackathon-starter | 35.3k stars, not archived (fetched). Recently gained passkeys, 2FA and AI examples |
| Starter | refinedev/refine (P) | React admin/CRUD meta-framework | (not evidenced this run) | Unverified |
| Starter | redwoodjs/graphql (V) | The original RedwoodJS | https://github.com/redwoodjs/graphql/releases | **Avoid.** Renamed RedwoodGraphQL and in maintenance mode since April 2025 |
| Starter | redwoodjs/sdk (V) | RSC framework on Cloudflare Workers | https://github.com/redwoodjs/sdk | Active v1.x, Cloudflare-only |
| Starter | cedarjs/cedar (V) | Community fork of RedwoodGraphQL | https://wasp.sh/resources/2026/09/09/redwoodjs-alternatives-2026 | Active, v6.x (Sep 2026) |
| Realtime | socketio/socket.io (P) | WebSocket rooms and events | https://kanopylabs.com/blog/yjs-vs-automerge-vs-liveblocks | Low level, so presence and persistence are up to you |
| Realtime | yjs/yjs (P) | CRDT for collaborative editing | https://kanopylabs.com/blog/yjs-vs-automerge-vs-liveblocks | Pair with Hocuspocus for the server |
| Realtime | ueberdosis/hocuspocus (P) | Self-hosted Yjs WebSocket backend | https://www.pkgpulse.com/guides/liveblocks-vs-partykit-vs-hocuspocus-realtime-2026 | |
| Realtime | partykit/partykit (P) | Stateful realtime on Cloudflare Workers | https://www.partykit.io/ | |
| Realtime | electric-sql/electric (P) | Postgres sync engine | https://electric-sql.com/docs/reference/alternatives | Also lists Zero, InstantDB, Jazz, Triplit and others |
| Jobs | taskforcesh/bullmq (P) | Redis job queue with cron, priorities and flows | https://www.pkgpulse.com/guides/best-nodejs-background-job-libraries-2026 | Added Bun, Python and Rust support by mid-2026 |
| Jobs | triggerdotdev/trigger.dev (P) | Durable long-running TypeScript tasks, good for AI jobs, self-hostable (Apache 2.0) | https://www.inngest.com/blog/best-job-queue-alternatives | |
| Jobs | inngest/inngest (P) | Event-driven step functions next to a Next.js app | https://www.buildmvpfast.com/blog/inngest-vs-trigger-dev-vs-bullmq-background-jobs-nextjs-2026 | One source says it cannot be self-hosted. I doubt this: it has an OSS dev server, so verify |
| Jobs | temporalio/temporal (P) | Enterprise durable workflows | https://trybuildpilot.com/610-trigger-dev-vs-inngest-vs-temporal-2026 | Too heavy for most hackathons |
| PaaS | coollabsio/coolify (P) | Self-hosted Heroku/Vercel-style panel on a VPS | https://massivegrid.com/blog/dokploy-vs-coolify-vs-caprover/ | About 57.3k stars (Jun 2026), 60k+ later |
| PaaS | Dokploy/dokploy (P) | Lightweight Docker/Swarm PaaS | https://massivegrid.com/blog/dokploy-vs-coolify-vs-caprover/ | About 35k stars, pre-1.0, fast riser |
| PaaS | caprover/caprover (P) | Stable, simple PaaS | https://massivegrid.com/blog/dokploy-vs-coolify-vs-caprover/ | About 15.1k stars |
| PaaS | dokku/dokku (P) | git-push PaaS, CLI-first | https://www.buildmvpfast.com/blog/coolify-vs-dokku-vs-caprover-self-hosted-paas-production-2026 | 31.9k+ stars, 15 open issues |
| Tunnel | fatedier/frp (P) | Self-hosted reverse proxy/tunnel | https://fxtun.dev/blog/ngrok-alternatives-open-source-2026/ | 100k+ stars |
| Tunnel | cloudflare/cloudflared (P) | `cloudflared tunnel --url` gives a free URL with no account | https://pinggy.io/blog/best_ngrok_alternatives/ | Best zero-setup demo tunnel |
| Tunnel | openziti/zrok (P) | Zero-trust OSS tunnel | https://pinggy.io/blog/best_ngrok_alternatives/ | |
| Tunnel | ekzhang/bore (P) | Minimal self-hosted TCP tunnel | https://pinggy.io/blog/best_ngrok_alternatives/ | Needs your own server |
| Tunnel | localtunnel/localtunnel (P) | npm tunnel | https://pinggy.io/blog/best_ngrok_alternatives/ | **Stale-ish.** "Not touched since August 2025" |
| Notify | novuhq/novu (V) | Multi-channel notifications with a drop-in Inbox component | https://github.com/novuhq/novu | Now framed as "communication infrastructure for agents and products" |
| Email | resend/react-email (P) | Build emails with React components | https://novu.co/blog/building-an-email-automation-system-with-react-flow-and-resend/ | |
| API test | usebruno/bruno (P) | Git-native offline API client | https://medium.com/@vignarajj/bruno-vs-hoppscotch-vs-postman-in-2026-choosing-the-right-api-client-for-backend-development-33b60644c51b | MIT |
| API test | hoppscotch/hoppscotch (P) | Browser API client for REST, GraphQL, WebSocket and MQTT | https://apiscout.dev/guides/bruno-vs-hoppscotch-vs-insomnia-vs-postman-2026 | Self-hostable |
| Awesome | awesome-selfhosted/awesome-selfhosted (V) | Discovery list for self-hostable services | https://github.com/awesome-selfhosted/awesome-selfhosted | 320k+ stars (search summary) |
| Awesome | mjhea0/awesome-fastapi (V) | FastAPI ecosystem list | https://github.com/mjhea0/awesome-fastapi | |
| Awesome | Kludex/awesome-fastapi-projects (V) | Projects built with FastAPI | https://github.com/Kludex/awesome-fastapi-projects | |

That is 66 rows. About 10 of them have no evidence URL this run.

## Findings

| # | claim | source URL | publisher | pub_date | accessed | confidence | class |
|---|---|---|---|---|---|---|---|
| 1 | Lucia was deprecated in March 2025 and reframed as a learning resource for building sessions from scratch | https://www.wisp.blog/blog/lucia-auth-is-dead-whats-next-for-auth ; https://github.com/lucia-auth/lucia | Wisp CMS blog; GitHub | 2025 | 2026-09-21 | high | deprecation |
| 2 | Auth.js/NextAuth has been maintained by the Better Auth team since the 22 Sep 2025 announcement. New projects are advised not to start with Auth.js, and it gets security patches only | https://better-auth.com/blog/authjs-joins-better-auth ; https://github.com/nextauthjs/next-auth/discussions/13252 | Better Auth; GitHub | 2025-09-22 | 2026-09-21 | high | deprecation/merger |
| 3 | better-auth/better-auth has about 30k stars, is not archived, and has 337 open issues and 394 PRs | https://github.com/better-auth/better-auth | GitHub | live | 2026-09-21 | high | metric |
| 4 | The original RedwoodJS was wound down in April 2025, renamed RedwoodGraphQL and put in maintenance mode. RedwoodSDK (Cloudflare-only, v1.x) is active, and the community fork cedarjs/cedar is active at v6.x | https://wasp.sh/resources/2026/09/09/redwoodjs-alternatives-2026 | Wasp (competitor, so possibly biased) | 2026-09-09 | 2026-09-21 | high | deprecation/rename |
| 5 | Figma acquired Payload on 17 Jun 2025. Payload stays open source, but Payload Cloud paused new sign-ups | https://www.figma.com/blog/payload-joins-figma/ ; https://www.crainsgrandrapids.com/news/technology/grand-rapids-tech-firm-acquired-by-san-francisco-web-designer/ | Figma; Crain's | 2025-06 | 2026-09-21 | high | acquisition |
| 6 | Drizzle has overtaken Prisma for new projects. Drizzle is at 0.45.2 with 1.0 in beta, and the Drizzle team works at PlanetScale. Prisma is at 7.10 with 8 in RC | https://makerkit.dev/blog/tutorials/drizzle-vs-prisma ; https://anotherwrapper.com/blog/drizzle-vs-prisma | MakerKit; AnotherWrapper | 2026 | 2026-09-21 | medium (from search summary; version numbers unverified) | trend |
| 7 | Hono passed 28k stars and about 9.3M weekly npm downloads in early 2026, and some measures put it above Fastify on downloads | https://www.pkgpulse.com/guides/hono-vs-express-vs-fastify-vs-elysia-2026 | PkgPulse | 2026 | 2026-09-21 | medium | trend/metric |
| 8 | tRPC growth has "leveled off" | https://zenn.dev/m_noto/articles/92168c3fa006ed?locale=en | Zenn | 2025/26 | 2026-09-21 | low-medium | trend |
| 9 | Self-hosted PaaS stars: Coolify about 57.3k (22 Jun 2026, 60k+ later), Dokploy about 35k, CapRover about 15.1k, Dokku 31.9k+ | https://massivegrid.com/blog/dokploy-vs-coolify-vs-caprover/ ; https://ansezz.com/blog/coolify-2026-self-hosted-paas/ | MassiveGRID; ansezz | 2026 | 2026-09-21 | medium | metric |
| 10 | localtunnel has "not been touched since August 2025". frp has 100k+ stars and is active. cloudflared quick tunnels need no account | https://pinggy.io/blog/best_ngrok_alternatives/ ; https://fxtun.dev/blog/ngrok-alternatives-open-source-2026/ | Pinggy (competitor); fxtun | 2026 | 2026-09-21 | medium | staleness |
| 11 | tursodatabase/turso (Rust SQLite rewrite) is in beta at v0.6.1 (May 2026) with 21k+ stars. libSQL is production-ready and powers Turso Cloud. Turso is also building a Postgres frontend | https://blog.openreplay.com/turso-rust-sqlite-evolution/ ; https://x.com/penberg/status/2032373944007688226 ; https://byteiota.com/turso-is-building-postgres-in-rust-what-that-means-for-your-database-stack/ | OpenReplay; Pekka Enberg (Turso CTO); byteiota | 2026 | 2026-09-21 | medium | rename/riser |
| 12 | BullMQ officially supports Bun, Python and Rust as of mid-2026. Trigger.dev is Apache 2.0 and self-hostable | https://www.pkgpulse.com/guides/best-nodejs-background-job-libraries-2026 | PkgPulse | 2026 | 2026-09-21 | medium | trend |
| 13 | sahat/hackathon-starter is still active: 35.3k stars, not archived, and has added passkeys, 2FA, LangChain and RAG examples | https://github.com/sahat/hackathon-starter | GitHub | live | 2026-09-21 | high | metric |
| 14 | Free-starter stars: create-t3-app 28k+, nextjs/saas-starter about 16.1k, Open SaaS about 15.7k (14k+ per Wasp), ixartz/SaaS-Boilerplate about 7.4k with monthly updates | https://makerkit.dev/blog/saas/best-nextjs-saas-boilerplate | MakerKit (sells a competing product) | 2026 | 2026-09-21 | medium | metric |
| 15 | Postman now forces login and cloud sync. Bruno (Git-native) and Hoppscotch (browser, self-host) are both MIT and import Postman collections | https://medium.com/@vignarajj/bruno-vs-hoppscotch-vs-postman-in-2026-choosing-the-right-api-client-for-backend-development-33b60644c51b ; https://apiscout.dev/guides/bruno-vs-hoppscotch-vs-insomnia-vs-postman-2026 | Medium; APIScout | 2026 | 2026-09-21 | medium | trend |
| 16 | One Inngest comparison says Inngest cannot be self-hosted | https://www.buildmvpfast.com/blog/inngest-vs-trigger-dev-vs-bullmq-background-jobs-nextjs-2026 | BuildMVPFast | 2026 | 2026-09-21 | low (conflicts with my prior belief that it has an OSS server) | disputed |

## Leads not chased / not found
- **Blitz.js status.** No 2025–26 evidence found. Check whether blitz-js/blitz is archived or stale.
- **Stars for Supabase, Appwrite, PocketBase, Convex, Nhost, Directus, Strapi.** No numbers retrieved this run. The lead needs to verify them.
- **Convex self-host licence** (get-convex/convex-backend) was not checked.
- **Clerk SDKs, Logto, Keycloak, SuperTokens** had no 2026 evidence this run.
- **oRPC** (unnoq/orpc) is a riser I did not evidence. SQLModel, NestJS, TypeORM maintenance and Refine were also not checked.
- **Postgres extensions** (pgvector, pg_cron, ParadeDB pg_search, PostGIS) were not searched directly.
- **Docker compose collections** (e.g. docker/awesome-compose) and Stripe samples (stripe-samples/*) were not searched.
- **Backend awesome lists** beyond awesome-selfhosted and the FastAPI lists: sindresorhus/awesome-nodejs, awesome-supabase and similar were not fetched.
- **Sync-engine risers** (Zero/rocicorp, InstantDB, Jazz, Triplit, LiveStore) are named in the Electric alternatives page, but I have no metrics.
- **Inngest self-host claim** (Finding 16) needs checking against inngest.com docs.
