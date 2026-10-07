import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

load_dotenv(os.path.join(BASE_DIR, '.env'))

DB_USER = os.getenv('DB_USER', 'admin')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'admin123')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'olist_db')
DB_HOST = os.getenv('DB_HOST', 'localhost')

if os.path.exists('/.dockerenv'):
    DB_HOST = 'postgres'

engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

csv_files = [
    'olist_customers_dataset.csv',
    'olist_geolocation_dataset.csv',
    'olist_order_items_dataset.csv',
    'olist_order_payments_dataset.csv',
    'olist_order_reviews_dataset.csv',
    'olist_orders_dataset.csv',
    'olist_products_dataset.csv',
    'olist_sellers_dataset.csv',
    'product_category_name_translation.csv'
]

def setup_schema():
    print("Setting up database schema...")
    with engine.begin() as conn:
        conn.execute(text("DROP SCHEMA IF EXISTS dwh CASCADE;"))
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS raw;"))
    print("Schema 'raw' is ready.\n")

def load_data_to_postgres():
    for file in csv_files:
        file_path = os.path.join(DATA_DIR, file)
        if os.path.exists(file_path):
            table_name = file.replace('.csv', '').replace('_dataset', '').replace('olist_', '')
            print(f"Loading {file} into raw.{table_name}...")           
            df = pd.read_csv(file_path)      
            df.to_sql(
                name=table_name, 
                con=engine, 
                schema='raw', 
                if_exists='replace', 
                index=False
            )
            print(f"Successfully loaded {len(df)} rows into raw.{table_name}!\n")
        else:
            print(f"File not found at {file_path}. Skipping.\n")

if __name__ == "__main__":
    setup_schema()
    load_data_to_postgres()
    print("ETL Extract & Load phase completed successfully!")