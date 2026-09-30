# Round 1 outline: three slides (DRAFT, 30 Sep 2026)

For Komal. Round 1 is **slides only**: a three-slide PDF answering the DAISI template prompts (`docs/team-plan.md`, "Round 1 slide draft", has the prompt-by-prompt answers). Nothing here needs a working build. Rules from the hackathon guide (`github/01-hackathon-playbook/docs/pitch-and-demo.md`, `github/08-datathon-handbook/01-playbook/`): one idea per slide, large visuals, at most 4 bullets, no walls of text.

**Rule for every number:** only a number we have measured or can cite, with the source. Anything else is written as a target ("we will measure...").

## Fitting the official template

The template (`pitch/daisi-round1-3-slide-template.pdf`, editable copy `pitch/daisi-round1-3-slide-template.pptx`) is a fixed list of prompts, one short line each, with the right half of every slide empty. So: **answer every prompt in one or two lines, keep the prompt labels as they are, and put one visual in the right half.** Long answers will overflow.

| Slide | Prompts to answer (template wording) | Visual for the free right half |
|---|---|---|
| 1 | Team name · Problem statement · The problem in one sentence · Who is affected, and how badly (a number from open data) · Why it matters now | One large burden-number callout |
| 2 | Your solution in one sentence · Who uses it, and what decision it changes · Datasets (exactly three numbered lines) · What makes your approach different from a generic dashboard | The mock post as a phone screen |
| 3 | Pipeline (name the Databricks components) · The user-facing output you will demo · Measurable impact if it worked · What you can realistically finish in the two-week sprint | The architecture diagram |

Template gotchas: the slide 1 example reads "A2 — Ageing in place", so **confirm our problem code and wording against the organiser's brief** rather than copying the example. Slide 2 allows three datasets, so group them. There is no member-details field on the slides; check whether those go on Devpost or in a slide footer.

### Copy fitted to the prompts (v1; brackets and VERIFY need a source before submission)

**Slide 1**
- Team name: [to decide]
- Problem statement: A2 · DengueRadar: real-time outbreak forecasting [VERIFY code and wording]
- The problem in one sentence: NEA's public cluster map and alerts show where dengue is now; nothing public shows where risk is heading over the next two weeks, so prevention starts late.
- Who is affected, and how badly: 35,261 dengue cases in 2020, peaking at 1,791 in a single week, and 32,130 in 2022 (MOH weekly bulletin, data.gov.sg; computed 30 Sep, Komal to cite), plus [N] active NEA clusters today (read from the live feed on the day).
- Why it matters now: Warmer, wetter weather extends the Aedes season [VERIFY source], and the mosquito's life cycle can be as short as seven days (NEA, VERIFY), so a two-week warning covers two breeding cycles.

**Slide 2**
- Your solution in one sentence: DengueRadar forecasts dengue risk for every planning area two weeks ahead, and lets a group-chat admin post what is rising, why, and what to do, in one tap.
- Who uses it, and what decision it changes: Residents, through the community chats their admins already run (a proposed channel), decide what to check at home this week. Admins decide what to post. NEA can compare a ranking of where the first 8 teams should go.
- Datasets:
  1. NEA Dengue Clusters, daily (data.gov.sg), plus cited 2015 to 2020 cluster archives for training (SG Outbreak; Nature Scientific Data 2022)
  2. NEA real-time and historical rainfall, air temperature and humidity (data.gov.sg)
  3. MOH weekly dengue bulletin, URA planning-area boundaries, Census 2020, NParks parks (data.gov.sg)
- What makes it different: NEA's cluster map and myENV alerts describe today. We look ahead: a two-week forecast per area, a ranking of where limited effort goes first, the drivers explained, and a ready-to-post message for the chats residents already use. Four hypotheses tested (weather lag, spatial spillover, recurrence, green space).

