# Project context: DAISI Challenge - DengueRadar

## Key dates (2026, Singapore Time)

- 16 Sep: Launch at Data+AI World Tour Singapore; registration opens.
- 24 Sep: Databricks hands-on training, 7-10pm SGT (completed; not recorded; self-paced course available).
- 6 Oct, 11:59pm: Round 1 submission closes on Devpost; submit a one-page concept note or three-slide pitch as PDF.
- 7-9 Oct: Shortlisting. 9 Oct: Top 10 announced and Demo Day details shared.
- 12 Oct: Virtual build kickoff and mentor assignments; 12-26 Oct: mentored build sprint.
- 27 Oct, 4-7pm: Demo Day; top three selected.
- 4 Nov: Finale at the new Databricks Singapore office.

## Overview

The Databricks AI Social Impact (DAISI) Challenge invites student teams from Singapore Institutes of Higher Learning to build data-driven solutions to local social challenges using Databricks and open data from data.gov.sg. Teams choose one problem statement and propose an end-to-end data solution. Ten teams enter a two-week mentored sprint; three are selected at Demo Day.

- Team: 1-4 students from Singapore IHLs. Databricks Free Edition is free for this challenge.
- Round 1 is an idea submission; no working build is required. Submit via Devpost.
- The three-slide template covers: Problem & why it matters; Solution & data; Databricks architecture & impact. Include the chosen problem, solution, datasets, intended architecture, and full member details (name, institution, course, year, email).

## Selected problem: DengueRadar

Real-time dengue outbreak forecasting by Singapore planning area. Dengue is hyperendemic in Singapore; weather shifts may extend Aedes breeding seasons. The proposal is to provide 2-4 week predictive risk intelligence to help communities act earlier than reactive cluster monitoring.

- Build a near-real-time pipeline joining NEA dengue clusters, weather readings, and geospatial data; engineer weather features and forecast risk by planning area.
- Data: NEA Dengue Clusters (GeoJSON polygons and case counts); Dengue Cases by Region (historical sub-region counts); real-time 5-minute station rainfall and island-wide air temperature APIs; historical rainfall collections (2016-2024) for training.
- Target demo: map current cluster intensity; two-week forecast trained on weather and historical cases; explainable Low/Medium/High planning-area risk; compare performance with a recent-history-average baseline.
- Stretch: hawker-centre density or green space as proxies, threshold alerts, and MLflow experiment comparisons.

## Databricks build path

1. Ingest data.gov.sg downloads/APIs and NEA sources into Delta Lake using Auto Loader or notebook ingestion with schema inference.
2. Clean and join raw data into analysis-ready tables; add data-quality checks and lineage documentation.
3. Train and evaluate forecasting models; use MLflow to compare experiments and register the best model.
4. Present actionable results in an interactive map/dashboard using Databricks analytics and app capabilities.
5. Stretch: catalogue data in Unity Catalog, document sources, govern access, and show lineage.

The data.gov.sg datastore API pattern is `https://data.gov.sg/api/action/datastore_search?resource_id=<dataset_id>&limit=100`. Confirm current endpoint and dataset availability before relying on a live demo.

## Free Edition and demo constraints

Free Edition is serverless, quota-limited, and for non-commercial learning/prototyping. Exceeding quotas can make affected compute unavailable for the rest of the day and, in extreme cases, the month. Keep data and workloads small, deploy early, rehearse in the final demo workspace, and prepare a fallback for live steps.

- One serverless SQL warehouse at 2X-Small; up to five concurrent job tasks per account; one active Lakeflow pipeline per supported type.
- Serving endpoints are limited; no GPU serving or provisioned throughput. AI Search has one endpoint/search unit; no Direct Vector Access.
- Up to three Databricks Apps per account; apps may auto-stop after 24 hours. One Lakebase project per account, with scale-to-zero.
- One workspace and metastore; no account APIs, SSO/SCIM, R or Scala, custom workspace storage, online tables, or clean rooms. No commercial-use rights or support SLA.
- Conserve quota: work locally when practical, deploy a small representative slice early, and stop idle notebooks, jobs, pipelines, apps, and endpoints.

## Round 1 judging

- Problem fit & social impact: 30% - clear problem and describable benefit.
- Solution quality & originality: 30% - thoughtful solution, not a generic dashboard.
- Data & technical feasibility: 25% - named open datasets, credible Databricks architecture, feasible in two weeks.
- Clarity of submission: 15% - concise, well-structured concept note or deck.

## Responsible use and references

- Do not upload confidential, personal, or customer data without permission, or any credentials. Review and test AI-generated code and outputs; disclose synthetic/cached data or prototype features and credit datasets, libraries, models, and templates.
- Challenge datasets: [data.gov.sg](https://data.gov.sg/) · [Developer API guide](https://guide.data.gov.sg/developer-guide/api-overview)
- Platform: [Databricks Free Edition](https://www.databricks.com/learn/free-edition) · [Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis) · [AI Dev Kit](https://github.com/databricks-solutions/ai-dev-kit)
- Training: [Get Started with Databricks: End to End](https://www.databricks.com/training/catalog/get-started-with-databricks-end-to-end-6270)
- Submission template: [PowerPoint](https://daisi.online/__l5e/assets-v1/0be60855-02ef-4eef-b359-c1f2a8200177/daisi-round1-3-slide-template.pptx) · [PDF](https://daisi.online/__l5e/assets-v1/142060d8-9903-41bc-9909-916f798030d2/daisi-round1-3-slide-template.pdf)
