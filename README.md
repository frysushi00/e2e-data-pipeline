# 🛒 Olist E-Commerce End-to-End Data Pipeline

## 📌 Project Overview
An automated ETL/ELT pipeline that extracts raw Brazilian e-commerce data, loads it into PostgreSQL, transforms it into a Star Schema using dbt, and visualizes key delivery KPIs in Power BI.

## 🏗️ Architecture
- **Extract & Load**: Python (Pandas, SQLAlchemy) via Apache Airflow
- **Transformation**: dbt (Data Build Tool) with Advanced SQL (CTEs, Joins)
- **Orchestration**: Apache Airflow (Dockerized)
- **Visualization**: Power BI Desktop

## 📂 Project Structure
```text
e2e-data-pipeline/
├── dags/               # Airflow DAGs
├── data/               # Raw CSV datasets
├── dwh/                # dbt project (models, profiles, tests)
── script/             # Python extract & load scripts
└── docker-compose.yml  # Local infrastructure setup