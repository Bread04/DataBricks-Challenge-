# ✍️ Prompt Engineering Standards

<!-- markdownlint-disable MD013 -->

> Combines Anthropic's and OpenAI's official guidance, with the 2026 breaking changes. Verified 2026-09-21.

---

## ⚠️ Breaking changes to know (Claude)

| Change | What to do instead | Source |
| --- | --- | --- |
| **Prefilling the assistant turn returns a 400 error from Claude 4.6 onward** | JSON → **Structured Outputs** or a tool schema. Classification → a tool with an `enum` field. Preamble → "Respond directly without preamble." in the system prompt | [Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) |
| `budget_tokens` replaced by **`effort`** for thinking | Set `effort`; on Opus 5, prefer thinking on at low effort over thinking off | same |

---

## Before you write a prompt

From [Anthropic's overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview):

1. **Success criteria:** what does a good output look like?
2. **A way to test it:** 10–20 real inputs you can re-run.
3. **A first draft.** The metaprompt generator in [claude-cookbooks](https://github.com/anthropics/claude-cookbooks) can write one.

Some latency and cost problems are better fixed by **changing the model** than by rewriting the prompt.

---

## The ten rules

| # | Rule | Source |
| --- | --- | --- |
| 1 | **Be clear and direct.** Golden rule: would a colleague with little context understand it? | Anthropic |
| 2 | **Explain why.** Give the reason behind each constraint | Anthropic |
| 3 | **Role in the system prompt**, one sentence | Anthropic |
| 4 | **XML-tag each kind of content:** `<instructions>`, `<context>`, `<input>`, `<documents>` | Anthropic; OpenAI also recommends XML for content boundaries |
| 5 | **3–5 examples**, relevant and diverse, wrapped in `<example>` tags | Anthropic; OpenAI (few-shot) |
| 6 | **Long documents first, query last** (for 20k+ tokens). Anthropic reports up to 30% better responses in its tests (single vendor figure) | Anthropic |
| 7 | **Quote first, then answer:** extract relevant quotes into `<quotes>` before answering | Anthropic |
| 8 | **Say what to do, not what not to do**; match the prompt's style to the output style you want | Anthropic |
| 9 | **OpenAI developer message order: Identity → Instructions → Examples → Context**; the `developer` role outranks `user` | [OpenAI](https://developers.openai.com/api/docs/guides/prompt-engineering) |
| 10 | **Stable content first** so prompt caching applies | Anthropic + OpenAI |

Model-type note (OpenAI): reasoning models do best with a **high-level goal**, while GPT (non-reasoning) models need **precise, explicit steps**.

---

## Canonical prompt skeleton

```text
SYSTEM (Anthropic) / developer (OpenAI):
You are <role in one sentence>. <Who the output is for and why it matters.>

<instructions>
1. <step — say what TO do>
2. <step>
If the answer is not in the documents, say so plainly.
Respond directly without preamble.
</instructions>

<examples>
  <example><input>…</input><output>…</output></example>
  <example><input>…</input><output>…</output></example>
  <example><input>…</input><output>…</output></example>
</examples>

USER:
<documents>
  <document index="1">
    <source>{{SOURCE}}</source>
    <document_content>{{CONTENT}}</document_content>
  </document>
</documents>

First extract the relevant quotes into <quotes>. Then answer inside <answer>.
<question>{{QUERY}}</question>
```

For **JSON output**, don't prefill `{`. Pass a schema through Structured Outputs, or define a tool whose input schema is the object you want.

---

## Reasoning and tools

- To show the model *how* to reason, include `<thinking>` in few-shot examples. A manual `<thinking>`/`<answer>` split is a fallback when native thinking is off.
- The latest Claude models make **parallel tool calls**. Anthropic publishes a `<use_parallel_tool_calls>` system-prompt block that pushes this to about 100%.
- Tool descriptions are prompts too: say when to use the tool, when *not* to, and what the fields mean.

Source: [Anthropic best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

---

## Hackathon prompt hygiene

- [ ] Prompts live in files (`prompts/*.md` or constants), not scattered through components
- [ ] Each prompt has 5–10 saved test inputs you re-run after edits
- [ ] No secrets in system prompts
- [ ] Output validated with a Zod schema before use
- [ ] Demo inputs rehearsed. The same input can give different output, so pick inputs that reliably produce good results

---

## References

- [Anthropic: Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [Anthropic: Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [OpenAI: Prompt engineering guide](https://developers.openai.com/api/docs/guides/prompt-engineering)
- [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks): ⭐ 52.9k · pushed 2026-09-18 (note the plural name)
- *Not covered:* Google's prompting guide wasn't fetched in this research.
