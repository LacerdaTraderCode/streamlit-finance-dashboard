import pytest

from charts import build_price_chart


def trace_names(figure):
    return [trace.name for trace in figure.data]


def test_default_chart_has_price_sma_rsi_and_macd(ohlcv):
    figure = build_price_chart(ohlcv)

    assert trace_names(figure) == [
        "Price",
        "SMA 20",
        "SMA 50",
        "RSI",
        "MACD",
        "Signal",
        "Histogram",
    ]
    assert figure.layout.yaxis2.title.text == "RSI"
    assert figure.layout.yaxis3.title.text == "MACD"
    assert figure.layout.height == 700


def test_price_only_chart(ohlcv):
    figure = build_price_chart(
        ohlcv,
        show_sma=False,
        show_bollinger=False,
        show_rsi=False,
        show_macd=False,
    )

    assert trace_names(figure) == ["Price"]
    assert len(figure.layout.shapes) == 0


def test_bollinger_bands_are_added_to_price_panel(ohlcv):
    figure = build_price_chart(ohlcv, show_sma=False, show_rsi=False, show_macd=False, show_bollinger=True)

    assert trace_names(figure) == ["Price", "BB Upper", "BB Lower"]
    assert figure.data[2].fill == "tonexty"


def test_rsi_panel_has_overbought_and_oversold_lines(ohlcv):
    figure = build_price_chart(ohlcv, show_sma=False, show_macd=False)

    levels = sorted(shape.y0 for shape in figure.layout.shapes)
    assert levels == [30, 70]


def test_macd_moves_to_second_panel_without_rsi(ohlcv):
    figure = build_price_chart(ohlcv, show_sma=False, show_rsi=False)

    assert figure.layout.yaxis2.title.text == "MACD"


def test_histogram_colors_follow_sign(ohlcv):
    figure = build_price_chart(ohlcv, show_sma=False, show_rsi=False)

    histogram = next(trace for trace in figure.data if trace.name == "Histogram")
    assert set(histogram.marker.color) <= {"green", "red"}


@pytest.mark.parametrize("column", ["Date", "Open", "High", "Low", "Close"])
def test_chart_requires_ohlc_columns(ohlcv, column):
    with pytest.raises(KeyError):
        build_price_chart(ohlcv.drop(columns=column))
