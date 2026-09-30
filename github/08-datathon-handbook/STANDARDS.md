# 📜 Datathon Standard Operating Procedures & Engineering Standards (`STANDARDS.md`)

<!-- markdownlint-disable MD013 -->

> **The definitive quality contract for competitive data science projects.**  
> Follow these engineering standards to ensure your datathon submission is mathematically sound, leak-free, reproducible, and ready to stand up against intense scrutiny from technical judges and industry sponsors.

---

## 🏛️ Standard 1: Repository Architecture & Directory Taxonomy

All datathon submissions must adhere to a clean separation of concerns. Do not mix scratchpad exploration with production modeling code or web applications.

```text
datathon-submission/
├── .gitignore                 # Prevents large data/model files from polluting Git
├── README.md                  # Project overview, hero metric, reproduction instructions
├── requirements.txt           # Pinned Python package dependencies
├── PROJECT_CONTEXT.md         # Single source of truth for problem, metric & features
│
├── data/                      # Local data directory (NEVER COMMITTED TO GIT)
│   ├── raw/                   # Immutable original competition files
│   └── processed/             # Cleaned, feature-engineered Parquet files
│
├── notebooks/                 # Scratchpad exploration & data inspection
│   ├── 01_eda_and_profiling.ipynb
│   └── 02_feature_experiments.ipynb
│
├── src/                       # Production-grade, reproducible Python modules
│   ├── __init__.py
│   ├── data_loader.py         # Polars/DuckDB ingestion & relational joins
│   ├── features.py            # Leak-free feature transformation functions
│   ├── validation.py          # K-fold split generators (Stratified/Group/Time)
│   └── model.py               # Model training, early stopping & OOF prediction
│
├── app/                       # The "Last-Mile" Interactive Solution
│   ├── app.py                 # Streamlit What-If Scenario Simulator
│   └── utils.py               # Preprocessing & inference wrappers for the UI
│
├── artifacts/                 # Outputs generated during runs
│   ├── oof_predictions.csv    # Full out-of-fold validation probabilities
│   ├── feature_importance.csv # Global feature attributions
│   └── test_submission.csv    # Final submission file for competition leaderboard
│
└── docs/                      # Presentation & evaluation collateral
    ├── executive_summary.md   # 2-page C-suite whitepaper
    └── presentation_deck.pdf  # Final 10-slide pitch deck
```

---

## 🔒 Standard 2: Data Hygiene & Git Protocols

1. **The Immutability Rule:** Never overwrite or modify files in `data/raw/`. Treat raw competition data as read-only.
2. **The Git Exclusion Rule:** Never commit raw data files, trained model binaries, or cache folders to version control.
   - Required `.gitignore` minimum:
     ```gitignore
     data/
     *.csv
     *.parquet
     *.zip
     *.tar.gz
     *.pkl
     *.joblib
     __pycache__/
     .ipynb_checkpoints/
     .env
     venv/
     .venv/
     ```
3. **Branching Discipline:**
   - `main`: Clean, runnable code only.
   - `feat/data-wrangling`: Schema inspection, joins, and cleaning.
   - `feat/modeling`: Cross-validation loops, LightGBM/CatBoost pipelines.
   - `feat/ui-demo`: Streamlit application and interactive widgets.

---

## 🛡️ Standard 3: Cross-Validation & Data Leakage Prevention

Data leakage is the single most common cause of catastrophic leaderboard shake-ups (teams dropping from 1st on the public leaderboard to 40th on the private leaderboard).

### The 4 Non-Negotiable Leakage Rules:
1. **Entity Grouping:** If an entity (e.g. `user_id`, `patient_id`, `store_id`) appears multiple times in the dataset, you **MUST** use `StratifiedGroupKFold` or `GroupKFold`. An entity must never exist in both train and validation folds.
2. **Temporal Integrity:** If the prediction involves a timestamp or sequence, you **MUST** use `TimeSeriesSplit` or a cutoff date. Never shuffle or look into the future.
3. **Fit on Train Only:** All transformers—including mean/median imputers, target encoders, min-max scalers, and TF-IDF vectorizers—must be fit **strictly** on the training fold, then used to transform the validation/test fold.
4. **Out-of-Fold (OOF) Logging:** You must generate and store Out-of-Fold predictions for the entire training set. Your local CV score is computed on these concatenated OOF predictions.

