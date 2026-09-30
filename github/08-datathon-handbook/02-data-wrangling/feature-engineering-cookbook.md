# 🍳 The 10-Family Tabular Feature Engineering Cookbook

<!-- markdownlint-disable MD013 -->

> 🟢 **In plain English:** In competitive tabular data science, **90% of model performance gains come from feature engineering**, not from hyperparameter tuning. These 10 copy-paste recipes provide the highest-yield feature transformations using Polars and Pandas.

---

## 📋 The 10 High-Yield Feature Families

| Family | What It Does | Best For | Code Snippet |
| --- | --- | --- | --- |
| **1. Group Aggregations** | Computes mean/std/max of numbers grouped by a category | Customer spending vs. merchant average | `Recipe 1` |
| **2. Domain Ratios** | Divides two related quantities (e.g. debt / income) | Financial risk, efficiency metrics | `Recipe 2` |
| **3. Rolling Window Stats** | Moving averages and cumulative sums over time | Time-series, sensor data, transaction logs | `Recipe 3` |
| **4. Cyclical Time** | Converts hour/month into sine/cosine pairs | Preserving clock continuity (hour 23 to 0) | `Recipe 4` |
| **5. Frequency Encoding** | Replaces categories with their total count | High-cardinality IDs, postal codes | `Recipe 5` |
| **6. Interaction Terms** | Multiplies two features that amplify each other | Temperature × Duration, Price × Quantity | `Recipe 6` |
| **7. Out-of-Fold Target Encoding** | Replaces categories with target probability without leakage | High-cardinality merchant/doctor categories | `Recipe 7` |
| **8. Quantile Binning** | Converts heavily skewed distributions into balanced bins | Income, price spreads, extreme outliers | `Recipe 8` |
| **9. Lightweight Embeddings** | Converts unstructured text notes into 384 numbers | Support tickets, clinical comments, reviews | `Recipe 9` |
| **10. Geospatial Distance** | Calculates km distance between latitude/longitude points | Logistics, delivery times, store catchments | `Recipe 10` |

---

## 🧑‍🍳 The Recipes

### Recipe 1: Group Aggregations (Polars & Pandas)
Compare an individual event against its peer group (e.g. *"Is this transaction higher than this user's average?"*):

```python
# Polars (Lightning fast across all CPU cores)
import polars as pl

df = df.with_columns([
    # Mean and Std of amount grouped by user_id
    pl.col("amount").mean().over("user_id").alias("user_avg_amount"),
    pl.col("amount").std().over("user_id").alias("user_std_amount"),
]).with_columns([
    # Relative ratio: how much higher than normal is this transaction?
    (pl.col("amount") / (pl.col("user_avg_amount") + 1e-5)).alias("amount_vs_user_avg")
])
```

### Recipe 2: Domain Ratios & Relative Spreads
Tree models cannot do division easily. Help the model by computing domain ratios explicitly:

```python
import polars as pl

df = df.with_columns([
    # Ratio: Credit balance to credit limit
    (pl.col("balance") / (pl.col("credit_limit") + 1.0)).alias("utilization_rate"),
    # Ratio: Revenue per minute of duration
    (pl.col("revenue") / (pl.col("duration_seconds") / 60.0 + 1.0)).alias("revenue_per_minute"),
    # Spread: Maximum minus Minimum
    (pl.col("max_heart_rate") - pl.col("resting_heart_rate")).alias("heart_rate_reserve")
])
```

### Recipe 3: Rolling Window & Lag Statistics (Time-Series)
Capture momentum and recent behavioral shifts:

```python
import polars as pl

# Ensure data is sorted by time before calculating rolling windows
df = df.sort(["user_id", "timestamp"]).with_columns([
    # Previous transaction amount (Lag 1)
    pl.col("amount").shift(1).over("user_id").alias("prev_amount"),
    # Rolling 7-day average spend
    pl.col("amount").rolling_mean(window_size=7).over("user_id").alias("rolling_7d_avg_amount"),
    # Time delta since last event in hours
    (pl.col("timestamp") - pl.col("timestamp").shift(1).over("user_id")).dt.total_hours().alias("hours_since_last_event")
])
```

### Recipe 4: Cyclical Datetime Features
Ensure the model knows that 11:59 PM (23:59) and 12:01 AM (00:01) are 2 minutes apart, not 24 hours apart:

