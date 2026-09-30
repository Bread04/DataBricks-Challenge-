# 🏆 Case Study: How Team "HealthPulse" Won 1st Place (48-Hour Datathon Walkthrough)

> *"An unvarnished, hour-by-hour anatomy of how four university students went from an unfamiliar 4.2 GB clinical dataset to unanimous 1st place in a premier national datathon."*

---

## 📋 The Datathon Brief
* **Event:** National Health Data Challenge (TAMU Datathon / Stanford WiDS style)
* **Time Limit:** 48 hours
* **The Data:** 4.2 GB across 4 relational CSV tables:
  1. `patients.csv` (Demographics, insurance type, zip code)
  2. `admissions.csv` (Admission dates, discharge dates, primary ICD-10 codes, readmission flag)
  3. `vitals_timeseries.csv` (Hourly heart rate, blood pressure, oxygen saturation during stays)
  4. `medications.csv` (Discharge prescriptions and dosage changes)
* **Goal:** Predict 30-day unplanned hospital readmission (`readmitted_30d` ∈ {0, 1}) and propose an actionable clinical intervention to reduce readmission penalties.
* **Evaluation Metric:** Competition leaderboard ranked by PR-AUC (Average Precision), with a final round judged on technical rigor, financial impact, and live demonstration.

---

## 👥 The Team & Roles

| Name | Role | Core Responsibility |
| :--- | :--- | :--- |
| **Maya** | **Problem Framing & Deck Lead** | Business economics, slides, executive report, pitch rehearsal |
| **Sam** | **Feature Engineer & Data Wrangler** | Relational merges, dirty data cleaning, clinical domain features |
| **Arjun** | **Modeling & Ensembling Lead** | Leak-free CV setup, LightGBM/CatBoost, Optuna, stacking |
| **Chloe** | **UI/UX & Deployment Lead** | Streamlit scenario simulator, SHAP integration, live demo polish |

---

## ⏱️ Hour-by-Hour Timeline

```
Hour 00-04: Setup, Leak-Free CV & First Git Commit
Hour 04-12: The "Dirty Data" Audit & First Working Baseline
Hour 12-24: Feature Engineering Sprint (Domain Ratios & Aggregations)
Hour 24-34: Model Ensembling, Hyperparameter Tuning & Error Analysis
Hour 34-42: Building the Streamlit Simulator & Executive Report
Hour 42-46: Pitch Rehearsal, Q&A War Gaming & Deck Polish
Hour 46-48: Final Submissions & The Winning 3-Minute Demo
```

---

### Phase 1: Hours 00–04 — Alignment, Architecture & The Leak-Free Split

#### What Amateur Teams Did
Most competing teams immediately dumped `admissions.csv` into a Jupyter notebook, ran `df.dropna()`, trained an XGBoost on 80/20 random train_test_split, and celebrated an artificial 0.94 ROC-AUC on Discord.

#### What Team HealthPulse Did
1. **Established the Git Contract:** Initialized a GitHub repo with the strict Datathon Directory structure. Every member worked on dedicated feature branches (`feat/wrangling-sam`, `feat/modeling-arjun`, `feat/ui-chloe`).
2. **Identified the Group Leakage Trap:** Arjun noticed `patient_id` appeared multiple times across admissions. A random 80/20 split would cause **data leakage** because the model would memorize individual chronic patients between train and validation.
3. **Built the Golden Evaluation Harness:**
   ```python
   # Arjun wrote src/validation.py before writing a single ML model
   from sklearn.model_selection import StratifiedGroupKFold
   sgkf = StratifiedGroupKFold(n_splits=5)
   # Groups = patient_id, Target = readmitted_30d
   ```
4. **Calculated the Economic Penalty:** Maya reviewed Medicare guidelines (HRRP) and found that hospitals lose up to 3% of total reimbursements for excess readmissions, costing the average regional hospital **\$3.8M annually**. This became their North Star metric.

---

### Phase 2: Hours 04–12 — The "Dirty Data" Audit & First Working Baseline

#### Discoveries During EDA
Sam analyzed missingness and data distributions:
- **Missing Vital Signs:** `vitals_timeseries.csv` had 35% missing blood pressure readings. Sam avoided mean imputation and used forward-fill within patient stays, followed by an indicator flag `is_bp_missing`.
- **Target Imbalance:** Only **11.4%** of admissions resulted in 30-day readmissions. Accuracy was a useless metric; PR-AUC and Recall@Top 15% were adopted.
- **Categorical Mess:** Over 850 distinct ICD-10 diagnosis codes. Arjun grouped them into 18 primary CCS (Clinical Classification Software) categories rather than one-hot encoding 850 columns.

#### Hour 10 Milestone: First Runnable Pipeline
At Hour 10, Arjun pushed a minimal LightGBM baseline script.
- **Local 5-Fold Stratified Group PR-AUC:** `0.382` (against a random baseline of `0.114`).
- **Leaderboard Score:** Submitted baseline predictions to the portal: `0.379` PR-AUC.
- **Victory:** Local CV matched the public leaderboard within 0.003. The team had a trusted evaluation harness and avoided leaderboard overfitting.

---

### Phase 3: Hours 12–24 — Feature Engineering Sprint

While Arjun worked on modeling, Sam spent 12 hours engineering clinical domain features.

#### Top 4 Game-Changing Feature Families Created:
1. **Prior Utilization Velocity:**
   - Count of emergency visits in the past 6 months and 12 months.
   - Ratio: `prior_er_visits_6m / (prior_er_visits_12m + 1)` (capturing accelerating illness).
