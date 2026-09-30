# 🤝 Team Git & Notebook Workflow: Preventing 3 AM Merge Disasters

<!-- markdownlint-disable MD013 -->

> 🟢 **In plain English:** Nothing ruins a datathon faster than 3 team members trying to merge their Jupyter notebooks at 3 AM and overwriting each other's models. This guide shows you the exact Git hygiene and team handoff rules used by top engineering teams.

---

## 💥 The #1 Nightmare: Jupyter Notebook Merge Conflicts

Jupyter notebooks (`.ipynb`) are stored as massive, opaque JSON files that contain metadata, base64 images, and cell execution counts. If two teammates edit cell 4 of the same notebook, **Git will corrupt the file with merge conflicts** that are almost impossible to fix under pressure.

### The 3 Ways Winning Teams Avoid This:

#### Option A (Recommended): Use Pure Python Scripts for Modeling
Keep Jupyter/Marimo for quick visual EDA in Hour 1–3, but move your reusable pipeline code into clean Python files (e.g. `data_clean.py`, `train.py`, `app.py`). Python files merge cleanly with Git!

#### Option B: Split Notebooks by Team Member & Phase
Never have two people work in `main.ipynb`. Use a numbered naming convention:
- `notebooks/01_eda_alice.ipynb` (Alice owns EDA)
- `notebooks/02_features_bob.ipynb` (Bob owns Feature Engineering)
- `notebooks/03_model_charlie.ipynb` (Charlie owns LightGBM/CatBoost)
- `app/streamlit_app.py` (David owns the UI)

#### Option C: Strip Outputs Before Committing (`nbstripout`)
Install `nbstripout` in your environment. It automatically removes heavy graphs and output tables before git saves the notebook:
```bash
pip install nbstripout
nbstripout --install
```

---

## 📁 The Winning Datathon Repository Directory Layout

Follow this battle-tested directory structure:

```text
my-datathon-project/
├── data/
│   ├── raw/               # ⚠️ READ ONLY! Never edit or overwrite raw files
│   └── processed/         # Cleaned Parquet tables (gitignored!)
├── notebooks/             # Exploratory notebooks (named by member/task)
│   ├── 01_eda.ipynb
│   └── 02_feature_tests.ipynb
├── src/                   # Reusable production code
│   ├── __init__.py
│   ├── data_clean.py      # Polars cleaning & datetime functions
│   ├── features.py        # Feature engineering recipes
│   └── train.py           # CV loop & model training
├── artifacts/             # Exported model weights & SHAP explainers
│   ├── best_model.pkl
│   └── shap_explainer.pkl
├── app/                   # The interactive user demo
│   └── streamlit_app.py
├── reports/               # Executive report & slide deck
│   ├── executive_summary.md
│   └── pitch_deck.pdf
├── requirements.txt       # Dependencies list
├── quickstart.py          # 1-command reproducible pipeline
└── .gitignore             # Ignores large datasets & virtual environments
```

---

## 📑 The 4 Team Role Handoff Contracts

To work at maximum speed, establish strict "Handoff Contracts" between roles:

```text
[Data Architect]
       │
       ▼ Clean Parquet + Schema Dict
[ML Modeler]
       │
       ▼ Serialized Model (.pkl) + Sample Features CSV
[UI & Demo Engineer]
       │
       ▼ Working Streamlit App URL + 30s Backup Video
[Pitch Lead & Storyteller]
```

### Contract 1: Data Architect ➔ ML Modeler (By Hour 6)
- **Deliverable:** `data/processed/train_clean.parquet` and `data/processed/test_clean.parquet`.
- **Contract Rule:** Must provide a short text snippet specifying:
  - Exact target column name.
  - List of categorical columns (for CatBoost/LightGBM).
  - List of numerical columns.
  - Confirmation that no IDs or leaky future timestamps are in the features!

### Contract 2: ML Modeler ➔ UI Engineer (By Hour 18)
- **Deliverable:** `artifacts/best_model.pkl` and `artifacts/sample_features.csv`.
- **Contract Rule:** The serialized model must have a standard `.predict_proba(X)` API. The sample features CSV must contain 10–20 realistic rows with their minimum and maximum ranges so the UI Engineer knows where to set the slider bounds.

### Contract 3: UI Engineer ➔ Pitch Lead (By Hour 36)
- **Deliverable:** Live Streamlit Community Cloud URL + a 30-second local 1080p screen recording of the app working.
- **Contract Rule:** The app must have a fallback surrogate model so that even if the server lags during the live pitch, the demo responds instantly.

---

## 🚫 The 4 Golden Git Rules During a Datathon

1. **Never commit raw data files over 10MB to GitHub.** Use `.gitignore` for `.csv`, `.parquet`, and `.zip`. Large files will freeze your Git pushes.
2. **Pull before you push:** Always run `git pull origin main` before pushing new work to avoid merge rejections.
3. **Commit often with short, clear messages:** E.g. `feat: add rolling 7d revenue feature` or `fix: drop leaking timestamp column`.
4. **Code freeze 2 hours before the deadline.** At Hour 46, stop touching model code! Spend the final 2 hours polishing slides, testing the demo, and rehearsing the pitch.
