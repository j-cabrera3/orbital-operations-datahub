import requests
import pandas as pd
from utils.db import get_db_connection
from utils.logger import logger

SPACEX_URL = "https://gateway.pipeworx.io/spacex/v4/launches/past?limit=300"


def fetch_spacex_data():
    logger.info("Starting SpaceX API request...")
    try:
        response = requests.get(SPACEX_URL, timeout=20)
        response.raise_for_status()
        logger.info("SpaceX API request successful.")
        return response.json()
    except Exception as e:
        logger.error(f"SpaceX API request failed: {e}")
        raise


def transform_data(raw):
    logger.info("Transforming raw SpaceX launch data...")

    try:
        df = pd.json_normalize(raw)

        # Ensure all expected fields exist
        expected_columns = [
            "id",
            "name",
            "date_utc",
            "success",
            "rocket",
            "details",
            "flight_number",
            "upcoming"
        ]

        for col in expected_columns:
            if col not in df.columns:
                df[col] = None

        logger.info(f"Transformation complete. Rows: {len(df)}")
        return df

    except Exception as e:
        logger.error(f"Error transforming SpaceX data: {e}")
        raise


def load_to_postgres(df):
    logger.info("Loading SpaceX data into PostgreSQL...")

    conn = get_db_connection()
    cur = conn.cursor()

    try:
        for _, row in df.iterrows():

            # Skip rows missing required primary key
            if not row.get("id"):
                logger.warning(
                    f"Skipping row with missing id: {row.get('name')}"
                )
                continue

            cur.execute("""
                INSERT INTO spacex_launches (
                    id, name, date_utc, success, rocket, details,
                    flight_number, upcoming
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT (id) DO NOTHING;
            """, (
                row.get("id"),
                row.get("name"),
                row.get("date_utc"),
                row.get("success"),
                row.get("rocket"),
                row.get("details"),
                row.get("flight_number"),
                row.get("upcoming")
            ))

        conn.commit()
        logger.info("SpaceX PostgreSQL load complete.")

    except Exception as e:
        logger.error(f"Error loading SpaceX data into PostgreSQL: {e}")
        conn.rollback()
        raise

    finally:
        cur.close()
        conn.close()


def run_pipeline():
    logger.info("SpaceX ETL pipeline started.")
    raw = fetch_spacex_data()
    df = transform_data(raw)
    load_to_postgres(df)
    logger.info("SpaceX ETL pipeline finished successfully.")


if __name__ == "__main__":
    run_pipeline()
