# Databricks notebook source
# MAGIC %md
# MAGIC # DengueRadar 00 - Free Edition check (run once, about 10 minutes)
# MAGIC
# MAGIC Answers the questions Round 1 depends on:
# MAGIC 1. **Egress:** can a Free Edition notebook reach data.gov.sg? If not, slide 3 must not promise a daily Databricks archive.
# MAGIC 2. **Features:** which parts of our architecture actually work here (Unity Catalog, spatial SQL, MLflow + model registry)?
# MAGIC 3. **Incremental ingestion (new, 28 Sep):** do Structured Streaming and Auto Loader run here? The brief asks for streaming or incremental ingestion.
# MAGIC
# MAGIC **How to run:** Connect to **Serverless**, then **Run all**. Every test catches its own error, so one failure never stops the rest.
# MAGIC The last cell prints a yes/no table. Screenshot it and paste it into the team doc.
# MAGIC
# MAGIC If the egress tests fail: verify your account with LinkedIn (Settings, then Account), then run the notebook again.

# COMMAND ----------

# MAGIC %pip install shapely --quiet

# COMMAND ----------

import traceback

results = []  # (area, test, passed, detail)


def check(area, test, fn):
    """Run one test, record pass/fail with a short reason, never raise."""
    try:
        detail = fn()
        results.append((area, test, "YES", str(detail)[:120]))
    except Exception as exc:
        results.append((area, test, "NO", f"{type(exc).__name__}: {str(exc)[:110]}"))
        traceback.print_exc(limit=1)

# COMMAND ----------

# MAGIC %md ## 1. Egress: can we reach data.gov.sg?

# COMMAND ----------

import requests

CLUSTERS = "d_dbfabf16158d1b0e1c420627c0819168"


def pypi_control():
    return requests.get("https://pypi.org/simple/requests/", timeout=20).status_code


def poll_download():
    meta = requests.get(f"https://api-open.data.gov.sg/v1/public/api/datasets/{CLUSTERS}/poll-download", timeout=30).json()
    url = meta["data"]["url"]
    geo = requests.get(url, timeout=60).json()  # the file itself lives on an AWS S3 link
    return f"{len(geo['features'])} dengue clusters downloaded"


def datastore_search():
    r = requests.get("https://data.gov.sg/api/action/datastore_search",
                     params={"resource_id": "d_ca168b2cb763640d72c4600a68f9909e", "limit": 1}, timeout=30).json()
    return f"{r['result']['total']} rows in weekly disease bulletin"


def realtime_rain():
    d = requests.get("https://api-open.data.gov.sg/v2/real-time/api/rainfall", timeout=30).json()["data"]
    return f"{len(d['stations'])} rain stations, reading {d['readings'][0]['timestamp']}"


check("Egress", "pypi.org (control: should work)", pypi_control)
check("Egress", "data.gov.sg dataset download (clusters GeoJSON)", poll_download)
check("Egress", "data.gov.sg datastore API (weekly cases)", datastore_search)
check("Egress", "data.gov.sg real-time API (rainfall)", realtime_rain)

# COMMAND ----------

# MAGIC %md ## 2. Unity Catalog + Delta: can we create our own schema and table?

# COMMAND ----------

CATALOG, SCHEMA = "workspace", "dengueradar"


def uc_schema_table():
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOG}.{SCHEMA}")
    spark.sql(f"CREATE OR REPLACE TABLE {CATALOG}.{SCHEMA}._feature_check (id INT, note STRING)")
    spark.sql(f"INSERT INTO {CATALOG}.{SCHEMA}._feature_check VALUES (1, 'hello')")
    n = spark.table(f"{CATALOG}.{SCHEMA}._feature_check").count()
    return f"{CATALOG}.{SCHEMA} writable, {n} row"


def delta_history():
    v = spark.sql(f"DESCRIBE HISTORY {CATALOG}.{SCHEMA}._feature_check").count()
    return f"{v} table versions (time travel works)"


check("Unity Catalog", "create schema + Delta table", uc_schema_table)
check("Unity Catalog", "Delta history / time travel", delta_history)

# COMMAND ----------

# MAGIC %md ## 3. Spatial: can we do "is this within 200 m?" in SQL, or do we need shapely?

# COMMAND ----------


def spatial_sql():
    # Two points in Taman Jurong about 150 m apart; answer should be true.
    row = spark.sql("""
      SELECT st_dwithin(st_transform(st_setsrid(st_point(103.7200, 1.3380), 4326), 3414),
                        st_transform(st_setsrid(st_point(103.7213, 1.3383), 4326), 3414), 200) AS within_200m
    """).first()
    return f"st_dwithin -> {row.within_200m}"


def h3_sql():
    return spark.sql("SELECT h3_longlatash3(103.72, 1.338, 9) AS cell").first().cell


def shapely_fallback():
    from shapely.geometry import Point
    return f"shapely works, distance = {Point(0, 0).distance(Point(3, 4))}"


check("Spatial", "Databricks spatial SQL (st_dwithin)", spatial_sql)
check("Spatial", "H3 functions", h3_sql)
check("Spatial", "shapely via %pip (fallback)", shapely_fallback)

# COMMAND ----------

# MAGIC %md ## 4. MLflow: can we log experiments and register a model in Unity Catalog?

# COMMAND ----------

import mlflow
import numpy as np
from sklearn.linear_model import Ridge


