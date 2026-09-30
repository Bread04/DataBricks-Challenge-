# 🚀 Datathon Starter Project Template

<!-- markdownlint-disable MD013 -->

> **Drop this entire directory into your new datathon repository to start with winning best practices.**  
> Pre-configured with a leak-free evaluation harness, clean directory structure, Streamlit interactive app boilerplate, and AI agent instructions.

---

## ⚡ Quickstart: 3 Steps for Hour 0

### 1. Install Pinned Dependencies
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Update Project Context
Open [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md) and fill in:
- The competition name & time limit
- Target variable name & evaluation metric
- Initial hypotheses and unit economics

### 3. Run the Baseline Model & Interactive App
```bash
# Run baseline ML pipeline
python -m src.model

# Launch the Streamlit Scenario Simulator
streamlit run app/app.py
```

---

## 📂 Project Architecture

```text
├── .gitignore                 # Pre-configured to prevent large data leaks
├── README.md                  # This file
├── requirements.txt           # Pinned datathon tech stack (Polars, LightGBM, Streamlit)
├── PROJECT_CONTEXT.md         # Persistent context for team & AI coding assistants
├── SKILLS.md                  # Agent skill specification for Cursor / Claude Code
│
├── data/                      # Local data (gitignored)
│   ├── raw/                   # Place original CSV/Parquet files here
│   └── processed/             # Cleaned feature tables
│
├── notebooks/                 # Scratchpad exploration only
│   └── 01_exploratory_eda.ipynb
│
├── src/                       # Production-grade Python modules
│   ├── __init__.py
│   ├── data_loader.py         # Polars/DuckDB data ingestion
│   ├── features.py            # Feature engineering functions
│   ├── validation.py          # Leak-free cross-validation split
│   └── model.py               # Model training & OOF evaluation
│
├── app/                       # Interactive Last-Mile UI
│   └── app.py                 # Streamlit What-If Scenario Simulator
│
└── docs/                      # Presentation deliverables
    ├── executive_summary.md   # 2-page brief for judges
    └── pitch_deck.pdf         # 10-slide presentation
```

---

## 🏆 The 5 Golden Rules
1. **Never commit data to Git:** Keep `data/` strictly gitignored.
2. **Never leak groups:** If you have repeated entities (patients, stores, users), use `StratifiedGroupKFold`.
3. **Never present raw loss alone:** Convert probabilities to dollar value ROI.
4. **Never show static slides only:** Give judges an interactive Streamlit simulator they can touch.
5. **Time-box everything:** Follow the 48-hour timeline in [`../01-playbook/datathon-battle-plan.md`](../01-playbook/datathon-battle-plan.md).
