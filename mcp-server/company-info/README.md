# Company Info MCP Server

Small MCP server that exposes two tools backed by a CSV of US companies.

## Data source
The data is taken from the [Open Data 500 Companies](https://www.kaggle.com/datasets/govlab/open-data-500-companies) dataset (original copy kept in `us_companies.csv`).

## Tools
- `get_company_location(company_name: str)` — returns a short location string for a company.
- `get_company_details(company_name: str)` — returns a few fields (year founded, location, category, business model).

## Quickstart (local)

If you use `uv`, it will create and manage the project `.venv` automatically. Run the following to install dependencies and run the server from the `uv`-managed environment:

```bash
uv sync
uv run server.py
```

## Deploy
- The project includes a `Dockerfile` and can be deployed to Cloud Run or another container platform. Typical Cloud Run flow:

```bash
gcloud run deploy company-info-mcp-server --allow-unauthenticated --region=us-central1 --source=.
```
