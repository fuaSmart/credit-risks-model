

import pytest
import pandas as pd
from datetime import datetime
from scripts.data_pipeline import create_rfm_features, create_time_features

def test_time_feature_creation():
    """Verify that time-based features are created correctly."""
    # 1. Arrange: Create a sample DataFrame
    data = {'TransactionStartTime': ['2025-01-01 15:30:00']}
    df = pd.DataFrame(data)
    df['TransactionStartTime'] = pd.to_datetime(df['TransactionStartTime'])

    # 2. Act: Run the function
    df_result = create_time_features(df)

    # 3. Assert: Check if the columns and values are correct
    assert 'TransactionHour' in df_result.columns
    assert 'DayOfWeek' in df_result.columns
    assert df_result['TransactionHour'].iloc[0] == 15
    assert df_result['DayOfWeek'].iloc[0] == 2 

def test_rfm_feature_creation():
    """Verify that RFM aggregation logic is correct."""
    # 1. Arrange: Create sample transaction data for two customers
    data = {
        'CustomerId': ['C1', 'C2', 'C1'],
        'TransactionId': ['T1', 'T2', 'T3'],
        'Value': [100, 50, 200],
        'TransactionStartTime': [
            '2025-08-10 10:00:00',
            '2025-08-12 12:00:00',
            '2025-08-15 14:00:00'
        ]
    }
    df = pd.DataFrame(data)
    df['TransactionStartTime'] = pd.to_datetime(df['TransactionStartTime'])

    # 2. Act: Run the RFM function
    rfm_result = create_rfm_features(df)

    # 3. Assert: Check the calculated values for Customer 'C1'
    assert rfm_result.loc['C1']['Frequency'] == 2
    assert rfm_result.loc['C1']['MonetarySum'] == 300

    assert rfm_result.loc['C1']['Recency'] == 1