2. **Vital Sign Volatility:**
   - Standard deviation and max-minus-min of systolic blood pressure during the final 24 hours prior to discharge (patients discharged with unstable vitals are readmitted at 3x rates).
3. **Polypharmacy Risk Index:**
   - Total distinct active medications at discharge, interacted with patient age: `num_meds * (age / 50)`.
4. **Social Vulnerability Index (SVI) Join:**
   - Sam merged an external public CDC Social Vulnerability Index dataset using patient 5-digit zip codes. Patients in low-income, low-transit zip codes had a 40% higher readmission hazard.

#### Results
Local CV PR-AUC jumped from `0.382` $\rightarrow$ `0.461`.

---

### Phase 4: Hours 24–34 — Ensembling, Calibration & Error Diagnostics

#### The 3-Model Diverse Ensemble
Arjun trained three structurally distinct models on the exact same 5-fold folds:
1. **LightGBM** (fast, tree-depth 6, heavy feature regularization).
2. **CatBoost** (exceptional handling of categorical insurance and hospital ward types).
3. **Regularized Logistic Regression** (linear baseline providing orthogonal, non-tree predictions).

#### Blending
Instead of a simple arithmetic mean, Arjun used **Rank Averaging**:
```python
rank_lgb = lgb_oof_preds.rank(pct=True)
rank_cat = cat_oof_preds.rank(pct=True)
rank_lr  = lr_oof_preds.rank(pct=True)
ensemble_pred = 0.50 * rank_lgb + 0.35 * rank_cat + 0.15 * rank_lr
```
* **Ensemble CV PR-AUC:** `0.488` (a +0.027 improvement over the best single model).

#### Error Analysis (Why Were We Missing?)
Arjun extracted false negatives (patients predicted safe who were readmitted). Sam and Maya reviewed them and found a clear pattern: patients discharged on a Friday afternoon were being readmitted at higher rates due to pharmacy closures. Sam engineered a binary feature `discharged_friday_weekend` which yielded an immediate +0.008 boost.

---

### Phase 5: Hours 34–42 — UI Simulator & Executive Report

While Arjun froze the final model weights, Chloe and Maya built the presentation assets:

#### Chloe's Streamlit App: "PulseShield"
Chloe built a 3-tab application:
1. **Executive Dashboard:** Showing the aggregate \$2.1M potential hospital savings based on a 15% intervention capacity.
2. **Real-Time Patient Intake Simulator:** Sliders for age, ICD category, discharge day, and prior ER visits. When a judge adjusted "Discharge Day" from Wednesday to Friday, the risk dial spiked into the red zone.
3. **SHAP Transparency Inspector:** A live waterfall plot explaining the exact top 3 factors driving that patient's risk score, accompanied by a suggested clinical protocol (*"Schedule 48h telehealth check-in & dispatch home nurse"*).

#### Maya's Executive Brief
Maya drafted a crisp 2-page PDF executive whitepaper following the handbook's template, quantifying:
- Cost per readmission penalty: \$14,500
- Cost of targeted post-discharge outreach: \$180 per patient
- Net Projected ROI for a 500-bed hospital: **\$1,840,000 annually**

---

### Phase 6: Hours 42–46 — Pitch Rehearsal & War Gaming

The team dedicated **4 full hours** solely to rehearsing their 3-minute pitch.

#### Maya Ran 8 Dry Runs With a Stopwatch:
- Run 1: 4 minutes 20 seconds (Disqualified if real).
- Cut technical slides, cut rambling data cleaning stories.
- Run 5: 2 minutes 55 seconds (Paced and confident).

#### War Gaming Difficult Judge Questions:
* *Judge asks:* "Did you account for data leakage with chronic repeat patients?"
  * *Arjun's ready answer:* "Yes, we enforced a strict Stratified Group 5-Fold split locked on unique patient IDs. Zero patient records cross-pollinated between train and validation."
* *Judge asks:* "Why would doctors trust this black box?"
  * *Chloe's ready answer:* "Every prediction in our UI is paired with a local TreeSHAP attribution waterfall showing the clinical drivers in plain English, and our system keeps the attending physician as the ultimate decision-maker."

---

### Phase 7: Hours 46–48 — The Final Pitch & The Win

During the final presentation round:
1. **Minute 1:** Maya opened with a real story of hospital penalties and the \$3.8M annual hemorrhage under HRRP guidelines.
2. **Minute 2:** Arjun explained the 5-fold Stratified Group CV, domain ratio features, and the 0.488 PR-AUC ensemble in 45 seconds.
3. **Minute 3:** Chloe demonstrated the live Streamlit simulator, invited a clinician judge to adjust a patient's vital volatility slider, and showed how the intervention trigger generated an immediate telehealth dispatch.

### The Judges' Deliberation Feedback
> *"Team HealthPulse did not just build the highest-performing model on the leaderboard. They were the only team that understood the clinical workflow, guarded against patient-level data leakage, and handed our executive panel an interactive solution ready to pilot in our wards on Monday morning."*
> 
> **Result: 1st Place Overall & Best Technical Execution Award.**

---

## 🔑 Key Lessons Learned

1. **Lock down CV early:** Never trust a single random split. If local CV matches public LB, you can iterate with complete confidence.
2. **Features beat hyperparameter tuning:** 80% of Team HealthPulse's score gains came from domain ratios and external data merges; Optuna tuning added only ~5%.
3. **Judges buy decisions, not probabilities:** Wrapping predictions in financial savings and human-in-the-loop workflows is what converts top-5 placement into 1st place.
