# Databricks notebook source
# MAGIC %md
# MAGIC # DengueRadar 01 - Daily NEA dengue cluster snapshot
# MAGIC
# MAGIC NEA's open dengue-cluster feed only shows **today's** clusters; yesterday's are overwritten.
# MAGIC This notebook saves a copy each day into a Delta table, so DengueRadar builds its own cluster history.
# MAGIC
# MAGIC * **Needs:** `00_free_edition_check` egress tests passing (data.gov.sg reachable).
# MAGIC * **Source:** data.gov.sg "Dengue Clusters (GEOJSON)", `d_dbfabf16158d1b0e1c420627c0819168` (NEA)
# MAGIC * **Writes:** `workspace.dengueradar.bronze_cluster_snapshots`, one row per cluster per day
# MAGIC * **Also writes:** `workspace.dengueradar.bronze_snapshot_runs`, **one row per day** with status `ok`, `empty` or `failed`.
# MAGIC   A day with zero clusters is `empty` (a real quiet day), a day the job broke is `failed`, and a day with no row at all means the job never ran.
# MAGIC   Count "days of live history" from this table, not from the snapshots table.
# MAGIC * **Safe to re-run:** a second run on the same day updates that day's rows instead of duplicating them
# MAGIC * **Fails loudly, on purpose:** a renamed or missing feed field, a negative or missing case size, or clusters with a total of 0 cases stops the job (a renamed field must never turn into silent zeros)
# MAGIC * **Schedule:** Schedule, Add schedule, every day 21:00, timezone Asia/Singapore, Serverless. **Also turn on the job's failure email notification** (Job, Edit notifications).

# COMMAND ----------

dbutils.widgets.text("catalog", "workspace")
dbutils.widgets.text("schema", "dengueradar")
CATALOG = dbutils.widgets.get("catalog")
SCHEMA = dbutils.widgets.get("schema")
TABLE = f"{CATALOG}.{SCHEMA}.bronze_cluster_snapshots"
RUNS_TABLE = f"{CATALOG}.{SCHEMA}.bronze_snapshot_runs"

# COMMAND ----------

import json
import time
from datetime import datetime, timedelta, timezone

import requests

DATASET_ID = "d_dbfabf16158d1b0e1c420627c0819168"
SGT = timezone(timedelta(hours=8))
CORE_FIELDS = {"OBJECTID", "LOCALITY", "CASE_SIZE"}  # if any of these disappear, the feed schema changed


def fetch_clusters_geojson(dataset_id=DATASET_ID, attempts=5):
    """Ask data.gov.sg for a download link, then download the GeoJSON. Retries because the API rate-limits."""
    for attempt in range(attempts):
        try:
            meta = requests.get(
                f"https://api-open.data.gov.sg/v1/public/api/datasets/{dataset_id}/poll-download", timeout=60
            ).json()
            return requests.get(meta["data"]["url"], timeout=120).json()
        except Exception as exc:
            print(f"attempt {attempt + 1} failed: {type(exc).__name__}: {exc}")
            time.sleep(5 * (attempt + 1))
    raise RuntimeError("data.gov.sg download failed after retries")


def to_rows(geojson, fetched_at):
    """Flatten GeoJSON features into plain rows (one per cluster). A missing case size stays None so the
    quality check can see it (it must never be turned into 0)."""
    rows = []
    for f in geojson.get("features", []):
        p = f.get("properties", {})
        updated = p.get("FMEL_UPD_D")
        case_size = p.get("CASE_SIZE")
        rows.append({
            "snapshot_date": fetched_at.astimezone(SGT).date(),
            "fetched_at": fetched_at,
            "cluster_id": str(p.get("OBJECTID")),
            "locality": p.get("LOCALITY"),
            "case_size": int(case_size) if case_size is not None else None,
            "homes_breeding": p.get("HOMES"),
            "public_places_breeding": p.get("PUBLIC_PLACES"),
            "construction_breeding": p.get("CONSTRUCTION_SITES"),
            "source_updated_at": datetime.strptime(updated, "%Y%m%d%H%M%S").replace(tzinfo=SGT) if updated else None,
            "geometry_geojson": json.dumps(f.get("geometry")),
        })
    return rows


def check_quality(rows, geojson):
    """Stop on clearly broken data; warn on merely unusual data."""
    features = geojson.get("features", [])
    if features:
        missing = CORE_FIELDS - set(features[0].get("properties", {}))
        if missing:
            raise ValueError(f"feed schema changed, missing fields: {sorted(missing)}")
    bad = [r["locality"] for r in rows
           if r["case_size"] is None or r["case_size"] < 0 or r["geometry_geojson"] in ("", "null")]
    if bad:
        raise ValueError(f"bad rows (missing or negative cases, or missing geometry): {bad}")
    if rows and sum(r["case_size"] for r in rows) == 0:
        raise ValueError("clusters present but total cases are 0: a feed field was probably renamed")
    if not rows:
        print("WARNING: feed returned 0 clusters - possible in a quiet period, recorded as an 'empty' day")

