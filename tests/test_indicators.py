import pandas as pd
import pytest

from indicators import bollinger_bands, ema, macd, rsi, sma


@pytest.fixture
def noisy_prices():
    return pd.Series([100 + (i % 7) * 3 - (i % 5) for i in range(80)], dtype="float64")


def test_sma_averages_rolling_window():
    result = sma(pd.Series([1.0, 2.0, 3.0, 4.0, 5.0]), period=3)

    assert result.isna().tolist() == [True, True, False, False, False]
    assert result.dropna().tolist() == [2.0, 3.0, 4.0]


def test_ema_weights_recent_prices():
    result = ema(pd.Series([1.0, 2.0, 3.0]), period=3)

    assert result.tolist() == pytest.approx([1.0, 1.5, 2.25])


def test_rsi_is_100_for_strictly_rising_prices():
    prices = pd.Series(range(1, 31), dtype="float64")

    assert rsi(prices).iloc[-1] == pytest.approx(100.0)


def test_rsi_is_0_for_strictly_falling_prices():
    prices = pd.Series(range(30, 0, -1), dtype="float64")

    assert rsi(prices).iloc[-1] == pytest.approx(0.0)


def test_rsi_stays_within_bounds(noisy_prices):
    values = rsi(noisy_prices).dropna()

    assert not values.empty
    assert values.between(0, 100).all()


def test_rsi_needs_a_full_window():
    result = rsi(pd.Series(range(1, 31), dtype="float64"), period=14)

    assert result.iloc[:14].isna().all()
    assert result.iloc[14:].notna().all()


def test_macd_returns_consistent_components(noisy_prices):
    result = macd(noisy_prices)

    assert set(result) == {"macd", "signal", "histogram"}
    difference = result["macd"] - result["signal"] - result["histogram"]
    assert difference.abs().max() < 1e-9


def test_macd_is_zero_for_constant_prices():
    result = macd(pd.Series([5.0] * 60))

    assert result["macd"].abs().max() < 1e-9
    assert result["histogram"].abs().max() < 1e-9


def test_bollinger_bands_known_values():
    result = bollinger_bands(pd.Series([1.0, 2.0, 3.0, 4.0, 5.0]), period=3, std_dev=2.0)

    assert result["middle"].dropna().tolist() == [2.0, 3.0, 4.0]
    assert result["upper"].dropna().tolist() == pytest.approx([4.0, 5.0, 6.0])
    assert result["lower"].dropna().tolist() == pytest.approx([0.0, 1.0, 2.0])


def test_bollinger_bands_are_ordered(noisy_prices):
    result = bollinger_bands(noisy_prices)

    valid = result["middle"].notna()
    assert (result["upper"][valid] >= result["middle"][valid]).all()
    assert (result["middle"][valid] >= result["lower"][valid]).all()
