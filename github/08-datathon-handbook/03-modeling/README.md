# 🤖 Rapid ML Modeling & Cross-Validation Guide

<!-- markdownlint-disable MD013 -->

> In a datathon, your goal is not to train the most complex deep neural network. Your goal is to establish a rock-solid, leak-free validation loop in Hour 2, iterate rapidly on features, and export an explainable model artifact for the demo.

---

## ⚡ The Modeling Hierarchy

```text
[Step 1] Baseline Plumber (Minute 30)
         └─ Logistic Regression / Ridge / Default LightGBM (ensure pipeline works)
[Step 2] Feature Velocity (Hour 2–12)
         └─ LightGBM (fastest iteration on CPU) & CatBoost (categorical dominance)
[Step 3] Automated Stacking (Hour 12–20)
         └─ AutoGluon (multi-layer ensembling with out-of-fold predictions)
[Step 4] Decision Optimization (Hour 20–24)
         └─ Threshold tuning for business cost & SHAP explainability export
```

---

## 🛡️ The 3 Rules of Leak-Free Validation

1. **Never Impute or Scale Before Splitting**:
   - If you compute `df.fillna(df.mean())` on the whole dataset before K-Fold, future test values bleed into the training folds.
   - Always fit your transformers strictly on `train_fold`, then `.transform()` on `val_fold`.
2. **Respect the Grouping**:
   - If multiple rows belong to the same hospital patient, user account, or physical building, standard K-Fold will put some rows in train and others in val. Use `GroupKFold`.
3. **Respect Time**:
   - If data has dates (e.g. daily sales, hourly traffic), standard shuffling evaluates past events using future data. Use `TimeSeriesSplit` or rolling validation windows.

---

## 🚀 Running the Baseline Pipeline

The provided script [`baseline-pipeline.py`](baseline-pipeline.py) sets up a full Stratified K-Fold pipeline, trains LightGBM, optimizes the decision threshold for imbalanced classes, and exports `best_model.pkl` and `shap_explainer.pkl` directly for the UI:

```bash
python baseline-pipeline.py
```
Outputs saved to `artifacts/`:
- `best_model.pkl`: Serialized model ready for instantaneous inference.
- `shap_explainer.pkl`: Precomputed TreeExplainer for the Streamlit dashboard.
- `sample_features.csv`: Reference rows for UI slider defaults.
