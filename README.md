# 🛒 Olist E-Commerce End-to-End Data Pipeline

[![dbt CI/CD Pipeline](https://github.com/frysushi00/e2e-data-pipeline/actions/workflows/dbt-ci.yml/badge.svg)](https://github.com/frysushi00/e2e-data-pipeline/actions/workflows/dbt-ci.yml)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791)
![dbt](https://img.shields.io/badge/dbt-Core-FF694B)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?logo=powerbi&logoColor=black)

## 📌 Project Overview
An automated, end-to-end ETL/ELT data pipeline that extracts raw [Brazilian e-commerce data](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), loads it into a PostgreSQL database, transforms it into a scalable Kimball Star Schema using dbt, and visualizes key delivery and operational KPIs in Power BI. 
This project demonstrates modern data engineering practices, including containerization, orchestration, modular SQL transformations, data quality testing, and automated CI/CD.


## 📸 Project Visuals
### 1. Airflow Orchestration
The pipeline is fully automated and monitored via Apache Airflow. All tasks (Extract, Transform, Test) execute sequentially with built-in retry logic and environment variable injection.
![Airflow DAG Success](https://github.com/user-attachments/assets/29b9a6a6-aef2-46b7-a146-6b811a95bde5)
> *Caption: All-green Airflow DAG indicating successful end-to-end execution.*

### 2. dbt Star Schema Modeling
Data is transformed from raw, denormalized CSVs into a clean, query-optimized Star Schema (`fct_orders`, `dim_customers`, `dim_products`, `dim_date`) to ensure fast and accurate BI reporting.
![Power BI Star Schema](https://github.com/user-attachments/assets/0addf9cd-e074-4799-88af-36577710992d)
> *Caption: Power BI Model View showing proper 1-to-Many relationships between Fact and Dimension tables.*

### 3. Power BI Dashboard
The final output is an interactive dashboard tracking core business metrics, including Total Order Volume, Order Status Breakdown, and Delivery Success Rates.
![Power BI Dashboard](https://github.com/user-attachments/assets/d8ea813f-e30a-4789-a719-c83dda598771)
> *Caption: Interactive Power BI dashboard tracking e-commerce delivery KPIs.*


## 🏗️ Architecture & Tech Stack
- **Extract & Load**: Python (Pandas, SQLAlchemy)
- **Transformation**: dbt (Data Build Tool) with Advanced SQL (CTEs, Joins, Window Functions)
- **Orchestration**: Apache Airflow (Dockerized)
- **Data Warehouse**: PostgreSQL 15
- **Visualization**: Power BI Desktop
- **CI/CD**: GitHub Actions (Automated `dbt parse` syntax and logic checking)


##  Project Structure
```text
e2e-data-pipeline/
├── .github/workflows/    # GitHub Actions CI/CD pipeline
├── dags/                 # Airflow DAG definitions
├── data/                 # Raw CSV datasets (Olist)
├── dwh/                  # dbt project (models, profiles, tests)
├── images/               # Screenshots for README documentation
├── script/               # Python extract & load scripts
├── docker-compose.yml    # Local infrastructure setup (Gitignored for security)
└── README.md             # Project documentation
```

## 🚀 How to Run Locally
### Prerequisites
- Docker & Docker Compose installed
- Power BI Desktop (for visualization)


## 🛡️ Data Quality & CI/CD
This project features an automated GitHub Actions workflow. On every push or pull request to `main`, the pipeline automatically runs `dbt parse` to validate all SQL, Jinja, and YAML syntax, ensuring no broken code is ever merged into the production branch.


