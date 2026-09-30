# Citation spot-check (2026-09-21)

10 load-bearing claims in research.md, each checked against the URL in the report's source appendix.

| ref | claim | supported? | note |
|---|---|---|---|
| [5] | ETHGlobal: AI must be disclosed; giant single commits risk DQ; no AI voiceover | yes | Tokyo 2026 details page: "Clearly document ... where and how AI tools were used"; "Submissions with large single commits or missing histories may be disqualified"; "DO NOT use a text to speech synthesizer / AI Voiceover". |
| [6] | MLH: AI allowed with transparency; no pre-event code; video 2 min or less naming the event | yes | "be honest and transparent about the AI code tools they used"; no re-use of previously worked project code (libraries/OSS allowed); "2 minute or less demo video" that "must state the name of the hackathon at the beginning". Small nuance: pre-existing libraries/open source are allowed, so "no pre-event code" means no project code written earlier. |
| [8] | CWV good thresholds LCP 2.5s / INP 200ms / CLS 0.1 | yes | web.dev/articles/vitals, measured at the 75th percentile. |
| [21] | RFC 9457 obsoletes 7807; members type/title/status/detail/instance | yes | "This document obsoletes RFC 7807"; defines all five members. |
| [24] | Supabase: Clerk JWT-template integration deprecated since 2025-04-01; third-party auth; role = authenticated | yes | "As of 1st April 2025 the previously available Clerk Integration with Supabase is considered deprecated"; authenticated users should carry the `authenticated` role claim. |
| [27] | Next.js 16 renamed middleware.ts to proxy.ts | partial | The cited BFF guide (v16.3.5) uses `proxy.ts` / `export function proxy` throughout and says "Third-party libraries may still refer to `proxy` as `middleware`". It does not state the rename or which version made it. A better source is the proxy file-convention page or the v16 upgrade guide. |
| [34] | Pricing: Sonnet 5 $2/$10, Opus 5 $5/$25, Haiku 4.5 $1/$5 | yes | Pricing table matches. A note says Sonnet 5's $2/$10 introductory price is now the standard price (the planned rise to $3/$15 was cancelled). |
| [38] | Claude 4.6+ does not support prefill (returns 400) | yes | "Starting with Claude 4.6 models ... prefilled responses ... on the last assistant turn are no longer supported. Requests with prefilled assistant messages to these models return a 400 error." Applies only to the last assistant turn. |
| [42] | Supabase hybrid search uses RRF with k=50 | yes | "`rrf_k` is the k smoothing constant ... The default is 50." |
| [47] | "Magic MCP is now the 21st MCP"; tools generate/get_inspiration/search_logo; keys reset | yes | README says exactly that. Old Magic API keys were invalidated. The tools also include `search`, and legacy tool names are still translated to the new ones. |

**Totals:** 9 yes, 1 partial, 0 no, 0 unreachable.
