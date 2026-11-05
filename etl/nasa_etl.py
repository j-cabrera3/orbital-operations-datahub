import requests
import pandas as pd
from utils.db import get_db_connection
from utils.logger import logger

NASA_URL = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=DEMO_KEY"


def fetch_nasa_data():
    logger.info("Starting NASA API request...")
    response = requests.get(NASA_URL)

    try:
        response.raise_for_status()
        logger.info("NASA API request successful.")
        return response.json()
    except Exception as e:
        logger.error(f"NASA API request failed: {e}")
        raise


def transform_data(raw):
    logger.info("Transforming raw NASA data...")

    try:
        df = pd.json_normalize(raw["near_earth_objects"])
        logger.info(f"Transformation complete. Rows: {len(df)}")
        return df
    except Exception as e:
        logger.error(f"Error transforming NASA data: {e}")
        raise


def load_to_postgres(df):
    logger.info("Loading NASA data into PostgreSQL...")

    conn = get_db_connection()
    cur = conn.cursor()

    try:
        for _, row in df.iterrows():

            # Safely extract close approach data
            cad = row.get("close_approach_data")
            if cad and isinstance(cad, list) and len(cad) > 0:
                cad_entry = cad[0]
                close_approach_date = cad_entry.get("close_approach_date")
                relative_velocity = cad_entry.get("relative_velocity", {}).get("kilometers_per_second")
                miss_distance = cad_entry.get("miss_distance", {}).get("kilometers")
            else:
                close_approach_date = None
                relative_velocity = None
                miss_distance = None

            cur.execute("""
                INSERT INTO nasa_neo (
                    id, name, nasa_jpl_url, absolute_magnitude,
                    is_potentially_hazardous,
                    estimated_diameter_min, estimated_diameter_max,
                    close_approach_date, relative_velocity, miss_distance
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT (id) DO NOTHING;
            """, (
                row.get("id"),
                row.get("name"),
                row.get("nasa_jpl_url"),
                row.get("absolute_magnitude_h"),
                row.get("is_potentially_hazardous_asteroid"),
                row.get("estimated_diameter.kilometers.estimated_diameter_min"),
                row.get("estimated_diameter.kilometers.estimated_diameter_max"),
                close_approach_date,
                relative_velocity,
                miss_distance
            ))

        conn.commit()
        logger.info("NASA PostgreSQL load complete.")

    except Exception as e:
        logger.error(f"Error loading NASA data into PostgreSQL: {e}")
        conn.rollback()
        raise

    finally:
        cur.close()
        conn.close()




def run_pipeline():
    logger.info("NASA ETL pipeline started.")
    raw = fetch_nasa_data()
    df = transform_data(raw)
    load_to_postgres(df)
    logger.info("NASA ETL pipeline finished successfully.")


if __name__ == "__main__":
    run_pipeline()

