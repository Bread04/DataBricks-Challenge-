# 🧠 Datathon & ML Hackathon Prompt Macros (`PROMPTS.md`)

<!-- markdownlint-disable MD013 -->

> **Copy-paste prompt templates for every hour of a Datathon.**  
> Designed for use with ChatGPT (o3 / GPT-4o), Claude 3.7 Sonnet / Opus, Google Gemini 2.5 Pro, or directly inside AI coding assistants like Antigravity, Claude Code, and Cursor.  
> Replace text inside `<angle brackets>` before running.

---

## 📑 Macro Quick-Index

| Code | Macro Name | Datathon Phase | Goal / Output |
| :--- | :--- | :--- | :--- |
| [`DT01`](#dt01--problem-framing--hypothesis-tree) | **Hypothesis Tree & Economic Value** | Hour 0–2: Ideate | Structure 3 testable hypotheses & business bottleneck |
| [`DT02`](#dt02--10-minute-eda--data-health-audit) | **10-Minute EDA & Health Audit** | Hour 2–4: Explore | Instant script to inspect shape, nulls, outliers, target balance |
| [`DT03`](#dt03--missingness--dirty-data-triage) | **Dirty Data & Missingness Strategy** | Hour 4–8: Clean | Classify MCAR/MAR/MNAR & generate leak-free cleaning pipeline |
| [`DT04`](#dt04--leak-free-cv-split-designer) | **Leak-Free CV Split Designer** | Hour 4–8: Validate | Identify grouped entities/time dependencies & build split code |
| [`DT05`](#dt05--domain-feature-brainstormer) | **Domain Feature Brainstormer** | Hour 8–16: Engineer | 15 high-leverage domain features tailored to the industry |
| [`DT06`](#dt06--polars-feature-pipeline-generator) | **Polars Fast Feature Pipeline** | Hour 12–20: Code | Production-grade Polars code for ratios, rolling stats & time |
| [`DT07`](#dt07--5-fold-lightgbm-workhorse-pipeline) | **5-Fold LightGBM Workhorse** | Hour 16–24: Model | Stratified 5-Fold training script with OOF logging & SHAP |
| [`DT08`](#dt08--error-diagnostics--residual-mining) | **False Negative & Error Mining** | Hour 24–30: Debug | Find systematically misclassified cohorts & fix blind spots |
| [`DT09`](#dt09--shap-waterfall--business-translation) | **SHAP Translation to Plain English** | Hour 28–34: Explain | Translate technical feature attributions into business drivers |
| [`DT10`](#dt10--threshold--unit-economics-optimizer) | **Optimal Decision Threshold & ROI** | Hour 32–36: Value | Compute dollar payoff matrix & optimize classification threshold |
| [`DT11`](#dt11--streamlit-counterfactual-simulator) | **Streamlit "What-If" Simulator** | Hour 34–40: Product | Full interactive web dashboard with sliders & real-time inference |
| [`DT12`](#dt12--2-page-executive-whitepaper-drafter) | **2-Page Executive Report Drafter** | Hour 38–44: Report | Complete written submission for premier data competitions |
| [`DT13`](#dt13--180-second-pitch-script-generator) | **180-Second Winning Pitch Script** | Hour 42–46: Pitch | Word-for-word timed script with hook, demo, and ROI close |
| [`DT14`](#dt14--judge-interrogation--qa-griller) | **Judge Interrogation & Q&A Griller** | Hour 44–47: Defend | Pressure-test the project against 5 ruthless technical judges |
| [`DT15`](#dt15--2-hour-panic-button--triage) | **Last 2-Hour Panic Button** | Hour 46–48: Submit | Ruthless triage checklist when models crash right before deadline |

---

## 🚀 The Prompts

---

### `DT01` · Problem Framing & Hypothesis Tree
> **When to use:** Hour 0–2 after the dataset and competition brief are released.

```text
Act as a Principal Quantitative Strategist at Citadel and a Senior Partner at McKinsey.
We are competing in a datathon with the following challenge:

- Challenge Brief: <paste competition prompt/task>
- Target Variable: <name of column, e.g. churned, readmitted, default, price>
- Available Data Tables & Schema: <paste column names or table descriptions>
- Evaluation Metric: <e.g. F1, ROC-AUC, PR-AUC, RMSE, custom profit>

Please do the following:
1. Identify the fundamental ECONOMIC BOTTLENECK. Why does this prediction problem matter financially or societally? What is the cost of doing nothing?
2. Construct a MECE (Mutually Exclusive, Collectively Exhaustive) Hypothesis Tree with 3 distinct pillars exploring what drives the target.
3. For each pillar, propose 2 concrete, testable hypotheses that can be validated directly against the provided dataset.
4. Define the single "Hero Metric" (in dollars, lives, or operational hours) that we will present to executive judges.
```

---

### `DT02` · 10-Minute EDA & Data Health Audit
> **When to use:** Hour 2–4 to run an instant sanity check on raw data files.

```text
Act as a Senior Data Engineer.
I need a robust, self-contained Python script to audit our raw datathon dataset.

Dataset path: <e.g. data/raw/train.csv>
Target column: <e.g. is_fraud>

Write a concise Python script using Polars (or Pandas) that performs a 10-minute diagnostic and outputs:
1. Dataset shape (rows, columns) and memory consumption.
2. Target distribution and exact class imbalance percentage.
3. Column-by-column missingness percentage (sorted descending, only displaying columns with >0% nulls).
4. High-cardinality categorical check (columns with >50 unique values).
5. Numerical outlier check (columns where max is >10x the 99th percentile).
6. Potential ID columns or duplicate rows that could cause leakage.

Include clean terminal printouts with dividers. No unnecessary charts—just raw actionable health diagnostics.
```

---

### `DT03` · Missingness & Dirty Data Triage
> **When to use:** Hour 4–8 when discovering messy values, NaNs, and unexpected strings.

```text
Act as a Lead Data Scientist specializing in messy real-world data cleaning.
Our datathon dataset has the following data hygiene problems:

- Columns with missing values and percentages: <e.g. income: 28% null, referral_code: 65% null, temp: 4% null>
- Messy categorical columns: <e.g. 900 unique store_city values with typos and mixed case>
- Suspicious numerical outliers: <e.g. age has values of -1 and 999>
- Target column distribution: <e.g. 98.5% class 0, 1.5% class 1>

Provide a clean, leak-free preprocessing plan:
1. For each column with nulls, determine if it is MCAR, MAR, or MNAR. Should we impute (mean/median/mode), use an indicator flag (`is_col_missing`), or let tree models handle it natively?
2. How should we clean the dirty categoricals without blowing up memory?
3. How should we treat extreme outliers?
4. Write copy-paste Python code for a scikit-learn compatible or Polars preprocessing function that can be fit ONLY on the training split and applied to test.
```

---

### `DT04` · Leak-Free CV Split Designer
> **When to use:** Hour 4–8 before training any models.

```text
Act as a Kaggle Grandmaster and Validation Expert.
I need to design a 100% leak-free local cross-validation strategy for our datathon dataset.

Here is the data structure:
- Target variable: <target column name and type, e.g. binary classification with 3% positive rate>
- Number of rows: <e.g. 250,000>
- Primary identifier columns: <e.g. patient_id, store_id, device_serial_number>
- Timestamp columns: <e.g. transaction_date from 2024-01-01 to 2024-12-31>
- Nature of test set: <e.g. future 3 months, or new unseen patients, or random rows>

Determine:
1. Which CV strategy is mandatory? (StratifiedKFold, StratifiedGroupKFold, or TimeSeriesSplit?) Explain the lethal data leakage trap that would occur if we used standard random train_test_split.
2. Provide a clean, copy-paste Python code snippet setting up a 5-fold cross-validation loop that logs Out-of-Fold (OOF) predictions and computes the competition metric across folds.
```

---

### `DT05` · Domain Feature Brainstormer
> **When to use:** Hour 8–16 to find features that vault the team up the leaderboard.

```text
Act as a Domain Expert in <industry: Healthcare / FinTech / Supply Chain / Renewable Energy / AdTech> and a Senior Competitive Machine Learning Specialist.

We have a dataset with the following schema:
<paste column names, types, and brief descriptions>

Target we are predicting: <e.g. customer default on microloan in 90 days>

Brainstorm 15 high-leverage domain features that tree models (LightGBM/CatBoost) love. Group them into:
1. Interaction & Domain Ratios (e.g. financial leverage, medical risk ratios).
2. Temporal Velocity & Acceleration (e.g. frequency of events in last 7 days vs last 60 days).
3. Grouped Aggregations (e.g. user transaction relative to average for their zip code/peer group).
4. Discrepancy & Anomaly Flags (e.g. mismatch between shipping address and IP location).

For each feature, provide the mathematical formula and 1 sentence explaining the behavioral or physical reason why it predicts the target.
```

---

### `DT06` · Polars Fast Feature Pipeline Generator
> **When to use:** Hour 12–20 to turn brainstormed features into high-speed code.

```text
Act as a Polars Performance Specialist.
Write an efficient, vectorized feature engineering pipeline in Polars for the following operations on our dataframe:

Features to create:
1. Ratios: <e.g. col_a / (col_b + 1e-5)>
2. Rolling aggregations: <e.g. 7-day rolling mean and max of amount partitioned by user_id>
3. Group-by statistics: <e.g. average and standard deviation of transaction amount per merchant category>
4. Cyclical time features: <e.g. sin and cos transformations of hour_of_day and day_of_week>
5. Recency: <e.g. days between current transaction and previous transaction per user_id>

Requirements:
- Must use native Polars expressions (`pl.col(...)`).
- Zero Pandas conversions.
- Safe division (avoid ZeroDivisionError).
- Memory-efficient data types (`pl.Float32` / `pl.Int32` where appropriate).
- Return a clean Python function `def engineer_features(df: pl.DataFrame) -> pl.DataFrame:`.
```

---

### `DT07` · 5-Fold LightGBM Workhorse Pipeline
> **When to use:** Hour 16–24 to establish a solid, leak-free modeling baseline.

```text
Act as an ML Engineer on a winning datathon team.
Write a complete, modular, self-contained Python script to train a 5-fold cross-validated LightGBM model.

Specifications:
- Input data: Cleaned dataframe with features `X` and target `y`.
- Task: <Binary Classification / Multi-class / Regression>
- Target column: <target_col>
- Metric to evaluate: <e.g. ROC-AUC / PR-AUC / Log-Loss / RMSE>
- Grouping or Stratification: <e.g. Stratified by target, or Grouped by group_id>

The script must:
1. Set up a clean 5-fold loop with pinned random seed.
2. Train LightGBM with early stopping (50 rounds) on validation fold.
3. Collect and save Out-of-Fold (OOF) predictions.
4. Calculate and print mean and standard deviation of validation metric across folds.
5. Compute global feature importance and save the top 15 features to a CSV or clean console printout.
6. Save the trained fold models or ensemble artifact.
```

---

### `DT08` · Error Diagnostics & Residual Mining
> **When to use:** Hour 24–30 to find what the model is getting wrong.

```text
Act as a Lead Data Scientist conducting Error Analysis.
Our LightGBM model has reached an Out-of-Fold score of <current score, e.g. 0.81 F1>, but we need to identify systematic errors to engineer the winning features.

Here is a summary of our Out-of-Fold predictions:
- False Negatives: <describe rows where model predicted 0 but actual was 1>
- False Positives: <describe rows where model predicted 1 but actual was 0>
- Features available: <list key features>

Please guide our diagnosis:
1. Write a Python snippet to isolate the top 100 worst errors (highest log-loss or residual error).
2. What statistical tests or slice comparisons should we run between the "easy cases" and "worst error cases"?
3. Based on common failure patterns in <domain: finance/health/operations>, what 3 specific interaction features or data filters could correct these systematic blind spots?
```

---

### `DT09` · SHAP Waterfall & Business Translation
> **When to use:** Hour 28–34 to build explainability assets for judges.

```text
Act as a Lead AI Explainer and Technical Consultant.
We trained a tree-based model (LightGBM/XGBoost) and computed SHAP values using `shap.TreeExplainer`.

Here are the top 5 features by mean absolute SHAP value:
1. `<feature_1>`: <technical description and impact direction>
2. `<feature_2>`: <technical description and impact direction>
3. `<feature_3>`: <technical description and impact direction>
4. `<feature_4>`: <technical description and impact direction>
5. `<feature_5>`: <technical description and impact direction>

Please do two things:
1. Write a 2-paragraph C-Suite Executive Summary translating these 5 statistical features into intuitive business/operational drivers. (Do NOT use ML jargon like "gradient weights" or "log-odds"—use business English).
2. For an individual flagged customer/case, write the exact text of a 3-bullet "Clinical/Managerial Explanation" that an operator will see on their dashboard screen.
```

---

### `DT10` · Decision Threshold & Unit Economics Optimizer
> **When to use:** Hour 32–36 to maximize financial ROI.

```text
Act as a Chief Financial Officer and Quantitative Risk Officer.
We have predicted probabilities `p` from our classifier, and we need to choose the optimal decision threshold rather than blindly using 0.50.

Here are our operational unit economics:
- Value of True Positive (Correct intervention): <e.g. +$1,500 saved customer revenue>
- Cost of False Positive (Wasted outreach/discount): <e.g. -$45 per voucher sent>
- Cost of False Negative (Missed event / catastrophic failure): <e.g. -$8,200 fine or lost account>
- Cost of True Negative: <e.g. $0>

Tasks:
1. Formulate the Net Expected Value equation.
2. Write a Python function that sweeps thresholds from 0.01 to 0.99 on our Out-of-Fold validation probabilities, finds the exact threshold that maximizes total dollar profit, and plots/prints the profit curve.
3. Compare the net dollar return of the optimal threshold vs the default 0.50 threshold to give us an explosive pitch stat (e.g. "Optimizing the decision threshold unlocked an additional $240,000 in annual profit").
```

---

### `DT11` · Streamlit "What-If" Simulator Generator
> **When to use:** Hour 34–40 to build the interactive demonstration.

```text
Act as a Full-Stack Data App Specialist.
Create a complete, single-file, production-ready Streamlit app (`app.py`) for our datathon submission.

Project context:
- Project Name: <e.g. OmniShield>
- Problem: <e.g. Predicting Supply Chain Delivery Disruption>
- Key Input Features for Simulator:
  1. `<Feature 1, e.g. Supplier Lead Time (days), slider 1 to 90>`
  2. `<Feature 2, e.g. Regional Weather Severity, selectbox Low/Medium/High>`
  3. `<Feature 3, e.g. Order Value ($), number input 100 to 50000>`
  4. `<Feature 4, e.g. Port Congestion Index, slider 0.0 to 1.0>`

App Requirements:
1. Clean modern UI with an Executive Summary banner and 3 hero KPI metrics (Risk Score, Financial Exposure $, Action Recommendation).
2. Left Column: Interactive Scenario Sliders letting judges change inputs.
3. Right Column: Real-time recalculation of risk probability with dynamic alert badge (Green/Amber/Red) and a mock SHAP attribution bar chart showing why the risk score changed.
4. Bottom Section: "Human-in-the-Loop Action Button" (e.g. "Reroute Shipment via Air Freight") that triggers an immediate confirmation toast.
5. High-performance, self-contained mock model function so it runs with zero lag on `localhost:8501`.
```

---

### `DT12` · 2-Page Executive Whitepaper Drafter
> **When to use:** Hour 38–44 when written documentation is evaluated.

```text
Act as an Executive Consultant at Boston Consulting Group (BCG) and a Principal Data Scientist.
Draft a concise, high-impact 2-page Executive Summary report for our datathon submission.

Project Details:
- Project Title: <Title>
- The Problem & Industry Context: <2 sentences>
- The Core Innovation (What we built): <2 sentences>
- Key Dataset & Validation Rigor: <e.g. 5-Fold Stratified Group CV, zero leakage>
- Model Performance vs Baseline: <e.g. 0.488 PR-AUC vs 0.114 random baseline>
- Financial ROI & Unit Economics: <e.g. $1.84M net annual savings for a 500-bed hospital>
- Ethical & Operational Safeguards: <e.g. fairness across cohorts, human-in-the-loop oversight>

Format the response in structured GitHub Markdown following the standard Executive Report template:
1. Executive Summary & Problem Statement
2. Quantitative Value Proposition (ROI Table)
3. Methodology & Leak-Free Validation
4. Solution Architecture & The "Last-Mile" UI
5. Risk Assessment & Operational Implementation Roadmap
```

---

### `DT13` · 180-Second Winning Pitch Script Generator
> **When to use:** Hour 42–46 to prepare the spoken presentation.

```text
Act as a Championship Pitch Coach for Datathons and Techstars Demo Days.
We have exactly 3 MINUTES (180 SECONDS) to present our datathon project to a mixed panel of C-suite executives and PhD ML researchers.

Our project:
- Name: <Project Name>
- Problem: <Problem and dollar impact>
- Technical Breakthrough: <e.g. engineered domain velocity features, 5-fold Stratified Group CV, CatBoost/LightGBM ensemble>
- Live Demo Highlight: <what we will show on Streamlit in 45 seconds>
- Business Value: <Net dollar savings or operational gain>

Generate:
1. A word-for-word spoken script with exact timestamp markers:
   - [0:00–0:35] The Relatable Hook & Economic Bleed
   - [0:35–1:15] The Breakthrough Insight & Validation Rigor
   - [1:15–2:10] The Live "What-If" Demo Walkthrough
   - [2:10–2:40] Feasibility, Privacy & Deployment Strategy
   - [2:40–3:00] The Unforgettable Closing Line
2. Stage directions in brackets `[like this]` indicating when to change slides, point at the screen, or move a slider on the dashboard.
```

---

### `DT14` · Judge Interrogation & Q&A Griller
> **When to use:** Hour 44–47 to rehearse before presenting.

```text
Act as a panel of 3 ruthless datathon judges:
1. Dr. Chen (PhD in Machine Learning, hyper-skeptical of data leakage, overfitting, and synthetic data).
2. Sarah Jenkins (VP of Business Operations, cares only about ROI, implementation costs, and operator adoption).
3. Marcus Vance (Chief Information Security Officer, hyper-focused on privacy, ethics, and regulatory compliance).

Our project:
<paste 2-paragraph summary of problem, methodology, validation, and UI solution>

Grill our team with the 5 hardest, most skeptical questions you would ask during the live Q&A.
For each question:
- State which judge is asking.
- Explain why the question is a trap.
- Provide the "Golden 20-Second Winning Answer" that completely disarms the critique with evidence and confidence.
```

---

### `DT15` · 2-Hour Panic Button & Triage Checklist
> **When to use:** 2 hours before the deadline when code is broken or models won't converge.

```text
EMERGENCY TRIAGE MODE: We have exactly 2 hours left in this datathon and we are in a panic.

Our current situation:
- What works right now: <e.g. data is cleaned, baseline notebook has a decent score>
- What is currently broken or missing: <e.g. ensembling code is crashing, Streamlit app has an error, deck is half-done>

Act as an Emergency Datathon Commander:
1. Give us a ruthless 120-minute triage schedule broken into 30-minute blocks.
2. What non-essential features or complex models should we IMMEDIATELY KILL to save the submission?
3. What are the minimum 3 viable deliverables we MUST submit before the portal locks to receive a valid score?
4. Give our team a 3-sentence calming tactical mantra to execute with focus.
```
