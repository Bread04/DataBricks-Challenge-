# 💬 Datathon LLM Prompts & Co-Pilots

<!-- markdownlint-disable MD013 -->

> Copy-paste prompts designed to get high-velocity, statistically rigorous results from AI assistants during a high-pressure competition.

---

## 🔍 Prompt 1: Rapid EDA & Data Anomaly Detection

```text
I am competing in a 24-hour datathon. Here is the schema and summary statistics of my dataset:
[PASTE HEAD(5) AND INFO() OR DATA TYPES]

Target variable: [SPECIFY TARGET] (Type: [Classification / Regression])
Objective: [DESCRIBE BUSINESS PROBLEM]

Act as a Principal Data Scientist:
1. Identify 5 potential data quality traps (e.g. high cardinality, zero-variance, skewed distributions, temporal drift).
2. Propose 8 domain-specific feature engineering ideas (ratios, interaction terms, rolling windows, aggregations) that directly target the objective.
3. Recommend the optimal cross-validation splitting strategy to prevent data leakage (Stratified, Group, or TimeSeries).
4. Provide the exact Python snippet using Polars to engineer the top 3 features.
```

---

## ⚙️ Prompt 2: Leak-Free Cross-Validation Pipeline

```text
Write a complete, modular Python script using Scikit-learn, LightGBM, and CatBoost for a tabular datathon dataset.
- Target column: [TARGET_COLUMN] (Binary classification / Multi-class / Regression)
- Imbalance ratio: [e.g. 10% positive class]
- Categorical features: [LIST COLUMNS]
- Numeric features: [LIST COLUMNS]

Requirements:
1. Use 5-Fold Stratified K-Fold CV (or TimeSeriesSplit if temporal).
2. Fit all imputation, scaling, and categorical encoders STRICTLY inside each training fold to prevent target leakage.
3. Evaluate using ROC-AUC, PR-AUC, and F1-score across out-of-fold predictions.
4. Include a function to find the optimal decision threshold maximizing F1 rather than defaulting to 0.5.
5. Export the final model artifact and precompute a SHAP TreeExplainer for a Streamlit app.
Keep code clean, self-contained, and runnable.
```

---

## 🎛️ Prompt 3: "What-If" Scenario Simulator UI Generator

```text
I need to build an interactive Streamlit demo for judges in 30 minutes.
My trained model takes the following input features:
[LIST 6-8 KEY FEATURES, DATA TYPES, AND MIN/MAX RANGES]

Create a Streamlit application with:
1. An executive header and 4 top KPI cards (Predicted Probability, Risk Tier, Estimated Value at Risk, Potential Savings).
2. A sidebar containing interactive sliders and dropdowns corresponding to each input feature.
3. Real-time model prediction that updates immediately when any slider moves.
4. A horizontal bar chart displaying feature attribution (simulated SHAP values) showing which inputs increased vs decreased the risk.
5. A clear operational recommendation banner based on the predicted risk tier.
Use clean, modern UI styling.
```

---

## 🎤 Prompt 4: The 3-Minute Winning Pitch Narrative

```text
We have built a working machine learning decision-support solution for the following datathon challenge:
- Problem: [DESCRIBE REAL-WORLD PROBLEM]
- Solution Name: [NAME]
- Model: [e.g. LightGBM + AutoGluon Ensemble with 0.89 PR-AUC vs 0.71 baseline]
- Key Insights: [TOP 2 FACTORS IDENTIFIED BY SHAP]
- User Interface: Interactive Streamlit decision dashboard with live "What-If" scenario simulator.
- Quantified Business ROI: [e.g. Reduces false positives by 35%, saving ~$180k/yr]

Write a punchy, persuasive 3-minute presentation script (under 450 words) structured for hackathon judges:
- Minute 1: The Human & Financial Pain Point (The Hook).
- Minute 2: The Tech & Solution Walkthrough (Show the Live Demo & Explainability).
- Minute 3: Business Impact, Feasibility, and Call to Action.
Make the tone authoritative, passionate, and business-focused. Avoid unnecessary machine learning jargon.
```
