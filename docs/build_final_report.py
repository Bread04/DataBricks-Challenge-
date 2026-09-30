# Regenerates docs/DengueRadar-final-report.pdf. Run: python docs/build_final_report.py
# Needs reportlab, matplotlib (for the DejaVu fonts) and Pillow. The report text is written inline below; edit it and re-run.
import os
import matplotlib
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
                                TableStyle, Image, PageBreak, KeepTogether, NextPageTemplate, CondPageBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "DengueRadar-final-report.pdf")

fd = os.path.join(matplotlib.get_data_path(), "fonts", "ttf")
pdfmetrics.registerFont(TTFont("DV", os.path.join(fd, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DV-B", os.path.join(fd, "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("DV-I", os.path.join(fd, "DejaVuSans-Oblique.ttf")))
pdfmetrics.registerFont(TTFont("DV-BI", os.path.join(fd, "DejaVuSans-BoldOblique.ttf")))
addMapping("DV", 0, 0, "DV"); addMapping("DV", 1, 0, "DV-B")
addMapping("DV", 0, 1, "DV-I"); addMapping("DV", 1, 1, "DV-BI")

NAVY = colors.HexColor("#12262E")
RED = colors.HexColor("#E8311A")
GREY = colors.HexColor("#5B6770")
LIGHT = colors.HexColor("#F3F5F6")
PALE_RED = colors.HexColor("#FDEEEC")
PALE_GREEN = colors.HexColor("#EAF5EE")
PALE_AMBER = colors.HexColor("#FFF6E0")
RULE = colors.HexColor("#D5DADD")

body = ParagraphStyle("body", fontName="DV", fontSize=8.6, leading=12.4, textColor=NAVY, spaceAfter=4.5)
small = ParagraphStyle("small", parent=body, fontSize=7.4, leading=10, textColor=GREY)
cell = ParagraphStyle("cell", parent=body, fontSize=7.5, leading=10, spaceAfter=0)
cellb = ParagraphStyle("cellb", parent=cell, fontName="DV-B")
cellh = ParagraphStyle("cellh", parent=cell, fontName="DV-B", textColor=colors.white)
h1 = ParagraphStyle("h1", fontName="DV-B", fontSize=16, leading=20, textColor=NAVY, spaceBefore=2, spaceAfter=6)
h2 = ParagraphStyle("h2", fontName="DV-B", fontSize=11, leading=14, textColor=RED, spaceBefore=9, spaceAfter=3, keepWithNext=1)
h3 = ParagraphStyle("h3", fontName="DV-B", fontSize=9, leading=12, textColor=NAVY, spaceBefore=6, spaceAfter=2, keepWithNext=1)
bul = ParagraphStyle("bul", parent=body, leftIndent=11, bulletIndent=2, spaceAfter=2.2)
cap = ParagraphStyle("cap", parent=small, spaceBefore=2, spaceAfter=7)

W = A4[0] - 36 * mm  # usable width in points
story = []


def P(t, s=body): story.append(Paragraph(t, s))
def H1(t): story.append(PageBreak()); story.append(Paragraph(t, h1)); story.append(rule())
def H2(t): story.append(Paragraph(t, h2))
def H3(t): story.append(Paragraph(t, h3))
def B(items):
    for i in items: story.append(Paragraph(i, bul, bulletText="\u2022"))
def SP(n=4): story.append(Spacer(1, n))


def rule():
    t = Table([[""]], colWidths=[W], rowHeights=[2])
    t.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, 0), 1.2, RED)]))
    return t


def T(rows, widths, header=True, zebra=True, fs=None):
    data = []
    for ri, r in enumerate(rows):
        row = []
        for c in r:
            if isinstance(c, str):
                st = cellh if (header and ri == 0) else cell
                row.append(Paragraph(c, st))
            else:
                row.append(c)
        data.append(row)
    tot = sum(widths)
    cw = [w * W / tot for w in widths]
    t = Table(data, colWidths=cw, repeatRows=1 if header else 0)
    st = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 4),
          ("RIGHTPADDING", (0, 0), (-1, -1), 4), ("TOPPADDING", (0, 0), (-1, -1), 3),
          ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("LINEBELOW", (0, 0), (-1, -1), 0.3, RULE)]
    if header:
        st += [("BACKGROUND", (0, 0), (-1, 0), NAVY)]
    if zebra:
        for i in range(1 if header else 0, len(data)):
            if (i % 2) == 0:
                st.append(("BACKGROUND", (0, i), (-1, i), LIGHT))
    t.setStyle(TableStyle(st))
    story.append(t)
    story.append(Spacer(1, 6))


def BOX(text, bg=PALE_RED, edge=RED):
    t = Table([[Paragraph(text, body)]], colWidths=[W])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("LINEBEFORE", (0, 0), (0, -1), 3, edge),
                           ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                           ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    story.append(t); story.append(Spacer(1, 6))


def IMG(path, width_frac, caption):
    from PIL import Image as PI
    w, h = PI.open(path).size
    tw = W * width_frac
    story.append(KeepTogether([Image(path, width=tw, height=tw * h / w), Paragraph(caption, cap)]))


# ---------------------------------------------------------------- page decorations
def on_page(c, d):
    c.saveState()
    c.setFont("DV", 7); c.setFillColor(GREY)
    c.drawString(18 * mm, 10 * mm, "DengueRadar: project record and Round 1 package  |  status as of 30 Sep 2026")
    c.drawRightString(A4[0] - 18 * mm, 10 * mm, "Page %d" % d.page)
    c.setStrokeColor(RED); c.setLineWidth(2.5); c.line(0, A4[1] - 3, A4[0], A4[1] - 3)
    c.restoreState()


def on_cover(c, d):
    c.saveState()
    c.setFillColor(NAVY); c.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)
    c.setFillColor(RED); c.rect(0, A4[1] - 14, A4[0], 14, stroke=0, fill=1)
    c.restoreState()


doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=17 * mm,
                      title="DengueRadar: project record and Round 1 package", author="Team DengueRadar",
                      subject="DAISI Challenge Singapore 2026, problem A2")
fr = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
doc.addPageTemplates([PageTemplate(id="cover", frames=[fr], onPage=on_cover),
                      PageTemplate(id="main", frames=[fr], onPage=on_page)])

# ---------------------------------------------------------------- cover
cw = ParagraphStyle("cw", fontName="DV-B", fontSize=34, leading=40, textColor=colors.white)
cs = ParagraphStyle("cs", fontName="DV", fontSize=13, leading=18, textColor=colors.HexColor("#DDE3E6"))
cm = ParagraphStyle("cm", fontName="DV", fontSize=9.5, leading=15, textColor=colors.HexColor("#B9C4CA"))
story += [Spacer(1, 70 * mm), Paragraph("DengueRadar", cw), Spacer(1, 6),
          Paragraph("Project record and Round 1 package", cs), Spacer(1, 4),
          Paragraph("Everything we have done, decided and learned, in one place", cs), Spacer(1, 26 * mm),
          Paragraph("DAISI Challenge Singapore 2026 &nbsp;|&nbsp; Problem A2: Real-time outbreak forecasting", cm),
          Paragraph("Team: Braedon (lead, platform and ML), Jingyi (weather data), Ziqi (dengue and places data, then demo), "
                    "Komal (story and pitch)", cm),
          Paragraph("Compiled 30 September 2026. Every statement reflects the project as of that date.", cm),
          Spacer(1, 16 * mm),
          Paragraph("How to read the labels in this document", ParagraphStyle("x", parent=cm, fontName="DV-B", textColor=colors.white)),
          Paragraph("<b>Measured</b>: we computed it from open data. <b>Cited</b>: taken from a named source. "
                    "<b>Designed</b>: our decision. <b>Planned</b>: not built yet. <b>Unverified</b>: needs a source before use.", cm),
          NextPageTemplate("main"), PageBreak()]

# ---------------------------------------------------------------- 1. at a glance
story.append(Paragraph("1. The project at a glance", h1)); story.append(rule())
BOX("<b>The idea in one sentence.</b> DengueRadar forecasts each Singapore planning area's dengue cluster activity two weeks "
    "ahead, explains why, ranks where limited effort should go first, and gives a community group-chat admin a short, sourced, "
    "ready-to-post message.")
H2("The gap we address")
P("NEA's public cluster map and alerts show where dengue is now. We searched and found no public tool that shows where risk is "
  "heading over the next two weeks (a search-limited finding, not proof). Research forecasts do exist, including one at planning-area "
  "level, so our claim is about the last mile: a two-week horizon, a ranking, plain-language drivers and a ready-to-post message.")
H2("Where we are")
T([["Done and verified", "Not done yet"],
   ["Free Edition workspace checks all passed (egress, Unity Catalog and Delta, spatial SQL, MLflow, AI/BI map, Genie, Apps)<br/>"
    "Daily cluster-snapshot job live since 28 Sep (day 1: 11 clusters, 117 cases)<br/>"
    "18-dataset catalogue with owners<br/>"
    "Burden numbers measured from the MOH weekly file<br/>"
    "Monthly lag chart (temperature, humidity, rain)<br/>"
    "Full design documents, three research reports, two judge-panel sessions, a design-thinking session<br/>"
    "Three-slide copy fitted to the official template",
    "Incremental-ingestion check (Structured Streaming, Auto Loader) has not run<br/>"
    "Per-area training panel (Ziqi, due 1 Oct) and Jingyi's weekly rainfall file<br/>"
    "Weekly lag chart<br/>"
    "Any trained model or backtest, so <b>no performance number exists</b><br/>"
    "The real conversation with a group-chat admin<br/>"
    "The slides themselves (only copy exists), team name, and the problem code check"]],
  [1, 1], zebra=False)
