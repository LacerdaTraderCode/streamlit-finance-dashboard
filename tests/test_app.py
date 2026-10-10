from pathlib import Path

import pandas as pd
import pytest
from streamlit.testing.v1 import AppTest

import data_loader

APP_PATH = str(Path(__file__).resolve().parent.parent / "app.py")
INFO = {"name": "Test Corp", "sector": "Tech", "currency": "USD", "market_cap": 1}


@pytest.fixture
def loader_calls():
    return []


@pytest.fixture
def app(monkeypatch, ohlcv, loader_calls):
    def fake_load(ticker, period="6mo"):
        loader_calls.append((ticker, period))
        return ohlcv

    monkeypatch.setattr(data_loader, "load_ticker_data", fake_load)
    monkeypatch.setattr(data_loader, "get_ticker_info", lambda ticker: INFO)
    return AppTest.from_file(APP_PATH, default_timeout=30)


def test_renders_header_metrics_and_chart(app):
    at = app.run()

    assert not at.exception
    assert "PETR4.SA" in at.title[0].value
    assert "Test Corp" in at.caption[0].value
    assert [metric.label for metric in at.metric] == [
        "Current price",
        "Period change",
        "Volatility",
        "Average volume",
    ]
    assert at.metric[0].value == "USD 159.00"
    assert len(at.get("plotly_chart")) == 1


def test_custom_ticker_overrides_suggestion(app, loader_calls):
    at = app.run()

    at.sidebar.text_input[0].input("msft").run()

    assert "MSFT" in at.title[0].value
    assert loader_calls[-1][0] == "MSFT"


def test_changing_category_changes_suggested_tickers(app):
    at = app.run()

    at.sidebar.selectbox[0].select("₿ Crypto").run()

    assert "BTC-USD" in at.title[0].value


def test_selected_period_is_forwarded_to_loader(app, loader_calls):
    at = app.run()
    assert at.sidebar.selectbox[2].value == "6mo"

    at.sidebar.selectbox[2].select("1y").run()

    assert loader_calls[-1] == ("PETR4.SA", "1y")


def test_indicator_toggles_do_not_break_rendering(app):
    at = app.run()

    for checkbox in at.sidebar.checkbox:
        checkbox.set_value(not checkbox.value)
    at.run()

    assert not at.exception
    assert len(at.get("plotly_chart")) == 1


def test_shows_error_and_stops_when_no_data(app, monkeypatch):
    empty_loader = lambda ticker, period="6mo": pd.DataFrame()  # noqa: E731
    monkeypatch.setattr(data_loader, "load_ticker_data", empty_loader)

    at = app.run()

    assert len(at.error) == 1
    assert len(at.metric) == 0
    assert len(at.get("plotly_chart")) == 0
