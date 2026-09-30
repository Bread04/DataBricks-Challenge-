# Dimension 1 Digest: Datathon Dynamics, Problem Framing & Judging Criteria

- Topic: Datathon & ML Hackathon Strategy
- Researcher: datathon-dynamics-r1-1
- Date: 2026-09-23

## Key Findings

### 1. Datathons vs Software Hackathons
- In a software hackathon, judges look primarily at functional software, UX polish, and product completeness.
- In a **datathon** (data hackathon / data science competition), judges evaluate:
  1. **Problem Framing & Domain Relevance (25%)**: Did the team understand the real-world operational or policy bottleneck, rather than just running an arbitrary algorithm?
  2. **Data Wrangling & Statistical Rigor (25%)**: Did the team address missing values, bias, class imbalance, and data leakage? Did they formulate a sound local cross-validation strategy?
  3. **Modeling & Insight Quality (25%)**: Model choice justification, metric alignment (e.g. PR-AUC for fraud/rare diseases vs ROC-AUC or RMSE), feature importance (SHAP/LIME), and actionable recommendations.
  4. **The "Last-Mile" Solution & Pitch (25%)**: Can a human operator (doctor, logistics planner, citizen) interact with the model via a dashboard/simulator to make a better decision?

### 2. The 24-48h Team Role Matrix
Winning teams avoid the "everyone open Jupyter and compete on ROC-AUC" trap. They divide into 4 crisp roles:
- **Role 1: Data Ingestion & Feature Architect**: Owns cleaning, parsing dates, missing value strategy, joining external data, and providing a clean Parquet table via Polars/DuckDB.
- **Role 2: ML Modeler**: Sets up Stratified K-Fold CV, trains baseline models (LightGBM/CatBoost), runs fast AutoML (AutoGluon), exports artifacts, and generates SHAP values.
- **Role 3: Solution & UI Builder**: Builds the interactive Streamlit, Gradio, or FastAPI+Next.js interface with sliders, scenario simulator ("what-if" calculators), and interactive charts.
- **Role 4: Domain Storyteller / Pitch Lead**: Synthesizes the business narrative, slides, executive summary, ROI calculation, and failure/risk mitigation.

### 3. Avoiding the Leaderboard Trap
- Public leaderboard overfitting is the #1 killer in competitive datathons.
- Rule: **Trust local CV over leaderboard feedback**. Set up a leak-free Stratified / Group / Time-Series K-Fold CV from Hour 2.

## Sources
- [1] Dev.to: Winning Data Hackathons and Datathons Strategy Guide (2025/2026)
- [2] Reddit r/datascience & r/machinelearning: "How top teams consistently win datathons"
- [3] HackerEarth: Datathon & Data Challenge Evaluation Rubrics
