# ⏱️ Datathon Battle Plan: 24-Hour & 48-Hour Execution Guide

<!-- markdownlint-disable MD013 -->

> Winning a datathon is 40% problem framing, 30% execution discipline, and 30% presentation. This battle plan breaks down your hours to ensure you never run out of time to build the demo or craft the pitch.

---

## 👥 The 4-Person Team Role Matrix

Assign these roles in **Hour 0**. Never have everyone working on the same notebook.

| Role | Primary Responsibility | Key Deliverables |
| --- | --- | --- |
| **Role 1: Data Architect** | Ingestion, data cleaning, datetime parsing, feature creation, external data joins | Cleaned Parquet file, feature dictionary, data profiling report |
| **Role 2: ML Modeler** | Local CV setup, baseline LightGBM/CatBoost, AutoML ensembling, threshold tuning | Validated model artifact (`model.cbm`/`lgb.pkl`), test predictions, SHAP values |
| **Role 3: Solution & UI Dev** | Interactive frontend, user flow, scenario simulator ("what-if" panel), charts | Functional Streamlit / Gradio web app deployed to cloud URL |
| **Role 4: Pitch & Story Lead** | Mentor interviews, domain context, business/ROI calculation, slide deck, demo script | 3-minute pitch deck (10 slides max), executive summary, presentation delivery |

---

## 🕒 The 48-Hour Datathon Timeline

### Phase 1: Problem Framing, Evaluation Metric & Data Triage (Hours 0 – 6)
> 💡 **Beginner Tip:** Don't write complex code yet! Run `ydata-profiling` to see what columns exist. In Hour 2, train a dummy model that just guesses the average to prove your code runs without crashing.

- [ ] **Hour 0–1: Read the Rubric & Talk to Mentors**
  - Identify the primary business/domain bottleneck.
  - Clarify the judging criteria (statistical metric vs. business utility).
  - Determine if external datasets are allowed.
- [ ] **Hour 1–3: Instant 10-Minute EDA**
  - Run `ydata-profiling` or `sweetviz` on raw training and test data.
  - Identify missingness patterns, high-cardinality categoricals, and class imbalance.
- [ ] **Hour 3–6: Establish Local Validation Strategy**
  - **Golden Rule:** Never trust a public leaderboard blindly.
  - Set up a leak-free Stratified K-Fold (for classification), Group K-Fold (if patient/user grouping applies), or TimeSeriesSplit (for temporal data).
  - Train an instant baseline (Logistic Regression / LightGBM default) and submit/score to verify pipeline mechanics.

### Phase 2: High-Yield Feature Engineering & Modeling (Hours 6 – 18)
- [ ] **Hour 6–12: Feature Engineering (Where 90% of Performance is Won)**
  - Domain-specific ratios and aggregations (e.g. `cost / duration`, `rolling_7d_avg`).
  - Cyclical datetime encodings (`sin`/`cos` of hour/month).
  - Target encoding with out-of-fold regularization for high-cardinality columns.
- [ ] **Hour 12–18: Model Exploration & LightGBM/CatBoost Tuning**
  - Compare LightGBM (fastest) and CatBoost (best with categoricals).
  - Train models inside the K-Fold loop, recording out-of-fold validation scores.
  - Tune classification thresholds (optimize F1-score or expected business cost instead of default 0.5).

### Phase 3: Ensembling & UI Architecture (Hours 18 – 30)
> 😴 **Mandatory Rest Window:** Schedule at least 4–5 hours of sleep around Hour 20–25. Exhausted teams introduce catastrophic bugs at 4 AM.
> 💡 **Beginner Tip:** Don't stress if AutoGluon seems too complex—stick to your LightGBM model from Phase 2! A simple model connected to a working Streamlit dashboard beats an untracked ensemble every time.

- [ ] **Hour 18–24: AutoGluon Multi-Layer Stacking**
  - Run AutoGluon with a 30-minute time budget (`presets='best_quality'`).
  - Compare AutoGluon ensemble score against manual LightGBM/CatBoost models.
  - Lock in the final model weights and serialize them (`model.pkl` or native binary).
- [ ] **Hour 24–30: Scaffold the Solution Interface**
  - Role 3 builds the Streamlit app layout: KPI metrics header, filter sidebar, and model inference connector.
  - Role 1 & 2 compute and export SHAP TreeExplainer values for the test sample.

### Phase 4: The "Last-Mile" Polish & What-If Simulators (Hours 30 – 42)
> 💡 **Beginner Tip:** The interactive sliders are your superpower. When judges see that dragging a slider updates the risk probability live, you win instant technical points.

- [ ] **Hour 30–36: The "What-If" Scenario Simulator**
  - Add interactive sliders to the UI (e.g., *"What if patient blood pressure increases by 10%?"* or *"What if shipping delay increases by 2 days?"*).
  - Connect sliders to live model inference so judges see dynamic re-scoring.
  - Render SHAP waterfall plots for individual sample explanations.
- [ ] **Hour 36–42: Deploy the App to Free Cloud**
  - Deploy Streamlit app to Streamlit Community Cloud (or Hugging Face Spaces) via GitHub.
  - Test the live URL on mobile and laptop.
  - Create a short 30-second backup screen recording of the app working locally in case conference WiFi fails!

### Phase 5: The Winning 3-Minute Pitch (Hours 42 – 48)
- [ ] **Hour 42–46: Craft the Slide Deck (10 Slides Max)**
  - Slide 1: Title & One-Sentence Hook.
  - Slide 2: The Real-World Pain Point & Financial/Human Cost.
  - Slide 3: Our Solution Overview (How AI solves it).
  - Slide 4: Data Engineering & Validation Rigor (DuckDB, leak-free CV).
  - Slide 5: Model Performance & Benchmarks (CV vs Baseline).
  - Slide 6: Model Explainability (SHAP: Why we can trust it).
  - Slide 7: **LIVE DEMO** (Switch to interactive Streamlit app).
  - Slide 8: Business ROI & Operational Deployment Feasibility.
  - Slide 9: Risk & Ethical Mitigation (Bias, Privacy, Fallbacks).
  - Slide 10: Team & Call to Action.
- [ ] **Hour 46–48: Rehearse Pitch 5 Times Under a Stopwatch**
  - 3 minutes strictly: 45s Problem, 45s Tech/Model, 60s Live Demo, 30s Business Impact & Close.

---

## ⚡ 24-Hour Express Hackathon Adaptations

If you are running a 24-hour sprint:
- **Hour 0–2:** Data triage + Baseline LightGBM model.
- **Hour 2–8:** High-impact feature engineering + AutoGluon run (15 min budget).
- **Hour 8–14:** Lock model, build Streamlit dashboard with 1 interactive slider.
- **Hour 14–20:** Deploy app, calculate SHAP plots, compute business ROI.
- **Hour 20–24:** Pitch deck, live demo rehearsal, code freeze.

---

## 📋 Pre-Submission Checklist: Are You Ready for Judges?

- [ ] **No data leakage:** Preprocessing and target encodings fitted strictly inside CV folds.
- [ ] **Appropriate metric:** Used PR-AUC or balanced F1 for imbalanced targets, not basic accuracy.
- [ ] **Saved model weights:** Model can be loaded in <1s in the UI without re-running data prep.
- [ ] **Interactive demo:** Judges can change inputs and see the prediction update.
- [ ] **Explainability present:** SHAP or feature importance chart explains the "why".
- [ ] **Quantified ROI:** Pitch explains how much time/money/lives are saved by this system.
- [ ] **Offline backup:** 1080p screen recording of the working demo ready on your laptop.
