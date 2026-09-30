# 📊 Datathon & ML Hackathon Playbook

<!-- markdownlint-disable MD013 -->

> **A beginner-friendly guide to winning data science hackathons and datathons** by turning messy real-world datasets into high-performing machine learning models and interactive, decision-grade user solutions.

---

## 👋 New to Datathons? Start Here in 3 Steps!

If this is your first time competing in a data hackathon, don't feel overwhelmed. Follow these 3 steps:

| Step | Open This | Time |
| --- | --- | --- |
| **1. Understand the Event** | [`first-datathon.md`](first-datathon.md): What a datathon actually is, what judges care about, and how to survive your first 24 hours | 10 min |
| **2. Learn the Lingo** | [`GLOSSARY.md`](GLOSSARY.md): Jargon-free explanations of scary words like *Overfitting*, *Data Leakage*, *SHAP*, and *Cross-Validation* | 10 min |
| **3. Run the 1-Click Starter** | Run `python quickstart-1-click.py`: Trains a real model and launches an interactive web dashboard in 30 seconds! | 1 min |

> 🚨 **Something broke at 2 AM?** Open the [`troubleshooting.md`](troubleshooting.md) Panic Button for instant 60-second fixes!

---

## 🏆 The Core Datathon Philosophy

Most teams lose datathons because they make one of two critical mistakes:
1. **The Kaggle Notebook Trap:** Spending 36 hours obsessing over the 4th decimal place of ROC-AUC in a `.ipynb` notebook, showing static matplotlib bar charts, and offering zero operational tools for non-technical judges.
2. **The Dummy UI Trap:** Building an aesthetically gorgeous dashboard that has no statistical rigor, runs on fake hardcoded numbers, and falls apart under basic questioning from technical judges.

**The Winning Formula:**
```text
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ Real-Life Data  │ ────► │ High-Speed ML   │ ────► │ "The Last-Mile" │ ────► │  Winning Pitch  │
│  Ingestion &    │       │  & Leak-Free    │       │ Interactive App │       │  & Actionable   │
│ Wrangling (Duck)│       │  Models (LGBM)  │       │ (Streamlit/SHAP)│       │   Business ROI  │
└─────────────────┘       └─────────────────┘       └─────────────────┘       └─────────────────┘
```
Winning teams treat the datathon as a rapid **decision-support product challenge**. They give the judges an interactive interface to touch, simulate "what-if" scenarios, inspect model explainability (SHAP), and calculate quantified financial/operational impact.

---

## 🗺️ What's in This Playbook

### 🤖 AI Agent Standards & Prompt Macros
* 📜 [`SKILLS.md`](SKILLS.md) — **Datathon AI Skill Specification:** Drop this into any datathon workspace so Claude Code, Cursor, Antigravity, or Copilot strictly follow leak-free evaluation, unit economics, and Streamlit standards.
* 🧠 [`PROMPTS.md`](PROMPTS.md) — **The Datathon Macro Catalog:** 15 copy-paste prompts (`DT01` to `DT15`) covering problem framing, 10-minute EDA, feature brainstorming, LightGBM pipelines, SHAP explainers, unit economics, pitch scripts, and judge Q&A defense.
* 📋 [`STANDARDS.md`](STANDARDS.md) — **Standard Operating Procedures (SOP):** Repository taxonomy, data hygiene rules, cross-validation integrity, deterministic seed rules, and pre-submission audit.
* 📦 [`PROJECT_TEMPLATE/`](PROJECT_TEMPLATE/README.md) — **Ready-to-Use Project Boilerplate:** Pre-built project folder with [`PROJECT_CONTEXT.md`](PROJECT_TEMPLATE/PROJECT_CONTEXT.md) single-source-of-truth, `requirements.txt`, `.gitignore`, and starter directories.

### 🟢 Fundamentals & Starters
* [`first-datathon.md`](first-datathon.md) — What a datathon actually is, how it differs from a software hackathon, the 4 vital roles, and the 10 Golden Rules.
* [`GLOSSARY.md`](GLOSSARY.md) — The plain-English cheat sheet for scary ML concepts (Overfitting, Data Leakage, Cross-Validation, SHAP, Imbalance).
* [`quickstart-1-click.py`](quickstart-1-click.py) — Runnable 1-click starter script that trains a LightGBM model and launches a Streamlit UI in 30 seconds.
* [`troubleshooting.md`](troubleshooting.md) — Fast fixes for out-of-memory errors, NaN values, merge blowups, and Streamlit crashes.

### 📘 01. Playbook & Strategy
* [`01-playbook/datathon-battle-plan.md`](01-playbook/datathon-battle-plan.md) — Hour-by-hour 24h & 48h timelines, judging criteria breakdown, and team responsibilities.
* [`01-playbook/hypothesis-and-problem-framing.md`](01-playbook/hypothesis-and-problem-framing.md) — The Citadel & McKinsey style hypothesis tree framework and economic bottleneck mapping.
* [`01-playbook/pitch-and-presentation-guide.md`](01-playbook/pitch-and-presentation-guide.md) — 10-slide blueprint, word-for-word 3-minute pitch script with timestamps, and defense against the 5 hardest judge questions.
* [`01-playbook/executive-report-template.md`](01-playbook/executive-report-template.md) — Fill-in-the-blank 2-page executive summary template for premier data competitions.
* [`01-playbook/team-git-and-notebook-workflow.md`](01-playbook/team-git-and-notebook-workflow.md) — Anti-merge conflict Git practices, clean directory structures, and role contracts.