```python
# Standard Golden 5-Fold Evaluation Harness
from sklearn.model_selection import StratifiedGroupKFold
import numpy as np

sgkf = StratifiedGroupKFold(n_splits=5)
oof_predictions = np.zeros(len(df))

for fold, (train_idx, val_idx) in enumerate(sgkf.split(X, y, groups=df["entity_id"])):
    X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
    X_val, y_val = X.iloc[val_idx], y.iloc[val_idx]
    
    # Preprocessing fit on train fold ONLY
    # model.fit(X_train, y_train)
    # oof_predictions[val_idx] = model.predict_proba(X_val)[:, 1]
```

---

## ⚙️ Standard 4: Code Quality & Reproducibility

1. **Seed Everything:** Every script involving random numbers must explicitly pin the random state:
   ```python
   SEED = 42
   import random, os, numpy as np
   random.seed(SEED)
   os.environ["PYTHONHASHSEED"] = str(SEED)
   np.random.seed(SEED)
   ```
2. **No Monolithic Notebooks:** Notebooks are for initial visualization and hypothesis checking. Once an approach works, refactor it into clean functions in `src/`.
3. **Execution Verification:** A technical judge must be able to clone the repository, install dependencies, and run:
   ```bash
   python -m src.model
   ```
   to reproduce your local cross-validation score without errors or missing files.

---

## 💰 Standard 5: Decisions & Unit Economics Over Raw Loss

Judges from industry sponsors do not evaluate machine learning models in a vacuum. A model that achieves 0.92 ROC-AUC is useless if it costs more to operate than the revenue it recovers.

1. **Calculate the Financial Payoff Matrix:**
   - $\text{Value}(\text{True Positive})$: Dollar savings or revenue gained.
   - $\text{Cost}(\text{False Positive})$: Cost of an unnecessary inspection, alert, or discount.
   - $\text{Penalty}(\text{False Negative})$: Cost of a missed fraud event, outage, or disease case.
2. **Optimize the Decision Threshold:**
   - Sweep the classification threshold $T \in [0.01, 0.99]$ on validation Out-of-Fold probabilities to maximize the **Net Dollar Value**, rather than blindly accepting $T = 0.50$.
3. **Report the Hero Metric:**
   - In slides and executive reports, frame your result as:
     > *"Our model prevents \$1.42M in annual equipment downtime with an 84% precision rate at the optimal 0.32 risk threshold."*

---

## 🎨 Standard 6: The "Last-Mile" UI Standards (Streamlit)

A model trapped in code is an academic exercise. A model running in a live interface is an investment-ready product.

1. **Latency:** Ensure inference executes in under **300 milliseconds**. Use `@st.cache_data` and pre-load model artifacts so sliders respond instantaneously.
2. **Offline Resilience:** The application must be able to run 100% locally on `localhost:8501` without an active internet connection in case conference Wi-Fi fails.
3. **The 3 Mandatory Dashboard Elements:**
   - **Top Row:** 3 Hero KPIs (Net Projected Value \$, Current Risk Level %, Action Status).
   - **Interactive Core:** Sliders and inputs that immediately recalculate the prediction in real time (Counterfactual What-If Simulator).
   - **Transparency View:** A local SHAP waterfall or driver attribution showing the top 3 factors explaining *why* this prediction was generated.

---

## ✅ Standard 7: Pre-Submission 10-Point Audit Checklist

Complete this checklist 2 hours before the competition submission portal closes:

- [ ] **1. Leakage Verification:** Are any feature names suspiciously correlated with the target? Did local CV score stay realistic ($<0.99$)?
- [ ] **2. Clean Submission CSV:** Does the submission file match the exact column names, row count, and ID order specified by the organizers?
- [ ] **3. No NaNs in Predictions:** Verified that `np.isnan(submission_preds).sum() == 0`.
- [ ] **4. Git Tree Clean:** Did you verify that no multi-GB data files or `.pkl` model checkpoints are staged for Git?
- [ ] **5. Requirements Frozen:** Is `requirements.txt` up-to-date with pinned versions?
- [ ] **6. UI Tested on Clean Port:** Did you run `streamlit run app/app.py` in a fresh terminal window and verify all sliders work?
- [ ] **7. Executive Summary Exported:** Is `executive_summary.md` exported to PDF or cleanly formatted in GitHub Markdown?
- [ ] **8. 3-Minute Pitch Timed:** Did the team rehearse the presentation with a live stopwatch under 3 minutes?
- [ ] **9. Backup Video Recorded:** Did you record a 60-second screen capture of the working UI in case the projector or laptop crashes?
- [ ] **10. Hero Metric Front & Center:** Is the quantified business ROI clearly visible on Slide 1 and the Dashboard banner?
