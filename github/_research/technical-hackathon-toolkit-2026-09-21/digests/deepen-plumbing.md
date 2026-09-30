# Deepen: Product plumbing and free credits (hackathon, Sep 2026)

Run budget: 12 tool calls, one round. Everything below comes from pages fetched on 2026-09-22. Two fetches failed (sentry.io/pricing, mapsplatform.google.com/pricing), so those topics are listed under Not found.

## Findings

Format: claim | source URL | publisher | date | accessed | confidence | class

1. PostHog's free tier gives 1M product-analytics events, 5K session-replay recordings, 1M feature-flag requests, 100K error-tracking exceptions and 1,500 survey responses each month | https://posthog.com/pricing | PostHog | undated (live pricing page) | accessed 2026-09-22 | high | official-pricing
2. PostHog needs no credit card to start. You only add payment details to go past the free limits, unlock advanced features or create extra projects | https://posthog.com/pricing | PostHog | undated | accessed 2026-09-22 | high | official-pricing
3. Vercel Web Analytics on the Hobby plan includes 50,000 events a month across all projects, with a 1-month reporting window and no custom events (those need Pro) | https://vercel.com/docs/analytics/limits-and-pricing | Vercel | last_updated 2026-08-25 | accessed 2026-09-22 | high | official-docs
4. Hobby teams are never charged for extra Vercel analytics events. Past the limit there is a 3-day grace period, then collection pauses (for 7 days, or until the next cycle, or until you upgrade). Events are shared across every project in the account | https://vercel.com/docs/analytics/limits-and-pricing | Vercel | 2026-08-25 | accessed 2026-09-22 | high | official-docs
5. Stripe sandboxes are isolated test environments, reached from the Dashboard account picker. Payments made with test API keys are simulated, so no money moves | https://docs.stripe.com/testing | Stripe | undated (live docs) | accessed 2026-09-22 | high | official-docs
6. Stripe's standard test card is 4242 4242 4242 4242. It takes any future expiry date, any 3-digit CVC (4 digits for Amex) and any values in the other fields. There are also test cards for declines, 3D Secure and disputes. Stripe's Services Agreement bans using real card details in live mode for testing | https://docs.stripe.com/testing | Stripe | undated | accessed 2026-09-22 | high | official-docs
7. Mapbox's free tier covers, per month: 50,000 GL JS web map loads, 25,000 mobile-SDK MAUs, 100,000 Geocoding API requests, 100,000 Directions API requests and 50,000 Static Images requests | https://www.mapbox.com/pricing | Mapbox | undated | accessed 2026-09-22 | high | official-pricing
8. OpenFreeMap's public instance is free, with no limits on map views or requests and no registration, API keys or cookies. It recommends MapLibre as the client, is MIT-licensed and uses OSM data. Attribution is required: "OpenFreeMap © OpenMapTiles Data from OpenStreetMap" | https://openfreemap.org/ | OpenFreeMap (hyperknot) | undated | accessed 2026-09-22 | high | official-project-site
9. Resend's free plan allows 3,000 emails a month with a cap of 100 a day. It includes 3 domains, 10,000 automation runs a month and 30-day data retention. When you hit a cap, sending stops until the next period; you are not charged overage | https://resend.com/pricing | Resend | undated | accessed 2026-09-22 | high | official-pricing
10. The GitHub Student Developer Pack includes: Azure ($100 credit plus 25+ free services, age 18+), Heroku ($13 a month for 24 months), GitHub Pro, Copilot for students, Codespaces at Pro level and JetBrains IDEs (free annual subscription) | https://education.github.com/pack | GitHub Education | undated (live page) | accessed 2026-09-22 | high | official-program-page
11. The Student Pack also includes: a free domain for 1 year from each of Namecheap (.me), Name.com (.dev/.app etc.) and .TECH; MongoDB Atlas ($50 credits); Datadog Pro (10 servers for 2 years); Sentry (50K errors, 100K transactions, 1GB attachments); New Relic; 1Password (1 year); and Stripe ($25 fee credit) | https://education.github.com/pack | GitHub Education | undated | accessed 2026-09-22 | medium (the page summarizer paraphrased the offer wording; check each offer when you redeem it) | official-program-page

## Recommended setup (derived)

- **Analytics, replay and errors in one tool:** PostHog cloud free tier. One SDK covers events, session replay, feature flags and error tracking, no card needed, and the limits are far above demo-day traffic [F1, F2]. Add Vercel Web Analytics only as a zero-config page-view counter if you deploy on Vercel. It has no custom events on Hobby, so it cannot replace PostHog [F3, F4].
- **Error tracking alternative:** if the team prefers Sentry, student members can redeem the Sentry offer in the Student Pack [F11]. The standalone Sentry free-plan limits were not verified this run.
- **Payments:** create a Stripe sandbox and demo with 4242 4242 4242 4242 (any future expiry, any CVC). Show a decline card to prove error handling. No money moves [F5, F6]. The Checkout and Payment Links one-liner is not evidenced this run (see Not found).
- **Maps:** default to MapLibre GL JS with OpenFreeMap tiles. There is no key or signup and no quota to hit on stage; just keep the attribution [F8]. Use Mapbox when you need geocoding or directions: 100K requests a month each is plenty for a demo [F7].
- **Email:** Resend free plan. Watch the 100-a-day cap if you demo sign-up emails in a loop or run load tests [F9].
- **Credits:** every eligible student should activate the GitHub Student Pack before the event. It gives Copilot, Codespaces, a free domain for the demo URL, Azure $100, Heroku, MongoDB Atlas $50 and Sentry [F10, F11].

## Repo candidates

| category | exact owner/repo slug | hackathon use | evidence URL |
| --- | --- | --- | --- |
| Maps tiles | hyperknot/openfreemap | Free, keyless vector tiles for MapLibre; can be self-hosted | https://openfreemap.org/ (links github.com/hyperknot/openfreemap) |

(Other slugs, such as maplibre/maplibre-gl-js, PostHog/posthog-js and resend/resend-node, are likely but were not verified this run, so they are left out of the table.)

## Not found

- **Sentry standalone free (Developer) plan limits:** the fetch of sentry.io/pricing failed. Only the Student Pack Sentry offer is evidenced [F11].
- **Google Maps Platform free usage and the 2025 change** from the $200 monthly credit to per-SKU free caps: the fetch failed (connection refused). This is unverified belief only.
- **Stripe Checkout and Payment Links no-code option:** not fetched. That it works in test mode is an unverified belief.
- **Protomaps** free tiles, **Novu** free tier, **OneSignal** free tier and **web push:** not fetched (out of budget).
- **Anthropic, OpenAI or Google hackathon and startup credit programs, AWS Activate, Google for Startups Cloud, standalone Azure for Students, MLH perks:** not fetched. Only the Azure $100 via the Student Pack is evidenced [F10].
- **PostHog startup program credits:** the pricing page did not mention any.
