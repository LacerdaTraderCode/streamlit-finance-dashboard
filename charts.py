import plotly.graph_objects as go
from plotly.subplots import make_subplots

from indicators import bollinger_bands, macd, rsi, sma


def _add_line(fig, x, y, name, row, line, **trace):
    fig.add_trace(go.Scatter(x=x, y=y, name=name, line=line, **trace), row=row, col=1)


def build_price_chart(
    data,
    show_sma: bool = True,
    show_bollinger: bool = False,
    show_rsi: bool = True,
    show_macd: bool = True,
) -> go.Figure:
    dates = data["Date"]
    close = data["Close"]
    rows = 1 + int(show_rsi) + int(show_macd)

    fig = make_subplots(
        rows=rows,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.05,
        row_heights=[0.5] + [0.25] * (rows - 1),
    )

    fig.add_trace(
        go.Candlestick(
            x=dates,
            open=data["Open"],
            high=data["High"],
            low=data["Low"],
            close=close,
            name="Price",
        ),
        row=1,
        col=1,
    )

    if show_sma:
        _add_line(fig, dates, sma(close, 20), "SMA 20", 1, {"color": "orange", "width": 1})
        _add_line(fig, dates, sma(close, 50), "SMA 50", 1, {"color": "blue", "width": 1})

    if show_bollinger:
        bands = bollinger_bands(close)
        band_line = {"color": "gray", "dash": "dash", "width": 1}
        _add_line(fig, dates, bands["upper"], "BB Upper", 1, band_line)
        _add_line(
            fig,
            dates,
            bands["lower"],
            "BB Lower",
            1,
            band_line,
            fill="tonexty",
            fillcolor="rgba(128,128,128,0.1)",
        )

    row = 2

    if show_rsi:
        _add_line(fig, dates, rsi(close), "RSI", row, {"color": "purple"})
        fig.add_hline(y=70, line_dash="dash", line_color="red", row=row, col=1)
        fig.add_hline(y=30, line_dash="dash", line_color="green", row=row, col=1)
        fig.update_yaxes(title_text="RSI", range=[0, 100], row=row, col=1)
        row += 1

    if show_macd:
        values = macd(close)
        _add_line(fig, dates, values["macd"], "MACD", row, {"color": "blue"})
        _add_line(fig, dates, values["signal"], "Signal", row, {"color": "red"})
        colors = ["green" if value >= 0 else "red" for value in values["histogram"]]
        fig.add_trace(
            go.Bar(x=dates, y=values["histogram"], name="Histogram", marker_color=colors),
            row=row,
            col=1,
        )
        fig.update_yaxes(title_text="MACD", row=row, col=1)

    fig.update_layout(
        height=700,
        xaxis_rangeslider_visible=False,
        showlegend=True,
        template="plotly_white",
    )
    return fig
