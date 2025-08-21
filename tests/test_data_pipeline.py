import pandas as pd
from pathlib import Path

from scripts.data_pipeline import (
    create_time_features,
    create_rfm_features,
    encode_categorical_features,
)

# --- Create a robust path to the dummy data ---
TESTS_DIR = Path(__file__).resolve().parent
DUMMY_DATA_PATH = TESTS_DIR / "dummy_data.csv"
# ---

df = pd.read_csv(DUMMY_DATA_PATH)
df = create_time_features(df)


def test_time_feature_creation():

    assert "TransactionHour" in df.columns
    assert df["TransactionHour"].iloc[0] == 10


def test_categorical_encoding():

    df_encoded = encode_categorical_features(df)
    assert "ChannelId_ChannelId_1" in df_encoded.columns
    assert "ProductCategory_airtime" in df_encoded.columns

    assert df_encoded["ChannelId_ChannelId_1"].iloc[1] == 1


def test_rfm_feature_creation():

    rfm_result = create_rfm_features(df)

    assert rfm_result.loc["C1"]["Frequency"] == 2
    assert rfm_result.loc["C1"]["MonetarySum"] == 7000
