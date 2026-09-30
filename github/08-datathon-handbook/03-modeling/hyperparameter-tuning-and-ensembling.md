# ⚡ Hyperparameter Tuning & Ensembling Under the Clock

<!-- markdownlint-disable MD013 -->

> 🟢 **In plain English:** In a 24-hour datathon, spending 6 hours running brute-force grid searches is a recipe for defeat. Winning teams use **time-capped Bayesian optimization** and **rank-based ensembling** to boost their leaderboard score in the final hours.

---

## ⏱️ Tuning Rule #1: Never Use GridSearchCV!

Standard `GridSearchCV` tries every single parameter combination exhaustively. On a 500,000-row dataset with 5-fold CV, a grid of 30 combinations will run for 4 hours and crash your laptop.

### What to Use Instead:
- **FLAML (Fast & Lightweight AutoML):** Automatically finds near-optimal hyperparameters within a strict budget (e.g. `time_budget=300` seconds).
- **Optuna with Pruning:** Tries smart parameter combinations using Bayesian search, killing unpromising trials after 3 trees.

---

## 🎯 The Only 4 Hyperparameters That Truly Matter

Don't tune 20 parameters. 95% of performance in gradient boosting comes from these four:

| Parameter | LightGBM Name | CatBoost Name | Recommended Search Range | What It Controls |
| --- | --- | --- | --- | --- |
| **Tree Depth / Size** | `num_leaves` | `depth` | `num_leaves`: [15, 63]<br>`depth`: [4, 8] | Model complexity (lower = less overfitting) |
| **Step Size** | `learning_rate` | `learning_rate` | [0.03, 0.10] | Shrinkage per tree (0.05 is the sweet spot) |
| **Feature Sampling** | `colsample_bytree` | `rsm` | [0.6, 0.9] | Fraction of columns sampled per tree |
| **Row Sampling** | `subsample` | `subsample` | [0.7, 0.95] | Fraction of data sampled per tree |

---

## 🛠️ Rapid Tuning Recipe with Optuna (10-Minute Cap)

```python
import optuna
import lightgbm as lgb
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score

def objective(trial):
    params = {
        "n_estimators": 250,
        "learning_rate": trial.suggest_float("learning_rate", 0.03, 0.12),
        "num_leaves": trial.suggest_int("num_leaves", 15, 63),
        "subsample": trial.suggest_float("subsample", 0.6, 0.95),
        "colsample_bytree": trial.suggest_float("colsample_bytree", 0.6, 0.95),
        "min_child_samples": trial.suggest_int("min_child_samples", 20, 100),
        "random_state": 42,
        "verbose": -1,
        "n_jobs": -1
    }
    
    skf = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
    scores = []
    
    for train_idx, val_idx in skf.split(X, y):
        X_tr, y_tr = X.iloc[train_idx], y.iloc[train_idx]
        X_va, y_va = X.iloc[val_idx], y.iloc[val_idx]
        
        model = lgb.LGBMClassifier(**params)
        model.fit(X_tr, y_tr)
        preds = model.predict_proba(X_va)[:, 1]
        scores.append(roc_auc_score(y_va, preds))
        
    return sum(scores) / len(scores)

# Run smart optimization capped at 10 minutes (600 seconds)
optuna.logging.set_verbosity(optuna.logging.WARNING)
study = optuna.create_study(direction="maximize")
study.optimize(objective, timeout=600) # Stops automatically at 10 minutes!

print("Best Parameters Found:")
print(study.best_params)
```

---

## 🤝 Winning Ensembling Techniques

Combining predictions from multiple distinct model architectures (e.g. LightGBM + CatBoost + XGBoost) almost always outperforms any single model.

### Technique 1: Rank-Averaging (The Secret Weapon)
Raw predicted probabilities from different models often have different calibrations (e.g., CatBoost might output probabilities between 0.10 and 0.40, while LightGBM outputs 0.02 to 0.85). If you take a simple arithmetic average, the model with higher variance will dominate.

**The Solution:** Convert probabilities to percentiles (ranks) before averaging!

```python
import numpy as np
from scipy.stats import rankdata

def rank_average_predictions(preds_list, weights=None):
    """
    Blends multiple prediction arrays by ranking them first.
    Prevents miscalibrated probabilities from breaking the ensemble.
    """
    if weights is None:
        weights = [1.0 / len(preds_list)] * len(preds_list)
        
    ranked_sum = np.zeros(len(preds_list[0]))
    for pred, w in zip(preds_list, weights):
        # Normalize ranks between 0 and 1
        normalized_ranks = rankdata(pred) / len(pred)
        ranked_sum += normalized_ranks * w
        
    return ranked_sum

# Usage
ensemble_preds = rank_average_predictions(
    [lgb_test_preds, catboost_test_preds, xgb_test_preds],
    weights=[0.45, 0.35, 0.20]
)
```

### Technique 2: Out-of-Fold Stacking
Train a meta-classifier (like Logistic Regression or Ridge) using the Out-Of-Fold predictions of your base models as inputs:

```python
from sklearn.linear_model import LogisticRegression

# 1. Stack OOF predictions from Phase 2
X_meta_train = np.column_stack([oof_lgb, oof_catboost, oof_xgb])
X_meta_test = np.column_stack([test_lgb, test_catboost, test_xgb])

# 2. Train simple meta-model
meta_model = LogisticRegression(C=1.0)
meta_model.fit(X_meta_train, y_train)

# 3. Final ensemble prediction
final_stacked_preds = meta_model.predict_proba(X_meta_test)[:, 1]
```
This multi-layer architecture is why AutoGluon consistently tops tabular benchmarks!
