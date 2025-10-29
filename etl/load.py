from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

env_path = Path('.') / '.env files/.env'
load_dotenv(dotenv_path=env_path)

def get_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    url = os.getenv("DB_URL")
    port = os.getenv("DB_PORT")
    dbname = os.getenv("DB_ROOT_BASE")
    if not all([user, password, url, port, dbname]):
        raise Exception("Не все переменные среды заданы!")
    engine_url = f"postgresql+psycopg2://{user}:{password}@{url}:{port}/{dbname}"
    engine = create_engine(engine_url)
    return engine


def load_and_write_data(engine, table_name):
    df = pd.read_parquet("data/converted_ds/dataset_converted.parquet")
    df = df.head(100)

    df.to_sql(
        name=table_name,
        con=engine,
        schema="public",
        if_exists="replace",
        index=False
    )
    print(f"Данные успешно записаны в таблицу public.{table_name}")

if __name__ == "__main__":
    engine = get_engine()
    table_name = "klimova"
    load_and_write_data(engine, table_name)
