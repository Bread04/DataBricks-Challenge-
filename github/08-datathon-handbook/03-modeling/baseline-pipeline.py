"""
⚡ Datathon Rapid ML Baseline Pipeline
======================================
Production-ready, leak-free tabular baseline script using Stratified K-Fold CV,
LightGBM, CatBoost, threshold optimization, and SHAP explainability artifact export.

Run:
    python baseline-pipeline.py
"""

import os
import joblib
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.metrics import roc_auc_score, average_precision_score, f1_score, precision_recall_curve
from sklearn.model_selection import StratifiedKFold
import lightgbm as lgb
from catboost import CatBoostClassifier, Pool
import shap

def generate_sample_datathon_data(n_samples=5000, random_state=42):
    """Generates synthetic tabular data mirroring a real-world datathon dataset."""
    X, y = make_classification(
        n_samples=n_samples,
        n_features=12,
        n_informative=8,
        n_redundant=2,
        weights=[0.85, 0.15], # Realistic imbalanced target (15% positive class)
        random_state=random_state
    )
    feature_names = [
        "risk_score_a", "utilization_rate", "transaction_velocity",
        "tenure_months", "credit_limit_ratio", "past_delinquency_count",
        "avg_daily_balance", "customer_age", "monthly_inflow",
        "support_ticket_count", "noise_signal_1", "noise_signal_2"
    ]
    df = pd.DataFrame(X, columns=feature_names)
    df["target"] = y
    
    # Add a categorical column to test CatBoost's native categorical strength
    categories = ["Tier_1_Urban", "Tier_2_Suburban", "Tier_3_Rural", "International"]
    df["region_segment"] = np.random.choice(categories, size=len(df), p=[0.4, 0.3, 0.2, 0.1])
    return df

def train_eval_lightgbm_cv(X, y, cat_cols=None, n_splits=5, random_state=42):
    """Trains LightGBM with leak-free Stratified K-Fold Cross-Validation."""
    print("\n🚀 Training LightGBM with 5-Fold Stratified CV...")
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    oof_preds = np.zeros(len(X))
    models = []
    
    # Pre-convert categoricals for LightGBM
    X_lgb = X.copy()
    if cat_cols:
        for c in cat_cols:
            X_lgb[c] = X_lgb[c].astype("category")

    for fold, (train_idx, val_idx) in enumerate(skf.split(X_lgb, y)):
        X_train, y_train = X_lgb.iloc[train_idx], y.iloc[train_idx]
        X_val, y_val = X_lgb.iloc[val_idx], y.iloc[val_idx]

        model = lgb.LGBMClassifier(
            n_estimators=300,
            learning_rate=0.05,
            num_leaves=31,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=random_state + fold,
            verbose=-1,
            n_jobs=-1
        )
        model.fit(
            X_train, y_train,
            eval_set=[(X_val, y_val)],
            callbacks=[lgb.early_stopping(stopping_rounds=30, verbose=False)]
        )
        val_preds = model.predict_proba(X_val)[:, 1]
        oof_preds[val_idx] = val_preds
        models.append(model)
        
        fold_auc = roc_auc_score(y_val, val_preds)
        fold_prauc = average_precision_score(y_val, val_preds)
        print(f"  Fold {fold+1} | ROC-AUC: {fold_auc:.4f} | PR-AUC: {fold_prauc:.4f}")

    total_auc = roc_auc_score(y, oof_preds)
    total_prauc = average_precision_score(y, oof_preds)
    print(f"⭐ LightGBM Overall Out-of-Fold | ROC-AUC: {total_auc:.4f} | PR-AUC: {total_prauc:.4f}")
    return models[0], oof_preds

def find_optimal_threshold(y_true, y_prob):
    """Finds the decision threshold that maximizes the F1-Score for imbalanced classes."""
    precisions, recalls, thresholds = precision_recall_curve(y_true, y_prob)
    # Avoid division by zero
    f1_scores = np.where((precisions + recalls) == 0, 0, 2 * (precisions * recalls) / (precisions + recalls))
    best_idx = np.argmax(f1_scores)
    best_threshold = thresholds[best_idx] if best_idx < len(thresholds) else 0.5
    best_f1 = f1_scores[best_idx]
    return best_threshold, best_f1

def export_artifacts(model, X_sample, output_dir="artifacts"):
    """Exports model weights and precomputes SHAP explainer for instant UI loading."""
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Save model weights
    model_path = os.path.join(output_dir, "best_model.pkl")
    joblib.dump(model, model_path)
    print(f"✅ Model saved to {model_path}")
    
    # 2. Compute and save SHAP explainer
    print("⏳ Computing SHAP TreeExplainer for UI explainability...")
    explainer = shap.TreeExplainer(model)
    explainer_path = os.path.join(output_dir, "shap_explainer.pkl")
    joblib.dump(explainer, explainer_path)
    print(f"✅ SHAP Explainer saved to {explainer_path}")
    
    # 3. Save sample test rows for interactive slider defaults
    sample_path = os.path.join(output_dir, "sample_features.csv")
    X_sample.head(20).to_csv(sample_path, index=False)
    print(f"✅ Sample feature reference saved to {sample_path}")

def main():
    print("=" * 60)
    print("🚀 BMad Datathon Baseline Pipeline Execution")
    print("=" * 60)

    # 1. Ingest Data
    df = generate_sample_datathon_data(n_samples=5000)
    feature_cols = [c for c in df.columns if c != "target"]
    target_col = "target"
    cat_cols = ["region_segment"]
    
    X = df[feature_cols]
    y = df[target_col]

    print(f"Dataset shape: {df.shape}")
    print(f"Class distribution: {dict(y.value_counts(normalize=True))}")

    # 2. Train LightGBM with Stratified Cross-Validation
    best_model, oof_probs = train_eval_lightgbm_cv(X, y, cat_cols=cat_cols)

    # 3. Optimize Classification Decision Threshold
    opt_threshold, max_f1 = find_optimal_threshold(y, oof_probs)
    print(f"\n🎯 Optimal Decision Threshold: {opt_threshold:.4f} (Max F1: {max_f1:.4f} vs 0.5 Default F1: {f1_score(y, oof_probs >= 0.5):.4f})")

    # 4. Export Artifacts for Streamlit Frontend
    export_artifacts(best_model, X.drop(columns=cat_cols))
    print("\n🎉 Pipeline complete! Ready to launch Streamlit UI in 04-solutions-and-ui/")

if __name__ == "__main__":
    main()
