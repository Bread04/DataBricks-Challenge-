# 🛡️ The Definitive Cross-Validation & Leakage Prevention Guide

<!-- markdownlint-disable MD013 -->

> 🟢 **In plain English:** In competitive datathons, **trusting your local cross-validation is the single most important technical habit**. Teams that rely blindly on the public test leaderboard almost always suffer severe leaderboard shakeups on the final private test set. This guide shows you how to pick the right CV scheme and log leak-free Out-Of-Fold (OOF) predictions.

---

## 🧭 The 4 Cross-Validation Schemes: Which One to Use?

Never use standard random `KFold(shuffle=True)` on real-world datasets! Choose using this decision tree:

```text
Do multiple rows belong to the same entity (patient, customer, vehicle, hospital)?
    ├── YES ──► Use GroupKFold (All rows for a patient must stay in ONE fold!)
    │
    └── NO ──► Is your data ordered in time (sales by day, sensor logs, stock prices)?
                ├── YES ──► Use TimeSeriesSplit (Train strictly on the past, test on the future!)
                │
                └── NO ──► Use StratifiedKFold (Preserves the exact % of positive labels in every fold)
```

---

## 🛠️ The 3 Winning CV Implementations

### Scheme 1: Stratified K-Fold (Standard Classification)
Use when rows are independent, but the positive class is rare (e.g. 5% churn, 2% fraud):

```python
from sklearn.model_selection import StratifiedKFold
import numpy as np

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
oof_predictions = np.zeros(len(X))

for fold, (train_idx, val_idx) in enumerate(skf.split(X, y)):
    X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
    X_val, y_val = X.iloc[val_idx], y.iloc[val_idx]
    
    # Fit model strictly on fold training data
    model.fit(X_train, y_train)
    
    # Predict on unseen validation fold
    oof_predictions[val_idx] = model.predict_proba(X_val)[:, 1]
```

### Scheme 2: Group K-Fold (Preventing Entity Leakage)
**Crucial for Healthcare, Fleet Management & Social Networks:** If Patient #402 has 5 hospital visits in the dataset, placing 3 visits in training and 2 visits in validation will make your model artificially look like a genius because it memorized Patient #402's baseline biology!

```python
from sklearn.model_selection import GroupKFold
import numpy as np

gkf = GroupKFold(n_splits=5)
groups = df["patient_id"] # or user_id, device_id

for fold, (train_idx, val_idx) in enumerate(gkf.split(X, y, groups=groups)):
    X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
    X_val, y_val = X.iloc[val_idx], y.iloc[val_idx]
    
    model.fit(X_train, y_train)
    oof_predictions[val_idx] = model.predict_proba(X_val)[:, 1]
```

### Scheme 3: Time-Series Split (Preventing Future Leakage)
In time-series data, random shuffling trains on tomorrow to predict yesterday. Use expanding-window evaluation:

```python
from sklearn.model_selection import TimeSeriesSplit

# Sort chronologically first!
df = df.sort_values("timestamp")

tscv = TimeSeriesSplit(n_splits=5)

for fold, (train_idx, val_idx) in enumerate(tscv.split(X)):
    # Training set only contains events chronologically prior to validation set
    X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
    X_val, y_val = X.iloc[val_idx], y.iloc[val_idx]
    
    model.fit(X_train, y_train)
```

---

## 🏆 What is "Out-Of-Fold" (OOF) and Why Does It Win Prizes?

When you run 5-fold cross-validation, every row in your training set was in the validation slice exactly **once**. When you assemble all those predictions together into an array, you get **Out-Of-Fold (OOF) Predictions**.

### Why OOF Predictions are Superpowers:
1. **Unbiased Performance Assessment:** You can compute ROC-AUC, F1-score, and calibration curves across the *entire* dataset without a single leaked data point.
2. **Threshold Tuning:** You find your optimal classification cutoff on OOF predictions, confident that it will generalize to the judges' test set.
3. **Ensemble Stacking:** OOF predictions from LightGBM, CatBoost, and XGBoost serve as the meta-features for training higher-level stacked ensembles!

---

## 🚨 The 5-Second Data Leakage Test

How do you know if you made a fatal data leakage mistake? Ask these 3 questions:

1. **Did you run `.fit_transform()` on the whole dataframe before splitting into folds?**
   - *If YES:* You have leakage! Standard scalers, mean imputers, and target encoders must be fit **inside** each fold loop.
2. **Is your validation score unexpectedly 0.998?**
   - *If YES:* Check feature correlations immediately. You left an ID, a post-event status code, or the target column in your features.
3. **Does your local CV score wildly disagree with the public leaderboard?**
   - *If YES:* Check if the test set distribution has temporal shift or group clustering that your local CV scheme failed to replicate.
