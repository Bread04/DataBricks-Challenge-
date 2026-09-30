# DengueRadar datasets

The single list of every dataset DengueRadar uses: what it is, where to get it, what it feeds, and who owns it. Checked against the data.gov.sg API on 27 Sep 2026. **Re-tiered 28 Sep 2026** after the correct-course pivot to planning-area forecasting for residents and community leaders (see `_bmad-output/planning-artifacts/sprint-change-proposal-2026-09-28.md`): the cited cluster archive is now training data, real-time rainfall is Core, and Census age data is a denominator and an extra-care flag, not the headline.

**Owners.** Round 1: Ziqi handles dengue and places data; Jingyi handles weather and environment data. From the sprint (12 Oct), Jingyi owns all data collection and Ziqi moves to the demo. New Round 1 job for Ziqi: build the weekly per-planning-area training panel from #17 and report coverage. New for Jingyi: map weather stations to planning areas (#18).

**How to get data.gov.sg data.**
- Datastore API (tables): `https://data.gov.sg/api/action/datastore_search?resource_id=<ID>&limit=100` (page with `&offset=`).
- File download (GeoJSON / large CSV): `https://api-open.data.gov.sg/v1/public/api/datasets/<ID>/poll-download` returns a download URL.
- Dataset page: `https://data.gov.sg/datasets/<ID>/view`.
- Send a browser-style `User-Agent` header, and pause 1 to 10 seconds between calls. The API returns HTTP 429 (rate limited) after a few quick calls.

## Summary

| # | Dataset | Agency | Used for | Tier | Owner |
|---|---|---|---|---|---|
| 1 | Weekly Infectious Disease Bulletin Cases | MOH | National model target (weekly dengue cases) | Core | Ziqi |
| 2 | Dengue Clusters | NEA | Local exposure points, block list, root cause | Core | Ziqi |
| 3 | Areas with High Aedes Population | NEA | Local exposure +1 (mosquito hotspots) | Core | Ziqi |
| 4 | Residents by Planning Area / Subzone, Age, Sex (Census 2020) | SingStat | Population per area; 65+ share for the extra-care flag | Should | Ziqi |
| 5 | Master Plan 2019 Subzone Boundary (No Sea) | URA | Scoring unit (332 subzones) | Core | Ziqi |
| 6 | Master Plan 2019 Planning Area Boundary (No Sea) | URA | Island view map | Core | Ziqi |
| 7 | Historical Rainfall across Singapore (2017 to 2024) | NEA | National model: accumulated rain, flushing days | Core | Jingyi |
| 8 | Historical Air Temperature across Singapore | NEA | National model: temperature lags | Core | Jingyi |
| 9 | Historical Relative Humidity across Singapore | NEA | National model: humidity lags (strongest weather predictor in studies) | Core | Jingyi |
| 10 | Realtime Rainfall across Singapore | NEA | Incremental ingestion of live weather (5-minute); current rain feature | Core | Jingyi |
| 11 | NParks Parks and Nature Reserves | NParks | Candidate feature: green-space share; places-where-people-gather actions | Should | Jingyi |
| 12 | Hawker Centres | NEA | Candidate feature and places-where-people-gather actions | Should | Jingyi |
| 13 | Historical Daily Weather Records | NEA | Optional: extend weather back to 2012 (one station) | Should | Jingyi |
| 14 | HDB Property Information | HDB | Block list, block age | Should | Ziqi |
| 15 | HDB Existing Building | HDB | Block locations for the centre view | Should | Ziqi |
| 16 | CHAS Clinics | MOH | "Nearest subsidised test" in the resident action | Should | Ziqi |
| 17 | Archived NEA clusters (SGCharts; Nature Scientific Data 2022) | External, cited | **Training panel** for the per-area forecast, and the 2020 replay test | Core (training) | Ziqi |
| 18 | Weather station locations (from the rainfall, temperature and humidity datasets) | NEA | Map stations to planning areas so weather features attach to each area | Core | Jingyi |

Core = the demo needs it. Should = adds a tested feature. Could = nice to have. Core (training) = trains the offline model; cited; the live product still runs on official feeds.

## Dataset details

