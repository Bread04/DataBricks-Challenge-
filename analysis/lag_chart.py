"""Lag chart: does weather line up with dengue cases some weeks/months later?

Monthly version (works now):
    python analysis/lag_chart.py
Weekly version (once Jingyi's weekly rainfall CSV exists, columns: week_start, rain_mm):
    python analysis/lag_chart.py --weekly-rain path/to/weekly_rain.csv

How to read it: each line is one weather measure. A point at lag L is the correlation between
"how unusual the weather was" and "how unusual dengue cases were" L months later
(Spearman, -1 to +1; 0 = no relationship). "Unusual" = compared with a typical year for that
month, so the normal dengue season doesn't fake a relationship.
"""
import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "analysis" / "data"
OUT = ROOT / "pitch" / "assets"
DATASETS = {"weekly_idb.csv": "d_ca168b2cb763640d72c4600a68f9909e",       # MOH weekly disease bulletin
            "climate_monthly.csv": "d_1744ca68dc7ed37221b17c441042405e"}  # monthly climate

INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"
SERIES = {"tmax": ("Max temperature", "#2a78d6"),
          "rh": ("Relative humidity", "#eb6834"),
          "rain": ("Rainfall", "#1baf7a")}


def download(name, dataset_id):
    path = DATA / name
    if path.exists():
        return path
    DATA.mkdir(parents=True, exist_ok=True)
    for attempt in range(5):
        try:
            meta = requests.get(f"https://api-open.data.gov.sg/v1/public/api/datasets/{dataset_id}/poll-download", timeout=60).json()
            path.write_bytes(requests.get(meta["data"]["url"], timeout=300).content)
            return path
        except Exception:
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"could not download {name}")


def weekly_cases():
    w = pd.read_csv(DATA / "weekly_idb.csv")
    d = (w[w.disease.isin(["Dengue Fever", "Dengue Haemorrhagic Fever"])]
         .groupby("epi_week")["no._of_cases"].sum().sort_index())
    # Epi weeks include 2014-W53 and 2020-W53, which ISO date parsing rejects, so number weeks in order.
    return pd.Series(d.values, index=pd.Timestamp("2012-01-02") + pd.to_timedelta(7 * np.arange(len(d)), unit="D"))


def anomaly(series, period):
    """Value minus the typical value for that month (or week) of the year."""
    return series - series.groupby(period(series.index)).transform("mean")


def monthly_lags(max_lag=4):
    cases = np.log1p(weekly_cases().resample("MS").sum())
    c = pd.read_csv(DATA / "climate_monthly.csv").set_index("DataSeries").T
    c.index = pd.to_datetime(c.index, format="%Y%b")
    c = c.sort_index().apply(pd.to_numeric, errors="coerce")
    c = c[["Air Temperature Means Daily Maximum", "24 Hours Mean Relative Humidity", "Total Rainfall"]]
    c.columns = ["tmax", "rh", "rain"]
    month = lambda idx: idx.month
    y = anomaly(cases, month)
    table = {v: [y.corr(anomaly(c[v], month).shift(lag).reindex(y.index), method="spearman")
                 for lag in range(max_lag + 1)] for v in c.columns}
    return pd.DataFrame(table, index=range(max_lag + 1)), "months", len(y)


def weekly_lags(rain_csv, max_lag=8):
    cases = np.log1p(weekly_cases())
    r = pd.read_csv(rain_csv, parse_dates=["week_start"]).set_index("week_start")["rain_mm"]
    week = lambda idx: idx.isocalendar().week.values
    y = anomaly(cases, week)
    ra = anomaly(r, week)
    y = y[y.index.isin(ra.index)]
    table = {"rain": [y.corr(ra.shift(lag).reindex(y.index), method="spearman") for lag in range(max_lag + 1)]}
    return pd.DataFrame(table, index=range(max_lag + 1)), "weeks", len(y)


def plot(table, unit, n):
    fig, ax = plt.subplots(figsize=(6.4, 3.4), dpi=200)
    ax.axhline(0, color=MUTED, lw=1)
    for key in table.columns:
        label, colour = SERIES[key]
        ax.plot(table.index, table[key], color=colour, lw=2, marker="o", ms=4, label=label)
        ax.annotate(f"{label} {table[key].iloc[-1]:+.2f}", (table.index[-1], table[key].iloc[-1]),
                    xytext=(6, 0), textcoords="offset points", va="center", fontsize=7.5, color=INK)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color(GRID)
    ax.grid(axis="y", color=GRID, lw=0.8)
    ax.tick_params(colors=MUTED, labelsize=8)
    ax.set_xticks(table.index)
    ax.set_xlim(table.index[0] - 0.2, table.index[-1] + 1.6)
    ax.set_xlabel(f"Weather this many {unit} before the cases", color=MUTED, fontsize=8)
    ax.set_ylabel("Correlation with dengue cases", color=MUTED, fontsize=8)
    ax.set_title("Warm months come before more dengue; rain alone barely lines up",
                 loc="left", fontsize=9.5, color=INK)
    ax.legend(frameon=False, fontsize=7.5, loc="upper left", labelcolor=MUTED)
    fig.text(0.01, 0.01, f"Singapore 2012-2022, {n} {unit}. Unusual weather vs unusual cases for that time of year (Spearman).\n"
             "Sources: MOH Weekly Infectious Disease Bulletin, MSS monthly climate (data.gov.sg).",
             fontsize=6, color=MUTED)
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"lag_chart_{unit}.png"
    fig.savefig(out, facecolor="white")
    plt.close(fig)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--weekly-rain", help="CSV with columns week_start, rain_mm (national weekly total)")
    args = parser.parse_args()
    for name, dataset_id in DATASETS.items():
        download(name, dataset_id)
    table, unit, n = weekly_lags(args.weekly_rain) if args.weekly_rain else monthly_lags()
    print(table.round(2).to_string())
    print("saved", plot(table, unit, n))


if __name__ == "__main__":
    main()