```python
import numpy as np
import polars as pl

df = df.with_columns([
    # Hour of day (0-23)
    (np.sin(2 * np.pi * pl.col("timestamp").dt.hour() / 24.0)).alias("hour_sin"),
    (np.cos(2 * np.pi * pl.col("timestamp").dt.hour() / 24.0)).alias("hour_cos"),
    # Day of week (0-6)
    (np.sin(2 * np.pi * pl.col("timestamp").dt.weekday() / 7.0)).alias("dow_sin"),
    (np.cos(2 * np.pi * pl.col("timestamp").dt.weekday() / 7.0)).alias("dow_cos"),
])
```

### Recipe 5: Frequency & Count Encoding
For high-cardinality categories (e.g. zip codes, device models) where One-Hot encoding would create thousands of sparse columns:

```python
import polars as pl

df = df.with_columns(
    # Count frequency of each zip code
    pl.col("zip_code").count().over("zip_code").alias("zip_code_frequency")
)
```

### Recipe 6: Interaction Terms & Polynomial Features
When two variables together create an amplified compound risk:

```python
import polars as pl

df = df.with_columns([
    # Compound risk: Age x Past Incidents
    (pl.col("age") * pl.col("past_incidents")).alias("age_incident_interaction"),
    # Non-linear congestion penalty
    (pl.col("container_queue_length") ** 2).alias("queue_length_squared")
])
```

### Recipe 7: Out-of-Fold Target Encoding (Leak-Free)
Encode categorical columns with target values without bleeding information across validation folds:

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold

def target_encode_cv(train_df, test_df, cat_col, target_col, n_splits=5, smoothing=10):
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    train_encoded = np.zeros(len(train_df))
    global_mean = train_df[target_col].mean()

    for train_idx, val_idx in kf.split(train_df):
        tr = train_df.iloc[train_idx]
        val = train_df.iloc[val_idx]
        stats = tr.groupby(cat_col)[target_col].agg(['count', 'mean'])
        smoothed = (stats['count'] * stats['mean'] + smoothing * global_mean) / (stats['count'] + smoothing)
        train_encoded[val_idx] = val[cat_col].map(smoothed).fillna(global_mean)

    full_stats = train_df.groupby(cat_col)[target_col].agg(['count', 'mean'])
    test_smoothed = (full_stats['count'] * full_stats['mean'] + smoothing * global_mean) / (full_stats['count'] + smoothing)
    test_encoded = test_df[cat_col].map(test_smoothed).fillna(global_mean).values

    return train_encoded, test_encoded
```

### Recipe 8: Quantile Binning for Skewed Features
Turn wild power-law distributions (e.g. wealth, transaction volume) into balanced percentile groups:

```python
import pandas as pd

# Create 5 equal-frequency quintiles (Q1, Q2, Q3, Q4, Q5)
df['revenue_quintile'] = pd.qcut(df['revenue'], q=5, labels=False, duplicates='drop')
```

### Recipe 9: Lightweight Text Embeddings (Sentence Transformers)
When your spreadsheet has a messy text column (customer remarks, triage notes):

```python
from sentence_transformers import SentenceTransformer
import pandas as pd

# Load tiny, fast 384-dimensional embedding model (runs in seconds on CPU)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings for text column
embeddings = model.encode(df['notes'].fillna("").tolist(), batch_size=64, show_progress_bar=False)

# Add top 4 principal components to tabular features
from sklearn.decomposition import PCA
pca = PCA(n_components=4)
text_features = pca.fit_transform(embeddings)

for i in range(4):
    df[f'text_pca_{i}'] = text_features[:, i]
```

### Recipe 10: Geospatial Haversine Distance (Kilometers)
Calculate straight-line distance between two latitude/longitude coordinate pairs:

```python
import numpy as np

def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0 # Earth's radius in kilometers
    phi1, phi2 = np.radians(lat1), np.radians(lat2)
    dphi = np.radians(lat2 - lat1)
    dlambda = np.radians(lon2 - lon1)
    
    a = np.sin(dphi / 2.0)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(dlambda / 2.0)**2
    c = 2.0 * np.arctan2(np.sqrt(a), np.sqrt(1.0 - a))
    return r * c

# Usage
df['distance_km'] = haversine_distance(df['pickup_lat'], df['pickup_lon'], df['drop_lat'], df['drop_lon'])
```
