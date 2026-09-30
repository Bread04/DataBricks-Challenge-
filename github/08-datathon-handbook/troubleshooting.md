# 🚨 The 2 AM Panic Button: Troubleshooting Guide

<!-- markdownlint-disable MD013 -->

> 🟢 **Take a deep breath.** Every single hackathon team runs into bugs, broken scripts, and unexpected crashes. This guide gives you instant, 60-second solutions to the most common emergencies.

---

## 🆘 Emergency 1: "My computer froze or crashed with `MemoryError`!"

### Why it happened:
You tried to load a 2GB+ CSV file into Pandas using `pd.read_csv()`. Pandas converts text into memory-heavy Python objects and uses 5x to 10x the file size in RAM, causing your laptop to freeze.

### The 60-Second Fix:
Switch to **Polars with lazy evaluation** or sample the file:

```python
# Fix A: Use Polars (Runs in Rust across all cores, zero memory blowup)
import polars as pl
df = pl.scan_csv("giant_file.csv").filter(pl.col("year") == 2024).collect()

# Fix B: Or read only the first 50,000 rows while prototyping
import pandas as pd
df_sample = pd.read_csv("giant_file.csv", nrows=50000)
```

---

## 🆘 Emergency 2: "My model got 99.9% accuracy on the first try!"

### Why it happened:
**You have Target Leakage.** You did not discover a Nobel prize-winning algorithm in 20 minutes; you accidentally included a column that gives away the answer key!

### The 60-Second Fix:
Check feature correlations or feature importances:
```python
# Look at the top correlated column with target
import pandas as pd
corrs = df.corr()['target'].abs().sort_values(ascending=False)
print(corrs.head(10))
```
- **If any feature has a correlation > 0.95**, inspect it immediately!
- Look for columns like `status_timestamp`, `account_closed_date`, `resolution_code`, or `diagnosis_notes` that only exist *after* the event happened. Drop that column and re-train.

---

## 🆘 Emergency 3: "`ModuleNotFoundError: No module named 'xyz'`"

### Why it happened:
A required Python library is not installed in your current Python environment or terminal.

### The 60-Second Fix:
Open your terminal and install it with `pip` or `uv`:
```bash
# Using standard pip
pip install lightgbm catboost shap streamlit polars duckdb

# Or if you have uv installed (much faster)
uv pip install lightgbm catboost shap streamlit polars duckdb
```

If it still says not found in Jupyter or VS Code, verify your kernel in the top-right corner is pointing to the same Python environment!

---

## 🆘 Emergency 4: "Streamlit won't start or says `Port 8501 is already in use`!"

### Why it happened:
A previous Streamlit process is still running quietly in the background and holding onto port 8501.

### The 60-Second Fix:
Tell Streamlit to run on a different port:
```bash
streamlit run streamlit-app-template.py --server.port 8502
```
Or kill all existing Streamlit processes:
- **Windows (PowerShell):** `Get-Process python | Stop-Process`
- **Mac/Linux:** `pkill -f streamlit`

---

## 🆘 Emergency 5: "The venue Wi-Fi is completely down and pitching starts in 30 minutes!"

### Why it happened:
500 people connected to the same conference router simultaneously and the venue router crashed. This happens at almost every in-person hackathon!

### The 60-Second Fix:
1. **Never rely on cloud-hosted URLs during the pitch.**
2. Run your Streamlit dashboard **100% locally on your laptop**:
   ```bash
   streamlit run streamlit-app-template.py
   ```
   Open `http://localhost:8501` in your browser. It doesn't need internet!
3. **The Ultimate Safety Net:** Use Windows Game Bar (`Win + Alt + R`) or QuickTime on Mac to record a 30-second video of you clicking through the app right now. If your laptop battery dies or HDMI refuses to connect, play the video from your phone or USB drive!

---

## 🆘 Emergency 6: "Our team is arguing and we can't agree on a model!"

### Why it happened:
Fatigue and stress. One person wants to try a complex deep neural net, another wants a random forest, and time is running out.

### The 60-Second Fix:
1. **The Hackathon Rule of Thumb:** Use **LightGBM**. It trains in 5 seconds on CPU, beats deep learning on 90% of tabular datasets, and is easy to interpret.
2. Put the disagreement to a vote based on **local cross-validation score**, not theoretical opinions.
3. Remember: Judges grade **25% on model**, but **75% on problem understanding, explainability, and the live interactive demo**. Shift team energy to the Streamlit app and slide deck!
