# 🤖 Model Selection & LLM Feature Macros

<!-- markdownlint-disable MD013 -->

> Copy-paste prompts for picking models, costing features and building LLM calls. Reference: `docs/model-selection.md` · `docs/prompt-engineering.md` · `docs/agents-and-tool-use.md`

---

## Contents

| Code | Macro |
| --- | --- |
| [ML1](#ml1--pick-a-model) | Pick a model |
| [ML2](#ml2--cost-the-feature) | Cost the feature |
| [ML3](#ml3--write-a-production-prompt) | Write a production prompt |
| [ML4](#ml4--structured-output-endpoint) | Structured output endpoint |
| [ML5](#ml5--streaming-chat-route) | Streaming chat route |
| [ML6](#ml6--prompt-test-harness) | Prompt test harness |
| [ML7](#ml7--demo-proof-the-ai-feature) | Demo-proof the AI feature |
| [ML8](#ml8--eda--preprocessing) | EDA + preprocessing (classic ML) |
| [ML9](#ml9--training-loop) | Training loop (classic ML) |
| [ML10](#ml10--model-failure-analysis) | Model failure analysis |
| [ML11](#ml11--routing--cascade) | Routing / cascade |
| [ML12](#ml12--scaffold-a-capped-agent) | Scaffold a capped agent (AI SDK v7 / Pydantic AI) |
| [ML13](#ml13--design-the-tools) | Design the tools |
| [ML14](#ml14--agent-safety-and-fallback-review) | Agent safety and fallback review |
| [ML15](#ml15--datathon-tabular-baseline--leak-free-cv) | Datathon: tabular baseline & leak-free CV (Polars + LightGBM/CatBoost) |
| [ML16](#ml16--datathon-what-if-simulator--shap-dashboard) | Datathon: What-If simulator & SHAP explainability dashboard |

> ML8–ML11 and ML15–ML16 are for **data or ML-track hackathons (datathons)**. For the full standalone playbook, templates and code: see [`08-datathon-handbook/`](../08-datathon-handbook/README.md) · Evidence: [`_research/technical-datathons-and-ml-solutions-2026-09-23/`](../_research/technical-datathons-and-ml-solutions-2026-09-23/research.md).

---

### ML1 · Pick a model

```text
Task: <what the model must do>. Volume: <calls/demo, calls/day>. Latency need: <interactive | background>. Budget: <$>.
Using this table (Sep 2026, per 1M in/out):
- Workhorse: Sonnet 5 $2/$10 · GPT-5.6 Terra $2/$12 · Gemini 3.8 Flash $0.75/$3.75 (promo to 2026-12-31)
- Reasoning: Opus 5 $5/$25 · GPT-5.6 Sol $4/$20 (promo) · Gemini 3.1 Pro Preview $2/$12
- Cheap: Haiku 4.5 $1/$5 · GPT-5.6 Luna $0.20/$1.20 · GPT-5-nano $0.05/$0.40 · Gemini 2.5 Flash-Lite $0.10/$0.40
Recommend one primary + one fallback model, split the pipeline by tier if useful (bulk → cheap, judged step → strongest), and say what you'd measure to confirm (quality on 10 test inputs, latency p50).
```

*Prices:* see `docs/model-selection.md`. Re-verify on vendor pages before the event.

### ML2 · Cost the feature

```text
Estimate the cost of <feature> for: the demo (≈<n> calls), a 24h hackathon (≈<n>), and 1,000 users/day.
Assume <model>, avg <in> input / <out> output tokens.
Apply: prompt caching (read = 0.1× input after the first write at 1.25×), Batch 50% off where async is fine, and the ~30% token uplift on Claude 4.7+ tokenizers.
Output a table and the single biggest cost lever.
```

### ML3 · Write a production prompt

```text
Write a system prompt for <task>. Follow these rules:
- One-sentence role; explain WHY constraints matter.
- XML sections: <instructions> (numbered, say what TO do), <examples> (3–5 diverse), then context.
- If documents are involved: documents first in <documents><document><source/><document_content/></document>, question LAST, ask for <quotes> then <answer>.
- "Respond directly without preamble."
- NO assistant prefill (Claude 4.6+ returns 400). For JSON use a schema via structured outputs.
Also give me 8 test inputs (incl. 2 edge cases, 1 adversarial) with expected outputs.
```

*Rules from:* [Anthropic best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), [OpenAI guide](https://developers.openai.com/api/docs/guides/prompt-engineering)

### ML4 · Structured output endpoint

```text
Build a server action/route that calls <model> via the Vercel AI SDK and returns typed JSON matching this Zod schema: <schema>.
- Use the AI SDK's current schema-based structured output API (check the docs via Context7: "use context7"), not prefill or regex parsing.
- Validate again with Zod; on failure retry once, then return RFC 9457 problem (502, "Upstream model returned invalid output").
- Rate-limit per user (10/min). Timeout 30s. Log token usage.
```

### ML5 · Streaming chat route

```text
Create a streaming chat endpoint with the Vercel AI SDK for <model>:
- System prompt from prompts/<name>.md (cached: stable content first).
- Tools: <list with when-to-use descriptions>. Allow parallel tool calls.
- Stream to a shadcn chat UI with loading/error states; stop button; regenerate.
- Per-user rate limit + max tokens cap. Never expose the API key client-side.
```

*SDK:* [vercel/ai](https://github.com/vercel/ai) · For a full chat UI, fork [vercel/chatbot](https://github.com/vercel/chatbot).

### ML6 · Prompt test harness

```text
Create scripts/eval-prompt.ts: loads prompts/<name>.md and tests/<name>.jsonl (input, expected / rubric), runs each case against <model>, and prints pass/fail with a short LLM-judged reason using Haiku 4.5.
I will run it after every prompt edit. Keep it under 80 lines.
```

### ML7 · Demo-proof the AI feature

```text
Our demo calls <model> for <feature>. Make it demo-safe:
1. Pick 3 demo inputs that reliably produce great outputs (run each 5× and report variance).
2. Add a cached/recorded response fallback behind DEMO_MODE=true for when the API is slow or down.
3. Stream the output so the judge sees progress within 1s.
4. Show a graceful error with retry, never a raw stack trace.
5. Do NOT set temperature/top_p/top_k (current Claude and GPT-6 models reject them). Rely on the fallback for consistency.
```

*Why:* "Mock everything you can" ([JetBrains judges](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/)).

### ML8 · EDA + preprocessing

```text
[ROLE] Data scientist. [CONTEXT] Dataset description/head: <paste>; goal: <target/metric from PRD>.
1. Missing data: impute vs drop, per column, with reasoning.
2. Feature engineering: 3–5 derived features from domain logic.
3. Distributions: skew → suggested transforms (log1p, Box-Cox).
4. Correlations / multicollinearity.
5. Data-quality summary table: raw rows vs cleaned rows (schema, duplicates, invalid values); add a source_file column for provenance.
Output: cleaning script (Python), insights bullets, matplotlib/seaborn snippets. Fixed random_state=42.
```

### ML9 · Training loop

```text
[ROLE] ML engineer. Train a <scikit-learn | XGBoost | PyTorch> model for <target>.
- Start with the simplest baseline (logistic regression / rules) and report it — every later model must beat it.
- K-fold CV (stratified if classification); early stopping on validation loss where applicable.
- Right-skewed regression target → train on log1p, back-transform MAE per-sample in original space.
- Honest plot: out-of-fold predictions via cross_val_predict.
- Log experiments (MLflow or a JSON file); save model as models/<name>_<timestamp>.joblib.
Optimise the metric the problem actually cares about (e.g. recall for fraud) — say which and why.
```

### ML10 · Model failure analysis

```text
[ROLE] Model auditor. Here are the confusion matrix, loss curves, and misclassified samples: <paste>.
1. Slice check: is it failing on specific feature slices / groups?
2. Over/under-fitting: train vs validation gap.
3. Regression: are residuals i.i.d.?
Output a prioritised list of next experiments (more data/augmentation, regularisation, feature pruning) — and which ONE to try in the next hour.
```

### ML11 · Routing / cascade

```text
Design a model cascade for <task> at <volume>/day: cheap model first (<Haiku 4.5 | small model>), escalate to <Sonnet 5 / Opus 5> only when confidence is low or validation fails.
Define the confidence signal, the escalation rule, and benchmark both against our golden set (quality, p95 latency, cost/1k requests). Recommend whether the cascade beats a single model.
```

### ML12 · Scaffold a capped agent

```text
Read docs/agents-and-tool-use.md first. Build the smallest agent for <job> in <Next.js with Vercel AI SDK v7 ToolLoopAgent | Python with Pydantic AI>.
1. First say whether a fixed workflow (chain/router) would do instead of an agent loop; if yes, build that.
2. Max <3–5> tools. Set the step cap explicitly (stopWhen: isStepCount(8) / equivalent) and handle hitting it with a friendly message.
3. Stream output; show each tool call in the UI (running → done → failed).
4. Use v7 names only (isStepCount, instructions, onEnd, toolApproval); no temperature; Node 22+, ESM.
5. Model id and API key from env; key server-side only.
```

*Why:* start simple, cap the loop ([Anthropic](https://www.anthropic.com/engineering/building-effective-agents), [AI SDK v7](https://ai-sdk.dev/docs/migration-guides/migration-guide-7-0)).

### ML13 · Design the tools

```text
Here are the actions our agent needs: <list>. Design the tool set:
- As few tools as possible (merge thin wrappers); namespaced names (<app>_<resource>_<verb>); unambiguous parameter names; enums for modes.
- A description per tool written for a new teammate: what it does, when to use it, what it returns.
- strict schemas (additionalProperties: false).
- Responses: short and human-readable (names not UUIDs), paginated, truncated.
- Error messages that tell the model exactly how to fix the call.
Output the schemas + one example good call and one example error per tool.
```

*Why:* [Anthropic: Writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents).

### ML14 · Agent safety and fallback review

```text
Review our agent before the demo. Report pass/fail for each:
1. Lethal trifecta: does any single agent have private data + untrusted input + a way to send data out? If so, how do we split it?
2. Every write/pay/send tool requires human approval.
3. Step cap set; MaxTurnsExceeded / step-limit handled gracefully.
4. Function stays under the Vercel 300 s limit (or runs in Vercel Workflows).
5. DEMO_MODE fallback returns cached answers for our 3 golden inputs.
6. Spend cap set on the API account; MCP servers are from trusted sources only.
7. 20+ pass/fail test cases from real failures; we've read at least 30 traces (Langfuse).
```

*Why:* [Lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) · [OWASP Agentic Top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) · [agent evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).

### ML15 · Datathon: tabular baseline & leak-free CV

```text
[ROLE] Senior Competitive Data Scientist. [CONTEXT] Real-world datathon dataset: <paste head(5) and types>; target: <target_col>; evaluation metric: <PR-AUC / ROC-AUC / F1>.
1. Ingest using Polars with lazy evaluation (pl.scan_csv / pl.scan_parquet).
2. Set up a leak-free 5-fold Stratified K-Fold (or TimeSeriesSplit if temporal). Ensure all imputation, scaling, and target encoding happen strictly inside each fold.
3. Train LightGBM (for fast iteration) and CatBoost (for native handling of categoricals/text).
4. Evaluate out-of-fold (OOF) predictions and find the optimal decision threshold that maximizes F1/cost utility instead of default 0.5.
5. Export best_model.pkl and precompute shap.TreeExplainer for instant frontend loading.
Output: self-contained Python script under 80 lines.
```

*Why:* Fast iteration + leak-free validation is the #1 predictor of datathon placement. See `Datathon-Playbook/03-modeling/baseline-pipeline.py`.

### ML16 · Datathon: What-If simulator & SHAP dashboard

```text
[ROLE] Fullstack Data App Engineer. Build a Streamlit decision-support dashboard for our datathon submission:
- Model inputs: <list 6-8 key features, min/max ranges, defaults>.
- Layout: 4 KPI scorecards at top (Predicted Risk %, Triage Tier, Expected Loss $, Potential Savings $).
- Sidebar: Interactive "What-If" scenario sliders allowing judges to tweak inputs and see the prediction update in real time (<50ms).
- Explainability: Horizontal bar chart showing local SHAP feature attributions (red = increases risk, green = protective factor).
- Guidance: Clear operational recommendation box based on the risk score (Emergency / Warning / Normal).
Make it self-contained with a fallback surrogate model so the demo NEVER crashes in front of judges.
```

*Why:* Judges reward working interactive decision-support products over static Jupyter notebooks. See `Datathon-Playbook/04-solutions-and-ui/streamlit-app-template.py`.

