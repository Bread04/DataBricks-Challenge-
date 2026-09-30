# Deepen: Voice / Realtime AI demo stack (hackathon, 24–48h)

Run date: 2026-09-22. Budget: 12 research calls (11 web + 1 tool load). Two fetches failed (github.com ECONNREFUSED for livekit/agents and pipecat-ai/pipecat).
Class key: P = primary/official vendor page; S = secondary (press/blog/aggregator); D = derived.

## Findings

1. OpenAI `gpt-realtime` is described as "our first general-availability realtime model", snapshot `gpt-realtime-2025-08-28`; the model page lists no mini variant or successor. | https://developers.openai.com/api/docs/models/gpt-realtime | OpenAI | undated page (snapshot 2025-08-28) | accessed 2026-09-22 | medium (the fetch tool summarized the page; a newer model could be listed elsewhere) | P
2. `gpt-realtime` audio pricing: $32 per 1M input tokens, $64 per 1M output tokens, $0.40 per 1M cached input tokens. | same as #1 | OpenAI | undated | accessed 2026-09-22 | medium | P
3. `gpt-realtime` takes audio and text in realtime over WebRTC, WebSocket or SIP. | same as #1 | OpenAI | undated | accessed 2026-09-22 | high | P
4. Google names "Gemini 3.8 Live" and "3.8 Live Extended Thinking" as its latest realtime voice models. The Gemini API docs call the older Live preview models legacy and recommend moving to 3.8 Live. Search snippets also claim Extended Thinking ranks #1 on Artificial Analysis' Speech-to-Speech leaderboard. | https://blog.google/innovation-and-ai/technology/developers-tools/build-real-time-voice-applications-gemini-audio/ ; https://ai.google.dev/gemini-api/docs/models | Google | 2026 (exact date not retrieved) | accessed 2026-09-22 | medium (search snippets only, pages not fetched) | P (snippet)
5. The Gemini Live API has native audio output and can also be reached through Firebase AI Logic (client SDK) and Vertex AI. | https://ai.google.dev/gemini-api/docs/live-api/capabilities ; https://firebase.google.com/docs/ai-logic/live-api | Google | 2026 | accessed 2026-09-22 | medium (snippet) | P (snippet)
6. Anthropic's voice features are consumer and Claude Code features: voice mode (beta, all plans, on mobile/desktop/web), with model choice (Opus/Sonnet/Haiku) added 2026-07-23, plus Claude Code voice dictation. **No public Anthropic realtime speech-to-speech API was found.** | https://techcrunch.com/2026/07/23/anthropic-updates-claude-voice-mode-with-more-capable-models/ ; https://support.claude.com/en/articles/11101966-use-voice-mode ; https://code.claude.com/docs/en/voice-dictation | TechCrunch / Anthropic | 2026-07-23 | accessed 2026-09-22 | medium (absence of evidence, snippet-level) | S/P
7. ElevenLabs API: Flash/Turbo TTS costs $0.05 per 1K characters, with "ultra-low latency (~75ms)". v3 costs $0.10 per 1K characters. Scribe v2 Realtime STT costs $0.39/hr at about 150ms. The agents product ("Speech Engine") costs $0.08/min. There is a Free/pay-as-you-go option, but the page did not state the free quota. | https://elevenlabs.io/pricing/api | ElevenLabs | undated | accessed 2026-09-22 | high for prices, low for free quota | P
8. Deepgram gives new users $200 of free credit, with no credit card needed for pay-as-you-go. Streaming STT (Nova-3, Flux) costs $0.0048–$0.0078/min. Aura-1 TTS costs $0.015 per 1K characters. The Voice Agent API starts at $0.075/min. | https://deepgram.com/pricing | Deepgram | undated | accessed 2026-09-22 | high | P
9. Cartesia Sonic has a free tier of 20,000 credits with no card (about 27 TTS minutes at 1 credit per character). Paid plans run $5–$299/mo. Cartesia claims under 90ms model latency. A third party reports about 166ms median including network (Vapi, June 2026). | https://invideo.io/blog/cartesia-sonic-ai-voice/ ; https://www.cloudtalk.io/blog/cartesia-pricing/ | third-party blogs | 2026 | accessed 2026-09-22 | low-medium (Cartesia's own page not fetched) | S
10. Kokoro-82M is an open-weight TTS model with 82M parameters and Apache-licensed weights. The model card cites an API market rate under $1 per 1M characters (as of April 2025). | https://huggingface.co/hexgrad/Kokoro-82M ; https://github.com/hexgrad/kokoro | hexgrad | 2025 | accessed 2026-09-22 | medium (snippet) | P (snippet)
11. Vapi gives new accounts about $10 of one-time trial credit. Self-serve pricing starts at $0.05/min, with model, TTS and telephony costs extra. | https://www.layer3labs.io/guides/vapi-pricing ; https://www.cloudtalk.io/blog/vapi-ai-pricing/ | third-party | 2026 | accessed 2026-09-22 | low-medium | S
12. Retell AI gives new accounts $10 of free credit (about 67–90 min at realistic rates), 20 free concurrent calls and 10 knowledge bases. The base rate is $0.07/min, but the all-in cost is higher. | https://www.cloudtalk.io/retell-ai-pricing/ ; https://www.layer3labs.io/guides/retell-ai-pricing | third-party | 2026 | accessed 2026-09-22 | low-medium | S
13. `getUserMedia()` works only in secure contexts: HTTPS, `localhost`, or `file:///`. In an insecure context `navigator.mediaDevices` is undefined, so the call fails with a TypeError. | https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia | MDN | undated | accessed 2026-09-22 | high | P
14. Browsers always ask the user for mic permission. `NotAllowedError` is thrown when access is denied or the page is insecure. Only top-level documents can request permission; an iframe needs `allow="microphone"` (Permissions-Policy). | same as #13 | MDN | undated | accessed 2026-09-22 | high | P

