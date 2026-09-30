# Deepen: Deploy targets beyond Vercel/Railway (free tiers, cold starts, demo-day limits)

Run date: 2026-09-22. Evidence retrieved this session only (11 tool calls). Class: F = fact from official page; S = official content seen only via search-result summary (not fetched); I = inference.

## Findings

1. Render Free web services spin down after 15 minutes with no inbound traffic; spin-up takes "about one minute". | https://render.com/docs/free | Render | undated | accessed 2026-09-22 | high | F
2. Render Free: 750 free instance hours per calendar month; services are suspended if the limit is reached (resets monthly). | https://render.com/docs/free | Render | undated | accessed 2026-09-22 | high | F
3. Render Free restrictions: one instance only, no persistent disks, no SSH/shell, no private-network traffic, outbound SMTP ports 25/465/587 blocked. Custom domains and managed TLS are supported. The page as fetched did not list free cron jobs or background workers. | https://render.com/docs/free | Render | undated | accessed 2026-09-22 | high (restrictions/domains); medium (cron/worker absence) | F
4. Render Free Postgres: 1 GB, expires 30 days after creation (14-day grace period before deletion), no backups. Free Key Value is in-memory only and data is lost on restart. | https://render.com/docs/free | Render | undated | accessed 2026-09-22 | high | F
5. Railway: one-time $5 trial grant. Trial caps are 2 replicas, 1 GB RAM, 2 vCPU, 1 GB ephemeral, 0.5 GB volume, 4 GB image. Free plan is $0/mo with $1 credit/month, 1 vCPU, 0.5 GB RAM, 1 replica. Hobby is $5/mo including $5 usage. Railway now requires a post-paid card ("as of March 30th"). | https://docs.railway.com/reference/pricing/plans | Railway | undated | accessed 2026-09-22 | high (figures); medium (card rule wording and year) | F
6. Fly.io has no free tier, only a Free Trial: 2 hours of machine runtime or 7 days, whichever comes first, with no free allowances during the trial. New orgs are then billed monthly pay-as-you-go and need a payment method. | https://fly.io/docs/about/free-trial/ ; https://fly.io/docs/about/pricing/ | Fly.io | undated | accessed 2026-09-22 | medium (direct fetch of the pricing page failed with ECONNREFUSED; these figures come from search summaries) | S
7. Cloudflare Workers Free: 100,000 requests/day, reset at midnight UTC. Going over returns Error 1027. 10 ms CPU per HTTP request (fetch/DB wait does not count), 128 MB memory per isolate, 50 subrequests/request, 64 MiB bundle, 100 Workers per account. No hard wall-clock limit while the client stays connected, and waitUntil can run up to 30 s after the response. | https://developers.cloudflare.com/workers/platform/limits/ | Cloudflare | 2026-09-05 | accessed 2026-09-22 | high | F
8. Netlify pricing is credit-based. Free = 300 credits/month. Rates: production deploy 15 credits each, bandwidth 20 credits/GB, compute 10 credits/GB-hour, requests 2 credits per 10k. Personal is $9/mo (1,000 credits) and Pro is $20/mo (3,000). The page did not say what happens when free credits run out. | https://www.netlify.com/pricing/ | Netlify | undated | accessed 2026-09-22 | high | F
9. Hugging Face Spaces: Static Spaces are free for everyone. Gradio and Docker Spaces "require a paid plan to create" (PRO for personal accounts). The exception is that free personal accounts may host up to 2 Gradio Spaces on ZeroGPU. The SDKs listed are Gradio, Docker and static HTML; Streamlit is not listed as a native SDK. | https://huggingface.co/docs/hub/spaces-overview | Hugging Face | undated | accessed 2026-09-22 | high | F
10. HF Spaces CPU Basic (2 vCPU, 16 GB RAM, 50 GB non-persistent disk) has no hourly cost. On free hardware a Space "will go to sleep" after an unused period (the page gives no duration). Outbound network is limited to ports 80, 443 and 8080. The cheapest GPU is T4-small at $0.40/h. | https://huggingface.co/docs/hub/spaces-overview | Hugging Face | undated | accessed 2026-09-22 | high | F
11. Streamlit Community Cloud: apps get 0.078–2 CPU cores, 690 MB–2.7 GB memory and up to 50 GB storage (figures "as of February 2024"). Apps with no traffic for 12 hours go to sleep. Any viewer can wake one by clicking "Yes, get this app back up!". | https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app | Streamlit (Snowflake) | undated | accessed 2026-09-22 | high | F
12. Streamlit Community Cloud hosts all apps in the US (not configurable) and allows at most 5 app updates per minute from GitHub. | https://docs.streamlit.io/deploy/streamlit-community-cloud/status | Streamlit | undated | accessed 2026-09-22 | high | F
13. Modal Starter gives $30/month free compute, up to 100 containers, GPU concurrency 10 and 3 seats. GPU per-second rates: T4 $0.000164, L4 $0.000222, A10 $0.000306, A100-40GB $0.000583, H100 $0.001097. Startup credits exist, and academics can get up to $10k. | https://modal.com/pricing | Modal | undated | accessed 2026-09-22 | high | F
14. Rough arithmetic from Finding 13: $30/mo buys about 50 h of T4 time or about 7.6 h of H100 time, which is plenty for a demo if the containers are pre-warmed. | derived from https://modal.com/pricing | — | — | accessed 2026-09-22 | medium | I

