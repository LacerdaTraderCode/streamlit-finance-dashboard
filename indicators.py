"""
Cálculo de indicadores técnicos.
"""
import pandas as pd
import numpy as np


def sma(prices: pd.Series, period: int = 20) -> pd.Series:
    """Simple Moving Average — Média Móvel Simples."""
    return prices.rolling(window=period).mean()


def ema(prices: pd.Series, period: int = 20) -> pd.Series:
    """Exponential Moving Average — Média Móvel Exponencial."""
    return prices.ewm(span=period, adjust=False).mean()


def rsi(prices: pd.Series, period: int = 14) -> pd.Series:
    """
    Relative Strength Index (RSI) — Índice de Força Relativa.
    Valores de 0 a 100. Acima de 70 = sobrecompra, abaixo de 30 = sobrevenda.
    """
    delta = prices.diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


def macd(prices: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9) -> dict:
    """
    MACD (Moving Average Convergence Divergence).
    Retorna dict com 'macd', 'signal' e 'histogram'.
    """
    ema_fast = ema(prices, fast)
    ema_slow = ema(prices, slow)
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    histogram = macd_line - signal_line
    return {
        "macd": macd_line,
        "signal": signal_line,
        "histogram": histogram,
    }


def bollinger_bands(prices: pd.Series, period: int = 20, std_dev: float = 2.0) -> dict:
    """
    Bandas de Bollinger.
    Retorna dict com 'upper', 'middle' (SMA) e 'lower'.
    """
    middle = sma(prices, period)
    std = prices.rolling(window=period).std()
    upper = middle + (std * std_dev)
    lower = middle - (std * std_dev)
    return {"upper": upper, "middle": middle, "lower": lower}
