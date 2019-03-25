# ShrinkSmart
## Shrink Smart Data Repository

ToDo list:
* Need to expand yelp/etc data to full 99 towns and note where missing.
* Run predictors to derive "smartness" categorization techniques using recursive feature elimination.

### data/childcare
* ChildCare-DB.csv - childcare data from the state of Iowa listen licensed providers with address information
* iowa-childcare-city-totals.csv - Summary of childcare capacity per city from state data.
### data/crime
* CrimeData.csv - national crime index data for cities in Iowa.
### data/evictions
* <CITY>\_<IA>\_evictions.csv - Evictions lab data per city in Iowa.
* all-eviction-data.csv - Evictions lab data by GEOID.
* city-eviction-data.csv - Eviction data after transforming GEOID to city.
* county-eviction-data.csv - Eviction data after transforming GEOID to county.
### data/istp
* Various ISTP data files
### data/lodes
* iowa-job-flow.csv, iowa-job-out.csv - Flow data of people to jobs, with LODES/LEHD data transformed to the city level.
* iowa-work-flow.csv, iowa-job-in.csv - Flow data of jobs to cities, i.e. which cities with jobs have workers arriving from which cities, with LODES/LEHD data transformed to the city level.
* iowa-job-plot.csv - intermediate file.
### data/summaryData
* city-basics\_iowa.csv - Basic info on all incorporated cities in Iowa.
* connection-metrics-services.csv, iowa-business-data.csv - List of all yelp-derived service/buisness connections between cities.
* iowa-childcare.csv - Copy of childcare data.
* iowa-evictions.csv - copy of evictions data.
* iowa-evictions-summary.csv - Condensed and more scalar values for evictions data, with temporal vectors removed.
* new-block-city-mappings.csv - Assignments for census blocks to cities based on proximity assumptions.
### data/trauma
* trauma\_centers.csv - All trauma centers in the state of Iowa, with information on trauma level.
### data/yelp
* <category>-<city>-<IA>.csv - Raw yelp data
### data/twitter
* Currently unused - initial scrapes recorded.
