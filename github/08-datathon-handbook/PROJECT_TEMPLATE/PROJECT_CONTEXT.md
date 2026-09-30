# 🎯 Project Context: <Insert Project Name Here>

<!-- markdownlint-disable MD013 -->

> **Single Source of Truth for Human Teammates & AI Coding Assistants.**  
> Keep this file updated throughout the datathon. Whenever an AI assistant (Antigravity, Claude Code, Cursor) is asked to build features or debug models, it reads this file to get full operational context.

---

## 📌 1. Challenge & Problem Brief

* **Competition Name:** `<e.g. National Health Data Challenge 2026 / TAMU Datathon>`
* **Track / Sponsor:** `<e.g. Healthcare Analytics Track / Blue Cross Blue Shield>`
* **Time Remaining:** `<e.g. 36 hours remaining (Ends Sunday 12:00 PM)>`
* **Target Variable ($y$):** `<e.g. readmitted_30d (Binary 0/1)>`
* **Official Evaluation Metric:** `<e.g. PR-AUC (Average Precision) / RMSE / F1-Score>`
* **Benchmark / Random Baseline Score:** `<e.g. 0.114 PR-AUC (random positive rate)>`
* **Our Current Best Local 5-Fold CV Score:** `<e.g. 0.488 PR-AUC>`
* **Our Current Public Leaderboard Score:** `<e.g. 0.481 PR-AUC>`

---

## 💡 2. The Core Hypothesis & Economic Bottleneck

### The Economic Bottleneck
* What is the real-world cost of this problem?
  > *`<e.g. Hospitals lose up to 3% of total Medicare reimbursements due to excessive 30-day readmissions, costing the average regional facility $3.8M annually.>`*
* What is our targeted Hero Business Metric?
  > *`<e.g. Projected Net Annual Savings: $1.84M across 1,200 beds by targeting top 15% high-risk patients.>`*

### The 3 Core Hypotheses
1. **Hypothesis 1 (Clinical Volatility):** `<e.g. Patients with high vital sign volatility in the final 24 hours prior to discharge are 3x more likely to be readmitted.>`
2. **Hypothesis 2 (Utilization Velocity):** `<e.g. Patients whose emergency room visit frequency doubled over the past 6 months vs prior year represent accelerating chronic illness.>`
3. **Hypothesis 3 (Social Determinants):** `<e.g. Patients residing in zip codes with high CDC Social Vulnerability Index scores suffer higher readmission due to lack of post-discharge transit.>`

---

## 📂 3. Data Dictionary & Relational Schema

| Table Name | File Name | Rows | Primary Key | Key Columns & Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Patients** | `data/raw/patients.csv` | 50,000 | `patient_id` | Demographics, insurance type, zip code |
| **Admissions** | `data/raw/admissions.csv` | 120,000 | `admission_id` | Admission/discharge dates, ICD-10 code, target `readmitted_30d` |
| **Vitals** | `data/raw/vitals.csv` | 1.8M | `vital_id` | Foreign key `admission_id`, hourly BP, HR, O2 readings |

### Data Hygiene Notes & Red Flags
* `patient_id` appears repeatedly across admissions: **Requires `StratifiedGroupKFold(groups=patient_id)` to avoid severe data leakage!**
* `vitals.csv` has 35% missing blood pressure entries: Handled via forward-fill within stay + `is_bp_missing` indicator.
* Target imbalance: Only **11.4%** positive class. Do not optimize accuracy. Optimize PR-AUC and tune decision threshold.

---

## 🛡️ 4. Validation Harness Protocol

* **Cross-Validation Scheme:** `StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=42)`
* **Group Column:** `patient_id`
* **Target Column:** `readmitted_30d`
* **Leakage Safeguards Enforced:**
  - Imputers and scalers fit on train fold ONLY.
  - Zero target encoding without out-of-fold smoothing.
  - Future timestamps strictly excluded from historical features.

---

## 🧪 5. Experiment Tracking & Model Leaderboard

| Exp ID | Model / Architecture | Key Features Added | Local 5-Fold CV | Public LB | Delta | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `EXP-00` | Random Guessing / Dummy | Baseline (none) | 0.114 | 0.112 | - | Benchmark |
| `EXP-01` | LightGBM Baseline | Raw numerical features only | 0.382 | 0.379 | +0.268 | Approved |
| `EXP-02` | LightGBM + Domain Ratios | Prior ER velocity + SVI join | 0.461 | 0.458 | +0.079 | Approved |
| `EXP-03` | CatBoost Native Categoricals| ICD-10 categories + insurance | 0.452 | 0.449 | -0.009 | Keep for ensemble |
| `EXP-04` | 3-Model Rank Average Ensemble| LightGBM (0.50) + CatBoost (0.35) + Ridge (0.15) | **0.488** | **0.481** | **+0.027** | **FINAL BEST** |

---

## 💰 6. Unit Economics & Decision Threshold

* **Cost of True Positive (Intervention):** `+$1,200 net benefit` (avoided readmission penalty minus outreach cost)
* **Cost of False Positive (Wasted Action):** `-$180` (nurse call & home telehealth kit)
* **Cost of False Negative (Missed Readmission):** `-$14,500` (hospital penalty and uncompensated emergency care)
* **Default Threshold (0.50) Net Value:** `$820,000 / year`
* **Optimized Threshold (0.28) Net Value:** **`$1,840,000 / year`** *(+$1.02M improvement!)*

---

## 🖥️ 7. Streamlit Simulator Specifications

* **App Entrypoint:** `app/app.py`
* **Interactive Sliders for Demo:**
  1. `Patient Age` (Slider 18 to 95)
  2. `Prior ER Visits in 6 Months` (Slider 0 to 8)
  3. `Systolic BP Volatility` (Slider 5 to 45 mmHg)
  4. `Discharge Day` (Selectbox Monday to Sunday — Sunday triggers spike)
* **Hero Outputs:**
  - Dynamic Risk Meter (Low / Moderate / High Sepsis-Readmission Hazard)
  - Estimated Net Financial Savings for Hospital
  - Local SHAP waterfall explaining top 3 risk drivers
  - "Dispatch Telehealth Voucher" instant button