### 1. Weekly Infectious Disease Bulletin Cases (MOH)
- **ID:** `d_ca168b2cb763640d72c4600a68f9909e` (CSV, 0.5 MB, datastore API)
- **Coverage:** 2012-W01 to 2022-W52, weekly, national only.
- **Fields:** `epi_week`, `disease`, `no._of_cases`. Filter `disease = "Dengue Fever"` (DHF is a separate row).
- **Checked:** 574 weeks, no duplicates or gaps. Outbreak years 2013, 2014, 2019, 2020 (35,261 cases, peak 1,791 in a week), 2022.
- **Used for:** the target of the national model; the 2020 replay.
- **Gap:** ends Dec 2022. Recent weeks must come from the Communicable Diseases Agency weekly bulletins (format to check).

### 2. Dengue Clusters (NEA)
- **ID:** `d_dbfabf16158d1b0e1c420627c0819168` (GeoJSON, poll-download)
- **Coverage:** today's snapshot only, updated daily. No history.
- **Fields:** `LOCALITY` (street and block numbers), `CASE_SIZE`, `HOMES`, `PUBLIC_PLACES`, `CONSTRUCTION_SITES` (breeding found by NEA), polygon.
- **Checked:** 27 Sep 2026, 11 clusters, 113 cases; only 2 clusters listed breeding sources.
- **Used for:** the live input to the forecast (cluster cases per planning area, spillover to neighbours), home-breeding and root-cause tags for the action table, and the current-clusters layer on the map.
- **Note:** snapshot only. History exists only if we save it daily (depends on the egress test).

### 3. Areas with High Aedes Population (NEA)
- **ID:** `d_5d060d8b7838a15e8906fb22c50dbf51` (GeoJSON, 0.4 MB)
- **Coverage:** republished monthly (last 27 Aug 2026), but the record's description says the areas come from Gravitrap surveys **from April to June 2019**, so the content is about seven years old. 135 zones (83 flat `FL`, 52 condo/landed `CO`), median about 0.09 km2. Checked 28 Sep 2026.
- **Fields:** `DESCRIPTION` (zone code and street list), `NAME` (NEA slogan), `HYPERLINK`, `INC_CRC`, `FMEL_UPD_D`, shape size. No mosquito counts, so Gravitrap counts are not downloadable.
- **Spread:** zones fall in 22 of 55 planning areas (Ang Mo Kio 34, Toa Payoh 13, Serangoon 13, Bukit Batok 12, Hougang 12, Bishan 9). 40 zones straddle two planning areas.
- **Used for:** a candidate static feature (inside a high-Aedes zone). Weak: a 2019 survey. Keep only if it improves validation, and say on the slides that it is a 2019 survey.
- **Local copy:** `analysis/data/nea_high_aedes_areas.geojson`.

### 4. Residents by Planning Area / Subzone of Residence, Age Group and Sex, Census 2020 (SingStat)
- **ID:** `d_d95ae740c0f8961a0b10435836660ce0` (CSV, datastore API, 388 rows)
- **Fields:** `Number` (area or subzone name; planning-area totals end in " - Total"), `Total_Total`, age bands `Total_65_69` to `Total_90andOver`.
- **Checked:** 614,380 residents aged 65+ (15.2%). Highest share: Bukit Merah 22.0%. Most seniors: Bedok 53,370.
- **Used for:** population per planning area (denominator) and the top-third 65+ share that adds an extra-care line to the action plan. No longer multiplies a risk score.
- **Note:** a June 2025 version is on the SingStat website. Seniors living alone was not found by subzone.

### 5. Master Plan 2019 Subzone Boundary, No Sea (URA)
- **ID:** `d_8594ae9ff96d0c708bc2af633048edfb` (GeoJSON, 3.2 MB, 332 subzones)
- **Used for:** mapping cluster points and places to planning areas (the forecast unit is the planning area; subzones are for finer maps and joins).

### 6. Master Plan 2019 Planning Area Boundary, No Sea (URA)
- **ID:** `d_4765db0e87b9c86336792efe8a1f7a66` (GeoJSON, 2.1 MB, 55 areas)
- **Used for:** the forecast unit (55 planning areas; about half are residential) and the island view map.

