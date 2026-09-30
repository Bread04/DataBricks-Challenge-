# 🔧 Product Plumbing: Analytics, Errors, Payments, Maps, Email

<!-- markdownlint-disable MD013 -->

> The services that make a demo feel like a real product, all on free tiers. From the Deepen research run (2026-09-22); sources are in [`evidence.md`](evidence.md) under "Product plumbing". Credits and perks are in [`../../01-hackathon-playbook/docs/free-credits.md`](../../01-hackathon-playbook/docs/free-credits.md).

---

| Need | Default | Free tier (official pages, 2026-09-22) | Demo tip |
| --- | --- | --- | --- |
| **Analytics + replay + errors** | **PostHog** | 1M events, 5K session replays, 1M flag requests, 100K exceptions, 1.5K survey responses a month; **no card** | One SDK covers everything; show a live funnel in the pitch |
| Page views only | Vercel Web Analytics | Hobby: 50K events/mo, **no custom events**; pauses after a 3-day grace period, never billed | A zero-config extra, not a PostHog replacement |
| Error tracking (alt) | Sentry | Standalone free plan not verified; **included in the GitHub Student Pack** | — |
| **Payments** | **Stripe sandbox** | Simulated payments; card `4242 4242 4242 4242`, any future expiry and CVC | Also demo a **decline** card to show error handling. Never use real cards for testing (prohibited) |
| **Maps (no key)** | **MapLibre + OpenFreeMap** | Unlimited, keyless, no signup; attribution required | Nothing can hit a quota on stage |
| Maps + geocoding / directions | Mapbox | 50K web map loads, 100K geocoding, 100K directions a month | Use it when you need search or routes |
| **Email** | **Resend** | 3K emails/mo, **100/day**; stops at the cap, never billed | Don't loop sign-up emails during rehearsal |

**Not verified this run:** Google Maps Platform free usage, Stripe Checkout/Payment Links, Novu/OneSignal free tiers, Protomaps.

---

## Setup order (about 30 minutes)

1. **PostHog:** add the snippet or SDK, identify the demo user, and create one funnel for the demo journey.
2. **Stripe sandbox:** create a test product and use the test keys only (`sk_test_…` server-side).
3. **Maps:** `maplibre-gl` + the OpenFreeMap style URL, plus the attribution line.
4. **Resend:** verify a domain (free domains are in the Student Pack) and send a test email.

## Repos

| Repo | ⭐ | Use |
| --- | --- | --- |
| [getsentry/sentry](https://github.com/getsentry/sentry) | 44.8k | Error tracking |
| [PostHog/posthog](https://github.com/PostHog/posthog) | 39.9k | Product analytics suite |
| [hyperknot/openfreemap](https://github.com/hyperknot/openfreemap) | 6.0k | Keyless map tiles |
| [maplibre/maplibre-gl-js](https://github.com/maplibre/maplibre-gl-js) | 11k | Open WebGL maps (see `../../02-frontend/docs/repos.md`) |
