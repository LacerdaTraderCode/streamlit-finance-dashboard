import pandas as pd


def sma(prices: pd.Series, period: int = 20) -> pd.Series:
    return prices.rolling(window=period).mean()


def ema(prices: pd.Series, period: int = 20) -> pd.Series:
    return prices.ewm(span=period, adjust=False).mean()


def rsi(prices: pd.Series, period: int = 14) -> pd.Series:
    delta = prices.diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


def macd(prices: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9) -> dict:
    macd_line = ema(prices, fast) - ema(prices, slow)
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    return {
        "macd": macd_line,
        "signal": signal_line,
        "histogram": macd_line - signal_line,
    }


def bollinger_bands(prices: pd.Series, period: int = 20, std_dev: float = 2.0) -> dict:
    middle = sma(prices, period)
    std = prices.rolling(window=period).std()
    return {
        "upper": middle + std * std_dev,
        "middle": middle,
        "lower": middle - std * std_dev,
    }
