"""
Finance Dashboard - App principal Streamlit.

Executar: streamlit run app.py
"""
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from data_loader import load_ticker_data, get_ticker_info, calculate_metrics
from indicators import sma, ema, rsi, macd, bollinger_bands


# ==================== CONFIG ====================
st.set_page_config(
    page_title="Finance Dashboard",
    page_icon="📈",
    layout="wide",
)

# ==================== SIDEBAR ====================
st.sidebar.title("⚙️ Configurações")

# Tickers populares como sugestões
SUGGESTIONS = {
    "🇧🇷 Ações BR": ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "MGLU3.SA", "BBAS3.SA"],
    "🇺🇸 Ações US": ["AAPL", "MSFT", "TSLA", "GOOGL", "AMZN", "NVDA"],
    "₿ Cripto": ["BTC-USD", "ETH-USD", "SOL-USD"],
    "📊 Índices": ["^BVSP", "^GSPC", "^IXIC"],
}

selected_category = st.sidebar.selectbox("Categoria", list(SUGGESTIONS.keys()))
suggested = SUGGESTIONS[selected_category]
ticker = st.sidebar.selectbox("Ticker sugerido", suggested)
custom_ticker = st.sidebar.text_input("Ou digite outro:", "")
if custom_ticker:
    ticker = custom_ticker.upper()

period = st.sidebar.selectbox(
    "Período",
    ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"],
    index=2,
)

st.sidebar.markdown("---")
st.sidebar.subheader("📊 Indicadores")
show_sma = st.sidebar.checkbox("SMA 20/50", value=True)
show_bollinger = st.sidebar.checkbox("Bandas de Bollinger", value=False)
show_rsi = st.sidebar.checkbox("RSI", value=True)
show_macd = st.sidebar.checkbox("MACD", value=True)

# ==================== MAIN ====================
st.title(f"📈 Finance Dashboard — {ticker}")

with st.spinner(f"Carregando dados de {ticker}..."):
    data = load_ticker_data(ticker, period)
    info = get_ticker_info(ticker)

if data.empty:
    st.error(f"❌ Não foi possível carregar dados de {ticker}. Verifique o ticker.")
    st.stop()

# Header info
st.caption(f"**{info['name']}** · Setor: {info['sector']} · Moeda: {info['currency']}")

# Métricas
metrics = calculate_metrics(data)
col1, col2, col3, col4 = st.columns(4)
col1.metric(
    "Preço Atual",
    f"{info['currency']} {metrics['current_price']:.2f}",
    f"{metrics['day_change_pct']:+.2f}%",
)
col2.metric("Variação Período", f"{metrics['period_change_pct']:+.2f}%")
col3.metric("Volatilidade", f"{metrics['volatility']:.2f}%")
col4.metric("Volume Médio", f"{metrics['avg_volume']:,.0f}")

# ==================== CANDLESTICK ====================
st.subheader("📊 Gráfico de Preços")

n_subplots = 1 + (1 if show_rsi else 0) + (1 if show_macd else 0)
row_heights = [0.5] + [0.25] * (n_subplots - 1)

fig = make_subplots(
    rows=n_subplots,
    cols=1,
    shared_xaxes=True,
    vertical_spacing=0.05,
    row_heights=row_heights,
)

# Candlestick
fig.add_trace(
    go.Candlestick(
        x=data["Date"],
        open=data["Open"],
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        name="Preço",
    ),
    row=1, col=1,
)

# SMA
if show_sma:
    fig.add_trace(
        go.Scatter(x=data["Date"], y=sma(data["Close"], 20),
                   name="SMA 20", line=dict(color="orange", width=1)),
        row=1, col=1,
    )
    fig.add_trace(
        go.Scatter(x=data["Date"], y=sma(data["Close"], 50),
                   name="SMA 50", line=dict(color="blue", width=1)),
        row=1, col=1,
    )

# Bollinger
if show_bollinger:
    bb = bollinger_bands(data["Close"])
    fig.add_trace(
        go.Scatter(x=data["Date"], y=bb["upper"], name="BB Superior",
                   line=dict(color="gray", dash="dash", width=1)),
        row=1, col=1,
    )
    fig.add_trace(
        go.Scatter(x=data["Date"], y=bb["lower"], name="BB Inferior",
                   line=dict(color="gray", dash="dash", width=1),
                   fill="tonexty", fillcolor="rgba(128,128,128,0.1)"),
        row=1, col=1,
    )

current_row = 2

# RSI
if show_rsi:
    rsi_values = rsi(data["Close"])
    fig.add_trace(
        go.Scatter(x=data["Date"], y=rsi_values, name="RSI",
                   line=dict(color="purple")),
        row=current_row, col=1,
    )
    fig.add_hline(y=70, line_dash="dash", line_color="red", row=current_row, col=1)
    fig.add_hline(y=30, line_dash="dash", line_color="green", row=current_row, col=1)
    fig.update_yaxes(title_text="RSI", range=[0, 100], row=current_row, col=1)
    current_row += 1

# MACD
if show_macd:
    macd_data = macd(data["Close"])
    fig.add_trace(
        go.Scatter(x=data["Date"], y=macd_data["macd"], name="MACD",
                   line=dict(color="blue")),
        row=current_row, col=1,
    )
    fig.add_trace(
        go.Scatter(x=data["Date"], y=macd_data["signal"], name="Signal",
                   line=dict(color="red")),
        row=current_row, col=1,
    )
    colors = ["green" if v >= 0 else "red" for v in macd_data["histogram"]]
    fig.add_trace(
        go.Bar(x=data["Date"], y=macd_data["histogram"], name="Histograma",
               marker_color=colors),
        row=current_row, col=1,
    )
    fig.update_yaxes(title_text="MACD", row=current_row, col=1)

fig.update_layout(
    height=700,
    xaxis_rangeslider_visible=False,
    showlegend=True,
    template="plotly_white",
)
st.plotly_chart(fig, use_container_width=True)

# ==================== DATA TABLE ====================
with st.expander("📋 Ver dados brutos"):
    st.dataframe(data.tail(50), use_container_width=True)

    # Download
    csv = data.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Baixar CSV",
        data=csv,
        file_name=f"{ticker}_{period}.csv",
        mime="text/csv",
    )

# ==================== FOOTER ====================
st.markdown("---")
st.caption(
    "📊 Dashboard construído com Streamlit e Plotly · "
    "Dados via Yahoo Finance · "
    "Desenvolvido por [Wagner Lacerda](https://github.com/LacerdaTraderCode)"
)
