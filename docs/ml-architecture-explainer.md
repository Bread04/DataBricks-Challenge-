# How DengueRadar's ML architecture works (beginner explainer)

For teammates new to data science. Status as of 30 Sep 2026. Design source: `docs/model-definitions.md`. Numbers in the worked example are **illustrative**, not model output.

## The idea in one paragraph

Think of a weather forecast. Meteorologists look at past patterns and say "70% chance of rain tomorrow." DengueRadar does the same for dengue: it looks at past cluster counts, weather and geography, then says "this planning area is more likely than usual to see clusters grow in the next 2 weeks." Then it turns that into a post someone can send to a group chat.

## The pipeline

```
 SOURCES ──▶ INGEST ──▶ STORE ──▶ FEATURES ──▶ TRAIN + TEST ──▶ PREDICT ──▶ EXPLAIN ──▶ DELIVER
 data.gov.sg  daily     Delta     numbers      compare to      weekly     top 3       posts,
 NEA, MOH     jobs      tables    the model    simple          batch      drivers     map, ranking
                                  can read     baselines       forecast
```

### 1. Sources: where the data comes from
- **NEA dengue clusters:** areas where cases are grouped together. The live feed only shows *today*, with no history.
- **Weather:** rainfall, temperature and humidity.
- **MOH weekly cases, planning-area boundaries, Census 2020.**
- **A cited archive of old clusters (2015 to 2020)** for training.

### 2. Ingest: collecting it automatically
A **Lakeflow Job** is a scheduled task, like a phone alarm that runs code. Ours runs daily at 21:00 and saves a copy of the day's clusters, which builds a history the feed does not keep.
- **Incremental ingestion** means loading only what is new, not everything again.

### 3. Store: keeping it organised
- **Delta Lake** is a storage format that behaves like a reliable spreadsheet: no half-saved rows, and you can look at old versions (**time travel**).
- **Bronze, silver, gold** are three tidiness levels. Bronze is raw, silver is cleaned and matched to planning areas, gold is ready to use (features, forecasts).
- **Unity Catalog** is the filing system that tracks every table, who owns it and where its data came from (**lineage**).

### 4. Features: turning data into numbers the model can use
A **feature** is one measurable clue, such as "rainfall 2 weeks ago" or "cases in neighbouring areas". Making them is **feature engineering**.
- A **lag** means looking back in time, for example rain from 3 weeks ago.
- Our four hypotheses (H1 to H4) each become a group of features: weather lag, neighbour spillover, recurrence, green space.
- The table has one row per **planning area per week**.

### 5. Train and test: teaching the model, then checking it honestly
- **The target** is what we predict: cluster cases over the next 2 weeks (**regression**, a number) and whether an area will be **Rising** (**classification**, yes or no).
- **LightGBM** is our model. It builds many small **decision trees** (chains of yes/no questions) that each fix the mistakes of the last. This is called **gradient boosting**.
- **Baselines** are simple guesses the model must beat. "Same as the last 4 weeks" is **persistence**. If a fancy model cannot beat it, it is not worth using.
- **Overfitting** means the model memorised the past instead of learning patterns.
- **Time-ordered validation** trains on earlier years and tests on later ones, never shuffling. A shuffled test would let the model peek at the future. That peeking is **data leakage**.
- **GroupKFold** hides some planning areas during training to check the model works in places it has not seen.
- **Prospective test:** later, we score our forecasts against live snapshots as they arrive (the training archive ends Nov 2020, so this checks today's conditions).

### 6. Predict: batch, not live
**Batch inference** means we run the model once a week for all areas and save the results in a gold table. It is cheaper and steadier on Free Edition than answering live requests.
- The model gives a **probability** (for example 0.6). **Calibration** means checking that "60%" really happens about 60% of the time.
- A **threshold** decides the cut-off for Low, Medium and High.
- A **cost matrix** says missing a real rise is worse than an unnecessary reminder (we assumed 5 times), so we set the threshold to favour catching rises.

### 7. Explain and deliver
- **SHAP** shows how much each feature pushed one area's prediction up or down. We take the top 3 as "why it is rising", in plain words.
- These map to actions in the **action library** (`docs/action-library.md`) and become the post and card.
- **Ranking:** a budget slider **K** ("teams available") highlights the top K areas. **Capture rate at K** measures what share of real new cases fell inside them.
- **AI/BI dashboard** draws maps and charts. **Genie** answers plain-English questions on our tables. A **Databricks App** is a small web page we host.

## Where MLflow fits
**MLflow** is the lab notebook for models. Each training attempt is a **run** in an **experiment**, and it records settings and scores. The best model goes into the **model registry**, a labelled shelf with versions, stored in Unity Catalog.

## A worked week (illustrative)
1. Monday: the model reads last week's features for one planning area.
2. It outputs "Rising probability 0.62, expected 8 cases".
3. That is above the High threshold, so the level is High.
4. SHAP says the top drivers are heavy rain 2 to 4 weeks ago and cases nearby.
5. Those map to two actions.
6. The card shows "higher than usual", and the admin kit produces a WhatsApp-ready post.

## What is built and what is planned
- **Built:** the daily snapshot job (hardened 30 Sep), Free Edition tests of Unity Catalog, Delta, MLflow, AI/BI, Genie and Apps, and a monthly lag chart.
- **Planned, not started:** the feature table, the baselines, LightGBM, the backtest, the ranking, the card and the post. Incremental weather loading is untested.

## Jargon cheat sheet

| Term | Plain meaning |
|---|---|
| Cluster | A group of nearby dengue cases NEA tracks |
| Planning area | One of Singapore's 55 URA districts, our forecast unit |
| GeoJSON | A file format for map shapes |
| Epi week | A standard public-health week number |
| Serverless | Databricks manages the computers, you just run code |
| MERGE | Add new rows and update existing ones without duplicates |
| Structured Streaming / Auto Loader | Ways to pick up new data as it arrives |
| Precision / recall | Of my flags, how many were right / of the real rises, how many I caught |
| PR-AUC | One score summarising precision against recall, good when rises are rare |
| MAE | Average size of the miss, in cases |
| Poisson / logistic model | Simple readable models used as a cross-check |
| Alert load | Share of areas flagged High; capped at 15% so alerts stay meaningful |
| Hit rate | Share of new or growing clusters that were in areas we rated High |
| Out-of-fold (OOF) | Predictions made on data the model did not train on |
