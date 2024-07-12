# Unified Real Estate Data

## Introduction
<p style="text-align: justify;">
A web application that collects updated data from Real Estate Marketplaces(like realtor.com) and provides a scalable and robust data pipeline to ensure data integrity and quality. The web app will provide a UX-friendly solution to study and analyze real estate data for market research to make decisions on top of factual data insights.
</p>
<p style="text-align: justify;">
Unified Real Estate Data solves the hustle of visiting different marketplaces to research real estate products or services. To be honest, doing this research manually is gonna cost you a lot of time and resources. Unified Real Estate Data is your one-stop solution to get hold of the market data and excel in competition.
</p>
<p style="text-align: justify;">
Unified Real Estate Data will assist buyers, sellers, market researchers, and agents to speed up the process of accessing the data and taking action using data insights.</p>
</p>

## Data Pipeline (ELT):
**Extract:** Data will be extracted(scraping, APIs, database, etc) from the real estate data source(like realtor.com)

**Transform/Load:** For optimal storage performance normalize "raw_data" into JSON format and add metadata(extraction timestamp, source, etc). Later dump this semi-structured data into a data lake(Mongo Db).

**Transform:** Data is further transformed into a structured format into a PostgreSQL database instance for persistent storage and querying by web application.

## 🔧Tech Stack:
- **Python:** For building FAST API Backend and requests module.
- **Javascript:** For building React frontend.
- **Databases:** MongoDB (interim database) / PostgreSQL (persistent database)

## Workflow:
1. Collect Raw -> Convert To JSON -> Add Metadata -> Dump JSON to Mongo Db
2. Transform Data -> Cleaned Data -> Clean Format -> Dump to PostgreSQL Db
3. FAST API Query Data From PostgreSQL and return structured data
4. React Web App will render data returning from the API endpoints

![unified-real-estate-data-workflow](https://raw.githubusercontent.com/seemab-yamin/unified-real-estate-data/main/unified-real-estate-data-workflow.png)