H2("How the idea scores today (our estimate)")
P("Two simulated judge-panel sessions scored the idea 5.4 then 5.8 out of 10 on average. Our own reading of the official rubric puts "
  "the current concept note near 67 out of 100, and about 82 if the open evidence items are closed. These are judgement calls, not "
  "results, and shortlisting is relative to other teams.")
H2("What matters most in the next few days")
B(["Have one real conversation with a group-chat admin and use one anonymised quote, or leave the slot out.",
   "Build the three slides from the copy in Section 12 and get someone outside the team to read them cold.",
   "Run the incremental-ingestion check and keep the daily snapshot job healthy.",
   "Never put an unmeasured number on a slide; state impact as targets."])

# ---------------------------------------------------------------- 2. challenge
H1("2. The challenge and the rules we play by")
P("The Databricks AI Social Impact (DAISI) Challenge invites student teams from Singapore institutes of higher learning to build "
  "data-driven solutions to local social challenges using Databricks and open data from data.gov.sg. Ten teams enter a two-week "
  "mentored sprint and three are selected at Demo Day. Databricks Free Edition is free for the challenge.")
H2("Key dates (Singapore time, 2026)")
T([["Date", "Event"],
   ["16 Sep", "Launch at Data+AI World Tour Singapore; registration opens"],
   ["24 Sep", "Databricks hands-on training (completed)"],
   ["**6 Oct, 11:59pm**".replace("**", ""), "Round 1 submission closes on Devpost: a three-slide pitch as PDF (team target: 4 Oct)"],
   ["7 to 9 Oct", "Shortlisting; top 10 announced 9 Oct"],
   ["12 to 26 Oct", "Virtual kickoff 12 Oct, then the mentored build sprint"],
   ["27 Oct, 4 to 7pm", "Demo Day; top three selected"],
   ["4 Nov", "Finale at the new Databricks Singapore office"]], [1, 3.4])
H2("Our problem statement: A2, DengueRadar")
P("<i>Cited (official brief):</i> dengue is hyperendemic in Singapore, with outbreaks affecting tens of thousands of residents. Rising "
  "temperatures and erratic rainfall extend the Aedes breeding season. NEA cluster monitoring today is largely reactive; predictive "
  "risk intelligence could let communities act 2 to 4 weeks ahead.")
P("<b>What to build:</b> a near-real-time pipeline combining live dengue cluster data, weather station readings and geospatial data "
  "into a forward-looking dengue risk forecast by planning area, showing streaming or incremental ingestion from live APIs, weather "
  "feature engineering and a predictive model on an interactive map. <b>Target demo:</b> map current cluster intensity; a two-week "
  "forecast trained on weather and historical cases; explainable Low, Medium and High planning-area risk; a comparison with a "
  "recent-history-average baseline. <b>Stretch:</b> hawker-centre density or green space as proxies, threshold alerts, MLflow "
  "experiment comparisons.")
H2("Round 1 judging rubric")
T([["Criterion", "Weight", "What judges look for"],
   ["Problem fit and social impact", "30%", "A clear problem and a describable benefit"],
   ["Solution quality and originality", "30%", "A thoughtful solution, not a generic dashboard"],
   ["Data and technical feasibility", "25%", "Named open datasets, a credible Databricks architecture, feasible in two weeks"],
   ["Clarity of submission", "15%", "A concise, well-structured concept note or deck"]], [2.2, 0.8, 4])
H2("Rules that shape our choices")
B(["Round 1 is an idea submission; no working build is required. The template has exactly three slides.",
   "Do not upload confidential, personal or customer data, or credentials. Disclose synthetic or cached data and prototype features, "
   "and credit datasets, libraries and models.",
   "Free Edition is serverless and quota-limited: one 2X-Small SQL warehouse, at most five concurrent job tasks, up to three Databricks "
   "Apps that can auto-stop after 24 hours, one Lakebase project, no commercial use. Exceeding quotas can stop compute for the rest of the day.",
   "Cited public data is allowed, so archived cluster data may be used for training if it is credited."])

# ---------------------------------------------------------------- 3. evolution
H1("3. How the idea evolved")
P("The design changed materially twice. This section records what we thought at each stage and why we changed. Nothing was deleted; "
  "superseded records are kept in <font face='DV-I'>_bmad-output/</font> with banners.")
T([["Date", "What happened", "Outcome"],
   ["26 Sep", "Brainstorm (fishbone, empathy map, how-might-we). We broke the problem into weather, mosquito, virus, human behaviour, "
    "environment and response lag. Insights: clusters appear 2 to 3 weeks after transmission starts; most infections are unreported "
    "(hidden iceberg); residents tend to ignore banners; fear only works when paired with one easy action.",
    "A forecast must be paired with a clear, easy action."],
   ["27 Sep", "Kickoff and first forge. First design: <b>senior-first</b>, with Active Ageing Centre staff as the primary user, a "
    "national weekly forecast (Level 1) and a local risk score (Level 2).",
    "Reshaped and hardened; later superseded."],
   ["28 Sep", "Three more forges (subzone risk matrix and root-cause routing; no individual identification; parks and hawker centres as "
    "core). Technical feasibility research: <b>GO with three conditions</b> (test outbound internet, respect quotas, NEA already forecasts). "
    "Free Edition checks all passed and the daily snapshot job went live.",
    "A buildable design, but aimed at the wrong focus."],
   ["28 Sep", "<b>Correct-course pivot.</b> The team realised the senior-first framing missed the brief, which asks for a per-planning-area "
    "forecast with incremental ingestion. New direction: a trained two-week forecast per planning area, explained drivers and a "
    "prescriptive action plan for residents and community leaders. Seniors stay only as a secondary extra-care flag.",
    "Approved by Braedon; docs rewritten."],
   ["30 Sep", "Round 1 judging-fit forge: no routing to a named Town Council, RC or MCST; top three drivers give ranked, deduplicated "
    "actions; a second axis routes by breeding-source tag; the action layer is rule-based and auditable.",
    "Locked."],
   ["30 Sep", "Design session (this report's main subject): H4 green-space hypothesis; a budgeted inspection ranking; a weekly action "
    "card; audience views; group-chat delivery; authority routing with a jurisdiction check; three research reports; two judge panels; "
    "design thinking; a measured burden number; the three-slide copy; repository tidy.",
    "Design locked; evidence gaps identified."]], [0.8, 5.2, 2])
BOX("<b>What was dropped and why.</b> The senior-first framing, Active Ageing Centre staff as primary users, a Senior Risk Index, "
    "\"Family Ping\", block-level carer lists and the exposure-times-vulnerability matrix. They answered a different question from the "
    "brief. We must not describe any of them as current.", PALE_AMBER, colors.HexColor("#E0A800"))

# ---------------------------------------------------------------- 4. the idea
H1("4. The final idea")
H2("The problem in our words")
P("NEA's public cluster map and alerts show where dengue is now. Nothing public that we found shows residents and community leaders where "
  "risk is heading over the next two weeks, so prevention (emptying containers, clearing gutters, checking drains) starts late. "
  "The Aedes life cycle can be as short as seven days (NEA, to be verified), so a two-week warning spans two breeding cycles.")
H2("The solution")
B(["<b>Ingest</b> the live NEA cluster feed and weather data incrementally into Delta tables, building the history the feed does not keep.",
   "<b>Forecast</b> each planning area's cluster activity two weeks ahead with a model trained on archived cluster history, judged against simple baselines.",
   "<b>Explain</b> the top three drivers per area in plain words.",
   "<b>Rank</b> where limited effort should go first (\"where do the first 8 teams go?\") in two lists: most cases, and highest risk per resident.",
   "<b>Prescribe</b> up to three ranked, deduplicated actions per area from an auditable rule table.",
   "<b>Deliver</b> a short, dated, sourced message that a community group-chat admin can copy into WhatsApp or Telegram, with NEA as a comparison view."])
H2("Who uses it and what decision it changes")
T([["User", "Decision", "How they get it"],
   ["Residents", "What to check at home this week", "Through the community chats their admins already run (a proposed channel)"],
   ["Group-chat admins and volunteers (RC, MCST council, engaged residents)", "What to post; what to check nearby", "An admin kit: ready-to-post text, area picker, valid-until date"],
   ["NEA (as a comparison view, not the user)", "Where inspection effort should go first", "A weekly export file and a data contract"]], [2.4, 2.2, 3.4])
H2("What makes it different")
P("The forecast on its own is table stakes: the brief asks for it and other teams will build it. Our difference sits in the decision and "
  "delivery layers: a budgeted ranking, drivers in plain words, actions tied to who owns them, and a message designed to be posted "
  "by a person who has to stand behind it.")
