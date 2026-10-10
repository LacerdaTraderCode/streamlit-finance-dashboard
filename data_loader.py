import pandas as pd
import streamlit as st
import yfinance as yf

CACHE_TTL_SECONDS = 300


@st.cache_data(ttl=CACHE_TTL_SECONDS)
def load_ticker_data(ticker: str, period: str = "6mo") -> pd.DataFrame:
    try:
        data = yf.Ticker(ticker).history(period=period)
    except Exception as exc:
        st.error(f"Failed to fetch {ticker}: {exc}")
        return pd.DataFrame()

    if data.empty:
        return pd.DataFrame()
    return data.reset_index()


@st.cache_data(ttl=CACHE_TTL_SECONDS)
def get_ticker_info(ticker: str) -> dict:
    try:
        info = yf.Ticker(ticker).info
        return {
            "name": info.get("longName") or info.get("shortName") or ticker,
            "sector": info.get("sector", "N/A"),
            "currency": info.get("currency", "USD"),
            "market_cap": info.get("marketCap"),
        }
    except Exception:
        return {"name": ticker, "sector": "N/A", "currency": "USD", "market_cap": None}


def calculate_metrics(data: pd.DataFrame) -> dict:
    if data.empty:
        return {}

    current = data["Close"].iloc[-1]
    previous = data["Close"].iloc[-2] if len(data) > 1 else current
    first = data["Close"].iloc[0]

    return {
        "current_price": current,
        "day_change_pct": ((current - previous) / previous * 100) if previous else 0,
        "period_change_pct": ((current - first) / first * 100) if first else 0,
        "avg_volume": data["Volume"].mean(),
        "volatility": data["Close"].pct_change().std() * 100,
        "max_price": data["High"].max(),
        "min_price": data["Low"].min(),
    }