## Recommended hackathon stack (derived)

- **Fastest path to a talking demo in the browser:** OpenAI `gpt-realtime` over WebRTC, straight from the browser [#1, #3]. Costs are per audio token ($32 in / $64 out per 1M) [#2], so set a spending cap. The alternative is Gemini Live (3.8 Live) through Firebase AI Logic for a client-side build [#4, #5]. Pick based on which one gives you free credits at the event.
- **Claude as the "brain":** there is no public Anthropic realtime voice API [#6]. Build a cascade instead: Deepgram streaming STT, then Claude, then ElevenLabs Flash or Cartesia TTS [#7, #8, #9], wired together with a framework (LiveKit Agents or Pipecat; status not verified this run, see Not found).
- **Near-zero cost:** Deepgram's $200 credit covers STT and TTS (Aura-1) for the whole event [#8]. Kokoro-82M works as offline/local TTS backup if the Wi-Fi fails [#10].
- **Phone-call demos or non-coders:** Vapi or Retell, each with about $10 free, roughly 1 hour of calls [#11, #12].
- **Demo-day gotchas:** deploy on HTTPS (for example a Vercel/ngrok tunnel), because a LAN IP over http has no mic access [#13]. Trigger the permission prompt before going on stage and handle `NotAllowedError` [#14]. Don't embed the demo in an iframe without `allow="microphone"` [#14]. Use headphones to avoid echo (echo-cancellation constraints were not verified this run).

## Repo candidates

| category | exact owner/repo slug | hackathon use | evidence URL |
|---|---|---|---|
| Voice-agent framework | livekit/agents | WebRTC voice agents with STT/LLM/TTS or realtime plugins | https://github.com/livekit/agents (fetch failed; slug from URL only) |
| Voice-agent framework | pipecat-ai/pipecat | Python pipeline for cascaded or speech-to-speech bots | https://github.com/pipecat-ai/pipecat (fetch failed; slug from URL only) |
| Local TTS | hexgrad/kokoro | Offline Apache-licensed TTS (82M) | https://github.com/hexgrad/kokoro |

## Not found / unverified

- LiveKit Agents and Pipecat: release versions, activity and plugin lists (github.com refused the connection). Vocode status was not researched.
- OpenAI TTS (gpt-4o-mini-tts etc.) pricing and a possible `gpt-realtime-mini` (neither found on the model page fetched).
- Gemini Live pricing, free tier and exact model IDs.
- ElevenLabs free-tier character quota. Cartesia's official pricing page (only third-party sources used).
- AssemblyAI Universal-Streaming pricing. Realtime suitability of Whisper, faster-whisper and WhisperX (not researched).
- WebRTC echo-cancellation constraint behavior and an end-to-end latency budget (no source fetched).
