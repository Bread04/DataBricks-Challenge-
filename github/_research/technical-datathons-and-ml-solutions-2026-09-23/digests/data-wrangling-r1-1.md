# Dimension 2 Digest: Real-World Data Sourcing, Ingestion & High-Speed Wrangling

- Topic: Real-World Data Sourcing, Ingestion & High-Speed Wrangling
- Researcher: data-wrangling-r1-1
- Date: 2026-09-23

## Key Findings

### 1. High-Performance Tabular Ingestion: Polars + DuckDB (The 2026 Gold Standard)
- **The Problem**: Real-world hackathon datasets are often 500MB to 10GB with millions of rows. Traditional Pandas crashes memory, executes single-threaded, and causes 10-minute wait times during rapid prototyping.
- **The Solution**: 
  - **Polars** (`polars`): Rust-backed, multi-threaded columnar DataFrame library. `pl.scan_csv()` and `pl.scan_parquet()` build lazy execution graphs, streaming data with zero memory blow-up.
  - **DuckDB** (`duckdb`): In-process SQL OLAP engine. Seamless zero-copy memory transfer with Polars via Apache Arrow (`duckdb.sql("SELECT ... FROM df_polars").pl()`).
  - **Speedup**: 10x-50x faster than Pandas on joins, aggregations, and window functions on a typical laptop CPU.

### 2. Fast EDA & Profiling Under 15 Minutes
- Rather than manually running `.describe()` on 80 columns:
  - **ydata-profiling** (`ydata-profiling`): Generates comprehensive HTML data reports (distributions, missing values, correlations, cardinality) in 1 line.
  - **Sweetviz** (`sweetviz`): Generates target-oriented comparison reports (comparing Train vs Test distributions to instantly detect distribution shift).
  - **Marimo** (`marimo`): Reactive Python notebooks stored as pure `.py` scripts. Prevents out-of-order execution bugs and git merge conflicts common in team `.ipynb` files.

### 3. Open Real-World Data Sourcing Portals
- **Civic & Public Data**: Data.gov, Data.gov.sg (LTA, NEA, SingStat for local events), Eurostat, NYC OpenData.
- **Science, Health & Climate**: Hugging Face Datasets, PhysioNet, NASA Earthdata, NOAA, World Bank Open Data.
- **Commercial & Kaggle**: Kaggle Datasets (100k+ curated tabular/image sets), AWS Registry of Open Data, Google Cloud Public Datasets.

### 4. Triaging Dirty Real-World Data
- **Timestamp normalization**: Always parse UTC, extract cyclical features (`hour_sin`, `hour_cos`, `day_of_week`, `is_weekend`).
- **High cardinality categoricals**: Target encoding with cross-validation fold smoothing (prevents target leakage).
- **Outliers**: Don't blindly drop outliers in real-world data (they often represent the critical fraud or failure events). Clip with 1st/99th percentiles or use tree models robust to monotonic transforms.

## Sources
- [1] Polars Official Documentation & Performance Benchmarks (2026)
- [2] DuckDB Documentation: In-Process Analytical SQL & Arrow Interop (2026)
- [3] YData-profiling & Sweetviz Documentation
- [4] Marimo: Reactive Notebooks for Python Data Science