### 7 to 9. Historical Rainfall / Air Temperature / Relative Humidity across Singapore (NEA)
- **Collections:** rainfall 2279, temperature 2246, humidity 2278. One dataset per year.
- **Rainfall 2017 to 2024 IDs:** `d_1990a5a1aeaf3dd243cf4dae294a61c4` (2017), `d_024fb501ce7092b71bb713eaf54fa7eb` (2018), `d_61995f092320e7155b7528050880b502` (2019), `d_9e7de44094f876f6804b8b5bcee45c81` (2020), `d_3b41598f74f1f11fc3430348fea51af5` (2021), `d_42d64cc6c176ace1c52fbb40b9ede302` (2022), `d_f864cc30d58b467db83659ad17c737bf` (2023), `d_a0b69d3e02576a1fd0ab673e71f83507` (2024).
- **Temperature and humidity IDs:** see collections 2246 and 2278 (listed in the dataset analysis PDF).
- **Fields:** `timestamp`, `station_id`, `station_name`, `location_latitude`, `location_longitude`, `reading_value`.
- **Size:** 5-minute readings, about 1.0 to 1.4 GB per year per variable (about 30 GB total).
- **Used for:** weather features for the national and per-area models: accumulated rain and flushing days (2 to 4 week lags), hot days, temperature and humidity lags (hypothesis H1).
- **Must do:** aggregate to daily per station **before** uploading to Databricks. Never load the raw files (Free Edition quota).

### 10. Realtime Rainfall across Singapore (NEA)
- **ID:** `d_6580738cdd7db79374ed3152159fbd69` (API, by station, from Dec 2016)
- **Used for:** the incremental-ingestion demo the brief asks for (only new readings each run) and the latest rain feature. Pre-aggregate; do not store every 5-minute reading long term.

### 11. NParks Parks and Nature Reserves (NParks)
- **ID:** `d_77d7ec97be83d44f61b85454f844382f` (GeoJSON polygons of parks and nature reserves)
- **Used for:** candidate green-space feature per area, and places-where-people-gather actions. NEA's own risk map uses vegetation as an input.
- **Kept only if** it improves validation.

### 12. Hawker Centres (NEA)
- **ID:** `d_4a086da0a5553be1d89383cd90d07ecd` (GeoJSON, 0.1 MB, current)
- **Used for:** candidate hawker-centre density feature and places-where-people-gather actions (framed as places of exposure, not a cause of dengue).
- **Kept only if** it improves validation.

### 13. Historical Daily Weather Records (NEA)
- **ID:** `d_03bb2eb67ad645d0188342fa74ad7066` (CSV, 0.2 MB)
- **Coverage:** 2009 to Nov 2017, **Admiralty station only**, 105 missing rain days.
- **Used for:** optional test of extending the model back to 2012.

### 14. HDB Property Information (HDB)
- **ID:** `d_17f5382f26140b1fdae0ba2ef6239d2f` (CSV, 1.0 MB)
- **Fields:** `blk_no`, `street`, `year_completed`, `max_floor_lvl`, `residential`, and more.
- **Used for:** matching cluster block numbers to real blocks; median block age per area (hypothesis H3).
- **Checked (28 Sep, Ziqi):** 13,357 rows, 24 columns; `year_completed` 1937 to 2026; 10,796 blocks flagged residential. Local copy: `analysis/data/hdb_property_information.csv`.
- **Gap:** no postal code or coordinates in this table. Join to #15 on `blk_no` plus street (#15 has `ST_COD`, a street code, not the street name, so the join key still needs checking).

### 15. HDB Existing Building (HDB)
- **ID:** `d_16b157c52ed637edd6ba1232e026258d` (GeoJSON, 57 MB)
- **Used for:** optional block-level detail in the Area view (which blocks are near a cluster). Not required for the planning-area forecast.
- **Checked (28 Sep, Ziqi):** 13,436 building polygons; fields `BLK_NO`, `ST_COD`, `POSTAL_COD`, `ENTITYID`. Local copy: `analysis/data/hdb_existing_building.geojson` (gitignored). Aggregate to block centroids before uploading to Databricks; do not load the 57 MB file as is.

### 16. CHAS Clinics (MOH)
- **ID:** `d_548c33ea2d99e29ec63a7cc9edcccedc` (GeoJSON, 1.6 MB, 1,193 clinics)
- **Used for:** "nearest subsidised test" in the resident action (see a doctor early for fever).
- **Checked (28 Sep, Ziqi):** 1,193 features; properties are only `Name` and `Description` (an HTML blob with address and phone), so address and postal code must be parsed out of `Description`. Local copy: `analysis/data/chas_clinics.geojson`.