H2("What we will and will not claim")
B(["We <b>will</b> say NEA's public cluster map and alerts describe today, and that we found no public two-week forecast tool.",
   "We <b>will not</b> say \"NEA does not predict\": NEA's institute appears to run internal national forecasts.",
   "We <b>will not</b> say nobody forecasts by planning area: a 2026 preprint forecasts hotspots for the 55 planning areas one week ahead.",
   "We <b>will not</b> claim group chats are how residents are informed as a fact; it is a proposed channel until a real admin says otherwise.",
   "We <b>will not</b> claim community messaging reduces dengue: the evidence is weak and mostly about mosquito counts.",
   "We <b>will not</b> put any performance number on a slide before it is measured."])

# ---------------------------------------------------------------- 5. data
H1("5. Data")
H2("The dataset catalogue")
P("<i>Designed and cited.</i> The full list, IDs, fields and access notes are in <font face='DV-I'>DATASETS.md</font>. The 18 datasets, "
  "checked against the data.gov.sg API on 27 Sep 2026:")
T([["#", "Dataset", "Source", "Used for", "Tier", "Owner"],
   ["1", "Weekly Infectious Disease Bulletin Cases (2012 to 2022)", "MOH", "National context and burden numbers", "Core", "Ziqi"],
   ["2", "Dengue Clusters (daily snapshot, polygons and case counts)", "NEA", "Live input; breeding-source tags; map", "Core", "Ziqi"],
   ["3", "Areas with High Aedes Population", "NEA", "Local exposure signal", "Core", "Ziqi"],
   ["4", "Residents by planning area, age, sex (Census 2020)", "SingStat", "Population per area; 65+ share", "Should", "Ziqi"],
   ["5, 6", "Master Plan 2019 subzone and planning-area boundaries", "URA", "Scoring unit and Island view", "Core", "Ziqi"],
   ["7 to 9", "Historical rainfall (2017 to 2024), air temperature, relative humidity", "NEA", "Weather features and lags", "Core", "Jingyi"],
   ["10", "Real-time rainfall (5-minute)", "NEA", "Incremental ingestion; current rain", "Core", "Jingyi"],
   ["11, 12", "NParks parks and nature reserves; hawker centres", "NParks, NEA", "Green-space share (H4); places where people gather", "Should", "Jingyi"],
   ["13", "Historical daily weather records", "NEA", "Optional: extend weather to 2012", "Should", "Jingyi"],
   ["14 to 16", "HDB property information; HDB existing building; CHAS clinics", "HDB, MOH", "Block age, block locations, nearest clinic", "Should", "Ziqi"],
   ["17", "Archived NEA clusters (SG Outbreak/SGCharts; Nature Scientific Data 2022)", "External, cited", "<b>Training panel</b> and the 2020 replay", "Core (training)", "Ziqi"],
   ["18", "Weather station locations", "NEA", "Map stations to planning areas", "Core", "Jingyi"]],
  [0.5, 3.2, 1, 2.6, 0.9, 0.7])
H2("Measured: how big the problem is")
P("<i>Measured 30 Sep</i> by summing the MOH weekly bulletin file (<font face='DV-I'>analysis/data/weekly_dengue_ziqi.csv</font>). "
  "This resolved a conflict between two team documents: the correct 2020 total is 35,261, not 35,012. Ziqi or Komal still confirms the "
  "source and cites it.")
T([["Year", "Cases", "Peak week", "Note"],
   ["2017", "2,759", "2017-W02 (90)", "Lowest recent year"],
   ["2019", "15,910", "2019-W28 (661)", ""],
   ["<b>2020</b>", "<b>35,261</b>", "<b>2020-W30 (1,791)</b>", "53 epi weeks in the file; record year"],
   ["2021", "5,251", "2021-W01 (194)", ""],
   ["<b>2022</b>", "<b>32,130</b>", "2022-W21 (1,563)", "Second surge"]], [1, 1.2, 2, 3])
P("The swing from 5,251 cases in 2021 to 32,130 in 2022 shows how volatile the disease is. It also shows that weather alone cannot "
  "explain surges, which shapes how carefully we word our claims.")
H2("The live snapshot job and the history gap")
B(["NEA's cluster feed is a <b>today-only snapshot</b>: no history (DATASETS.md). A Lakeflow Job runs daily at 21:00 and saves each day's "
   "clusters to a Delta table, so the history exists only because we build it. It has run since 28 Sep (day 1: 11 clusters, 117 cases).",
   "The <b>training archives</b> (SG Outbreak/SGCharts: 256 snapshots, 3 Jul 2015 to 6 Nov 2020; Nature Scientific Data 2022: 20 weekly "
   "snapshots, 28 Feb to 9 Jul 2020, 213 subzones mapped with at least 92% of points inside the matched subzone) end in Nov 2020.",
   "So there is a <b>five-year gap</b> between the end of the archives and the start of the live feed. A rolling backtest cannot say the "
   "model holds in the current regime, so we treat the live snapshots as a <b>prospective, out-of-time test</b> and say so on the slides.",
   "2020 has dense snapshots to May, then monthly only, and cases outside clusters are missing. We will report the weeks and areas with usable data."])
H2("Target caveat (must appear on the slides)")
BOX("The archive holds only cases inside NEA clusters. The model predicts <b>cluster activity</b> (new or growing cluster cases in a "
    "planning area over the next two weeks), not total dengue cases.", PALE_AMBER, colors.HexColor("#E0A800"))
H2("A note on boundaries")
P("Planning areas do not match Town Council, constituency or MCST boundaries, and no open dataset maps one to the other. The HDB "
  "property file has a <font face='DV-I'>bldg_contract_town</font> code per block, which might support a block-to-HDB-town mapping, but "
  "that is not the same as Town Council boundaries and does not cover condos. It is recorded as a possible roadmap input only.")

# ---------------------------------------------------------------- 6. method
H1("6. Method: hypotheses, models and validation")
H2("Targets")
B(["<b>Regression target:</b> cluster cases in planning area A over weeks t+1 and t+2.",
   "<b>Classification target (\"Rising\"):</b> cases in the next two weeks are at least 20% above the area's 4-week average and above a "
   "minimum count, so tiny numbers do not flap.",
   "<b>Risk level shown to users:</b> Low, Medium or High from the calibrated Rising probability. Posts lead with \"higher than usual\" "
   "and show the level second."])
H2("The four hypotheses")
P("Following the hackathon handbook, each hypothesis links a domain factor to a measurable feature. Any may be disproven, and we will say so.")
T([["ID", "Hypothesis", "Features", "Status"],
   ["<b>H1</b> Weather lag", "Warm periods, and rain 2 to 4 weeks earlier followed by dry spells, raise next-fortnight cluster activity "
    "(faster breeding, standing water)", "hot_days_31c, rain_lag2..4, temp_lag, humidity_lag, flushing_days",
    "<b>Partly measured (monthly):</b> max temperature +0.29 at a 4-month lag, humidity -0.26, rain -0.10. Weekly chart pending."],
   ["<b>H2</b> Spatial spillover", "Clusters in neighbouring areas raise an area's own risk", "cluster_cases_adjacent, dist_to_nearest_cluster_km", "Untested"],
   ["<b>H3</b> Recurrence", "Areas with clusters in the past year recur, especially in older housing", "cluster_weeks_last_52, median_block_age", "Untested"],
   ["<b>H4</b> Green space (added 30 Sep)", "Areas with more green space have more cluster activity, <b>after controlling for population density</b>. "
    "Say \"associated with\", not \"causes\"", "green_space_share (NParks parks / land area), pop_density, median_block_age",
    "Untested. Needs the leave-areas-out check, because it never varies within an area"]], [1.3, 3, 2.3, 2.4])
H2("Baselines and models")
T([["Name", "Rule", "Why"],
   ["B1 Persistence (main)", "Next two weeks equal the last four weeks' average cluster cases in that area", "What a reader of NEA's dashboard would guess"],
   ["B2 Seasonal average", "Same week averaged over training years", "Dengue is seasonal"],
   ["B3 Explainable points score", "Hand-set points: cluster size, high-Aedes zone, national trend, recent rain, hot days", "Shows what training adds; also our honest fallback"],
   ["M1 Trained model", "LightGBM (regression plus a Rising classifier) logged in MLflow; a Poisson or logistic model as a readable cross-check", "Handbook default for tabular data"]],
  [1.6, 4, 2.4])
P("<b>Fallback rule:</b> if M1 does not beat B1 and B2, we say so and present the explainable score with the honest result. The best "
  "model is registered in Unity Catalog.")
H2("How we test honestly")
B(["<b>Time-ordered, never random.</b> Rolling origin: train 2015 to 2018, test 2019; train 2015 to 2019, test January to July 2020. Weeks are never shuffled.",
   "<b>Leave-areas-out check</b> (GroupKFold by planning area): confirms the model learns weather and spillover patterns, not each area's own history.",
   "<b>No leakage.</b> Features for week t use only data available before week t. NEA publishes cases about a week late, so we use lags of "
   "one week or more. Imputers, scalers and encoders are fitted inside each fold. Out-of-fold predictions are logged to MLflow.",
   "<b>Prospective test.</b> Log each forecast with its date and score it against the live snapshots two weeks later; report how many forecast "
   "dates it covers and never blend it into the backtest numbers.",
   "<b>Known weakness, stated first:</b> published Singapore models catch the timing of peaks but underpredict their size."])
