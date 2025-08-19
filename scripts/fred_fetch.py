"""Fetch macroeconomic indicators from FRED API."""

from fredapi import Fred


def get_inflation_data(api_key):
    """Returns CPI data for feature engineering."""
    fred = Fred(api_key=api_key)
    return fred.get_series("CPIAUCSL")
