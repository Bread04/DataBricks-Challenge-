# 📖 Datathon & Data Science Glossary

<!-- markdownlint-disable MD013 -->

> 🟢 **In plain English:** Data science is filled with scary-sounding academic buzzwords. Here is what every single term actually means, explained using simple real-world analogies.

---

## 🏗️ The Data Basics

### Features (Independent Variables / Inputs)
- **The Fancy Word:** Features, covariates, attributes, predictor columns.
- **In Plain English:** The clues or questions on an exam. If you are predicting house prices, the features are square footage, number of bedrooms, and location.
- **In Code:** Usually called `X`.

### Target (Dependent Variable / Label / Ground Truth)
- **The Fancy Word:** Target, label, response variable, ground truth, $y$.
- **In Plain English:** The answer to the mystery that you are trying to guess. In a house price challenge, the target is the price. In a hospital challenge, the target is whether the patient gets sick (1 or 0).
- **In Code:** Usually called `y`.

### Tabular Data
- **In Plain English:** Good old-fashioned rows and columns, like a standard Excel spreadsheet or CSV file. Most real-world business and hackathon problems deal with tabular data.

### Parquet File (`.parquet`)
- **In Plain English:** A modern, super-compressed upgrade to CSV files. A 2GB CSV file shrinks to 200MB when saved as Parquet, and loads into Python 10x faster.

---

## 🧪 Training & Testing Concepts

### Training Set vs. Validation Set vs. Test Set
Think of learning data science like preparing for a high school math exam:
- **Training Set (Practice Homework):** The practice questions where you get both the questions and the answers so you can study.
- **Validation Set (Mock Exam):** A practice test you take the night before to see if you actually understand the concepts or if you need to study more.
- **Test Set (The Final Exam):** The actual questions given by the judges where you do **not** have the answers. You submit your guesses to be graded.

### Baseline Model
- **In Plain English:** The absolute simplest guess you can make before doing anything clever.
- **Example:** If 90% of customers don't churn, a baseline model that guesses "Nobody will churn" is 90% accurate! Your clever machine learning model is only useful if it beats this simple baseline.

### Overfitting (The "Memorizer" Trap)
- **In Plain English:** When a student memorizes the exact answers on the practice homework instead of learning the math formula. They score 100% on homework, but fail the final exam because the numbers changed slightly!
- **How to spot it:** Your model gets 98% accuracy on training data, but drops to 65% on validation data.

### Underfitting (The "Lazy" Trap)
- **In Plain English:** When a student didn't study enough at all and fails both the practice homework and the final exam.
- **How to spot it:** Accuracy is terrible on both training and test data.

### Cross-Validation (K-Fold CV)
- **In Plain English:** Instead of splitting your data once, you cut your data into 5 equal slices (folds). You train on 4 slices and test on the 5th. Then you repeat this 5 times so every single row gets tested once.
- **Why do it?** It gives you an honest, reliable score you can trust, preventing lucky or unlucky guesses.

### Data Leakage / Target Leakage (The "Accidental Cheating" Trap)
- **In Plain English:** When information from the future (or the answer key) accidentally sneaks into the questions your model is studying.
- **Real-World Example:** In a hospital challenge to predict which patients have pneumonia, the dataset included a column called `antibiotic_prescribed`. Because doctors only prescribe antibiotics *after* diagnosing pneumonia, the model had 99.9% accuracy by just looking at prescriptions! But in the real world, you need to predict pneumonia *before* doctors write prescriptions.
- **Golden Rule:** If your model has 99.9% accuracy on the first try, you almost certainly have target leakage. Find the column that gave away the answer!

---

## 📊 Evaluation Metrics: How You're Graded

### Accuracy
- **In Plain English:** What percentage of total guesses were correct?
- **The Trap:** If 99% of credit card transactions are legitimate and 1% are fraud, a dumb model that guesses "No fraud" is 99% accurate, but completely useless! Never rely solely on accuracy for rare events.

### Precision vs. Recall
Imagine a spam filter on your email:
- **Precision:** When the model flags an email as spam, how often is it *actually* spam? (High precision means your important emails don't end up in the junk folder).
- **Recall:** Out of all the spam emails that exist, how many did the model manage to catch? (High recall means no spam slips through into your inbox).

### F1-Score
- **In Plain English:** The balanced sweet spot between Precision and Recall. Great for grading models when one class is rare.

### ROC-AUC (Area Under the Curve)
- **In Plain English:** A score from 0.5 to 1.0 measuring how well the model separates good things from bad things.
  - `0.50` = Pure random guessing (like flipping a coin).
  - `0.70` = Decent baseline.
  - `0.85+` = Very strong competitive model.
  - `1.00` = Perfect separation (or target leakage!).

---

## 🤖 The Models & Tools

### Decision Tree
- **In Plain English:** A flowchart of yes/no questions. E.g.: *"Is income > $50k? If yes, is age > 30? If yes, approve loan."*

### Gradient Boosting (LightGBM, CatBoost, XGBoost)
- **In Plain English:** A team of hundreds of small decision trees working together. Tree #1 makes a guess. Tree #2 looks at the mistakes Tree #1 made and tries to fix them. Tree #3 fixes Tree #2's mistakes, and so on.
- **LightGBM:** The fastest runner in the group; trains in seconds on standard laptops.
- **CatBoost:** The specialist that handles messy text and categories without needing manual setup.

### AutoML (AutoGluon)
- **In Plain English:** An automated robot that tries dozens of different models, tunes their settings, and glues the best ones together into an ensemble while you eat dinner.

### SHAP (SHapley Additive exPlanations)
- **In Plain English:** Showing the receipts! Instead of the AI acting like a black box saying *"Denied"*, SHAP produces a chart showing: *"Denied because credit score was -25 points and late payments added -40 points, despite high income (+15 points)."* Judges love this.

### What-If Scenario Simulator
- **In Plain English:** An interactive screen with sliders that lets judges play with your model in real time (e.g. *"What happens if we increase shipping budget by $5,000?"*).

### Polars & DuckDB
- **In Plain English:** Ultra-fast, modern replacements for Pandas. They use all your computer's CPU cores and handle massive multi-gigabyte datasets without freezing or crashing your laptop.