H2("Metrics and the cost matrix")
T([["Metric", "Meaning", "Target"],
   ["Rising recall and precision", "Of real rises, how many we flagged; of our flags, how many were real", "Recall first (a missed rise costs more)"],
   ["PR-AUC", "Quality of the Rising probability when rises are rare", "Above B1 and B3"],
   ["Hit rate", "Share of new or growing clusters in areas rated High", "Above B1; compare with NEA's roughly 90% for its 1 km2 map"],
   ["<b>Capture rate at K = 8</b>", "Share of the next fortnight's new cluster cases that fall inside our top eight areas", "Above the last-four-weeks baseline (to be measured)"],
   ["Lead time (weeks)", "How many weeks before an area crossed the alert size we first flagged it", "Measure it; never claim it first"],
   ["Alert load", "Share of areas rated High in a typical week", "At most 15%"],
   ["MAE (cases per area per fortnight)", "Average miss", "Below B1 and B2"]], [2.3, 3.4, 2.6])
P("<b>Cost matrix.</b> A missed rising area is set at five times the cost of an unnecessary reminder, as a <i>starting assumption</i>. "
  "The Rising threshold, the minimum count, the 15% cap, the 5x ratio and the risk cut-offs are tuned on validation years and frozen "
  "before the test year is scored. The trigger for a \"sustained\" flag is tuned the same way; a fixed \"two consecutive weeks\" rule is "
  "avoided because two-week forecast windows overlap.")
H2("What the literature says (from the feasibility research)")
B(["NEA's operational LASSO model forecasts national weekly cases 1 to 12 weeks ahead with an error of 17% at one week and 24% at three months.",
   "Recent cases carry most of the forecast skill; weather-only models perform poorly. Absolute humidity is the steadiest weather predictor; heavy rain can lower risk for weeks.",
   "Two of our early rules (hot days above 31 C and heavy rain both raise risk) conflict with parts of the literature, which is why H1 is worded carefully and why we test rather than assume.",
   "Training on a short weather-overlap window (about 310 weeks) argues for a simple model with few lags and rolling validation."])

# ---------------------------------------------------------------- 7. prescriptive
H1("7. The prescriptive layer: from forecast to action")
P("DengueRadar predicts, then prescribes. The action layer is <b>deliberately rule-based, not model-generated</b>: it is auditable and "
  "tied to NEA's public guidance, unlike unverified generated advice. All wording is a draft until checked against NEA's pages.")
H2("Two independent routing axes")
T([["Axis", "What it does", "Caveat"],
   ["<b>Axis 1: why it is rising</b> (the backbone)", "The top three SHAP (or rule-score) drivers map to up to three ranked, deduplicated actions; overlapping actions collapse into one line", "Depends on the model, or on B3 if the model does not win"],
   ["<b>Axis 2: who caused it</b> (bonus layer)", "NEA's cluster feed tags breeding source: HOMES, PUBLIC_PLACES, CONSTRUCTION_SITES. A construction tag routes to an NEA enforcement referral; home and public-place tags feed the resident checklist",
    "The field is sparse: 2 of 11 clusters were tagged on 27 Sep. When absent, the Area view says \"root cause not yet identified by NEA\". The tag is used only after a cluster exists, never as a model feature"]], [2.2, 3.6, 3])
BOX("<b>Locked decision: no routing to a named Town Council, RC or MCST.</b> Planning areas do not align with those boundaries and no "
    "open dataset maps them. Naming an institution would imply a routing capability the data cannot support. Every community action is a "
    "checklist that any engaged resident, RC volunteer or MCST council member in a flagged area can read, act on or escalate.")
H2("6a. Inspection priority ranking (the decision layer)")
P("Answers \"we only have effort for K areas this week, which K?\". It orders areas; it does <b>not</b> claim that acting there reduces cases.")
B(["<b>Two lists, both shown:</b> \"most cases\" (probability times expected cases) favours large areas; \"highest risk per resident\" "
   "(per 10,000 residents) favours small areas with a sudden rise.",
   "<b>Budget slider K</b> (5 to 15, default 8, about the 15% alert cap).",
   "<b>Metric: capture rate at K</b> on the backtest, against B1. Filled only from measured values.",
   "<b>Guardrails:</b> state \"cluster cases only\"; show rank change versus last week so the list does not flap; mark poor-coverage areas \"low data\"."])
H2("6b. The weekly action card")
B(["Area, risk band and what changed since last week.", "Top three drivers in plain words (\"heavy rain 2 to 4 weeks ago, now warm\"); feature names never appear.",
   "Up to three ranked, deduplicated actions as a tick-box checklist, each with a recommended window.",
   "A root-cause line from Axis 2, an extra-care flag where the share of residents aged 65 and over is in the top third, and a source link.",
   "A <b>confidence line</b> (backtest hit rate for that band), shown only once measured."])
H2("The action library (draft)")
P("Eleven draft actions, each tagged to a hypothesis or axis. B-L-O-C-K and S-A-W are NEA's own prevention steps (found via search; "
  "Komal must read the source pages). Full table in Appendix A.")
T([["Steps", "NEA's wording (search summary only; to verify)"],
   ["<b>B-L-O-C-K</b>", "Break up hardened soil; Lift and empty flowerpot plates; Overturn pails and wipe their rims; Change water in vases; Keep roof gutters clear and add BTI insecticide"],
   ["<b>S-A-W</b>", "Spray insecticide in dark corners; Apply insect repellent regularly; Wear long sleeves and long pants"]], [1.2, 6])
H2("6c. Who gets what (audience views)")
P("One forecast, three decisions. The split is by <b>relevance, not secrecy</b>: cluster locations are already public, and a public prototype "
  "has no access control.")
T([["Lens", "Decision", "Sees", "Does not see by default"],
   ["Resident (reached mainly through a chat)", "What do I do at home this week?", "Own area's band, what changed, top three plain-language actions, extra-care line, adjacent areas' bands", "Probabilities, island ranking, model metrics"],
   ["Volunteer or group-chat admin", "What should our neighbourhood check, and what do I post?", "The resident view plus the community checklist and the admin kit", "The full island ranking"],
   ["NEA (comparison view)", "Where should limited effort go first?", "Both priority lists, K slider, drivers, tags, confidence and coverage, backtest scores", "Resident-level content"]], [1.8, 2, 3.4, 1.8])
T([["Band", "Resident", "Volunteer", "NEA view"],
   ["Low", "Routine card (\"Low is not zero\")", "Nothing", "Nothing"],
   ["Medium", "Card with actions", "Digest", "Nothing"],
   ["High", "Alert message", "Checklist", "In the ranking"],
   ["Sustained or tagged", "Same", "Same", "Flag, or referral row"]], [1.6, 2.4, 2, 2])
P("<b>Alert fatigue.</b> Each High area is marked \"new\" or \"persistent\" (tied to H3 recurrence) so recurring areas do not cry wolf, and "
  "the backtest reports the distribution of weeks in High per area. <b>Language rules:</b> \"forecast cluster activity\", \"prevention "
  "priority\"; never \"worst\", \"dangerous\" or \"safe\"; every view carries the cluster-cases-only caveat.")
H2("6d. Dissemination modes and authority routing")
P("<b>Route by who owns the action, not by geography.</b> National agencies need no boundary match, so they can be addressed directly; "
  "boundary-based groups are reached through the admin kit and never named. The prototype sends nothing to anyone: the app generates "
  "each audience's payload, and a person or the agency's own platform takes it from there.")
T([["Authority", "Owns", "Trigger", "Mode"],
   ["NEA", "Dengue control and inspection", "Weekly; flag on sustained High", "Weekly export file plus a data contract"],
   ["NEA enforcement", "Construction-site breeding", "CONSTRUCTION_SITES tag present", "Structured record per trigger"],
   ["NEA drain cleansing (Department of Public Cleanliness)", "Drain and canal cleansing", "High or rising with the rain-then-warm driver", "Structured record per trigger"],
   ["NParks (role unconfirmed)", "Parks and nature reserves", "High with high green-space share (H4)", "Structured record per trigger; illustrative"],
   ["Residents, RCs, MCSTs, group-chat admins", "Community action", "Weekly, only on a band change", "Admin kit with copy buttons"],
   ["CDA and MOH; HDB, JTC, SLA", "Clinical response; other estates", "n/a", "Roadmap only"]], [2.4, 1.8, 2.3, 2.2])
H3("The admin kit")
P("One post per planning area per week, only when the band changes. It carries the area name and \"your estate may span a different "
  "boundary\", the band and what changed, up to three actions, a source line, a date and a <b>valid-until</b> line (forwarded messages "
  "live in chats for weeks), and \"a forecast, not a diagnosis\". Separate WhatsApp and Telegram versions, a multi-select area picker, "
  "no bot, no token and no stored user data. Extra languages are a stretch with speaker-reviewed translations.")
