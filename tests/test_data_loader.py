from unittest.mock import MagicMock

import pandas as pd
import pytest

import data_loader


class FakeTicker:
    def __init__(self, history=None, info=None, error=None):
        self._history = history
        self._info = info
        self._error = error
        self.requested_period = None

    def history(self, period):
        self.requested_period = period
        if self._error:
            raise self._error
        return self._history

    @property
    def info(self):
        if self._error:
            raise self._error
        return self._info


@pytest.fixture
def install_ticker(monkeypatch):
    def _install(**kwargs):
        ticker = FakeTicker(**kwargs)
        monkeypatch.setattr(data_loader.yf, "Ticker", lambda symbol: ticker)
        return ticker

    return _install


def test_load_ticker_data_resets_index_and_forwards_period(install_ticker, ohlcv):
    ticker = install_ticker(history=ohlcv.set_index("Date"))

    result = data_loader.load_ticker_data("AAPL", "1y")

    assert "Date" in result.columns
    assert len(result) == len(ohlcv)
    assert ticker.requested_period == "1y"


def test_load_ticker_data_returns_empty_frame_when_no_data(install_ticker):
    install_ticker(history=pd.DataFrame())

    assert data_loader.load_ticker_data("NOPE").empty


def test_load_ticker_data_reports_fetch_errors(install_ticker, monkeypatch):
    install_ticker(error=RuntimeError("network down"))
    error = MagicMock()
    monkeypatch.setattr(data_loader.st, "error", error)

    result = data_loader.load_ticker_data("FAIL")

    assert result.empty
    error.assert_called_once()
    assert "network down" in error.call_args.args[0]


def test_get_ticker_info_maps_fields(install_ticker):
    install_ticker(
        info={
            "longName": "Apple Inc.",
            "sector": "Technology",
            "currency": "USD",
            "marketCap": 3_000_000,
        },
    )

    assert data_loader.get_ticker_info("AAPL") == {
        "name": "Apple Inc.",
        "sector": "Technology",
        "currency": "USD",
        "market_cap": 3_000_000,
    }


def test_get_ticker_info_falls_back_to_short_name_then_symbol(install_ticker):
    install_ticker(info={"shortName": "Short"})
    assert data_loader.get_ticker_info("SHRT")["name"] == "Short"

    install_ticker(info={})
    assert data_loader.get_ticker_info("BARE")["name"] == "BARE"


def test_get_ticker_info_returns_defaults_on_error(install_ticker):
    install_ticker(error=RuntimeError("boom"))

    assert data_loader.get_ticker_info("ERR") == {
        "name": "ERR",
        "sector": "N/A",
        "currency": "USD",
        "market_cap": None,
    }


def test_calculate_metrics(ohlcv):
    metrics = data_loader.calculate_metrics(ohlcv)

    assert metrics["current_price"] == 159.0
    assert metrics["day_change_pct"] == pytest.approx(1 / 158 * 100)
    assert metrics["period_change_pct"] == pytest.approx(59.0)
    assert metrics["avg_volume"] == 1_000.0
    assert metrics["max_price"] == 161.0
    assert metrics["min_price"] == 98.0
    assert metrics["volatility"] > 0


def test_calculate_metrics_handles_empty_data():
    assert data_loader.calculate_metrics(pd.DataFrame()) == {}


def test_calculate_metrics_with_single_row(ohlcv):
    metrics = data_loader.calculate_metrics(ohlcv.head(1))

    assert metrics["day_change_pct"] == 0
    assert metrics["period_change_pct"] == 0


def test_calculate_metrics_guards_against_zero_prices(ohlcv):
    ohlcv.loc[0, "Close"] = 0.0

    metrics = data_loader.calculate_metrics(ohlcv)

    assert metrics["period_change_pct"] == 0
