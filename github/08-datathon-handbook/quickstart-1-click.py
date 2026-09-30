"""
🎉 1-Click Datathon Quickstart (Beginner-Friendly)
=================================================
A guided script that loads data, trains a machine learning model,
scores accuracy, exports explainability artifacts, and offers to launch
your interactive Streamlit demo immediately!

Run:
    python quickstart-1-click.py
"""

import os
import sys
import time
import subprocess
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score
import lightgbm as lgb
import joblib

def print_banner():
    print("""
===================================================================
🚀 WELCOME TO YOUR FIRST DATATHON QUICKSTART!
===================================================================
This script will take you from raw data to a working machine learning
model and an interactive web dashboard in under 30 seconds.
-------------------------------------------------------------------
""")

def step_1_load_data(csv_path=None):
    print("📁 [Step 1 of 5] Loading Data...")
    time.sleep(0.5)
    
    if csv_path and os.path.exists(csv_path):
        print(f"  ✓ Loading your dataset from '{csv_path}'...")
        df = pd.read_csv(csv_path)
    else:
        print("  ✓ No CSV specified — generating a realistic sample dataset (5,000 rows)...")
        X, y = make_classification(
            n_samples=5000,
            n_features=8,
            n_informative=6,
            weights=[0.8, 0.2],
            random_state=42
        )
        feature_names = [
            "Risk_Index", "Utilization_Rate", "Activity_Velocity",
            "Tenure_Months", "Commitment_Ratio", "Past_Incidents",
            "Metric_Spread", "Subject_Age"
        ]
        df = pd.DataFrame(X, columns=feature_names)
        df["target"] = y

    print(f"  ✓ Dataset successfully loaded! Size: {len(df):,} rows × {len(df.columns)} columns.")
    return df

def step_2_prepare_data(df):
    print("\n🧪 [Step 2 of 5] Splitting Data into Training & Test Sets...")
    time.sleep(0.5)
    
    target_col = "target" if "target" in df.columns else df.columns[-1]
    feature_cols = [c for c in df.columns if c != target_col]
    
    X = df[feature_cols]
    y = df[target_col]
    
    # 80% study homework (train), 20% practice exam (test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"  ✓ Training on {len(X_train):,} rows | Testing on {len(X_test):,} unseen rows.")
    return X_train, X_test, y_train, y_test, feature_cols

def step_3_train_model(X_train, y_train, X_test, y_test):
    print("\n🤖 [Step 3 of 5] Training LightGBM Machine Learning Model...")
    time.sleep(0.5)
    
    # LightGBM trains hundreds of small trees working together
    model = lgb.LGBMClassifier(
        n_estimators=100,
        learning_rate=0.08,
        num_leaves=31,
        random_state=42,
        verbose=-1
    )
    
    start_time = time.time()
    model.fit(X_train, y_train)
    elapsed = time.time() - start_time
    print(f"  ✓ Model trained in {elapsed:.2f} seconds across your computer's CPU cores!")
    return model

def step_4_evaluate(model, X_test, y_test):
    print("\n📊 [Step 4 of 5] Evaluating Model Performance...")
    time.sleep(0.5)
    
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    
    acc = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob)
    f1 = f1_score(y_test, y_pred)
    
    print("-------------------------------------------------------------------")
    print(f"  🎯 Test Accuracy : {acc * 100:.1f}% (Correct guesses out of 100)")
    print(f"  ⭐ ROC-AUC Score : {auc:.3f} (Separation quality: 0.5=Coin flip, 1.0=Perfect)")
    print(f"  📈 F1-Score      : {f1:.3f} (Balance between Precision & Recall)")
    print("-------------------------------------------------------------------")
    print("  💡 Tip for judges: Explain that your score comes from UNSEEN test data,")
    print("     proving that your model generalizes to real-world cases!")

def step_5_export_and_launch(model, X_test):
    print("\n💾 [Step 5 of 5] Saving Artifacts for the Interactive Web Demo...")
    artifacts_dir = os.path.join(os.path.dirname(__file__), "04-solutions-and-ui", "artifacts")
    os.makedirs(artifacts_dir, exist_ok=True)
    
    model_file = os.path.join(artifacts_dir, "best_model.pkl")
    joblib.dump(model, model_file)
    print(f"  ✓ Saved trained model to '{model_file}'.")
    
    app_file = os.path.join(os.path.dirname(__file__), "04-solutions-and-ui", "streamlit-app-template.py")
    
    print("\n" + "=" * 65)
    print("🎉 SUCCESS! You have a working, production-grade machine learning model.")
    print("=" * 65)
    print(f"\nTo launch your interactive decision dashboard for judges, run:")
    print(f"  streamlit run {app_file}\n")
    
    # Optional auto-launch prompt
    try:
        launch = input("👉 Would you like to launch the interactive dashboard right now? (y/n): ").strip().lower()
        if launch in ["y", "yes"]:
            print("\n🚀 Launching Streamlit web dashboard in your browser...")
            subprocess.run(["streamlit", "run", app_file])
    except KeyboardInterrupt:
        print("\nExiting. Good luck at your datathon!")

def main():
    print_banner()
    df = step_1_load_data()
    X_train, X_test, y_train, y_test, feature_cols = step_2_prepare_data(df)
    model = step_3_train_model(X_train, y_train, X_test, y_test)
    step_4_evaluate(model, X_test, y_test)
    step_5_export_and_launch(model, X_test)

if __name__ == "__main__":
    main()