**Slide 3**
- Pipeline: data.gov.sg and NEA APIs → Lakeflow Jobs (daily and incremental) → Delta bronze, silver, gold in Unity Catalog → MLflow (baselines vs LightGBM, SHAP drivers) → AI/BI map, Genie and a Databricks App. **Why a platform:** NEA's cluster feed keeps no history, so a scheduled Lakeflow job builds it into Delta from 28 Sep, and that same history becomes our out-of-time test.
- The user-facing output you will demo: Island map of Low, Medium, High per area → click an area → action card and a copy-ready post, plus a 2020 replay.
- Measurable impact if it worked (targets we will measure): capture rate at K = 8 against the last-4-weeks baseline; lead time in weeks on the 2020 replay; alert load at most 15% of areas High; and a prospective check of our forecasts against the live snapshots collected since 28 Sep (training archives end Nov 2020).
- What you can realistically finish in two weeks: the pipeline, the forecast with SHAP, the ranking, the copy-ready post, the Island and Area views and the 2020 replay. Not in scope: sending to real people, agency agreements, effect sizes for actions.

## Two pieces of evidence for the slides (answers the panel's objections 1 and 2)

### 1. One measured number (done)

Computed 30 Sep by summing `analysis/data/weekly_dengue_ziqi.csv` (MOH Weekly Infectious Disease Bulletin, dataset #1 in `DATASETS.md`):

| Year | Cases | Note |
|---|---|---|
| 2017 | 2,759 | lowest recent year |
| 2019 | 15,910 | |
| **2020** | **35,261** | 53 epi weeks in the file; **peak week 2020-W30 with 1,791 cases** |
| 2021 | 5,251 | |
| **2022** | **32,130** | peak week 2022-W21 with 1,563 cases |

This settles the earlier conflict: **35,261 is right** (matches `DATASETS.md`); the 35,012 in the older checkpoint doc is not supported by the file. Komal still confirms the source and cites it.

**Slide 1 callout (hero number):** "35,261 dengue cases in 2020, peaking at 1,791 in a single week." Supporting line: "32,130 in 2022, against 5,251 the year before."

Also measurable and true by 4 Oct: the number of days of live cluster snapshots collected by the daily job. Read `days_of_history` from `bronze_snapshot_runs` (status ok or empty) on the day; do not estimate, and do not count from the snapshots table (a quiet day writes no snapshot rows).

*Optional, only if Ziqi's per-area panel is ready by 2 Oct:* the status-quo baseline's capture rate at K = 8 from the 2015 to 2020 archive.

### 2. One real conversation (NOT done yet; only a person can do this)

Talk to one RC volunteer, MCST council member or group-chat admin (a relative or neighbour who runs a block or estate chat counts). 15 minutes. Do not record names, numbers or contact details; ask permission to quote anonymously.

1. Do you post health or safety notices in your chat? How often, and in which languages?
2. If a dengue warning for your area reached you, what would you need before posting it (source, wording, length, a date)?
3. Would you post it? What would stop you?
4. Do official notices (from the RC, MP, NEA or your town) already reach your chat, and in which languages? Have you seen NEA's dengue alerts in myENV?
5. Here is a draft post (show the mock). What would you change?
6. May we quote one sentence, anonymously?

**Interview kit (from the 30 Sep design thinking session, `_bmad-output/design-thinking-2026-09-30.md`).** Print or screenshot these. All wording is a draft; the B-L-O-C-K and S-A-W steps still need Komal's check against NEA's pages, and any NEA link goes in only once verified. The posts are illustrative, not a real forecast.

*Variant A (full)*
```
DENGUE FORECAST · [Area] · week of 6 Oct
Next 2 weeks: higher than usual (level HIGH, up from Medium)
Why: heavy rain 2 to 4 weeks ago, now warm; cases rising nearby.
This week:
1. Lift and empty flowerpot plates, overturn pails and wipe rims, change vase water
2. Keep roof gutters clear
3. Use repellent, wear long sleeves and pants
Valid until 19 Oct. Forecast by DengueRadar, a student project using NEA data. Not a diagnosis. Your estate may span another area.
```

*Variant B (short)*
```
[Area]: dengue risk higher than usual for the next 2 weeks.
This week: empty flowerpot plates and pails, keep gutters clear, use repellent.
Valid until 19 Oct. Source: NEA data, DengueRadar (student project).
```

*Answer card (for the admin's replies)*
- "Is this official?" → "No. It's a student forecast built on NEA's public data. NEA's own cluster map has the official picture."
- "What do I do?" → "The three steps in the post: empty containers, keep gutters clear, use repellent."
- "Should I worry?" → "It's a forecast of higher activity nearby, not a report that anyone is ill."

*Extra tasks for the conversation*
1. Admin: read Variant A, then B. Which would you post, and what would you change?
2. Admin: a neighbour replies "is this official?". What do you say? (then show the answer card)
3. Optional, two or three recipients (family or friends, including one older person): read each variant for ten seconds, then say in your own words what it tells you and what you would do.
4. Note the **assumptions**: will an admin post an unofficial forecast if the source is clear; is "student project using NEA data" acceptable; do people understand "higher than usual"; would weekly posting be too much; does the estate map to one area.
5. Capture answers in four boxes (Likes, Questions, Ideas, Changes). No names or contact details.

**Decision rules once results are in:** an admin who refuses an unofficial source means the slide should say endorsement is on the roadmap; misread wording gets changed before it reaches a slide; an estate spanning several areas keeps the multi-area picker in the design; "weekly is too often" means we post only on a change and drop the weekly claim; an admin who would post it as is gives us the one-sentence quote for slide 2. Choose Variant A or B for the slide 2 mock from their reaction.

**Slide use:** one line on slide 2, "Field check: 'quote' (group-chat admin, [date])", plus any wording change the person asked for, applied to the mock post. **If the conversation does not happen, leave the line out.** Never write a paraphrase as a quote, and never imply a conversation took place.

## The one sentence (guide template: `<Product> lets <person> <do thing> in <time>`)

> **DengueRadar lets a group-chat admin post a two-week dengue warning for their planning area in one tap: what is rising, why, and what to do.**

## Slide 1: Problem and why it matters

- **Hook:** NEA's public cluster dashboard shows clusters after people are already sick. Say "public cluster dashboard", never "NEA does not predict".
- **Number:** "35,261 dengue cases in 2020, peaking at 1,791 in one week" (measured, see the evidence section) and today's live cluster count.
- **Why a two-week warning:** NEA says the Aedes life cycle can be as short as seven days (source: https://www.nea.gov.sg/dengue-zika/stop-dengue-now; VERIFY by reading the page), so two weeks spans two breeding cycles.
- **Resident story** in three sentences (Komal): a family in a block that becomes a cluster two weeks later, and what an early message would have let them do.
- **Visual:** the burden number as one large callout.

## Slide 2: Solution and data

- **Hero visual: the mock post** (below), shown as a phone screen. This is the memorable image.
- **Line under it:** "Same forecast, three decisions: residents, volunteers who post it, and NEA to compare with its own forecast."
- **Decision, not just a forecast:** a budgeted ranking, "where do the first 8 teams go?", in two lists (most cases, highest risk per resident).
- **Delivery (a proposed channel):** the admin of a community group chat copies the post into WhatsApp or Telegram. No app to install, no bot. It complements NEA's myENV alerts, which describe current conditions.
- **Hypothesis strip (one line):** "We test four hypotheses: weather lag, spatial spillover, recurrence, green space. Early monthly data supports temperature lag and not rain alone (VERIFY with the weekly chart before use)."
- **Field check (only if the conversation happens):** one anonymised line from a group-chat admin, with the date.
- **Datasets:** as in the team-plan draft (named, with source and date range).
- **Do not put on this slide:** the lens matrix, escalation table, agency table, action library, data contract.

### Mock post (ILLUSTRATIVE layout; not a real forecast; label it on the slide)

```
DENGUE FORECAST: [Area]   Week of 6 Oct
Next 2 weeks: higher than usual (level HIGH, up from Medium)
Why: heavy rain 2 to 4 weeks ago, now warm; cases rising in a neighbouring area.
This week:
1. Lift and empty flowerpot plates, overturn pails and wipe rims, change water in vases
2. Keep roof gutters clear
3. Use repellent, wear long sleeves and pants
Valid until 19 Oct. A forecast, not a diagnosis. Your estate may span a different boundary.
Based on NEA cluster and weather data.
```

The three actions use NEA's B-L-O-C-K and S-A-W wording (`docs/action-library.md`, links found by search and still to be read by Komal). CONFIRM before the slide is final.

## Slide 3: Databricks architecture and impact

- **Sponsor tech, one job each (max 4 bullets):**
  - Lakeflow Jobs: daily NEA cluster snapshots (running since 28 Sep; the public feed keeps no history, so this job builds it) and incremental weather loading (planned; the Structured Streaming and Auto Loader check has not run yet).
  - Delta bronze, silver, gold, governed in Unity Catalog with lineage.
  - MLflow: baselines and LightGBM compared, best model registered, SHAP drivers.
  - AI/BI map, Genie and a Databricks App for the Island and Area views.
- **Visual:** `pitch/assets/architecture.png` (needs the admin-kit and export outputs added by Braedon).
- **Impact, stated as targets we will measure (nothing claimed):**
  - **Capture rate at K = 8:** share of the next fortnight's new cluster cases inside the 8 areas we rank highest, against the last-4-weeks baseline.
  - **Lead time** in weeks from the 2020 replay.
  - **Alert load** at most 15% of areas High.
  - *Optional, only if Ziqi's per-area panel is ready by 2 Oct:* one measured number for the status-quo baseline, "the 8 areas with the most cases last month covered X% of the next fortnight's cases". Label it "baseline, measured on the 2015 to 2020 archive".
- **Known data gap, stated openly:** training cluster archives end in Nov 2020 and the live feed starts in Sep 2026. We test on the live snapshots as they accumulate and report that check honestly.
- **What we won't claim:** cluster cases only, not total cases; a forecast, not a diagnosis; no effect sizes for actions; nothing is sent to anyone in the prototype.
- **Two weeks if shortlisted:** end-to-end pipeline, forecast with SHAP, the budgeted ranking, the admin kit with copy buttons, the Island and Area views, and the 2020 replay.

## Claim guardrails (from Deep Recon, 30 Sep; reports in `_bmad-output/planning-artifacts/research/`)

Say:
- "NEA's public cluster map and alerts show where dengue is now" (NEA's map is current-state with no forecast; its Dengue Community Alert System pushes current-state alerts through the myENV app).
- "Nothing public shows where risk is heading over the next two weeks" (search-limited; say "we found none").
- "Group chats are a proposed delivery channel."

Do not say:
- "NEA does not predict" (NEA's institute appears to run internal national forecasts).
- "Nobody forecasts by planning area" (a 2026 arXiv preprint forecasts hotspots for the 55 planning areas one week ahead; a 2018 BMC Medicine paper forecast 1 km grids up to 12 weeks ahead).
- "Residents are informed through RC and constituency chats" as a fact (no source found; it is our observed practice, so the field check matters).
- The 80% WhatsApp figure (aggregator, conflicting numbers). Say "widely used".
- That community messaging reduces dengue (a 2025 meta-review of 15 systematic reviews calls the evidence weak and mostly about mosquito counts). Promise a delivery mechanism, not a behaviour change.

If space allows on slide 2, add one related-work line: "Research already forecasts planning-area dengue hotspots one week ahead (arXiv, 2026); we add a two-week horizon, a ranking, and delivery."

## Cut list (keep off the three slides)

Lens matrix, escalation ladder, agency routing table and jurisdiction check, data contract, action library, new-vs-persistent flag, extra languages, feedback loop. Mention at most one roadmap line: "next: multilingual posts and an NEA feed".

## Before submission (owners in `docs/team-plan.md`)

- [ ] Burden numbers with sources, and the resident story (Komal)
- [ ] Mock post drawn in Canva as a phone screen (Komal)
- [ ] Weekly lag chart confirms or drops the "rain alone is not the signal" line (Braedon)
- [ ] Every named agency and every action wording checked against the source pages (Komal)
- [ ] Member details, template, PDF, Devpost confirmation (Komal, 4 Oct)
- [ ] Cold-judge check: someone outside the team reads the three slides once and explains the idea back