H3("The data contract (v0.1, a proposal)")
P("One versioned schema, and each authority takes only the fields it needs (Appendix B). We have no agreement with any agency; all "
  "example values are illustrative.")
story.append(CondPageBreak(60 * mm)); H3("The jurisdiction check: what it caught")
P("We checked our routing against official pages. Several direct page fetches failed, so most points rest on search summaries and "
  "Komal must read the pages before any slide uses them.")
T([["Our claim", "Result"],
   ["NEA and BCA enforce construction-site breeding", "NEA is supported (Stop Work Orders, court charges, the ECO Scheme). <b>BCA did not appear</b>, so we now say NEA only"],
   ["PUB cleans public drains", "<b>Not supported.</b> Regular cleansing is done by NEA's Department of Public Cleanliness; PUB does structural repairs and litter devices"],
   ["NParks owns park dengue control", "<b>Not found.</b> NParks appears only in the One Health Framework and gardening advice; marked unconfirmed"],
   ["MOH is the health-sector body", "<b>Partly.</b> The Communicable Diseases Agency gives dengue clinical guidance and the 24-hour notification rule (page fetched)"]], [3, 5.2])

# ---------------------------------------------------------------- 8. architecture
H1("8. Databricks architecture")
IMG(os.path.join(ROOT, "pitch", "assets", "architecture.png"), 1.0,
    "Figure 1. The architecture diagram (pitch/assets/architecture.png). The staging note on the diagram says incremental weather loading is planned and untested.")
H2("Each component and its job")
T([["Component", "Its job in DengueRadar", "Why not a laptop script"],
   ["<b>Lakeflow Jobs</b>", "Scheduled daily cluster snapshots (live since 28 Sep) and planned incremental weather loading", "NEA's feed keeps no history; a scheduled job builds it"],
   ["<b>Delta Lake</b> (bronze, silver, gold)", "Bronze: raw as received. Silver: cleaned and mapped to planning areas. Gold: weekly area features, forecasts, action rules", "Append-only snapshot history, MERGE and time travel"],
   ["<b>Unity Catalog</b>", "Governed tables, documented sources and lineage", "The brief asks for cataloguing and lineage"],
   ["<b>MLflow</b>", "Compare baselines with LightGBM, register the best model, log out-of-fold predictions and SHAP drivers", "Reproducible experiments and an audit trail"],
   ["<b>AI/BI map, Genie, Databricks App</b>", "Island and Area views, plain-English questions on the gold tables, the demo interface", "Non-technical users read it without code"]], [2.1, 3.8, 2.4])
P("<b>Why a platform:</b> because NEA's cluster feed keeps no history, a scheduled Lakeflow job builds it into Delta from 28 Sep, and that same "
  "history becomes our out-of-time test. The copy-paste post is simply an output and uses no Databricks feature.")
H2("Free Edition checks (Braedon's workspace, 28 Sep)")
T([["Area", "Test", "Result"],
   ["Egress", "pypi.org; data.gov.sg dataset download, datastore API and real-time rainfall API", "Yes (4 of 4)"],
   ["Unity Catalog and Delta", "Create schema and table; Delta history and time travel", "Yes (2 of 2)"],
   ["Spatial", "st_dwithin in SQL; H3; shapely fallback", "Yes (3 of 3)"],
   ["MLflow", "Log a run and model; register the model in Unity Catalog", "Yes (2 of 2)"],
   ["Lakeflow Jobs", "Daily 21:00 schedule of the cluster-snapshot notebook", "Yes; live since 28 Sep"],
   ["AI/BI dashboard", "Point map of today's clusters (draft Island view)", "Yes"],
   ["Genie", "\"Which cluster has the most cases?\"", "Yes (Taman Jurong, 80 cases)"],
   ["Databricks Apps", "Streamlit template starts", "Yes"],
   ["<b>Incremental ingestion</b>", "Structured Streaming, Auto Loader, MERGE fallback", "<b>Not yet run</b>"]], [1.9, 4.4, 2])
H2("Constraints we work within")
B(["Free Edition quotas are unpublished; keep workloads small and pre-aggregate the roughly 30 GB of raw 5-minute weather outside Databricks.",
   "Databricks Apps can stop after 24 hours, so a demo needs a local fallback (a cached snapshot) and a short screen recording.",
   "The daily snapshot job must stay healthy; the number of snapshot days is read from the table on the day, never estimated."])

# ---------------------------------------------------------------- 9. research
H1("9. Research findings")
H2("9.1 Feasibility research (28 Sep): GO with three conditions")
B(["<b>Outbound internet</b> is restricted on Free Edition. <i>Resolved:</i> data.gov.sg was reachable in our tests on 28 Sep.",
   "<b>Quotas are real but unpublished.</b> Conserve compute and pre-aggregate large weather files.",
   "<b>NEA already forecasts.</b> Our originality cannot rest on forecasting alone."])
H2("9.2 What already exists (competitive recon, 30 Sep)")
T([["Existing thing", "What it does", "Forecast?"],
   ["NEA cluster map and table", "Active clusters, localities, case counts; Red 10+ cases, Yellow fewer than 10, Green no new cases (monitored 21 days); updated at 1am", "No"],
   ["NEA Dengue Community Alert System", "Colour-coded banners; alerts on high Aedes mosquito population and clusters near you through the myENV app or a web portal", "No forward-looking projection on the page"],
   ["myENV notifications", "Users save locations and enable dengue and Aedes notifications; based on Gravitrap surveillance (search summary)", "Current counts, not future cases"],
   ["NEA institute's internal models", "LASSO models, national weekly forecasts 1 to 12 weeks ahead (search summary)", "Internal"],
   ["Research: neighbourhood forecast (BMC Medicine, 2018)", "315 neighbourhoods, up to 12 weeks ahead, AUC above 0.75", "Research"],
   ["Research: hotspot forecast (arXiv preprint, 2026)", "Predicts hotspots by subzone, aggregated to 55 planning areas, one week ahead, F-score 0.79; not peer reviewed", "Research"]], [2.4, 4.4, 1.6])
P("<b>Implication:</b> keep the gap claim but narrow it (\"nothing public shows where risk is heading over the next two weeks\", search-limited). "
  "Position explicitly against myENV: alerts today, a forecast plus a ready-to-post message tomorrow. Cite the planning-area preprint as related work. "
  "Not searched: SG Outbreak and community projects, the myENV launch date.")
H2("9.3 Group-chat delivery and community messaging (user-voice recon, 30 Sep)")
B(["<b>The channel is plausible.</b> WhatsApp is widely used (roughly 80 to 90% monthly, aggregator figures that conflict; treat as \"widely used\"). Resident-run "
   "Telegram groups exist as neighbourhood hubs with volunteer moderators. Government bodies such as REACH run chat groups.",
   "<b>Direct evidence is missing.</b> No source shows RC or condo chats circulating official notices, or NEA using chat groups for dengue outreach. "
   "So \"residents are informed through group chats\" is our team's observed practice, not a sourced fact.",
   "<b>Effect evidence is weak.</b> A 2025 review of 15 systematic reviews found only modest changes in mosquito indices and called the evidence "
   "weak, with most outcomes being mosquito counts rather than disease. NEA's 2022 outreach with 5,000 grassroots volunteers reports activity counts, not outcomes.",
   "<b>Risk:</b> forwarded messages spread fast and are often partly wrong (in a 2020 Singapore study, 52.3% of 151 adults forwarded at least one COVID message). "
   "An unofficial post carries no official authority, which is why every post has a source line, a date and a valid-until."])
story.append(CondPageBreak(100 * mm)); H2("9.4 The lag chart: what the data says so far")
IMG(os.path.join(ROOT, "pitch", "assets", "lag_chart_months.png"), 0.82,
    "Figure 2. Monthly lag chart (pitch/assets/lag_chart_months.png). Singapore 2012 to 2022, 132 months, unusual weather against unusual cases for that time of year (Spearman). Measured.")
P("<b>Reading it:</b> warm months come before more dengue (maximum temperature +0.29 at a four-month lag), humidity shows a negative link (-0.26) and "
  "rainfall alone barely lines up (-0.10). This supports the temperature part of H1 and argues against \"more rain equals more risk\". It is "
  "<b>monthly only</b>: the weekly version waits for Jingyi's rainfall file, and the line goes on a slide only if the weekly chart agrees.")

# ---------------------------------------------------------------- 10. judge feedback
H1("10. Stress-testing the idea")
P("We tested the idea with several methods. The judge panels are <b>simulated personas</b>, not real judges, and their scores are a "
  "structured way to find weaknesses, not a prediction.")
H2("Assumption audit, pre-mortem and Shark Tank pass (30 Sep)")
T([["Risk found", "What we changed"],
   ["Nothing is sent, so \"delivery\" was unspecified", "Each audience now has a defined mode; the prototype generates payloads and sends nothing"],
   ["Recurring areas would be High every week, so posts get ignored", "New-versus-persistent flag; weeks-in-High report; 15% alert cap"],
   ["A fixed \"two weeks High\" escalation rule is weak because forecast windows overlap", "Tune the trigger on validation years and freeze it"],
   ["\"NEA would use our NEA view\" is an assumption", "Reframed as a comparison view, decision support beside NEA's own forecast"],
   ["Too many audiences blur the story", "Three lenses only; the rest on the roadmap"],
   ["Benefit claims with no numbers", "Impact stated as targets; benefit numbers only after the backtest"],
   ["Area labels could stigmatise", "Language rules: \"forecast cluster activity\", \"prevention priority\", never \"worst\" or \"safe\""]], [3.6, 4.6])
