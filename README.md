# UP Dataset Catalog

## Project Overview

The goal of this project is to build a pipeline that collects 
metadata about Uttar Pradesh government datasets from India's 
Open Government Data platform (data.gov.in), cleans and 
structures the data, and surfaces useful insights for the 
State Data Authority (SDA).

## My Approach

I chose to use the CKAN-compatible API provided by data.gov.in 
as my primary data collection method, since it directly returns 
structured metadata in JSON format without needing to parse HTML.

## Data Collection

I attempted to fetch data using the following API endpoint:

https://data.gov.in/api/3/action/package_search?q=uttar+pradesh&rows=50&start=0

Unfortunately, the API consistently returned 504 Gateway Timeout 
and 404 errors throughout my development window. I also attempted 
web scraping as a fallback using requests and BeautifulSoup, 
but the catalog pages on data.gov.in use JavaScript-based dynamic 
loading, which means the dataset content does not appear in the 
raw HTML response.

## What I Built

- collect_data.py: Handles API requests with pagination and error 
  logging. Falls back to scraping when API fails.
- consolidate_data.py: Reads raw JSON files, extracts required 
  fields, standardises column names, handles missing values, 
  removes duplicates, and saves a clean CSV.
- analyse.py: Loads the processed CSV and generates visualisations 
  for top titles, organisation coverage, and data freshness.

## Challenges

The main blocker was data.gov.in server availability. The API 
was returning errors consistently and the website relies on 
JavaScript rendering which blocked BeautifulSoup scraping. 
Given the deadline, I have submitted the full pipeline code 
with the logic intact. The scripts will work correctly once 
the API becomes accessible.

## Tech Stack

- Python 3
- requests
- pandas
- matplotlib
- beautifulsoup4

## How to Run

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run data collection:
   python src/collect_data.py
4. Run consolidation:
   python src/consolidate_data.py
5. Run analysis:
   python src/analyse.py