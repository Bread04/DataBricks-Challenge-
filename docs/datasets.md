# DengueRadar Datasets Tracking Table

| Dataset | Owner | Link | Format | Date Range | Granularity | Update Frequency | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Historical Rainfall across Singapore** | Jingyi | https://data.gov.sg/datasets/d_8e4fa646ee1855a15998aabfccbb5927/view | CSV | Dec 2016 – 2024 | Station level | Historical collection | 9 annual CSV files; needed for lag chart & baseline training |
| **Historical Surface Air Temperature** | Jingyi | https://data.gov.sg/ | CSV | 2016 – 2024 | Station level | Historical collection | Daily min/max/mean temperatures across Singapore |
| **Real-time Rainfall API** | Jingyi | https://api-open.data.gov.sg/v2/real-time/api/rainfall | JSON API | Real-time / Daily | Station level | 5-min intervals | Verified via OpenAPI v1.0.11; accepts `?date=YYYY-MM-DD` |
| **Real-time Air Temperature API** | Jingyi | https://api-open.data.gov.sg/v2/real-time/api/air-temperature | JSON API | Real-time / Daily | Station level | 1-min intervals | Unit in °C; accepts `?date=YYYY-MM-DD` |
| **Real-time Relative Humidity API** | Jingyi | https://api-open.data.gov.sg/v2/real-time/api/relative-humidity | JSON API | Real-time / Daily | Station level | 1-min intervals | Unit in %; accepts `?date=YYYY-MM-DD` |
| **Weather Station Locations & Coordinates** | Jingyi | Extracted from `data.stations` in Real-time APIs | CSV / GeoJSON | Current | Lat/Long point coordinates | Semi-static | Used to map weather stations to URA planning areas |
| **NEA Dengue Clusters** | Ziqi | | GeoJSON | | Cluster polygons | Weekly | |
| **Weekly Dengue Case Counts** | Ziqi | | CSV | | National / Regional | Weekly | |
| **Master Plan Planning-Area Boundaries** | Ziqi | | GeoJSON | | Planning area polygons | Static | |
| **Resident Population by Planning Area & Age** | Ziqi | SingStat | CSV | | Planning area | Annual | SingStat census data |
| **Seniors Living Alone by Planning Area** | Ziqi | SingStat | CSV | | Planning area | Annual | If available from SingStat |
