# Online Retail II - Data Pipeline & EDA

End-to-end data engineering pipeline for the [Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii) dataset from UCI Machine Learning Repository.

## What This Project Does

Takes 1M+ raw e-commerce transactions, cleans them through a structured pipeline, loads into PostgreSQL, and performs exploratory data analysis to extract business insights.

## Architecture

```
CSV (1M rows) → Python/Pandas → PostgreSQL → SQL Queries → EDA Visualizations
```

### Database Schema

```sql
-- PostgreSQL database: data_mastery_db

-- Raw data (untouched)
CREATE TABLE retail_transactions (
    "Invoice"     TEXT,
    "StockCode"   TEXT,
    "Description" TEXT,
    "Quantity"     INTEGER,
    "InvoiceDate"  TIMESTAMP,
    "Price"        FLOAT,
    "Customer ID"  FLOAT,
    "Country"      TEXT
);

-- Cleaned data
CREATE TABLE retail_clean (
    -- same schema + TotalPrice column
    "TotalPrice"   FLOAT
);
```

## Cleaning Pipeline

| Step | Action | Rows Removed | Remaining |
|------|--------|-------------|-----------|
| 0 | Raw data | - | 1,067,371 |
| 1 | Remove cancellations (Invoice starts with 'C') | 19,494 | 1,047,877 |
| 2 | Remove bad quantity/price (<=0) | 6,207 | 1,041,670 |
| 3 | Remove null Customer IDs | 236,121 | 805,549 |
| 4 | Remove exact duplicates | 26,124 | 779,425 |

Total removed: 287,946 rows (27.0%)

## Key Findings

- **Business type:** B2B wholesale retailer (not consumer-facing). Evidence: orders only during business hours (10AM-3PM), no Saturday operations, bulk quantities.
- **Geography:** 92% UK, Ireland/Netherlands/Germany are top international markets.
- **Revenue drivers:** Quantity drives revenue (r=0.83 with TotalPrice), not unit price (r=0.14).
- **Customer behavior:** Median customer places 3 orders. Most buy 1-3 times and leave. Top 2 customers account for ~£1.1M.
- **Seasonality:** November peak (holiday wholesale stocking), revenue growing year-over-year.
- **Data quality:** "Manual" and "POSTAGE" entries in top products are not real products (adjustments/shipping fees).

## How to Run

```bash
# 1. Setup PostgreSQL database
createdb data_mastery_db

# 2. Install dependencies
pip install -r requirements.txt

# 3. Place dataset
# Download online_retail_II.csv from UCI and place in data/

# 4. Run notebooks in order
# retail_pipeline.ipynb  → loads and cleans data
# retail_eda.ipynb       → exploratory analysis
```

## Notebooks

| Notebook | Purpose |
|----------|---------|
| `retail_pipeline.ipynb` | Data ingestion, cleaning, and loading into PostgreSQL |
| `retail_eda.ipynb` | Exploratory data analysis with visualizations |

## Tech Stack

- Python 3.14, Pandas, NumPy
- PostgreSQL 17 + SQLAlchemy + psycopg2
- Matplotlib, Seaborn
