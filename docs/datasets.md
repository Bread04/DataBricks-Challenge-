# DengueRadar Datasets Tracking Table

| Dataset | Owner | Link | Format | Date Range | Granularity | Update Frequency | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Historical Rainfall across Singapore** | Jingyi | https://data.gov.sg/collections/2246/view | CSV | 2016 – 2024 | Station level | Historical collection | Annual CSV files; needed for lag chart & baseline training |
| **Historical Surface Air Temperature** | Jingyi | https://data.gov.sg/collections/2246/view | CSV | 2016 – 2024 | Station level | Historical collection | Daily mean/min/max temperature records |
| **Real-time Rainfall API** | Jingyi | https://api-open.data.gov.sg/v2/real-time/api/rainfall | JSON API | Real-time / Daily | Station level | 5-min intervals | Verified endpoint; accepts `?date=YYYY-MM-DD` |
| **Real-time Air Temperature API** | Jingyi | https://api-open.data.gov.sg/v2/real-time/api/air-temperature | JSON API | Real-time / Daily | Station level | 1-min intervals | In °C; accepts `?date=YYYY-MM-DD` |
| **Real-time Relative Humidity API** | Jingyi | https://api-open.data.gov.sg/v2/real-time/api/relative-humidity | JSON API | Real-time / Daily | Station level | 1-min intervals | In %; accepts `?date=YYYY-MM-DD` |
| **Weather Station Locations & Coordinates** | Jingyi | Extracted from API `data.stations` | JSON / CSV | Current | Lat/Long point coordinates | Semi-static | Embedded directly in real-time API station responses |
| **Singapore Public & School Holidays (Stretch)** | Jingyi | https://data.gov.sg/collections/691/view | CSV | 2016 – 2024 | National | Annual | Used for empty-homes feature |
| **NEA Dengue Clusters** | Ziqi | | GeoJSON | | Cluster polygons | Weekly | |
| **Weekly Dengue Case Counts** | Ziqi | | CSV | | National / Regional | Weekly | |
| **Master Plan Planning-Area Boundaries** | Ziqi | | GeoJSON | | Planning area polygons | Static | |
| **Resident Population by Planning Area & Age** | Ziqi | SingStat | CSV | | Planning area | Annual | SingStat census data |
| **Seniors Living Alone by Planning Area** | Ziqi | SingStat | CSV | | Planning area | Annual | If available from SingStat |