### 16b. Active Ageing Centre locations: no longer needed
- Not openly available (AIC's "Find an AAC" map has no download or API; data.gov.sg only has yearly counts, `d_0f70d7095a527be4ea443a7e30597896`).
- **Status after the 28 Sep pivot:** the product no longer depends on a centre list. Its users are residents and community leaders (town councils, RCs, condo MCSTs), reached at planning-area level. Kept here only as a record of the search.

### 17. Archived NEA cluster data (external, must be cited; training data)
- **SGCharts Outbreak archive:** outbreak.sgcharts.com/data (zip: outbreak.sgcharts.com/sgcharts.zip). Inspected 28 Sep 2026.
  - Clean CSVs: 256 snapshots, 3 Jul 2015 to 6 Nov 2020, 56,976 rows, all coordinates inside Singapore. No header row. Columns: cases, address, lat, lon, cluster_no, recent_cases, total_cases, date, month.
  - Older files (23 May 2013 to 17 Apr 2015, 91 snapshots): SGCharts flags the lat/lon as wrong, so they need geocoding. Skip for the replay.
  - Gap: 2020 is dense Jan to May but only one snapshot a month from June, so it barely covers the July surge. Use the Nature data for that.
  - Licence: free to use; attribute NEA (nea.gov.sg/dengue-zika/dengue/dengue-clusters) and link back to SG Outbreak.
- **Nature Scientific Data (2022):** "Geographical clusters of dengue outbreak in Singapore during the Covid-19 nationwide lockdown of 2020" (doi 10.1038/s41597-022-01666-y). Data on Figshare (doi 10.6084/m9.figshare.12814733), CC BY 4.0.
  - Version 1 file has 15,638 rows, 20 weekly snapshots, 28 Feb to 9 Jul 2020; the paper reports 16,116 rows (version 2, not downloadable via the API).
  - Columns include `subzone id` (213 subzones, IDs 1 to 322). **Mapping to URA subzones done (28 Sep, Ziqi):** `analysis/data/nature_subzone_id_map.csv`. Each Nature ID was matched to the URA subzone that contains most of its case points. All 213 IDs map to 213 different subzones, and every ID has at least 92% of its points inside its matched subzone (nearly all 100%). Only cases inside clusters; sporadic cases are missing.
  - Do not sum `recent case number` across rows: it looks cluster-level, repeated per location.
- **Local copies:** `analysis/data/sgcharts_raw/`, `analysis/data/nature_dengue_singapore_2020.csv`.
- **Used for:** (1) the weekly per-planning-area **training panel** for the forecast model (targets and lag features), and (2) the 2020 replay test. It does not feed the live product, which runs on official feeds.
- **Target caveat:** holds only cases inside NEA clusters, so the model predicts cluster activity, not total dengue cases. 2020 is dense to May, then monthly only; Nature fills the surge (Feb to Jul).
- **Rule:** DAISI allows additional public datasets if cited (daisi.online). Cite on the slides and in the repo.

### 18. Weather station locations (NEA)
- **Source:** the station id, name, latitude and longitude fields already in the rainfall, temperature and humidity datasets (#7 to 9) and the real-time APIs (#10).
- **Used for:** attaching each station's readings to a planning area (nearest station, or a Voronoi split) so every area has its own weather features. Owner: Jingyi.
- **Check:** how many stations sit near each planning area; note areas with no nearby station.

## Not used, and why

| Dataset | ID | Reason |
|---|---|---|
| Weekly Number of Dengue and DHF Cases (MOH) | `d_ac1eecf0886ff0bceefbc51556247015` | 2014 to 2018 only; covered by #1 |
| Dengue (Cases) by region (NEA) | e.g. `d_5f90123ce50e3d323bfd0ff3c9a84601` | Stale 2023 to 2024 snapshots; several IDs return 404 |
| Dengue Outbreak Statistics (NEA) | `d_8763ae810003718ad638e719ec9118df` | Yearly rate 2007 to 2015; slide context only |
| Eldercare Services (MOH) | `d_f0fd1b3643ed8bd34bd403dedd7c1533` | Last updated 2016; find a current Active Ageing Centre list instead |
| HDB Elderly Resident Population by town (HDB survey) | `d_4180067b350bc9839a4cea487841d5d1` | 2003 to 2018 survey; Census 2020 (#4) is better |
| Seniors living alone by area | not available | National figure only (88,400); the extra-care flag uses 65+ share instead |

## Before relying on any dataset
- [ ] Re-check each ID resolves (some data.gov.sg IDs have been retired).
- [ ] Test data.gov.sg access from a Free Edition notebook (egress may be blocked).
- [ ] Aggregate weather to daily before upload.
- [ ] Cite every dataset and the archive on the slides and in the repo.

Related: `_bmad-output/dataset-analysis/DengueRadar_Dataset_Analysis.pdf` (charts and profiling), `_bmad-output/planning-artifacts/research/technical-dengueradar-feasibility-2026-09-28/research.md` (feasibility).
