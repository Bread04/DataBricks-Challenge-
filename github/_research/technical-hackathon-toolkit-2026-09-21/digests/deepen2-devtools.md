# Deepen-2 digest: free AI dev tools for hackathon teams (Sep 2026)

Accessed 2026-09-22. Budget-limited single round (12 tool calls). "Official" = the vendor's own pricing or docs page was fetched or surfaced. "Search-summary" = figure taken from a search-engine synthesis of third-party pages; treat it as a lead to verify, not as fact.

Cost tags: 🆓 free/OSS · 🆓* free tier with limits · 💳 trial only · 💰 paid

## Table

| category | tool | cost tag | free allowance (exact from source) | source URL | confidence |
|---|---|---|---|---|---|
| Coding assistant | GitHub Copilot Free | 🆓* | "2,000 completions per month", "Limited chat and agent usage". Pro is "$10 USD per user / month". "Verified students have access to the GitHub Copilot Student plan" (the page doesn't say what it costs) | https://github.com/features/copilot/plans | High (official) |
| Coding assistant | Cursor Hobby | 🆓* | "Limited Agent requests", "Access to Composer". No numbers published on the page. Pro "$20 / mo." There's a /students page I didn't fetch | https://cursor.com/pricing | High (official, but the limits are vague) |
| Coding assistant | Windsurf | ? | windsurf.com/pricing now 308-redirects to devin.ai/pricing. I didn't fetch the new page | https://windsurf.com/pricing → https://devin.ai/pricing | Low (only the redirect is verified) |
| Coding assistant | Google Antigravity | 🆓* | Individual tier $0. Limits are set by available capacity; free plan moved to a "weekly based rate limit". No fixed quota is published | https://antigravity.google/pricing/ ; https://antigravity.google/blog/changes-to-antigravity-plans (surfaced, not fetched) | Medium (search-summary) |
| Coding assistant | Kiro | 🆓* | Free $0 with 50 credits/month, no rollover. Pro $20 (1,000 credits). Students can get a free year | https://kiro.dev/pricing/ ; https://kiro.dev/blog/students-2026/ (surfaced, not fetched) | Medium (search-summary) |
| Coding assistant | Zed AI, JetBrains AI | — | Not researched this round | — | — |
| OSS agent | OpenCode, Cline, Aider, OpenHands, Goose, Kilo Code | 🆓 (unverified) | Not researched this round | — | Unverified belief |
| App builder | v0 (Vercel) | 🆓* | "$5 in monthly credits", resets each billing cycle, plus a "7-message daily limit" | https://v0.app/pricing (surfaced) | Medium (search-summary) |
| App builder | Bolt.new | 🆓* | 1M tokens/month with a 300K/day cap. Daily tokens don't roll over | https://support.bolt.new/account-and-subscription/tokens (surfaced) | Medium (search-summary) |
| App builder | Lovable | 🆓* | "a daily grant of 5 build credits (up to 30 a month), plus monthly grants of 20 Cloud credits", plus "4 credits usable by AI features built into user apps" | https://lovable.dev/pricing | High (official) |
| App builder | Replit Agent (Starter) | 🆓* | Daily Agent credits up to a monthly cap. The exact number isn't published | https://docs.replit.com/billing/plans/starter-plan (surfaced) | Medium (search-summary) |
| App builder | Firebase Studio | ⚠ closing | Being shut down on March 22, 2027. Since June 22, 2026, new sign-ups and new workspaces are disabled. Previously free with 3 workspaces (30 with Google Developer Program Premium) | https://firebase.google.com/docs/studio/pricing (surfaced) | Medium (search-summary; verify before relying on it) |
| LLM API | Gemini API free tier | 🆓* | The docs page no longer lists fixed free-tier numbers: "Rate limits depend on a variety of factors (such as your usage tier) and can be viewed in Google AI Studio" | https://ai.google.dev/gemini-api/docs/rate-limits | High (official; no numbers given) |
| LLM API | Groq | 🆓* | 30 RPM, 6,000 TPM, 14,400 requests/day (org level; varies by model) | https://console.groq.com/docs/rate-limits (surfaced) | Medium (search-summary) |
| LLM API | OpenRouter `:free` models | 🆓* | 20 RPM per free model. 50 requests/day across free models if lifetime credit purchases are under $10; 1,000/day after a one-time $10 purchase | https://openrouter.ai/docs/api_reference/limits (surfaced) | Medium (search-summary) |
| LLM API | Cerebras | 🆓* | 1,000,000 tokens/day, no credit card, 10–30 RPM depending on model | https://inference-docs.cerebras.ai/support/rate-limits (surfaced) | Medium (search-summary; one result mentions a "$5 credit" instead, so the terms may have changed) |
| LLM API | GitHub Models | ❌? | Reportedly retired on 2026-07-30 | https://github.com/robhunter/agentdeals/issues/1672 | Low (third-party GitHub issue only) |
| LLM API | Mistral free tier, Ollama (local) | — | Not researched this round | — | — |
| Design | Figma Starter | 🆓* | "150 AI credits/day, up to 500 AI credits/mo". Education plan: "Yes! Learn more on figma.com/education". File/page limits not shown | https://www.figma.com/pricing/ | High (official) |
| Design | Penpot, Excalidraw | 🆓 (unverified) | Not researched this round | — | Unverified belief |

## Findings

1. GitHub Copilot Free gives "2,000 completions per month" and "Limited chat and agent usage". Pro costs $10/user/month. A GitHub Copilot Student plan exists for verified students. Source: github.com/features/copilot/plans, publisher GitHub, undated page, accessed 2026-09-22. Confidence: high.
2. Cursor Hobby is free with "Limited Agent requests" and "Access to Composer". No numeric limit is published. Pro is $20/month. Source: cursor.com/pricing, publisher Anysphere, accessed 2026-09-22. Confidence: high.
3. windsurf.com/pricing now permanently redirects (308) to devin.ai/pricing, which suggests Windsurf pricing has been folded into Devin/Cognition. I did not verify the free-plan terms. Source: HTTP response, accessed 2026-09-22. Confidence: high for the redirect, none for the terms.
4. Google Antigravity's Individual tier is $0. Its limits depend on capacity, with a weekly rate limit for free users, and no fixed quota is published. Source: search synthesis citing antigravity.google/pricing and the Antigravity blog, accessed 2026-09-22. Confidence: medium.
5. Kiro Free is $0 with 50 credits/month (no rollover). Pro is $20 for 1,000 credits. A free year is offered to students worldwide (kiro.dev/blog/students-2026). Source: search synthesis of kiro.dev/pricing and third-party pages, accessed 2026-09-22. Confidence: medium.
6. Lovable Free gives a daily grant of 5 build credits (up to 30 a month), 20 Cloud credits a month, and 4 in-app AI credits. Source: lovable.dev/pricing, publisher Lovable, accessed 2026-09-22. Confidence: high.
7. v0 Free gives $5 of monthly credits and a 7-message daily limit. Source: search synthesis (v0.app/pricing and third-party pages), accessed 2026-09-22. Confidence: medium.
8. Bolt.new Free gives 1M tokens/month capped at 300K/day. Source: search synthesis (support.bolt.new and third-party pages), accessed 2026-09-22. Confidence: medium.
9. Replit Starter includes daily Agent credits up to a monthly cap. The number is not published. Source: search synthesis (docs.replit.com starter-plan), accessed 2026-09-22. Confidence: medium.
10. Firebase Studio stopped new sign-ups and new workspaces on 2026-06-22 and shuts down on 2027-03-22, so a new team can't adopt it. Source: search synthesis citing firebase.google.com/docs/studio, accessed 2026-09-22. Confidence: medium. Verify on the official page.
11. The Gemini API docs no longer publish a fixed free-tier RPM/TPM/RPD table. Limits are per account and shown in AI Studio. Source: ai.google.dev/gemini-api/docs/rate-limits, publisher Google, accessed 2026-09-22. Confidence: high.
12. Groq's free tier is about 30 RPM / 6K TPM / 14.4K requests per day (org level). Source: search synthesis citing console.groq.com/docs/rate-limits, accessed 2026-09-22. Confidence: medium. Limits vary by model.
13. OpenRouter `:free` models allow 20 RPM and 50 requests/day, rising to 1,000/day after a lifetime purchase of at least $10. Source: search synthesis citing openrouter.ai/docs/api_reference/limits, accessed 2026-09-22. Confidence: medium.
14. Cerebras offers 1M free tokens/day with no card. Source: search synthesis citing inference-docs.cerebras.ai rate limits and third-party pages, accessed 2026-09-22. Confidence: medium. A conflicting "$5 credit" result appeared, so check the current terms.
15. GitHub Models was reportedly retired on 2026-07-30. Source: GitHub issue robhunter/agentdeals#1672 (third party), accessed 2026-09-22. Confidence: low. Don't recommend it until confirmed.
16. Figma Starter includes 150 AI credits/day, up to 500/month. Education plans exist. Source: figma.com/pricing, publisher Figma, accessed 2026-09-22. Confidence: high.

## Recommended $0 stack (derived)

- **Editor/assistant:** Google Antigravity ($0 Individual) or Copilot Free (2,000 completions/month) as the everyday IDE. Use Kiro's 50 credits or Cursor Hobby as backups. Students should first check the Copilot Student plan and Kiro's free year.
- **Agent (to verify):** an OSS CLI agent (OpenCode/Aider/Cline) pointed at a free LLM API. This wasn't evidenced this round.
- **Free LLM backends:** Cerebras (1M tokens/day) and Groq (14.4K requests/day) for speed. Use Gemini API free tier with limits checked in AI Studio. OpenRouter `:free` only at 50/day unless someone spends $10.
- **Prototype UI:** Spread the team's first screens across v0 ($5/month), Bolt (300K tokens/day) and Lovable (5 credits/day). Each account's allowance is small, so every member can use their own account. Avoid Firebase Studio because it's closing.
- **Design:** Figma Starter (150 AI credits/day). Penpot/Excalidraw are OSS alternatives but weren't verified this round.

## Repo slugs

- robhunter/agentdeals (issue #1672: GitHub Models retirement claim)
- ClawLabsAI/free-ai-models (daily-updated list of free LLM APIs; surfaced, not fetched)
- Not verified this round: sst/opencode, cline/cline, Aider-AI/aider, All-Hands-AI/OpenHands, block/goose, Kilo-Org/kilocode, penpot/penpot, excalidraw/excalidraw, ollama/ollama. These are from memory, so confirm them before citing.

## Not found

- Windsurf (now devin.ai) free-plan terms: redirect not followed.
- Zed AI and JetBrains AI free tiers: not searched.
- Any OSS agent requirements (OpenCode, Cline, Aider, OpenHands, Goose, Kilo Code): not searched.
- Mistral free tier and Ollama: not searched.
- Penpot and Excalidraw: not searched.
- Numeric free-tier limits for Gemini API, Cursor Hobby, Replit Starter and Antigravity: vendors don't publish fixed numbers.
- Official confirmation of GitHub Models retirement and of Firebase Studio's sunset dates.