H2("Judge panel: two sessions")
P("A five-person panel (technical judge, business judge, sponsor judge, a group-chat admin as target user, and a demo-day sceptic) "
  "scored the idea from their own lens.")
T([["Judge", "Session 1", "Session 2", "Main point"],
   ["Priya (technical)", "6", "6", "Cleaner and more honest; new hole: training archives end Nov 2020, live feed starts Sep 2026; nothing built"],
   ["Marcus (business)", "5", "6", "Sharp wedge; \"that number is about dengue, not your idea\"; no evidence anyone wants it"],
   ["Aiko (sponsor)", "6", "6", "Which parts truly need Databricks? The \"history that does not exist\" reason was not yet on the slide"],
   ["Sam (target user)", "6", "6", "Would try it if short, sourced, calm and multilingual; posts must not read as official; nobody has asked yet"],
   ["Ravi (demo sceptic)", "4", "5", "Round 1 needs no demo; Demo Day needs a local fallback and a recording"],
   ["<b>Average</b>", "<b>5.4</b>", "<b>5.8</b>", "The cleanup improved clarity and honesty but added no evidence about the product"]], [1.6, 0.9, 0.9, 6])
H2("Strengths")
B(["Follows the brief closely and adds a real differentiator in the decision and delivery layers.",
   "Honest caveats: cluster cases only, a fallback score if the model does not win, and a stated data gap.",
   "Leak-free validation design, and a jurisdiction check that caught two errors before they reached a slide.",
   "The daily ingestion job is live and the Free Edition checks passed.",
   "The idea fits how information actually moves in Singapore neighbourhoods (to be confirmed by one real conversation)."])
H2("Weaknesses and loopholes")
B(["<b>No measured evidence about the product</b>: no backtest, no baseline number, no model.",
   "<b>No user evidence</b>: nobody from a group chat or RC has been asked. It is the biggest gap.",
   "<b>The five-year data gap</b> between the training archives and the live feed.",
   "<b>Target overreach risk</b>: slides must say cluster activity, not \"dengue risk\" for all cases.",
   "<b>Incremental ingestion is unrun</b>, and it is the brief's explicit ask.",
   "<b>Placeholders remain</b>: live cluster count, team name and problem code.",
   "<b>A bare \"HIGH\" could alarm a chat</b>; posts lead with \"higher than usual\".",
   "<b>Single point of failure</b>: the per-area panel; if it is too thin we fall back to the rule score."])
H2("Top three objections and short answers")
T([["Objection", "Answer (only what is true today)"],
   ["\"That number is about dengue, not your idea.\"", "It answers the template's open-data prompt. Our own evidence will be the baseline capture rate and the live-snapshot test once measured; until then we state targets."],
   ["\"Your training data stops in 2020. How do you know it works in 2026?\"", "That is our main risk. The daily job collects live snapshots from 28 Sep and we treat them as an out-of-time test, reported honestly."],
   ["\"Why does this need Databricks?\"", "NEA's feed keeps no history. A scheduled Lakeflow job builds it into Delta, and MLflow tracks the model against baselines."]], [3.4, 5])
H2("Our rubric estimate")
T([["Criterion", "Weight", "Now", "If open items close"],
   ["Problem fit and social impact", "30", "about 21", "about 25"],
   ["Solution quality and originality", "30", "about 21", "about 25"],
   ["Data and technical feasibility", "25", "about 17", "about 20"],
   ["Clarity of submission", "15", "about 8", "about 12"],
   ["<b>Total</b>", "100", "<b>about 67</b>", "<b>about 82</b>"]], [3.4, 1, 1.4, 2])
P("These are our judgement, with no calibration against real judges, and shortlisting is relative to the other teams.", small)

# ---------------------------------------------------------------- 11. design thinking
H1("11. Design thinking: the admin and the resident")
P("Goal: prepare the 15-minute real conversation and sharpen the mock post and slide 2. <b>We have not yet spoken to any user.</b> "
  "Observations are marked as sourced or as hypotheses, and the test results are deliberately blank.")
H2("Challenge statement")
BOX("How might we help a community group-chat admin share a short, sourced, calm two-week dengue warning that neighbours understand and act on, "
    "without the admin having to sound like an authority or risk spreading something wrong?")
H2("Point of view")
P("A community group-chat admin needs a post they can put their name behind, because being wrong or sounding official costs them their "
  "neighbours' trust. The difficulty is not typing the message but standing behind it.")
H2("Empathy map (hypotheses to test)")
T([["", "The admin", "The resident"],
   ["Says", "\"Where is this from?\" \"Is it official?\" \"Can it be shorter?\"", "\"Is this real?\" \"What do I do?\" \"Why is it in English?\""],
   ["Thinks", "\"If it is wrong, people will blame me.\" \"Will the aunties and uncles understand it?\"", "\"Do I need to worry?\" \"Who sent this?\""],
   ["Does", "Copies and forwards from trusted sources, adds a greeting, sometimes translates, answers replies", "Skims, forwards to family, ignores long posts"],
   ["Feels", "Responsible, cautious, wary of spamming the chat", "Anxious at a bare \"HIGH\", numb if it repeats weekly"]], [0.8, 3.6, 3.6])
H2("The journey and where an admin may drop out")
P("Trigger, then trust check, then fit check, then edit, then post, then replies, then follow-up. The likeliest drop-outs are the trust check "
  "(no clear source), the fit check (an estate spanning two areas), the replies (no ready answers) and the follow-up (weekly fatigue).")
H2("Top concepts")
T([["Concept", "Where it goes"],
   ["<b>The trust-first post:</b> five lines at most, plain words, calm \"higher than usual\", three actions, a date and valid-until, and an honest source line", "Slide 2 mock"],
   ["<b>The answer card:</b> reply-ready one-liners for \"Is this official?\", \"What do I do?\", \"Should I worry?\"", "Test in the conversation"],
   ["<b>Preview and pre-post check:</b> show the admin what neighbours will see and confirm area and date", "Sprint concept"]], [6, 2.2])
H2("The two prototypes we will show (illustrative, not a real forecast)")
T([["Variant A (full)", "Variant B (short)"],
   ["DENGUE FORECAST | [Area] | week of 6 Oct<br/>Next 2 weeks: higher than usual (level HIGH, up from Medium)<br/>Why: heavy rain 2 to 4 weeks ago, now warm; cases rising nearby.<br/>"
    "This week: 1. Lift and empty flowerpot plates, overturn pails and wipe rims, change vase water 2. Keep roof gutters clear 3. Use repellent, wear long sleeves and pants<br/>"
    "Valid until 19 Oct. Forecast by DengueRadar, a student project using NEA data. Not a diagnosis. Your estate may span another area.",
    "[Area]: dengue risk higher than usual for the next 2 weeks.<br/>This week: empty flowerpot plates and pails, keep gutters clear, use repellent.<br/>"
    "Valid until 19 Oct. Source: NEA data, DengueRadar (student project)."]], [1, 1], zebra=False)
story.append(CondPageBreak(60 * mm)); H2("Test plan and assumptions")
T([["Assumption", "What would disprove it"],
   ["An admin will post an unofficial forecast if the source is clear", "The admin says they only forward official notices"],
   ["\"Student project using NEA data\" is acceptable", "The admin says it makes the post unusable"],
   ["Recipients understand \"higher than usual\"", "They read it as \"someone is ill\" or \"nothing to do\""],
   ["Recipients know what to do after reading", "They cannot name one action"],
   ["Admins would post weekly", "They say monthly, or only when serious"],
   ["One planning area fits the admin's estate", "Their estate spans two or more areas"]], [4.2, 4])
P("The full script, decision rules and answer card are in the outline (Section 12). If the admin refuses an unofficial source, the slide says "
  "endorsement is on the roadmap; if recipients misread the wording, we change it before it reaches a slide.")

# ---------------------------------------------------------------- 12. round 1 package
H1("12. The Round 1 package")
P("Round 1 is a three-slide PDF answering the official template's prompts. The template is a fixed list of one-line prompts with the right "
  "half of each slide free, so every answer must be short and each slide gets one visual. The editable template is at "
  "<font face='DV-I'>pitch/daisi-round1-3-slide-template.pptx</font>. Brackets need a source before submission.")
T([["Slide", "Visual for the free half"],
   ["1. Problem and why it matters", "One large number callout: 35,261 dengue cases in 2020, peaking at 1,791 in one week"],
   ["2. Solution and data", "The mock post as a phone screen"],
   ["3. Databricks architecture and impact", "The architecture diagram"]], [3, 5])