def mlflow_tracking():
    X, y = np.arange(20).reshape(-1, 1), np.arange(20) * 2.0
    with mlflow.start_run(run_name="feature_check") as run:
        model = Ridge().fit(X, y)
        mlflow.log_metric("mae", float(np.abs(model.predict(X) - y).mean()))
        mlflow.sklearn.log_model(model, "model", input_example=X[:2])
    return run.info.run_id


def mlflow_registry():
    mlflow.set_registry_uri("databricks-uc")
    run_id = [r for r in results if r[1] == "log a run + model"][0][3]
    mv = mlflow.register_model(f"runs:/{run_id}/model", f"{CATALOG}.{SCHEMA}.feature_check_model")
    return f"registered version {mv.version}"


check("MLflow", "log a run + model", mlflow_tracking)
check("MLflow", "register model in Unity Catalog", mlflow_registry)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Incremental ingestion: can we stream or load only new data? (added 28 Sep after the brief refocus)
# MAGIC
# MAGIC The brief asks for "streaming or incremental ingestion from live APIs". Three ways to show it, from most to least impressive.
# MAGIC If Auto Loader or streaming fails, the fallback is a scheduled job that loads only rows newer than the last one saved (MERGE), the same pattern `01_cluster_snapshot_job` uses.

# COMMAND ----------

import json
import time

VOLUME = "landing"


def structured_streaming_delta():
    # Built-in test stream -> Delta, processing what is available and stopping (works on serverless).
    tbl = f"{CATALOG}.{SCHEMA}._stream_check"
    spark.sql(f"DROP TABLE IF EXISTS {tbl}")
    ckpt = f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}/_ckpt_rate"
    spark.sql(f"CREATE VOLUME IF NOT EXISTS {CATALOG}.{SCHEMA}.{VOLUME}")
    q = (spark.readStream.format("rate").option("rowsPerSecond", 5).load()
         .writeStream.option("checkpointLocation", ckpt).trigger(availableNow=True).toTable(tbl))
    q.awaitTermination(60)
    return f"{spark.table(tbl).count()} rows streamed into Delta"


def auto_loader():
    # Drop two small JSON files into a volume, load them with Auto Loader, then add a third and load only that.
    base = f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}/rain"
    dbutils.fs.rm(base, True)
    dbutils.fs.rm(f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}/_ckpt_al", True)
    tbl = f"{CATALOG}.{SCHEMA}._autoloader_check"
    spark.sql(f"DROP TABLE IF EXISTS {tbl}")

    def drop(name, n):
        dbutils.fs.put(f"{base}/{name}.json", "\n".join(json.dumps({"station": f"S{i}", "mm": i}) for i in range(n)), True)

    def load():
        (spark.readStream.format("cloudFiles").option("cloudFiles.format", "json")
         .option("cloudFiles.schemaLocation", f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}/_schema_al")
         .load(base).writeStream.option("checkpointLocation", f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}/_ckpt_al")
         .trigger(availableNow=True).toTable(tbl).awaitTermination(90))

    drop("a", 3); drop("b", 2); load()
    first = spark.table(tbl).count()
    drop("c", 4); load()
    second = spark.table(tbl).count()
    return f"first load {first} rows, after new file {second} rows (expected 5 then 9)"


def merge_watermark():
    # Fallback pattern: keep only rows newer than what we already have.
    tbl = f"{CATALOG}.{SCHEMA}._merge_check"
    spark.sql(f"CREATE OR REPLACE TABLE {tbl} (ts INT, v STRING)")
    spark.sql(f"INSERT INTO {tbl} VALUES (1,'a'),(2,'b')")
    spark.sql(f"""MERGE INTO {tbl} t USING (SELECT * FROM VALUES (2,'b'),(3,'c') AS s(ts, v)) s
                  ON t.ts = s.ts WHEN NOT MATCHED THEN INSERT *""")
    return f"{spark.table(tbl).count()} rows, no duplicate (expected 3)"


check("Incremental ingestion", "Structured Streaming -> Delta (availableNow)", structured_streaming_delta)
check("Incremental ingestion", "Auto Loader (cloudFiles) picks up only new files", auto_loader)
check("Incremental ingestion", "MERGE watermark fallback", merge_watermark)

# COMMAND ----------

# MAGIC %md ## Results - screenshot this and paste into the team doc

# COMMAND ----------

display(spark.createDataFrame(results, "area STRING, test STRING, passed STRING, detail STRING"))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Check these by hand (2 minutes each), then add them to the table in the team doc
# MAGIC
# MAGIC | Feature | How to check | Works if... |
# MAGIC |---|---|---|
# MAGIC | **Jobs (scheduling)** | This notebook: **Schedule**, then **Add schedule** | You can pick a daily time and save it (delete it afterwards) |
# MAGIC | **AI/BI Dashboard + map** | Sidebar **Dashboards**, then **Create dashboard**; add a visual on `workspace.dengueradar._feature_check` | A visual appears; check whether a **Map** visual type is offered |
# MAGIC | **Genie** | Sidebar **Genie**, then **New**, and add the same table | You can ask "how many rows?" and get an answer |
# MAGIC | **Databricks Apps** | Sidebar **Compute**, then the **Apps** tab, then **Create app**; pick the Streamlit template | The app starts and opens (stop it after, since there are only 3 app slots) |
# MAGIC
# MAGIC **Clean up:** `DROP TABLE workspace.dengueradar._feature_check` and delete the `feature_check_model` model when done.
