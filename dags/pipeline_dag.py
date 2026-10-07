from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    'olist_etl_dwh_pipeline',
    default_args=default_args,
    description='End-to-end Olist ETL and dbt transformation',
    schedule_interval=None,  
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['olist', 'postgres', 'dbt'],
) as dag:

    # Task 1: Extract & Load 
    extract_load = BashOperator(
        task_id='extract_and_load_raw_data',
        bash_command='cd /opt/airflow/project/script && python extract.py',
    )

    # Task 2: Run dbt models (Transform) 
    dbt_run = BashOperator(
        task_id='dbt_run_transformations',
        bash_command='export PATH=$PATH:/home/airflow/.local/bin && cd /opt/airflow/project/dwh && dbt run --profiles-dir .',
    )

    # Task 3: Run dbt tests (Data Quality Check)
    dbt_test = BashOperator(
        task_id='dbt_test_data_quality',
        bash_command='export PATH=$PATH:/home/airflow/.local/bin && cd /opt/airflow/project/dwh && dbt test --profiles-dir .',
    )

    # Define the flow
    extract_load >> dbt_run >> dbt_test