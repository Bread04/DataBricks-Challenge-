# 🆓 Free AI Dev Tools (cost-tagged)

<!-- markdownlint-disable MD013 -->

> What a team can use for **$0** in September 2026: coding assistants, app builders, free LLM APIs and design tools. From the MCP & tools research run (2026-09-22); sources are in [`evidence.md`](evidence.md).

**Tags:** 🆓 free / open source · 🆓* free tier with limits · 💳 trial only · 💰 paid.
**Conf:** H = official pricing page · M = search summary of official or third-party pages (verify before relying on it).

---

## ⚠️ Gone or going

| Tool | Status | Source |
| --- | --- | --- |
| **GitHub Models** | ❌ **Fully retired 2026-07-30**: playground, catalog, inference API and BYOK are gone for everyone | [GitHub changelog](https://github.blog/changelog/2026-07-30-github-models-is-now-retired/) (H) |
| **Firebase Studio** | ❌ No new sign-ups or workspaces since 2026-06-22; **shuts down 2027-03-22**. Google suggests Antigravity or AI Studio | [Firebase docs](https://firebase.google.com/docs/studio/migrating-project) (H) |
| **Gemini CLI** | ❌ Free/individual service ended 2026-06-18, replaced by the closed-source Antigravity CLI | See `../../06-repo-catalog/` F20 |
| Windsurf | ⚠️ windsurf.com/pricing now redirects to devin.ai; free terms not verified | (H for the redirect) |

---

## Coding assistants

| Tool | Tag | Free allowance | Conf |
| --- | --- | --- | --- |
| **GitHub Copilot Free** | 🆓* | **2,000 completions/month**, limited chat and agent use. Verified students get the **Copilot Student** plan | H |
| **Google Antigravity** | 🆓* | Individual tier **$0**; capacity-based **weekly** rate limit, no fixed quota published | M |
| Cursor Hobby | 🆓* | "Limited agent requests", no number published | H |
| Kiro | 🆓* | 50 credits/month; **students get a free year** | M |
| Claude Code | 💳/💰 | **Not on the Free plan**; Pro $20/month or an API key | H |

## Open-source agents (🆓 software; you supply the model)

OpenCode, Cline, Aider, OpenHands, Goose and Kilo Code are free to run. Pair them with a free LLM API (below) or a local model. Their star counts and status are in [`repos.md`](repos.md) and `../../06-repo-catalog/` (for example OpenCode moved to `anomalyco/opencode`, and Goose to `aaif-goose/goose`). Their setup requirements weren't researched this run.

## App builders (use each teammate's own free account)

| Tool | Tag | Free allowance | Conf |
| --- | --- | --- | --- |
| **Lovable** | 🆓* | **5 build credits/day (up to 30/month)** + 20 Cloud credits/month | H |
| v0 (Vercel) | 🆓* | $5 monthly credits + 7 messages/day | M |
| Bolt.new | 🆓* | 1M tokens/month, max 300K/day | M |
| Replit Agent (Starter) | 🆓* | Daily credits up to a monthly cap (number not published) | M |

## Free LLM APIs (for your app or an OSS agent)

| Provider | Tag | Free allowance | Conf |
| --- | --- | --- | --- |
| **Gemini API** | 🆓* | Free tier on Flash models. **Limits are no longer published; check them in AI Studio.** Free-tier data is used to improve Google's products | H |
| **Cerebras** | 🆓* | ~1M tokens/day, no card (one source mentions a "$5 credit" instead) | M |
| **Groq** | 🆓* | ~30 RPM, 6K TPM, 14.4K requests/day (varies by model) | M |
| OpenRouter `:free` models | 🆓* | 20 RPM; **50 requests/day**, or 1,000/day after a one-time $10 purchase | M |
| Local models (Ollama, llama.cpp) | 🆓 | Unlimited; limited by your hardware | See `../../04-ai-and-rag/docs/repos.md` |
| Claude / OpenAI APIs | 💰 | Pay-as-you-go (small signup credits) | `../../04-ai-and-rag/docs/model-selection.md` |

## Design & prototyping

| Tool | Tag | Free allowance | Conf |
| --- | --- | --- | --- |
| **Figma Starter** | 🆓* | 150 AI credits/day (max 500/month); education plans exist. ⚠️ **Figma MCP needs a paid seat** | H |
| Excalidraw | 🆓 | Open source | Repo (see `../../01-hackathon-playbook/docs/repos.md`) |
| Penpot | 🆓 | Open-source Figma alternative | Not researched this run |
| Google Stitch | 🆓* (unverified) | See `stitch-mcp.md` | M |

---

## 🧰 The $0 stack

| Need | Pick |
| --- | --- |
| Editor + assistant | **Antigravity** ($0) or **Copilot Free**; students should claim Copilot Student and Kiro's free year |
| Terminal agent | **OpenCode** or Cline + a free API below |
| LLM for your app | **Gemini free tier** (check limits in AI Studio) · **Cerebras** / **Groq** for speed · **Ollama** offline |
| First UI draft | Spread across **Lovable** (5/day), **v0** ($5/month) and **Bolt** (300K tokens/day), one account per teammate |
| Design | **Figma Starter** + Excalidraw |
| MCP servers | The $0 set in [`mcp-catalog.md`](mcp-catalog.md) |
| Hosting | Vercel Hobby, Supabase Free, Cloudflare Workers (see `../../skills/hackathon-deployment/SKILL.md`) |
