import pandas as pd
import pytest

import data_loader


@pytest.fixture
def ohlcv():
    close = pd.Series(range(100, 160), dtype="float64")
    data = {
        "Date": pd.date_range("2024-01-01", periods=60, freq="D"),
        "Open": close - 1,
        "High": close + 2,
        "Low": close - 2,
        "Close": close,
        "Volume": 1_000.0,
    }
    return pd.DataFrame(data)


@pytest.fixture(autouse=True)
def clear_streamlit_caches():
    data_loader.load_ticker_data.clear()
    data_loader.get_ticker_info.clear()