H2("Slide 1: Problem and why it matters")
T([["Template prompt", "Draft answer"],
   ["Team name", "[to decide]"],
   ["Problem statement", "A2, DengueRadar: real-time outbreak forecasting [confirm the code and wording; the template's example reads \"A2 - Ageing in place\"]"],
   ["The problem in one sentence", "NEA's public cluster map and alerts show where dengue is now; nothing public shows where risk is heading over the next two weeks, so prevention starts late."],
   ["Who is affected, and how badly", "35,261 dengue cases in 2020, peaking at 1,791 in a single week, and 32,130 in 2022 (MOH weekly bulletin, data.gov.sg), plus [N] active NEA clusters today (read from the live feed)."],
   ["Why it matters now", "Warmer, wetter weather extends the Aedes season [source], and the mosquito's life cycle can be as short as seven days (NEA, to verify), so a two-week warning covers two breeding cycles."]], [2, 6.2])
H2("Slide 2: Solution and data")
T([["Template prompt", "Draft answer"],
   ["Your solution in one sentence", "DengueRadar forecasts dengue risk for every planning area two weeks ahead, and lets a group-chat admin post what is rising, why, and what to do, in one tap."],
   ["Who uses it, and what decision it changes", "Residents, through the community chats their admins already run (a proposed channel), decide what to check at home this week. Admins decide what to post. NEA can compare a ranking of where the first 8 teams should go."],
   ["Datasets (three lines)", "1. NEA Dengue Clusters, daily (data.gov.sg), plus cited 2015 to 2020 cluster archives for training. 2. NEA real-time and historical rainfall, air temperature and humidity (data.gov.sg). 3. MOH weekly dengue bulletin, URA planning-area boundaries, Census 2020, NParks parks (data.gov.sg)."],
   ["What makes it different from a generic dashboard", "NEA's cluster map and myENV alerts describe today. We look ahead: a two-week forecast per area, a ranking of where limited effort goes first, the drivers explained, and a ready-to-post message for the chats residents already use. Four hypotheses tested."]], [2, 6.2])
H2("Slide 3: Databricks architecture and impact")
T([["Template prompt", "Draft answer"],
   ["Pipeline", "data.gov.sg and NEA APIs to Lakeflow Jobs (daily and incremental) to Delta bronze, silver, gold in Unity Catalog to MLflow (baselines against LightGBM, SHAP drivers) to AI/BI map, Genie and a Databricks App. Why a platform: NEA's cluster feed keeps no history, so a scheduled job builds it from 28 Sep, and that history becomes our out-of-time test."],
   ["The output you will demo", "Island map of Low, Medium, High per area, then click an area for the action card and a copy-ready post, plus a 2020 replay."],
   ["Measurable impact if it worked (targets, not claims)", "Capture rate at K = 8 against the last-four-weeks baseline; lead time in weeks on the 2020 replay; alert load at most 15% of areas High; a prospective check against live snapshots (training archives end Nov 2020)."],
   ["What you can realistically finish in two weeks", "The pipeline, the forecast with SHAP, the ranking, the copy-ready post, the Island and Area views and the 2020 replay. Not in scope: sending to real people, agency agreements, effect sizes for actions."]], [2, 6.2])
H2("Claim guardrails")
T([["Say", "Do not say"],
   ["\"NEA's public cluster map and alerts show where dengue is now\"", "\"NEA does not predict\""],
   ["\"Nothing public shows where risk is heading over the next two weeks\" (we found none)", "\"Nobody forecasts by planning area\""],
   ["\"Group chats are a proposed delivery channel\"", "\"Residents are informed through RC chats\" as a fact; the 80% WhatsApp figure"],
   ["Targets for the impact line", "That community messaging reduces dengue, or any unmeasured performance number"]], [4, 4.2])
H2("The one real conversation")
P("One 15-minute talk with a group-chat admin, an RC volunteer or an MCST council member (a relative or neighbour who runs a chat counts). "
  "No names, numbers or contact details are recorded, and permission is asked to quote anonymously. Questions: how often do you post notices and "
  "in which languages; what would you need before posting a dengue warning; would you post it and what would stop you; do official notices "
  "already reach your chat, and have you seen NEA's alerts in myENV; here is a draft, what would you change; may we quote one sentence. "
  "<b>If the conversation does not happen, the slot is left out. A quote is never paraphrased or invented.</b>")
H2("What stays off the three slides")
P("The audience matrix, escalation tables, agency routing and jurisdiction check, data contract, action library, new-versus-persistent flag, "
  "extra languages and the feedback loop. At most one roadmap line: \"next: multilingual posts and an NEA feed\".")

# ---------------------------------------------------------------- 13. plan
H1("13. Plan, open items and next steps")
H2("Team roles")
T([["Person", "Role", "Round 1 responsibilities"],
   ["Braedon", "Team lead, platform and data architect, ML modeller", "Workspace and Free Edition checks, incremental-ingestion check, architecture diagram, lag chart, hypotheses, baselines and metrics, the daily job, action rules"],
   ["Jingyi", "Weather and environment data", "Weather datasets, weekly national rainfall and temperature file, station-to-area map with gaps; owns all data collection from the sprint"],
   ["Ziqi", "Dengue and places data, then demo", "Per-area training panel with coverage table, reconciled 2020 count, post-2022 case sources; then the Island and Area views"],
   ["Komal", "Story and pitch", "Sourced statistics, resident story, mock-ups, slides, PDF and Devpost submission"]], [1, 2.4, 5])
H2("Timeline to submission")
T([["When", "Step", "Who"],
   ["30 Sep to 1 Oct", "Lock the copy; pick the team name; confirm the problem code; burden numbers with sources; read the NEA source pages; Ziqi's panel and coverage table; go/adjust checkpoint on 1 Oct", "Everyone"],
   ["1 to 2 Oct", "Weekly lag chart (needs Jingyi's file); optional baseline capture rate; the real conversation; check the architecture diagram matches the final design (it already shows the group-chat post)", "Braedon, Ziqi, anyone with an admin contact"],
   ["2 Oct", "Make the three visuals; build the slides in the official PPTX and export a PDF", "Komal, Braedon"],
   ["3 Oct", "Mock judging and cold-judge read by someone outside the team; fixes", "Everyone"],
   ["4 Oct", "Final PDF, member details, Devpost submission, confirmation screenshot (team target)", "Komal"],
   ["6 Oct, 11:59pm", "Hard deadline", ""]], [1.4, 5.4, 1.8])
H2("Open items")
T([["Item", "Owner", "Why it matters"],
   ["The real conversation with a group-chat admin", "Anyone with a contact", "Closes the biggest evidence gap; otherwise the slot is removed"],
   ["Read the NEA pages behind B-L-O-C-K, S-A-W, the seven-day life cycle and the alert system", "Komal", "Most links rest on search summaries"],
   ["Confirm the problem code and the file source for the case numbers", "Komal, Ziqi", "The template example says \"A2 - Ageing in place\""],
   ["Run the incremental-ingestion check", "Braedon", "The brief's explicit ask; slide 3 says \"planned\" until it passes"],
   ["Per-area training panel and weekly rainfall file", "Ziqi, Jingyi", "Go/adjust decision on the trained model"],
   ["Team name", "Everyone", "First line of slide 1"],
   ["Re-check the diagram after final decisions (add the weekly export if wanted)", "Braedon", "The older PDFs predate the latest design and sit in docs/archive"]], [4, 1.6, 3])
H2("If we are shortlisted (sprint, 12 to 26 Oct)")
T([["Date", "Milestone"],
   ["9 to 11 Oct", "Turn the idea into a spec and stories with the MoSCoW list as the cut line; agree table designs"],
   ["12 Oct", "Kickoff with the mentor. Ask who would act on a two-week area forecast and what would make the action list credible"],
   ["15 Oct", "Walking skeleton: real data flows load, a baseline forecast and a rough map"],
   ["19 Oct", "All MUST items working; midpoint check; cut what is behind"],
   ["20 to 24 Oct", "SHOULD items: 2020 replay polish, extra features"],
   ["25 Oct", "Feature freeze, code review, record the 30-second backup video"],
   ["27 Oct", "Demo Day"]], [1.4, 7])
P("<b>MUST:</b> daily archive running; incremental weather ingestion; per-area training panel; a trained two-week forecast beating the "
  "persistence and seasonal baselines in MLflow on unseen years; SHAP drivers; the action table; Island and Area views; measured lead time "
  "and hit rate. <b>SHOULD:</b> national MOH forecast as context; the 2020 replay screen; a Genie space; the budgeted ranking and admin kit; "
  "parks and hawker centres if validation keeps them. <b>Sprint-only builds</b> (scheduled after Round 1): the two gold tables, the K and "
  "threshold sliders, the audience selector, the admin kit, the agency records, and the demo fallbacks.")