# COMMAND ----------

from pyspark.sql.types import DateType, IntegerType, StringType, StructField, StructType, TimestampType

schema = StructType([
    StructField("snapshot_date", DateType(), False),
    StructField("fetched_at", TimestampType(), False),
    StructField("cluster_id", StringType(), False),
    StructField("locality", StringType(), True),
    StructField("case_size", IntegerType(), False),
    StructField("homes_breeding", StringType(), True),
    StructField("public_places_breeding", StringType(), True),
    StructField("construction_breeding", StringType(), True),
    StructField("source_updated_at", TimestampType(), True),
    StructField("geometry_geojson", StringType(), True),
])


def ensure_tables():
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOG}.{SCHEMA}")
    spark.sql(f"""
      CREATE TABLE IF NOT EXISTS {TABLE} (
        snapshot_date DATE, fetched_at TIMESTAMP, cluster_id STRING, locality STRING, case_size INT,
        homes_breeding STRING, public_places_breeding STRING, construction_breeding STRING,
        source_updated_at TIMESTAMP, geometry_geojson STRING)
      COMMENT 'Daily snapshots of NEA dengue clusters from data.gov.sg (d_dbfabf16158d1b0e1c420627c0819168). One row per cluster per day.'
    """)
    spark.sql(f"""
      CREATE TABLE IF NOT EXISTS {RUNS_TABLE} (
        snapshot_date DATE, fetched_at TIMESTAMP, n_clusters INT, total_cases INT, status STRING, message STRING)
      COMMENT 'One row per day the snapshot job ran: ok, empty (feed had 0 clusters) or failed. Count days of history from here.'
    """)


def log_run(snapshot_date, fetched_at, n_clusters, total_cases, status, message=""):
    """Record today's run. A re-run the same day replaces that day's row (for example failed, then ok)."""
    ensure_tables()
    spark.createDataFrame(
        [(snapshot_date, fetched_at, n_clusters, total_cases, status, message[:300])],
        "snapshot_date DATE, fetched_at TIMESTAMP, n_clusters INT, total_cases INT, status STRING, message STRING",
    ).createOrReplaceTempView("run_row")
    spark.sql(f"""
      MERGE INTO {RUNS_TABLE} t USING run_row s ON t.snapshot_date = s.snapshot_date
      WHEN MATCHED THEN UPDATE SET *
      WHEN NOT MATCHED THEN INSERT *
    """)


def write_snapshot(rows):
    ensure_tables()
    if rows:
        spark.createDataFrame(rows, schema).createOrReplaceTempView("todays_clusters")
        # MERGE = insert new rows, update rows already saved today, so re-running never duplicates.
        spark.sql(f"""
          MERGE INTO {TABLE} t
          USING todays_clusters s
          ON t.snapshot_date = s.snapshot_date AND t.cluster_id = s.cluster_id
          WHEN MATCHED THEN UPDATE SET *
          WHEN NOT MATCHED THEN INSERT *
        """)

# COMMAND ----------

fetched_at = datetime.now(timezone.utc)
today = fetched_at.astimezone(SGT).date()
try:
    geojson = fetch_clusters_geojson()
    rows = to_rows(geojson, fetched_at)
    check_quality(rows, geojson)
    write_snapshot(rows)
    total_cases = sum(r["case_size"] for r in rows)
    log_run(today, fetched_at, len(rows), total_cases, "ok" if rows else "empty")
    print(f"{len(rows)} clusters, {total_cases} cases, snapshot {today}")
except Exception as exc:
    log_run(today, fetched_at, 0, 0, "failed", f"{type(exc).__name__}: {exc}")
    raise  # the job run still shows as failed, so the failure email fires

# COMMAND ----------

# MAGIC %md ### History built so far

# COMMAND ----------

display(spark.sql(f"""
  SELECT snapshot_date, status, n_clusters, total_cases, message
  FROM {RUNS_TABLE} ORDER BY snapshot_date DESC
"""))

# COMMAND ----------

# Days of live history = days the job ran successfully (ok or empty). Quote this number on the slide.
display(spark.sql(f"""
  SELECT COUNT(*) AS days_of_history, MIN(snapshot_date) AS first_day, MAX(snapshot_date) AS last_day
  FROM {RUNS_TABLE} WHERE status IN ('ok', 'empty')
"""))
