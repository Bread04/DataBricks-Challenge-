---
name: hackathon-datathon
description: Complete datathon and machine learning hackathon skill. Covers hypothesis framing, leak-free cross-validation (Stratified vs Group vs TimeSeries), dirty data handling, domain feature engineering, speed modeling (LightGBM, CatBoost, AutoGluon), decision thresholds, unit economics, SHAP explainability, and interactive Streamlit simulators. Use when participating in, preparing for, or reviewing projects for datathons, predictive modeling hackathons, and real-world data challenges.
---

# Datathon & ML Hackathon Skill

<!-- markdownlint-disable MD013 -->

> Condensed rules for winning data science competitions, Kaggle days, and corporate datathons. Full detail: `../../08-datathon-handbook/` · macros in `../../08-datathon-handbook/PROMPTS.md`. Verified 2026-09-23.

---

## 🏆 The Core Rule: Decisions Over Decimals

Judges never fund an isolated F1 score. They fund **operational decisions and measurable business outcomes**.
1. **Never stop at a Jupyter notebook:** Always deploy a live, interactive UI (Streamlit) featuring a **"What-If" Counterfactual Simulator**.
2. **Translate error metrics to dollars:** Convert every False Positive and False Negative into financial penalties, saved revenue, or operational headcount hours.
3. **Guard against data leakage:** A single leaked feature ruins a team during judge audits. Lock down your evaluation harness before engineering a single feature.

---

## ⚡ The 2026 Datathon Tech Stack

| Step | First Choice | Fallback | Avoid |
| :--- | :--- | :--- | :--- |
| **Data Engine** | **Polars** (10x-50x faster, zero memory crashes) | DuckDB (analytical SQL queries) | Pandas for >1 GB CSVs |
| **Fast EDA** | **ydata-profiling** (1-line HTML report) | Seaborn/Matplotlib scripts | 4-hour manual plotting |
| **Workhorse ML**| **LightGBM** (fast CPU gradient boosting) | **CatBoost** (great for categorical/text) | Complex PyTorch architectures for tabular data |
| **AutoML Stacking** | **AutoGluon** (multi-layer ensembling) | Custom Weighted Rank Average | Plain uncalibrated averages |
| **Explainability** | **TreeSHAP** (`shap.TreeExplainer`) | Feature Importance MDI | Black-box uninterpretable predictions |
| **Interactive UI** | **Streamlit** (instant Python web dashboards) | Gradio | Jupyter notebook scrolling |

---

## 🛡️ Leak-Free Validation Hierarchy

Pick the split that matches the data generating process:

| Data Structure | Correct Split | Why / Warning |
| :--- | :--- | :--- |
| **Independent rows** | `StratifiedKFold(n_splits=5)` | Preserves target class balance in imbalanced sets. |
| **Grouped entities** (e.g. `patient_id`, `store_id`) | `StratifiedGroupKFold(n_splits=5)` | **Mandatory.** Prevents memorizing the same entity across train and test. |
| **Temporal / Time-series** | `TimeSeriesSplit(n_splits=5)` | **Mandatory.** Always train on past, validate on future. Never shuffle time! |

> **5-Second Leakage Sanity Test:** If your local CV score jumps $>0.15$ higher than baseline after adding one feature, or if a single feature commands $>60\%$ of total feature importance, suspect target leakage immediately.

---

## 🧹 Dirty Data & Imbalance Rules

1. **Missing Data:**
   - MCAR (random): Impute with median/mode + add binary indicator column `is_{col}_missing`.
   - MNAR (informative): Tree models handle NaNs natively (`np.nan`). Do not impute if missingness itself is a signal.
2. **Extreme Class Imbalance (<5% positives):**
   - **Do NOT default to SMOTE.** Synthetic interpolation creates unrealistic tabular edge cases.
   - **Do this instead:** Set `scale_pos_weight = count(negative) / count(positive)` in LightGBM/XGBoost, optimize **PR-AUC (Average Precision)**, and tune the decision threshold on validation Out-of-Fold (OOF) probabilities.
3. **Outliers:**
   - Clip extreme tails to 1st and 99th percentiles (`df.clip(lower=q01, upper=q99)`).

---

## 🎛️ The 5 Must-Have UI Patterns (Streamlit)

1. **What-If Scenario Simulator:** Sliders and toggles that recompute predictions in $<300\text{ ms}$.
2. **Realized Dollar Value / ROI Ticker:**
   $$\text{Net Value} = (\text{True Positives} \times \text{Benefit}) - (\text{False Positives} \times \text{Cost}) - (\text{False Negatives} \times \text{Penalty})$$
3. **Glass-Box SHAP Waterfall:** Local feature attributions showing why a specific user/patient was flagged.
4. **Cohort Filter:** Slice performance by region, tier, or demographic.
5. **Human-in-the-Loop Action Trigger:** A button that dispatches a retention voucher, schedules an appointment, or flags an alert.

---

## ⏱️ 48-Hour Execution Budget

```
Hour 00–04: Problem Framing, Value Driver Tree, Git Setup & Leak-Free CV Split
Hour 04–12: Ingestion via Polars, Missingness Audit & 1st Working Baseline
Hour 12–24: Feature Engineering Sprint (Ratios, Rolling Windows, Cyclical Time)
Hour 24–34: Hyperparameter Tuning (Optuna), Rank-Average Ensembling & Diagnostics
Hour 34–42: Streamlit Interactive Simulator & Executive Whitepaper
Hour 42–46: Pitch Rehearsal (Timed 3-Min Script) & Q&A War Gaming
Hour 46–48: Final Leaderboard Submission & Live Presentation
```

---

## 🎤 The 3-Minute Pitch Formula

* **0:00–0:40 (The Hook):** Real human or economic pain point + dollar cost of current failure.
* **0:40–1:20 (The Core Insight):** Data ingestion, key domain feature discovered, and leak-free CV performance.
* **1:20–2:15 (The Live Demo):** Open Streamlit app, move a slider, show the SHAP explanation, show the net ROI.
* **2:15–2:45 (Feasibility & Ethics):** Data leakage safeguards, bias checks, and rollout roadmap.
* **2:45–3:00 (Call to Action):** Summary sentence: *"We turned raw telemetry into \$1.8M in prevented downtime."*

---

## 🔗 Related Resources

- Complete Handbook: `../../08-datathon-handbook/README.md`
- Prompt Macros: `../../08-datathon-handbook/PROMPTS.md`
- Standard Practices: `../../08-datathon-handbook/STANDARDS.md`
- Codebase Recipes: `../../08-datathon-handbook/02-data-wrangling/recipes.md`
- Worked 48h Example: `../../08-datathon-handbook/07-worked-example/worked-example.md`
