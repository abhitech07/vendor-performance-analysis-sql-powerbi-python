import pandas as pd
from sqlalchemy import create_engine
import os
import logging
import time

# Ensure logs folder exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
    filemode="a"
)

# Function to insert DataFrame into database
def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    logging.info(f"Table {table_name} ingested successfully.")

# Function to load all CSV files from folder
def load_raw_data():
    start = time.time()
    folder = r"C:\Users\Admin\OneDrive\Desktop\Abhijeet Kr Pandey\Data Analyst\Vendor Analysis\data"

    for file in os.listdir(folder):
        if file.endswith(".csv"):
            file_path = os.path.join(folder, file)
            df = pd.read_csv(file_path)
            logging.info(f"Ingesting {file} in db")
            ingest_db(df, file[:-4], engine)  # Table name = CSV file name without .csv

    end = time.time()
    total_time = (end - start) / 60
    logging.info("Ingestion Complete")
    logging.info(f"Total Time Taken: {total_time:.2f} minutes")

# Optional: run ingestion directly
if __name__ == "__main__":
    engine = create_engine("postgresql+psycopg2://postgres:Abhi%40123@localhost:5432/inventory")
    load_raw_data()
