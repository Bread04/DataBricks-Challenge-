# 🧼 Handling Dirty Real-World Data: The Practical Triage Guide

<!-- markdownlint-disable MD013 -->

> 🟢 **In plain English:** In textbook data science courses, datasets are clean and tidy. In a real datathon, datasets have missing values, bizarre timestamps, 98% class imbalance, and extreme outliers. This guide gives you the battle-tested rules to clean data without destroying predictive signals.

---

## 🧩 1. Missing Data: Stop Blindly Imputing Medians!

Beginners often run `df.fillna(df.median())` on all columns. **This is often a mistake.** In real life, *why* data is missing is frequently more predictive than the value itself!

### The Missingness Rule of Thumb:
- **MCAR (Missing Completely at Random):** A sensor battery died. Median or mean imputation is fine.
- **MNAR (Missing Not at Random):** A doctor did *not* order a troponin lab test because the patient showed *no signs of a heart attack*. Here, missingness indicates low risk! If you replace missing values with the median, you falsely make healthy patients look sick!

### The Winning Triage Pattern: The Indicator + Median Pair
Always add a binary flag column before imputing:
```python
import polars as pl

# 1. Create a binary flag telling the model: "This was originally missing"
df = df.with_columns(
    pl.col("lab_test_result").is_null().cast(pl.Int8).alias("lab_test_was_missing")
)

# 2. Impute with median
median_val = df["lab_test_result"].median()
df = df.with_columns(
    pl.col("lab_test_result").fill_null(median_val)
)
```
Now, tree models can split on `lab_test_was_missing == 1` while still having numeric values for calculations!

---

## ⚖️ 2. Severe Class Imbalance: Why SMOTE Fails on Tabular Data

In fraud detection, rare disease diagnosis, or equipment failure, the target is heavily imbalanced (e.g. 1% positive, 99% negative).

### The Beginner Mistake: SMOTE (Synthetic Minority Over-sampling)
Beginners try using SMOTE to generate fake synthetic rows. In tabular data with mixed categories and non-linear relationships, SMOTE often creates anatomically or financially impossible rows (e.g. a 4-year-old child with a 30-year mortgage), degrading test set performance.

### The Winning Approach: Tree Weights + Threshold Moving
Do **not** resample the data. Keep the real-world distribution and use these two techniques:

#### Step A: Use Class Weights in LightGBM / CatBoost
Tell the algorithm that making a mistake on the rare positive class is 10x or 20x more expensive:
```python
import lightgbm as lgb

# Calculate imbalance ratio: (negatives / positives)
neg_count = (y == 0).sum()
pos_count = (y == 1).sum()
imbalance_ratio = neg_count / pos_count

model = lgb.LGBMClassifier(
    scale_pos_weight=imbalance_ratio, # Forces tree splits to prioritize the minority class!
    n_estimators=300
)
```

#### Step B: Threshold Optimization (Never Default to 0.5!)
If fraud happens 2% of the time, a default cutoff of 50% probability will predict 0 fraud cases! Sweep thresholds from 0.05 to 0.50 to maximize your F1-score or business ROI:
```python
from sklearn.metrics import precision_recall_curve
import numpy as np

precisions, recalls, thresholds = precision_recall_curve(y_true, y_probs)
f1_scores = 2 * (precisions * recalls) / (precisions + recalls + 1e-8)
best_threshold = thresholds[np.argmax(f1_scores)]

print(f"Optimal decision cutoff: {best_threshold:.3f}")
# In production / demo, classify as positive if prob >= best_threshold!
```

---

## 📈 3. Extreme Outliers: Clip, Don't Delete!

In datathons, you almost **never delete rows**. Every row in the test set must be predicted! If you delete outliers during training, your model will crash when it encounters them in testing.

### The Winning Pattern: Winsorization (Percentile Clipping)
Cap extreme values at the 1st and 99th percentiles:
```python
import polars as pl

# Compute 1st and 99th percentiles
p01 = df["transaction_amount"].quantile(0.01)
p99 = df["transaction_amount"].quantile(0.99)

# Clip values between percentiles
df = df.with_columns(
    pl.col("transaction_amount").clip(p01, p99).alias("transaction_amount_clipped")
)
```

---

## 🏷️ 4. Categorical Features: The 3-Way Decision Rule

How should you encode categories like `country`, `merchant_type`, or `department`?

```text
How many unique values in this column?
    ├── 2 to 5 values (e.g. Yes/No, Gender, Low/Med/High):
    │   └── One-Hot Encoding (pd.get_dummies / pl.col().to_dummies)
    │
    ├── 6 to 50 values (e.g. US States, Car Brands):
    │   └── Native CatBoost / LightGBM Categorical (Pass directly as category dtype!)
    │
    └── 50+ values (e.g. Zip codes, Doctor IDs, Merchant Names):
        └── Out-of-Fold Target Encoding OR Frequency Encoding (See Cookbook Recipe 5 & 7)
```

---

## ⏰ 5. Dirty Timestamps: The Triage Checklist

Real-world datasets often have timestamps recorded across multiple formats:
1. **Always force parsing with UTC:** Avoid timezone shifts by standardizing on UTC:
   ```python
   import pandas as pd
   df['timestamp_clean'] = pd.to_datetime(df['raw_timestamp'], utc=True, errors='coerce')
   ```
2. **Flag corrupted dates:** Create an `is_corrupted_date` boolean column for rows where timestamps failed to parse.
3. **Check for Future Data Leakage:** Ensure test set events occurred *after* train set events. If timestamps are present, never use standard random K-Fold—use `TimeSeriesSplit`!
