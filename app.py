import streamlit as st

from charts import build_price_chart
from data_loader import calculate_metrics, get_ticker_info, load_ticker_data

SUGGESTIONS = {
    "🇧🇷 Brazilian stocks": ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "MGLU3.SA", "BBAS3.SA"],
    "🇺🇸 US stocks": ["AAPL", "MSFT", "TSLA", "GOOGL", "AMZN", "NVDA"],
    "₿ Crypto": ["BTC-USD", "ETH-USD", "SOL-USD"],
    "📊 Indices": ["^BVSP", "^GSPC", "^IXIC"],
}
PERIODS = ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"]

st.set_page_config(
    page_title="Finance Dashboard",
    page_icon="📈",
    layout="wide",
)

st.sidebar.title("⚙️ Settings")

selected_category = st.sidebar.selectbox("Category", list(SUGGESTIONS.keys()))
ticker = st.sidebar.selectbox("Suggested ticker", SUGGESTIONS[selected_category])
custom_ticker = st.sidebar.text_input("Or enter another:", "")
if custom_ticker:
    ticker = custom_ticker.upper()

period = st.sidebar.selectbox("Period", PERIODS, index=2)

st.sidebar.markdown("---")
st.sidebar.subheader("📊 Indicators")
show_sma = st.sidebar.checkbox("SMA 20/50", value=True)
show_bollinger = st.sidebar.checkbox("Bollinger Bands", value=False)
show_rsi = st.sidebar.checkbox("RSI", value=True)
show_macd = st.sidebar.checkbox("MACD", value=True)

st.title(f"📈 Finance Dashboard — {ticker}")

with st.spinner(f"Loading data for {ticker}..."):
    data = load_ticker_data(ticker, period)
    info = get_ticker_info(ticker)

if data.empty:
    st.error(f"❌ Could not load data for {ticker}. Check the ticker symbol.")
    st.stop()

st.caption(f"**{info['name']}** · Sector: {info['sector']} · Currency: {info['currency']}")

metrics = calculate_metrics(data)
col1, col2, col3, col4 = st.columns(4)
col1.metric(
    "Current price",
    f"{info['currency']} {metrics['current_price']:.2f}",
    f"{metrics['day_change_pct']:+.2f}%",
)
col2.metric("Period change", f"{metrics['period_change_pct']:+.2f}%")
col3.metric("Volatility", f"{metrics['volatility']:.2f}%")
col4.metric("Average volume", f"{metrics['avg_volume']:,.0f}")

st.subheader("📊 Price chart")
figure = build_price_chart(
    data,
    show_sma=show_sma,
    show_bollinger=show_bollinger,
    show_rsi=show_rsi,
    show_macd=show_macd,
)
st.plotly_chart(figure, use_container_width=True)

with st.expander("📋 View raw data"):
    st.dataframe(data.tail(50), use_container_width=True)
    st.download_button(
        label="📥 Download CSV",
        data=data.to_csv(index=False).encode("utf-8"),
        file_name=f"{ticker}_{period}.csv",
        mime="text/csv",
    )

st.markdown("---")
st.caption(
    "📊 Built with Streamlit and Plotly · "
    "Data via Yahoo Finance · "
    "Developed by [Wagner Lacerda](https://github.com/LacerdaTraderCode)"
)
