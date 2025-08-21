

import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "data.csv"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "model_ready_data.csv"

def load_data(path: Path) -> pd.DataFrame:
    """Loads the raw CSV data."""
    print(f"Loading data from {path}...")
    return pd.read_csv(path)

def create_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """Creates time-based features from 'TransactionStartTime'."""
    print("Creating time-based features...")
    # Ensure column is in datetime format
    df['TransactionStartTime'] = pd.to_datetime(df['TransactionStartTime'])
    
    df['TransactionHour'] = df['TransactionStartTime'].dt.hour
    df['DayOfWeek'] = df['TransactionStartTime'].dt.dayofweek
    df['DayOfMonth'] = df['TransactionStartTime'].dt.day
    return df

def encode_categorical_features(df: pd.DataFrame) -> pd.DataFrame:
    """One-hot encodes 'ProductCategory' and 'ChannelId'."""
    print("Encoding categorical features...")
    categorical_cols = ['ProductCategory', 'ChannelId']
    df_encoded = pd.get_dummies(df, columns=categorical_cols, prefix=categorical_cols, dtype=int)
    return df_encoded

def create_rfm_features(df: pd.DataFrame) -> pd.DataFrame:
    """Creates Recency, Frequency, and Monetary (RFM) features for each customer."""
    print("Creating RFM features...")
    snapshot_date = df['TransactionStartTime'].max() + pd.Timedelta(days=1)
    
    rfm = df.groupby('CustomerId').agg({
        'TransactionStartTime': lambda x: (snapshot_date - x.max()).days,
        'TransactionId': 'count',
        'Value': ['sum', 'mean']
    })
    
    rfm.columns = ['Recency', 'Frequency', 'MonetarySum', 'MonetaryMean']
    return rfm

def run_pipeline():
    """Orchestrates the end-to-end data processing pipeline."""
    df = load_data(RAW_DATA_PATH)
    df = create_time_features(df)
    
    rfm_features = create_rfm_features(df)
    df_processed = encode_categorical_features(df)
    
    df_final = df_processed.merge(rfm_features, on='CustomerId', how='left')
    
    columns_to_drop = [
        'TransactionId', 'BatchId', 'AccountId', 'SubscriptionId',
        'CurrencyCode', 'CountryCode', 'ProviderId', 'ProductId',
        'TransactionStartTime'
    ]
    df_final = df_final.drop(columns=columns_to_drop)
    
    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    # Save the final dataset
    df_final.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"\nPipeline complete. Processed data saved to:\n{PROCESSED_DATA_PATH}")

if __name__ == "__main__":
    run_pipeline()