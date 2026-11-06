import psycopg2
import yaml
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    with open("config/db_config.yaml", "r") as f:
        cfg = yaml.safe_load(f)

    conn = psycopg2.connect(
        host=cfg["etl_host"],
        port=cfg["port"],
        database=cfg["database"],
        user=cfg["user"],
        password=os.getenv("DB_PASSWORD")
    )
    return conn