# ---------------------------------------------------------------- 14. repo
H1("14. The repository")
H2("Where things live")
T([["Path", "What is in it"],
   ["README.md", "Start-here overview and reading order"],
   ["project-context.md", "Challenge brief, dates, our angle, build path, judging criteria"],
   ["DATASETS.md", "Every dataset: source, tier, owner, how to pull it"],
   ["docs/", "Model definitions, action library, data contract, team plan, ML explainer, checkpoint notes; this report; docs/archive/ for superseded PDFs"],
   ["pitch/", "Round 1 outline and slide copy, the official template (PDF and PPTX), architecture diagram source and images"],
   ["analysis/", "Analysis scripts; analysis/data/ is working data and is gitignored (about 69 MB)"],
   ["notebooks/", "Free Edition checks and the daily cluster-snapshot job"],
   ["_bmad-output/", "Brainstorm, forged ideas (history), the pivot, research reports, design thinking, judge-panel memory, with an index"],
   ["github/, .toolkit/", "Reference playbooks (not our code); .toolkit is a subset used by the BMad party-mode configuration"],
   ["_bmad/, .claude/, .agent/, .agents/, .opencode/", "BMad and assistant tooling; do not edit by hand"]], [2.6, 5.6])
H2("What the tidy did (30 Sep)")
B(["Moved the two superseded PDFs (the 28 Sep meeting pack and the earlier concept reference) into docs/archive/; nothing was deleted.",
   "Moved the official template PDF into pitch/ beside the PPTX and fixed the one reference to it.",
   "Removed a regenerable Python cache folder.",
   "Added an index to docs/ and to _bmad-output/, and rewrote the root README so it points to this report first.",
   "Extended .gitignore for OS and notebook clutter.",
   "Checked every relative Markdown link in our own documents: none were broken.",
   "Left github/ and .toolkit/ alone: they overlap, but other documents and the BMad configuration point at them."])
P("Known leftovers: the archived PDFs and the dataset-analysis PDF still use the older framing; the sprint-change proposal is history and "
  "records the pivot; most of the project files are untracked in git and nothing has been committed in this session.", small)

# ---------------------------------------------------------------- appendices
H1("Appendix A: Action library (draft v0.1)")
P("Wording and source links are drafts. NEA links were found by search and the pages could not all be fetched, so Komal must read each one. "
  "Rows saying CONFIRM have no source. No row names a Town Council, RC or MCST.", small)
T([["ID", "Driver tags", "Resident text", "Community checklist", "Days", "Owner (confirm)"],
   ["A01", "H1", "Lift and empty flower-pot plates, overturn pails and wipe rims, change water in vases", "Remind neighbours to do the same on balconies and corridors", "7", "Residents"],
   ["A02", "H1", "Keep roof gutters clear and add BTI insecticide as NEA advises (gully traps not confirmed)", "Check and clear roof gutters and common-area standing water; report blocked public drains", "7", "Residents; NEA (drain cleansing)"],
   ["A03", "H2 cluster nearby", "Apply repellent, wear long sleeves and pants, spray insecticide in dark corners; see a doctor early for fever (not confirmed in sources found)", "Share the repellent and fever reminder with nearby neighbours", "3", "Residents"],
   ["A04", "H2 cluster nearby", "Check your home and corridor for standing water today", "Remind neighbours in the blocks around the cluster", "3", "Community volunteers"],
   ["A05", "H2 neighbour rising", "Do your usual weekly checks and stay alert", "Pre-check known problem spots; watch the neighbouring forecast", "7", "Community volunteers"],
   ["A06", "H3", "Keep up your routine weekly checks", "Scheduled walk-through of spots that had breeding before", "14", "Residents"],
   ["A07", "H3", "(none)", "Walk known recurring spots and note standing water", "14", "Community volunteers"],
   ["A08", "H4", "Use repellent before outdoor meals or exercise; check plant pot plates", "(none)", "7", "Residents"],
   ["A09", "H4", "(none)", "Check drains, bins and stagnant water in nearby parks and eating areas; report to NEA", "7", "NEA; NParks (unconfirmed)"],
   ["A10", "Axis 2: CONSTRUCTION_SITES", "(none)", "Enforcement referral: locality, case size and date go to NEA", "3", "NEA (BCA role not found)"],
   ["A11", "Extra-care flag", "Check on older neighbours and family members", "Check on older neighbours", "7", "Residents"]],
  [0.5, 1.3, 2.9, 2.8, 0.7, 1.5])
H1("Appendix B: Data contract (draft v0.1)")
P("One row per planning area per week. Each authority takes only the fields it needs. This is a proposal: we have no agreement with any agency and "
  "the prototype sends nothing.", small)
T([["Field", "Type", "Meaning"],
   ["contract_version", "string", "Schema version, \"0.1\""],
   ["area_id, area_name", "string", "URA planning area code and name (55 areas)"],
   ["week", "date", "Monday of the forecast week"],
   ["band, band_change, persistence", "enums", "Low, Medium, High; up, same, down, new; new or persistent"],
   ["top_drivers, action_ids", "arrays", "Up to three plain-words drivers; up to three action IDs, deduplicated and ranked"],
   ["rank_cases, rank_rate", "int", "Priority ranks (NEA view only)"],
   ["confidence", "string or null", "Backtest hit rate for the band; null until measured"],
   ["coverage_flag, tag", "enums", "ok or low_data; NEA breeding-source tag or null"],
   ["caveat, valid_until", "string, date", "\"Forecast cluster activity, not a diagnosis. Cluster cases only.\"; end of the forecast window"]], [2.6, 1.4, 4.2])
T([["Consumer", "Fields", "Trigger"],
   ["NEA weekly export", "All fields (CSV or GeoJSON)", "Weekly"],
   ["Enforcement, drain-cleansing and NParks records", "area, week, band, tag, drivers, actions, caveat, valid_until (JSON)", "Only when the trigger fires"],
   ["Admin kit post", "area_name, band, band_change, drivers, actions, caveat, valid_until (text)", "Weekly, only on a band change"]], [2.6, 4, 1.6])
H1("Appendix C: Key sources")
P("Links found or fetched on 30 Sep 2026. Where a source was read only through a search summary it is marked; those need a direct read by Komal.", small)
T([["Source", "Used for", "Read"],
   ["NEA cluster map: nea.gov.sg/dengue-zika/dengue/dengue-clusters", "Current-state map; tiers; updated 1am", "Fetched"],
   ["NEA Dengue Community Alert System: nea.gov.sg/dengue-zika/dengue/dengue-community-alert-system", "myENV and banner alerts; no forecast", "Fetched"],
   ["NEA Stop Dengue Now: nea.gov.sg/dengue-zika/stop-dengue-now", "B-L-O-C-K and S-A-W; seven-day life cycle", "Search summary"],
   ["NEA construction sites: nea.gov.sg/our-services/pest-control/mosquito-control/mosquito-control-in-construction-sites", "NEA enforcement at construction sites", "Search summary"],
   ["PUB drain cleansing and maintenance page", "PUB does structural repairs; NEA DPC cleans drains", "Search summary (fetch returned 403)"],
   ["CDA dengue fever page: cda.gov.sg/professionals/diseases/dengue-fever", "Dengue notifiable within 24 hours; clinical guidance", "Fetched"],
   ["Neighbourhood dengue forecast: BMC Medicine, 6 Aug 2018 (PMC6091171)", "Related research", "Fetched"],
   ["Hotspot forecasting preprint: arXiv 2601.12856 (Jan 2026)", "Planning-area forecast, one week ahead; not peer reviewed", "Fetched"],
   ["HardwareZone / Straits Times, 22 Jul 2025: BTO Telegram groups", "Resident-run chats", "Fetched"],
   ["Singapore WhatsApp forwarding study (PMC8709420)", "Forwarded-message risk", "Fetched"],
   ["Community mobilisation meta-review, 21 Aug 2025 (PMC12501563)", "Weak effect evidence", "Fetch summary"],
   ["NEA and PA volunteer outreach news release, Jul 2022", "Volunteers carry dengue messages", "Search result"],
   ["MOH Weekly Infectious Disease Bulletin (data.gov.sg dataset d_ca168b2cb763640d72c4600a68f9909e)", "Burden numbers (computed)", "Measured from our copy"]], [4.2, 3, 1.6])
H1("Appendix D: Glossary")
T([["Term", "Meaning"],
   ["Cluster", "NEA's grouping of two or more dengue cases with onset within 14 days and within 150 m (tiers: Red 10+ cases, Yellow fewer than 10, Green no new cases, monitored 21 days)"],
   ["Planning area", "One of 55 URA areas; our scoring and display unit"],
   ["Epi week", "Epidemiological week, as used in MOH's weekly bulletin"],
   ["Aedes", "The mosquito genus that spreads dengue"],
   ["B-L-O-C-K, S-A-W", "NEA's home prevention steps and personal protection steps"],
   ["Baseline", "A simple prediction method the model must beat"],
   ["Capture rate at K", "Share of the next fortnight's new cluster cases falling inside our top K areas"],
   ["Prospective test", "Scoring forecasts made now against data that arrives later"],
   ["SHAP", "A method that shows which features drove a prediction"],
   ["Lakeflow, Delta, Unity Catalog, MLflow", "Databricks job scheduling, table storage, governance and lineage, and experiment tracking"],
   ["Bronze, silver, gold", "Raw, cleaned and ready-to-use table layers"],
   ["Admin kit", "Ready-to-post text, an area picker and a valid-until date for a group-chat admin"]], [2.4, 5.8])

doc.build(story)
print("built", OUT)
