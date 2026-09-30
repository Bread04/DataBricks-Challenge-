"""Draw the DengueRadar architecture diagram for slide 3.

Run:  python pitch/architecture_diagram.py   ->  pitch/assets/architecture.png
Edit the STAGES list to change the wording; the layout follows automatically.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).resolve().parent / "assets" / "architecture.png"

INK, MUTED, LINE = "#1b1f23", "#5d6870", "#d9d6cf"
ORANGE, TINT, BAND = "#ff3621", "#fff1ee", "#f6f7f8"

# (heading, Databricks component, lines)
STAGES = [
    ("1  Sources", "data.gov.sg (open data)", [
        "NEA dengue clusters (daily)",
        "NEA weather: rain, temp,",
        "humidity (5-minute readings)",
        "MOH weekly cases 2012-2022",
        "URA planning-area boundaries",
        "Census 2020 (population)",
        "Cited archive 2015-20 (training)",
    ]),
    ("2  Ingest", "Lakeflow Jobs, incremental", [
        "Daily NEA cluster snapshots,",
        "live since 28 Sep 2026",
        "(the feed keeps no history)",
        "Weather: only new readings",
        "each run (planned, untested)",
        "Big 5-min files are",
        "pre-aggregated first",
    ]),
    ("3  Store + govern", "Delta Lake in Unity Catalog", [
        "Bronze: raw, as received",
        "Silver: cleaned, mapped to",
        "planning areas",
        "Gold: weekly area features,",
        "area risk, action rules",
        "Lineage + time travel",
    ]),
    ("4  Forecast", "MLflow + SHAP", [
        "2-week risk forecast per",
        "planning area (LightGBM)",
        "To be compared with baselines",
        "on unseen years (2020 replay)",
        "Top 3 drivers per area",
    ]),
    ("5  Act", "AI/BI map + App + Genie", [
        "Island view: planning areas",
        "Low / Medium / High",
        "Area view: why, and what",
        "to do, with timing",
        "Copy-ready post for the",
        "chats residents already use",
        "Genie: ask in plain English",
    ]),
]
USERS = "Residents (via their group chats)  ·  admins who post  ·  NEA (comparison view)"

W, H = 13.0, 5.4
fig = plt.figure(figsize=(W, H), dpi=200)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")

ax.text(0.35, H - 0.4, "DengueRadar on Databricks Free Edition", fontsize=15, fontweight="bold", color=INK, va="top")
ax.text(0.35, H - 0.82, "From reactive dashboards to a 2-week forecast with a plan of action. Tested on our Free Edition "
        "workspace on 28 Sep 2026: Unity Catalog, Delta, MLflow, AI/BI, Genie, Apps, scheduled jobs.",
        fontsize=9.5, color=MUTED, va="top")
ax.text(0.35, H - 1.06, "Not yet tested: streaming and Auto Loader for incremental weather loading (planned).",
        fontsize=9.5, color=MUTED, va="top")

# Databricks band behind stages 2-5
n = len(STAGES)
margin, gap = 0.35, 0.32
bw = (W - 2 * margin - gap * (n - 1)) / n
top, bh = H - 1.55, 2.85
band_x = margin + bw + gap - 0.14
ax.add_patch(FancyBboxPatch((band_x, top - bh - 0.3), W - margin - band_x + 0.14, bh + 0.52,
                            boxstyle="round,pad=0,rounding_size=0.12", fc=BAND, ec=LINE, lw=1))
ax.text(band_x + 0.12, top - bh - 0.2, "Databricks Free Edition (serverless)", fontsize=8, color=MUTED, va="center")

for i, (head, comp, lines) in enumerate(STAGES):
    x = margin + i * (bw + gap)
    fc = TINT if i else "#ffffff"
    ax.add_patch(FancyBboxPatch((x, top - bh), bw, bh, boxstyle="round,pad=0,rounding_size=0.1",
                                fc=fc, ec=ORANGE if i else LINE, lw=1.2))
    ax.text(x + 0.14, top - 0.2, head, fontsize=11, fontweight="bold", color=ORANGE, va="top")
    ax.text(x + 0.14, top - 0.55, comp, fontsize=8.6, fontweight="bold", color=INK, va="top")
    for j, line in enumerate(lines):
        ax.text(x + 0.14, top - 0.95 - j * 0.27, line, fontsize=8.2, color=INK, va="top")
    if i < n - 1:
        ax.add_patch(FancyArrowPatch((x + bw + 0.03, top - bh / 2), (x + bw + gap - 0.03, top - bh / 2),
                                     arrowstyle="-|>", mutation_scale=12, color=MUTED, lw=1.4))

# users under the Act box
x_last = margin + (n - 1) * (bw + gap)
ax.add_patch(FancyArrowPatch((x_last + bw / 2, top - bh - 0.32), (x_last + bw / 2, top - bh - 0.62),
                             arrowstyle="-|>", mutation_scale=10, color=MUTED, lw=1.2))
ax.text(W - margin, top - bh - 0.78, "Used by:  " + USERS, fontsize=8.6, color=INK, ha="right", va="top")
ax.text(margin, 0.2, "No personal data: outputs are planning areas and public places only.",
        fontsize=7.5, color=MUTED, va="bottom")

OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, facecolor="white")
print("saved", OUT)
