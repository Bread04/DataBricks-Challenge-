# 🎥 Multi-Modal Analysis Pipelines

<!-- markdownlint-disable MD013 -->

> For hackathon projects that analyse real-world media (video, audio, documents) and turn signals into feedback. Adapted from [help-me-papi](https://github.com/maxi-cmyk/help-me-papi) `AI/skills/modeling.md`. The pattern comes from **it'sPEAK**, a 24-hour hackathon project: a public-speaking coach built with FastAPI, Celery, MediaPipe, Librosa, OpenAI, Supabase and Vercel.

---

## Architecture

The analysis is too heavy for a request/response cycle, and Vercel Hobby functions cap at 300 s ([Vercel](https://vercel.com/docs/functions/limitations)). Use a queue and a worker:

```text
Browser ──upload──▶ Supabase Storage (signed upload URL; avoids Vercel's 4.5 MB body limit)
   │                         │
   └─POST /jobs─▶ FastAPI (Railway) ──enqueue──▶ Redis ──▶ Worker (Celery / BullMQ)
                                                           │  FFmpeg · MediaPipe · Librosa → metrics
                                                           │  LLM narrates the metrics
                                                           ▼
                                            Supabase (results table) ──Realtime / poll──▶ UI
```

---

## Six rules

### 1 · Run deterministic pre-checks first

Run cheap checks **before** spending tokens or GPU time, and reject bad input with a clear message:

| Media | Pre-checks |
| --- | --- |
| Video | Framing, lighting, face visible, duration |
| Audio | Level, clipping, silence, sample rate, channel count, signal-to-noise |
| Document | File type, size, OCR confidence |

### 2 · The LLM narrates facts; it doesn't invent them

- Pass **structured metrics** as the prompt context (for example pace in words per minute, pitch variation in Hz, filler-word count, eye-contact %).
- Instruct it: *"Base feedback only on these metrics. Do not make claims about personality, emotion or medical state."*
- Use structured output, validated before display.

### 3 · Always have a deterministic fallback

If the LLM fails or times out, produce feedback from **rule-based templates keyed on the metrics**. The demo must never show a blank screen.

### 4 · Separate scoring from narration

- **Scoring** is deterministic, so unit-test it.
- **Narration** is LLM-generated, so evaluate it with a golden set.
- Build a small golden set of (input, expected metrics, expected feedback highlights) and re-run it after every prompt or model change.
- **Pin the exact model ID.** A floating alias can silently change behaviour.

### 5 · Keep the worker clean

- Heavy ML libraries (MediaPipe, Librosa, FFmpeg) **leak memory across jobs**, so restart the worker after each full analysis. A durable queue (Redis) means no job is lost.
- **One job at a time per worker.** Concurrency fights over memory or GPU and hurts accuracy.
- Temporary artefacts (extracted audio, landmark files) should expire (for example after 24 h). Final reports live in Supabase.

### 6 · Be honest about what you're classifying

Results describe **observable signals**. State explicitly that the output is **not** a medical, psychological, personality or employment assessment. It keeps the product honest, and judges notice when claims are responsible.

---

## Hackathon build order

1. **Hour 1:** upload → store → a fake "analysis complete" result shown in the UI (walking skeleton).
2. Pre-checks plus **one** real metric, end to end.
3. LLM narration of that metric, with the rule-based fallback.
4. More metrics, one at a time, as time allows.
5. Pre-record 2–3 demo inputs whose results you know are good (see `../PROMPTS-ML.md` ML7).

Deploy commands are in `../../skills/hackathon-deployment/SKILL.md` (Railway worker + Vercel frontend). Prompt: `../../03-backend/PROMPTS.md` B13.

---

## Product lesson from Echo (a dementia-therapy PWA)

help-me-papi also records a design principle from its Echo hackathon project: **"prioritise familiar memories over novelty"**. The AI acts as an *adaptation engine* for the user's state (for example voice-adaptive and sundowning modes), not just a content generator. When the users are vulnerable, design the AI around their needs and limits, not around what the model can do.
