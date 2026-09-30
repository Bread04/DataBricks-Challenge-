# 🧹 Real-World Data Wrangling Recipes

<!-- markdownlint-disable MD013 -->

> Real-world datathon data is dirty, large, and filled with missing timestamps, skewed distributions, and high-cardinality categories. These recipes give you high-performance, leak-free snippets to process multi-gigabyte data in seconds.

---

## 1. Instant 10-Minute Exploratory Data Analysis (EDA)

Never spend hours manually charting 50 columns. Run automated profilers in cell 1:

### Recipe 1A: Comprehensive 1-Line HTML Profile (`ydata-profiling`)
```python
import polars as pl
from ydata_profiling import ProfileReport

# Load sample or full dataset
df = pl.read_csv("train.csv").to_pandas()

# Generate full interactive report
profile = ProfileReport(df, title="Datathon EDA Report", minimal=True)
profile.to_file("eda_report.html")
print("EDA report generated at eda_report.html!")
```

### Recipe 1B: Train vs. Test Distribution Drift Check (`sweetviz`)
Detect distribution shifts before modeling (e.g. if test set has different demographics or missing categories):
```python
import sweetviz as sv
import pandas as pd

train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")

# Compare Train vs Test distributions
report = sv.compare([train_df, "Train"], [test_df, "Test"], target_feat="target")
report.show_html("train_vs_test_drift.html")
```

---

## 2. High-Performance Tabular Ingestion with Polars

Polars executes in Rust across all CPU cores. Use lazy evaluation (`scan_csv`) to eliminate RAM exhaustion:

### Recipe 2A: Out-of-Core Lazy Filtering & Feature Creation
```python
import polars as pl

# 1. Define lazy computation graph (no memory used yet)
lazy_df = (
    pl.scan_csv("large_events.csv")
    .filter(pl.col("status") == "COMPLETED")
    .with_columns([
        # Parse ISO timestamps
        pl.col("timestamp").str.to_datetime("%Y-%m-%d %H:%M:%S").alias("dt"),
        # Create domain ratio
        (pl.col("revenue") / (pl.col("duration_seconds") + 1.0)).alias("revenue_per_sec"),
    ])
    .with_columns([
        # Extract cyclical temporal features
        pl.col("dt").dt.hour().alias("hour"),
        pl.col("dt").dt.weekday().alias("day_of_week"),
    ])
)

# 2. Collect only what you need
df_clean = lazy_df.collect()
print(f"Processed shape: {df_clean.shape}")
```

---

## 3. High-Speed In-Process SQL Analytics with DuckDB

When complex window functions or multi-table joins are needed, DuckDB runs SQL directly on Polars DataFrames or raw Parquet files with **zero copy**:

### Recipe 3A: Complex Aggregations via SQL over Polars
```python
import duckdb
import polars as pl

df_events = pl.read_parquet("events.parquet")

# DuckDB automatically sees `df_events` in Python scope!
query = """
SELECT 
    user_id,
    COUNT(*) AS total_transactions,
    AVG(revenue) AS avg_spend,
    SUM(revenue) AS total_spend,
    MAX(revenue) - MIN(revenue) AS spend_spread,
    AVG(revenue) OVER(
        PARTITION BY country 
        ORDER BY timestamp 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_country_spend
FROM df_events
GROUP BY user_id, country, timestamp, revenue
"""

# Query outputs directly back to Polars
df_aggregated = duckdb.sql(query).pl()
print(df_aggregated.head())
```

### Recipe 3B: Querying Multi-File Parquet Archives
```python
import duckdb

# Query hundreds of partitioned Parquet files directly from disk without loading to RAM
summary = duckdb.sql("""
    SELECT 
        date_trunc('day', timestamp) AS day,
        category,
        count(*) AS total_events,
        sum(amount) AS total_val
    FROM 'data/partitioned/*.parquet'
    GROUP BY 1, 2
    ORDER BY 1 DESC
""").df()
```

---

## 4. Triage Patterns for Dirty Real-World Data

### Recipe 4A: Leak-Free Out-of-Fold Target Encoding
When you have high-cardinality categories (e.g. zip codes, doctor IDs, merchant IDs), standard target encoding leaks labels. Use K-Fold out-of-fold encoding:

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold

def out_of_fold_target_encode(train_df, test_df, cat_col, target_col, n_splits=5, smoothing=10):
    """
    Computes smoothed target encoding inside a CV loop to prevent data leakage.
    """
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    train_encoded = np.zeros(len(train_df))
    global_mean = train_df[target_col].mean()
    
    # Out-of-fold encoding for training data
    for train_idx, val_idx in kf.split(train_df):
        tr = train_df.iloc[train_idx]
        val = train_df.iloc[val_idx]
        
        # Smoothed mean: (count * mean + smoothing * global) / (count + smoothing)
        stats = tr.groupby(cat_col)[target_col].agg(['count', 'mean'])
        smoothed = (stats['count'] * stats['mean'] + smoothing * global_mean) / (stats['count'] + smoothing)
        
        train_encoded[val_idx] = val[cat_col].map(smoothed).fillna(global_mean)
        
    # Full dataset encoding for test data
    full_stats = train_df.groupby(cat_col)[target_col].agg(['count', 'mean'])
    test_smoothed = (full_stats['count'] * full_stats['mean'] + smoothing * global_mean) / (full_stats['count'] + smoothing)
    test_encoded = test_df[cat_col].map(test_smoothed).fillna(global_mean).values
    
    return train_encoded, test_encoded
```

### Recipe 4B: Cyclical Datetime Features
Machine learning models struggle to understand that hour 23 and hour 0 are 1 hour apart. Convert timestamps to cyclical sine/cosine pairs:

```python
import numpy as np
import pandas as pd

def add_cyclical_time_features(df, datetime_col):
    dt = pd.to_datetime(df[datetime_col])
    
    # Hours (0-23)
    df['hour_sin'] = np.sin(2 * np.pi * dt.dt.hour / 24.0)
    df['hour_cos'] = np.cos(2 * np.pi * dt.dt.hour / 24.0)
    
    # Day of week (0-6)
    df['dow_sin'] = np.sin(2 * np.pi * dt.dt.dayofweek / 7.0)
    df['dow_cos'] = np.cos(2 * np.pi * dt.dt.dayofweek / 7.0)
    
    # Month (1-12)
    df['month_sin'] = np.sin(2 * np.pi * (dt.dt.month - 1) / 12.0)
    df['month_cos'] = np.cos(2 * np.pi * (dt.dt.month - 1) / 12.0)
    
    return df
```
