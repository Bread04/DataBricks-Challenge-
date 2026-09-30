# Digest: D1 platform + D3 implementation, round 1, assistant 1

Note: docs.databricks.com reset connections; official docs read via the Microsoft Learn mirror (same MicrosoftDocs/databricks-pr source, ms.date 2026-09-11). AWS/GCP copies of the Free Edition limitations page exist but were not fetched.

## D1 findings
- Free Edition is serverless-only and quota-limited; it replaced the legacy Community Edition (retired 2025); students/hobbyists, no commercial use. | https://learn.microsoft.com/en-us/azure/databricks/getting-started/free-edition | Databricks/Microsoft Learn | 2026-09-11 | accessed 2026-09-28 | high | feature
- Exceeding quota shuts down compute "for the rest of the day (and in extreme cases, the rest of the month)"; data/settings kept. Quota numbers not published ("fair usage policy"). | https://learn.microsoft.com/en-us/azure/databricks/getting-started/free-edition-limitations | Databricks/Microsoft Learn | 2026-09-11 | 2026-09-28 | high | limit
- Serverless only; no custom compute; notebook serverless "limited compute size and usage"; one SQL warehouse, 2X-Small. | same | 2026-09-11 | high | limit
- Jobs: max 5 concurrent job tasks per account. | same | 2026-09-11 | high | limit
- Lakeflow pipelines: one active pipeline per pipeline type. | same | 2026-09-11 | high | limit
- Databricks Apps: max 3 per account; auto-stop after 24 hours from start/update/redeploy; manual restart. | same | 2026-09-11 | high | limit
- Model Serving: limited active endpoints; no GPU serving, no provisioned throughput, no custom GPU models, no batch inference; some models unavailable. | same | 2026-09-11 | high | limit
- One AI Search endpoint; one Lakebase project with scale-to-zero. | same | 2026-09-11 | high | limit
- Not supported: R/Scala, custom storage locations, online tables, clean rooms, legacy features, Knowledge Assistant; one workspace/metastore; no account console; no SLA; inactive accounts may be deleted. | same | 2026-09-11 | high | limit
- Outbound internet "restricted to a limited set of trusted domains". LinkedIn identity verification unlocks "outbound internet access" and limited serverless GPU compute. | same | 2026-09-11 | high | limit
- No published allowlist; pypi.org works, wikipedia.org blocked; staff: list not public, may vary by region. | https://community.databricks.com/t5/databricks-free-edition-help/whitelist-for-outbound-network-access/td-p/146591 | Databricks Community (staff) | 2026-02-02 | 2026-09-28 | high | limit
- requests.get to google.com failed (name resolution); intentional anti-abuse; pre-dates LinkedIn option. | https://community.databricks.com/t5/data-engineering/free-edition-outbound-internet-suddenly-blocked-error/td-p/121832 | Databricks Community | 2025-06/09 | 2026-09-28 | medium | limit
- Notebook-scoped %pip from PyPI works; wheels from UC volume; no cluster-scoped libraries. | https://community.databricks.com/t5/databricks-free-edition-help/is-it-possible-to-install-python-libraries-or-any-python-wheels/td-p/125594 | Databricks Community (non-staff) | 2025-07-17 | 2026-09-28 | medium | feature
- Serverless limits: Spark Connect only (no RDD); cache/persist/checkpoint error; UDFs no internet, 1 GB memory; notebook libraries not cached across sessions; job notebook tasks install libs in-notebook; no Spark UI. | https://learn.microsoft.com/en-us/azure/databricks/compute/serverless/limitations | Databricks/Microsoft Learn | 2026-09-11 | 2026-09-28 | high | limit
- Marketing lists notebooks, Assistant, Genie, ETL pipelines, dashboards, classical ML, LLM agents, scheduled runs; no specifics on MLflow/registry/lineage. | https://www.databricks.com/learn/free-edition | Databricks | undated | 2026-09-28 | medium | feature
- Signup page: Unity Catalog included, plus Genie, Lakeflow, Lakebase. | free-edition docs URL | 2026-09-11 | medium | feature

## D3 findings
- Spatial SQL (GEOMETRY + 90+ ST_ functions) GA; GEOGRAPHY Public Preview; AI/BI Maps added; announced 2026-06-11; Free Edition not mentioned. | https://www.databricks.com/blog/geospatial-unbounded-spatial-sql-ga-aibi-maps-delta-sharing-and-iceberg-v3 | Databricks Blog | 2026-06-11 | 2026-09-28 | high | version
- ST functions in Databricks SQL and DBR 17.1+: st_contains, st_buffer, st_intersects, st_within, st_dwithin, st_distancesphere, st_transform, st_union_agg. | https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/sql-ref-st-geospatial-functions | Databricks/Microsoft Learn | 2026-09-11 | 2026-09-28 | high | feature
- H3 functions built in; DBR 17.0+ supported on all compute except classic SQL warehouses (serverless should work; Free Edition unconfirmed). | https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/sql-ref-h3-geospatial-functions | Databricks/Microsoft Learn | 2026-09-11 | 2026-09-28 | high/medium | feature
- UI upload limit 5 GB per file; larger via SDK, CLI, Files REST API, PUT INTO; notebook download from internet depends on egress. | https://learn.microsoft.com/en-us/azure/databricks/volumes/volume-files | Databricks/Microsoft Learn | 2026-09-15 | 2026-09-28 | high | limit
- Inference (assistant): without LinkedIn verification, upload via CLI/SDK or pre-aggregate to Parquet; also hedges unpublished quotas. | inference | medium | limit

## Leads
- Test data.gov.sg reachability from a notebook in hour one; LinkedIn verification scope.
- Serverless environment dependency pinning page; download-internet-files page; AI/BI Maps on Free Edition; GitHub LuisMay12/pmlcast#3; MLflow/UC lineage in Free Edition UI.

## Not found
- Numeric daily quotas/storage caps; explicit per-feature confirmation for MLflow, registry, lineage, AI/BI, FM APIs; ST/H3 on Free Edition specifically; domain allowlist.