## Decision table

| Host | Best for | Free tier | Sleep / cold start | Gotcha |
|---|---|---|---|---|
| Render (F1–F4) | Python/Node web API from Git | 750 instance-h/mo | Sleeps after 15 min idle; ~1 min wake | Free Postgres deleted after 30 d (+14 d grace); no disk, SMTP blocked; cron/workers not listed as free (unconfirmed); ~1 min first-request stall mid-demo |
| Railway (F5) | Python workers (already chosen) | $5 one-time trial, then $1/mo Free plan (0.5 GB RAM) | Not stated on plans page | Needs a card; $1/mo Free plan is tiny, so plan on Hobby $5 for demo week |
| Fly.io (F6) | Docker apps in specific regions | None: trial of 2 machine-hours or 7 days | Not fetched | Trial runs out within hours of real use; card needed after |
| Cloudflare Workers (F7) | Edge APIs, proxies, light JSON backends | 100k req/day | Cold starts not covered in limits doc | 10 ms CPU cap rules out heavy compute; Error 1027 if the daily cap is hit (reset 00:00 UTC) |
| Netlify (F8) | Static/Jamstack front ends | 300 credits/mo | Not stated | Each production deploy costs 15 credits, so ~20 deploys uses up the month; behaviour when credits run out not documented on the page |
| HF Spaces (F9–F10) | Gradio ML demos | Static free; free Gradio only on ZeroGPU (max 2 Spaces) | Sleeps when unused on free hardware (duration not stated) | Docker, CPU-Gradio and Streamlit Spaces now need PRO; disk not persistent; outbound ports limited to 80/443/8080 |
| Streamlit Community Cloud (F11–F12) | Streamlit data demos | Free, up to 2.7 GB RAM | Sleeps after 12 h with no traffic; viewer clicks to wake | Open it shortly before judging; US-only hosting; limited RAM for models |
| Modal (F13–F14) | GPU inference / batch ML | $30/mo credit | Serverless containers (warm-up not fetched) | Watch GPU burn; cap concurrency |

Demo-day implications (I, drawn from F1, F10, F11): open every free-tier URL in the 5–10 minutes before presenting. Render needs traffic within 15 min to stay awake, and Streamlit within 12 h. Custom domains plus managed TLS are confirmed for Render (F3), and custom domains for public/protected HF Spaces (F9 page).

## Not found

- Official Render, Fly or Railway guidance for or against keep-warm cron pings. Not retrieved.
- Fly Machines auto-stop/auto-start cold-start timings, and Fly certificate/IPv4 costs. The pricing page fetch failed (ECONNREFUSED).
- Railway sleep ("serverless") behaviour on trial/free. Not on the plans page.
- HF Spaces sleep duration for free hardware, and ZeroGPU quotas. Not fetched.
- What happens when Netlify free credits run out (pause vs. overage).
- Cloudflare Pages free limits (builds/month), and Workers cold-start guidance.
- Dockerfile deploy specifics for Render, Fly and Railway, and Coolify gotchas. Not covered within the call budget.
- Whether Modal requires a card for Starter, and Modal cold-start guidance.
