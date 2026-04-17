"""
Data Loader - busca dados financeiros via yfinance.
"""
import yfinance as yf
import pandas as pd
import streamlit as st


@st.cache_data(ttl=300)  # Cache de 5 minutos
def load_ticker_data(ticker: str, period: str = "6mo") -> pd.DataFrame:
    """
    Busca dados históricos de um ticker.
    
    Args:
        ticker: Símbolo (ex: 'PETR4.SA', 'AAPL', 'BTC-USD')
        period: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    """
    try:
        data = yf.Ticker(ticker).history(period=period)
        if data.empty:
            return pd.DataFrame()
        data = data.reset_index()
        return data
    except Exception as e:
        st.error(f"Erro ao buscar {ticker}: {e}")
        return pd.DataFrame()


@st.cache_data(ttl=300)
def get_ticker_info(ticker: str) -> dict:
    """Retorna metadados do ticker (nome, setor, etc.)."""
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
    """Calcula métricas resumidas."""
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
