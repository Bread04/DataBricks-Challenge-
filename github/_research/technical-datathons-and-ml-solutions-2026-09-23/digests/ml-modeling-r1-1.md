# Dimension 3 Digest: Rapid ML Baselines to Competitive Models

- Topic: Machine Learning Modeling Under Datathon Clocks
- Researcher: ml-modeling-r1-1
- Date: 2026-09-23

## Key Findings

### 1. The Modeling Speed Hierarchy: LightGBM vs CatBoost vs AutoGluon
- **Phase 1: Minute 0–30 Baseline**:
  - Run a simple heuristic or Scikit-learn Ridge / Logistic Regression to verify pipeline plumbing and submit a benchmark row.
- **Phase 2: The Gradient Boosting Workhorses**:
  - **LightGBM** (`lightgbm`): The reigning speed champion for tabular data. Leaf-wise splitting with GOSS (Gradient-based One-Side Sampling) trains in seconds on CPU. Best for rapid feature iteration cycles.
  - **CatBoost** (`catboost`): The gold standard when datasets contain rich text or categorical features (e.g. merchant names, medical codes, postal districts). CatBoost computes ordered target statistics on the fly, eliminating target leakage from manual label encoding.
  - **XGBoost** (`xgboost`): Strong, but typically slower to train on CPU compared to LightGBM.
- **Phase 3: Automated Ensembling with AutoGluon**:
  - **AutoGluon** (`autogluon.tabular`): The most effective AutoML framework in competitive data science. Using `TabularPredictor(label=...).fit(train_data, time_limit=900, presets='best_quality')`, it multi-layer stacks LightGBM, CatBoost, XGBoost, FastAI neural nets, and Random Forests. Often beats manual tuning within a 15-minute budget.
  - **FLAML** (`flaml`): Ultra-fast, lightweight alternative to Optuna when compute resources are constrained.

### 2. Unstructured Data & LLM Augmentation
- When real-life datasets include messy unstructured text (customer complaints, incident reports, clinical notes):
  - Fast embeddings: `sentence-transformers` (e.g. `all-MiniLM-L6-v2` or `bge-small-en-v1.5`) generated in 60 seconds on CPU.
  - Zero-shot classification: DeBERTa-v3 or modern quantized LLMs (via Ollama or Gemini/OpenAI API) to create structured categorical columns from free-text notes.

### 3. Avoiding the 3 Deadly Datathon Traps
1. **Target Leakage**: Preprocessing (scaling, imputing, target encoding) before cross-validation splitting. Rule: Always fit scalers/encoders inside the CV loop.
2. **Temporal Leakage**: In time-series or sequential data, random K-Fold leaks future rows into past predictions. Rule: Use `TimeSeriesSplit` or rolling-window evaluation.
3. **Threshold Neglect**: For imbalanced classification (e.g., fraud rate = 0.5%), a 0.5 probability threshold is useless. Use Precision-Recall curves or tune the decision threshold to maximize F1/Cost-Utility.

## Sources
- [1] AWS AutoGluon: AutoGluon-Tabular Documentation & Kaggle Benchmark papers
- [2] LightGBM / CatBoost Official Documentation & Comparative Benchmarks
- [3] Scikit-learn Model Evaluation & Cross-Validation Guide