### 🧹 02. Data Wrangling & Feature Engineering
* [`02-data-wrangling/recipes.md`](02-data-wrangling/recipes.md) — Polars & DuckDB recipes for multi-gigabyte data ingestion and automated 10-minute EDA.
* [`02-data-wrangling/feature-engineering-cookbook.md`](02-data-wrangling/feature-engineering-cookbook.md) — 10 high-yield feature families (ratios, rolling stats, cyclical time, frequency encoding) with copy-paste code.
* [`02-data-wrangling/handling-dirty-data.md`](02-data-wrangling/handling-dirty-data.md) — Handling missingness, high cardinality, extreme outliers, and class imbalance (cost-sensitive learning over SMOTE).

### 🤖 03. Fast Modeling & Validation
* [`03-modeling/baseline-pipeline.py`](03-modeling/baseline-pipeline.py) — Leak-free 5-fold Stratified K-Fold LightGBM/CatBoost training pipeline with SHAP values.
* [`03-modeling/cross-validation-guide.md`](03-modeling/cross-validation-guide.md) — Stratified vs Group vs TimeSeries CV, OOF logging, and the 5-second leakage sanity test.
* [`03-modeling/hyperparameter-tuning-and-ensembling.md`](03-modeling/hyperparameter-tuning-and-ensembling.md) — Why to avoid GridSearchCV, Optuna 10-minute budgets, and weighted rank-averaging ensembles.
* [`03-modeling/automl-autogluon.py`](03-modeling/automl-autogluon.py) — Multi-layer stacking script with automated fallbacks to dominate leaderboards.

### 🖥️ 04. Solutions & Interactive UI
* [`04-solutions-and-ui/streamlit-app-template.py`](04-solutions-and-ui/streamlit-app-template.py) — Complete, runnable Streamlit app with scenario sliders, SHAP watermarks, and unit economics ticker.
* [`04-solutions-and-ui/dashboard-design-patterns.md`](04-solutions-and-ui/dashboard-design-patterns.md) — The 5 UI patterns judges love (Counterfactual simulators, ROI tickers, glass-box explanations, cohort filters, action queues).

### 📦 05. Catalog & References
* [`05-repo-catalog/README.md`](05-repo-catalog/README.md) — Curated collection of top open-source tools, public data portals, and winning repositories.
* [`06-prompts/datathon-prompts.md`](06-prompts/datathon-prompts.md) — Guide to prompt engineering in competitive data science.

### 🏆 07. Worked Example Case Study
* [`07-worked-example/worked-example.md`](07-worked-example/worked-example.md) — Hour-by-hour case study of how a 4-person team took 1st place overall in a 48-hour clinical datathon.

---

## ⚡ 2026 Recommended Datathon Tech Stack

| Need | Recommended Tool | Why It Wins at Hackathons | Level |
| --- | --- | --- | --- |
| **Instant 1-Click EDA** | [ydata-profiling](https://github.com/ydataai/ydata-profiling) | Complete interactive HTML report in 1 line of Python | 🟢 |
| **Speed ML Workhorse**| [LightGBM](https://github.com/microsoft/LightGBM) | Fastest CPU gradient boosted tree training; trains in seconds | 🟢 |
| **Messy Categoricals**| [CatBoost](https://github.com/catboost/catboost) | Native handling of categorical & text features with zero leakage | 🟢 |
| **Interactive App** | [Streamlit](https://github.com/streamlit/streamlit) | Instant Python web apps with sliders, scorecards, and free cloud URLs | 🟢 |
| **Explainability (XAI)**| [SHAP](https://github.com/slundberg/shap) | Proves to judges *why* the model made a prediction | 🟡 |
| **Data Engine** | [Polars](https://github.com/pola-rs/polars) | 10x-50x faster than Pandas; zero memory crashes on multi-GB CSVs | 🟡 |
| **Analytical SQL** | [DuckDB](https://github.com/duckdb/duckdb) | In-process analytical SQL; queries Parquet files with zero copy | 🟡 |
| **AutoML Stacking** | [AutoGluon](https://github.com/autogluon/autogluon) | Multi-layer stacking ensemble; tops leaderboards in 15–30 min | 🟡 |

---

## 🚀 Quickstart: 3 Steps for Hour 0

1. **Install Core Datathon Environment:**
   ```bash
   pip install polars duckdb lightgbm catboost shap streamlit ydata-profiling
   ```
2. **Run the 1-Click Starter:**
   ```bash
   python quickstart-1-click.py
   ```
3. **Open the Battle Plan:**
   Read [`01-playbook/datathon-battle-plan.md`](01-playbook/datathon-battle-plan.md) and assign your 4 team roles before writing a single line of code!
