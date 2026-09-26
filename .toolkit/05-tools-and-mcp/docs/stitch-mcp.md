# 🧵 Stitch MCP Manual (Design → Code Sync)

<!-- markdownlint-disable MD013 -->

Connect Google Stitch to Claude Code and turn Stitch designs into tokens and components. Verified 2026-09-21.

> [!WARNING]
> **Test this before the event.** The official endpoint is confirmed, but [claude-code issue #41664](https://github.com/anthropics/claude-code/issues/41664) (opened 2026-03-31, closed as "not planned" and marked a duplicate) reports that Claude Code **ignores the `X-Goog-Api-Key` header** and attempts OAuth discovery. That fails with `Incompatible auth server: does not support dynamic client registration`. If you hit it, use **Option B**.

---

## What "sync" really means

The sync is **one-way: Stitch → code.** The agent pulls design context (palette, typography, tokens, layout rules) and screen HTML/CSS out of Stitch. No source found shows edits flowing from code back into Stitch. After you change a design in Stitch, **pull it again** ([Google Codelab](https://codelabs.developers.google.com/design-to-code-with-antigravity-stitch)).

---

## Option A: Official Google remote server

| | |
| --- | --- |
| Endpoint | `https://stitch.googleapis.com/mcp` |
| Auth | `X-Goog-Api-Key: <key>` header |
| Get a key | Stitch → Profile → Settings → API key (stitch.withgoogle.com/settings) |
| Official docs | [stitch.withgoogle.com/docs/mcp/setup](https://stitch.withgoogle.com/docs/mcp/setup) (renders with JavaScript; open it in a browser) |

```bash
claude mcp add stitch --transport http https://stitch.googleapis.com/mcp \
  --header "X-Goog-Api-Key: $STITCH_API_KEY" -s user
```

Evidence: the endpoint and command appear in third-party guides ([SOTAAZ](https://sotaaz.com/post/stitch-mcp-guide-en)) and in the Claude Code issue's config. They weren't read from Google's JavaScript-rendered docs page.

---

## Option B: Community proxy (fallback)

**[davideast/stitch-mcp](https://github.com/davideast/stitch-mcp)** (⭐ 969 · pushed 2026-05-28). ⚠️ The README says it is **"NOT affiliated with, endorsed by, or sponsored by Google LLC"**, and that it's experimental and provided as is.

```bash
npx @_davideast/stitch-mcp init        # wizard: gcloud / OAuth / API key
claude mcp add -e GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID -s user stitch -- npx -y @_davideast/stitch-mcp proxy
```

| Auth option | How |
| --- | --- |
| Wizard | `init` (gcloud / OAuth) |
| API key | `STITCH_API_KEY` env var |
| System gcloud | `STITCH_USE_SYSTEM_GCLOUD=1` |

**Extra virtual tools:** `build_site` (maps screens to routes), `get_screen_code`, `get_screen_image`. It also passes through upstream Stitch tools such as `list_projects`, `list_screens`, `extract_design_context` and `generate_screen_from_text`. A GCP project is required, and the README summary mentions billing being enabled.

Another community option is [Kargatharaakash/stitch-mcp](https://github.com/Kargatharaakash/stitch-mcp) (⭐ 122 · last push 2026-02, less active). Its tools are `extract_design_context` ("Design DNA"), `fetch_screen_code`, `fetch_screen_image` and `generate_screen_from_text`.

---

## Workflow: Stitch → DESIGN.md → Tailwind tokens → components

```text
1. DESIGN    stitch.withgoogle.com: prompt or voice 2–3 directions for the demo screen; pick one
2. CONNECT   add the MCP server (Option A, else B)
3. PULL      "List my Stitch projects and screens. Extract the design context for <screen>."
4. SPEC      "Write DESIGN.md: hex/OKLCH palette with names, type scale, spacing rules, radii, component notes."
5. TOKENS    "Convert DESIGN.md into Tailwind v4 @theme primitives + @theme inline semantics." (Frontend PROMPTS F2)
6. CODE      "Fetch the screen code for <screen> and port it to React + shadcn using our tokens only."
7. VERIFY    Playwright MCP screenshots at 375 / 1280 px; /impeccable audit
8. ITERATE   Change it in Stitch → repeat steps 3–6 (one-way sync)
```

`DESIGN.md` is the single source of truth. Google has open-sourced Stitch's DESIGN.md format, so it carries design intent to any coding agent ([Google](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/), search snippet only).

---

## Prompts

```text
Using the Stitch MCP: list my projects, then for screen "<name>" extract the design context.
Write DESIGN.md with: named colour tokens (hex + oklch) and their WCAG contrast vs the main surface, font families and a type scale, spacing scale, radii, shadows, and per-component notes (button, input, card).
Flag any colour pair that fails 4.5:1 for text or 3:1 for UI.
```

```text
Fetch the code for Stitch screen "<name>". Port it to a Next.js page using shadcn components and ONLY our @theme tokens — replace every hard-coded colour/size with the nearest token and list the replacements. Keep semantic HTML and accessibility intact.
```

---

## Unknowns (updated 2026-09-22)

- Stitch API/MCP **quotas and pricing** weren't found; only community listings call it free.
- **Issue #41664 is still not fixed.** It was closed as a duplicate rather than resolved, and a related regression (header auth falling into OAuth discovery) is reported in [#78534](https://github.com/anthropics/claude-code/issues/78534) as still present in **Claude Code v2.1.211**. Expect Option A to fail and plan on Option B; the stdio proxy also hasn't been tested.
- The exact contents of Google's official MCP setup page (it renders with JavaScript).
