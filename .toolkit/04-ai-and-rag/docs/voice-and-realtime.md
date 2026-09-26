# 🎙️ Voice & Realtime AI

<!-- markdownlint-disable MD013 -->

> How to build a talking demo (voice agent, live transcription, spoken assistant) in 24–48 hours. From the Deepen research run (2026-09-22); sources are in [`evidence.md`](evidence.md) under "Voice and realtime AI".

---

## Pick your architecture

| Path | How it works | Choose when | Cost |
| --- | --- | --- | --- |
| **A · Speech-to-speech API** | Browser ↔ WebRTC ↔ **OpenAI `gpt-realtime`** (or Gemini 3.8 Live) | Fastest "wow"; natural interruptions; one vendor | `gpt-realtime` audio: **$32 in / $64 out per 1M tokens**, so set a spend cap |
| **B · Cascade (STT → LLM → TTS)** | Deepgram STT → **Claude** (or any LLM) → ElevenLabs/Deepgram TTS, orchestrated by **Pipecat** or **LiveKit Agents** | You want Claude as the brain, tool use, or control of each stage | Deepgram **$200 free credit** covers STT and TTS for the event |
| **C · Hosted voice agent** | Vapi or Retell | Phone-call demos, or teams without backend time | About $10 trial credit each (third-party figure) |

> [!NOTE]
> **No public Anthropic realtime speech-to-speech API was found** (as of 2026-09-22). To use Claude in a voice demo, use path B.

---

## Components (verified prices)

| Stage | Option | Price / free tier | Notes |
| --- | --- | --- | --- |
| Realtime S2S | OpenAI `gpt-realtime` (GA, snapshot 2025-08-28) | $32 / $64 per 1M audio tokens; $0.40 cached | WebRTC, WebSocket or SIP |
| Realtime S2S | Gemini 3.8 Live | Pricing not verified | Older Live previews are now "legacy" |
| STT (streaming) | Deepgram Nova-3 / Flux | $0.0048–$0.0078 per min; **$200 free, no card** | Also Aura-1 TTS at $0.015 per 1K characters |
| STT (realtime) | ElevenLabs Scribe v2 Realtime | $0.39 per hr (~150 ms) | — |
| TTS | ElevenLabs Flash/Turbo | $0.05 per 1K characters (~75 ms) | Free quota not stated on the page |
| TTS | Cartesia Sonic | 20K free credits (third-party figure) | Claims <90 ms |
| TTS (offline) | [Kokoro-82M](https://github.com/hexgrad/kokoro) | Free, Apache-licensed | Backup if venue Wi-Fi dies; repo code last pushed 2025-08 |
| Orchestration | [Pipecat](https://github.com/pipecat-ai/pipecat) (15.8k ⭐) | OSS | Python pipelines, cascade or S2S |
| Orchestration | [LiveKit Agents](https://github.com/livekit/agents) (14.3k ⭐) | OSS | WebRTC-native agents with plugins |
| ❌ Avoid | Vocode | — | Last push 2024-11 |

---

## Demo-day gotchas (these kill voice demos)

- **HTTPS or localhost only.** `getUserMedia` fails in insecure contexts, so a LAN IP over `http://` has **no microphone**. Deploy (Vercel) or tunnel ([cloudflared](https://github.com/cloudflare/cloudflared)).
- **Trigger the mic permission before you go on stage.** Handle `NotAllowedError` with a visible message, not a silent failure.
- **Iframes need `allow="microphone"`**, which matters for embedded demos (for example Devpost or slides).
- **Use headphones** to avoid echo feedback loops. (Echo-cancellation constraints weren't verified in the research.)
- **Budget guard:** cap spend on the realtime API key and rate-limit the endpoint (`../../03-backend/docs/security.md`).
- **Fallback:** record the conversation for the backup video, and keep Kokoro or pre-recorded audio behind `DEMO_MODE`.

---

## Prompts

```text
VOICE-1 · Speech-to-speech demo: Build a Next.js page that connects to OpenAI gpt-realtime over WebRTC (ephemeral key minted by a server route; never ship the API key). Push-to-talk + barge-in, live transcript panel, visible "listening/thinking/speaking" states, NotAllowedError handling, and a per-session spend cap.
```

```text
VOICE-2 · Claude voice cascade: Using Pipecat (Python), wire Deepgram streaming STT → Claude (pinned model, short system prompt, tools: <list>) → ElevenLabs Flash TTS. Target <1s turn latency: stream tokens into TTS, interrupt on user speech. Deploy the bot on Railway; expose a WebRTC transport the web client joins.
```

Related: [`multimodal-pipelines.md`](multimodal-pipelines.md) (heavy media analysis), [`model-selection.md`](model-selection.md) (LLM choice), [`repos.md`](repos.md) → Voice & realtime.
