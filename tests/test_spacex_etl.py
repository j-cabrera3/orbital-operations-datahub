import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd

from etl.spacex_etl import transform_data


def test_transform_data_returns_dataframe():

    sample_data = [
        {
            "id": "123",
            "name": "Test Launch",
            "date_utc": "2026-01-01",
            "success": True
        }
    ]

    df = transform_data(sample_data)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1