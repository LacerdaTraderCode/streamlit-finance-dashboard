<div align="center">

# 📈 Streamlit Finance Dashboard

**Interactive financial analysis dashboard with candlestick charts and technical indicators**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/python/)
[![License](https://img.shields.io/badge/License-MIT-orange)](https://github.com/LacerdaTraderCode/streamlit-finance-dashboard/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-LacerdaTraderCode-181717?logo=github)](https://github.com/LacerdaTraderCode/streamlit-finance-dashboard)
[![Unofficial Data](https://img.shields.io/badge/Data-Unofficial-red)](https://github.com/LacerdaTraderCode/streamlit-finance-dashboard)

</div>

---

## 📌 About the Project

Interactive financial analysis dashboard built with **Streamlit** and **Plotly**. Lets you analyze stocks, cryptocurrencies, and indices with candlestick charts, technical indicators (SMA, EMA, RSI, MACD, Bollinger), and comparisons across multiple assets — all running locally, with no infrastructure required.

> ⚠️ Data is sourced via `yfinance`, an **unofficial** wrapper for Yahoo Finance. There is no affiliation with Yahoo Finance. Data is for informational purposes only and does not constitute investment advice.

### Features

- ✅ **Real-time quotes** via Yahoo Finance (yfinance)
- ✅ **Interactive candlestick chart** with Plotly
- ✅ **Technical indicators** — SMA, EMA, RSI, MACD, Bollinger Bands
- ✅ **Normalized multi-asset comparison**
- ✅ **Period filters** — 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, max
- ✅ **Quick metrics** — change, volatility, average volume
- ✅ **CSV data download**
- ✅ **Responsive, modern interface**

---

## 🖼️ Preview

```
┌─────────────────────────────────────────────────┐
│  📈 Finance Dashboard                           │
├─────────────────────────────────────────────────┤
│  [Ticker: PETR4.SA ▼]  [Period: 6mo ▼]          │
│                                                   │
│  Price: $38.42  ↑ +2.15%  Vol: 45M               │
│                                                   │
│  ╭─────────────────────────────────────────╮     │
│  │        [Candlestick Chart]              │     │
│  ╰─────────────────────────────────────────╯     │
│                                                   │
│  ╭─────────────────────────────────────────╮     │
│  │        [RSI + MACD]                     │     │
│  ╰─────────────────────────────────────────╯     │
└─────────────────────────────────────────────────┘
```

---

## 🛠️ Technologies

- **Streamlit** — Framework for building fast dashboards
- **Plotly** — Interactive charts
- **yfinance** — Financial data from Yahoo Finance
- **Pandas** — Data manipulation
- **NumPy** — Technical indicator calculations

---

## 📁 Structure

```
streamlit-finance-dashboard/
├── app.py              # Main dashboard (entry point)
├── indicators.py       # Technical indicator calculations
├── data_loader.py      # Data fetching via yfinance
├── requirements.txt
└── README.md
```

---

## 📦 Installation

```bash
git clone https://github.com/LacerdaTraderCode/streamlit-finance-dashboard.git
cd streamlit-finance-dashboard

python -m venv venv
source venv/bin/activate      # Linux/Mac
# venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

---

## ⚡ Usage

```bash
streamlit run app.py
```

Automatically opens at `http://localhost:8501`

---

## 💡 Example Tickers

| Market | Examples |
|--------|----------|
| **BR Stocks** | `PETR4.SA`, `VALE3.SA`, `ITUB4.SA`, `MGLU3.SA` |
| **US Stocks** | `AAPL`, `MSFT`, `TSLA`, `GOOGL`, `AMZN` |
| **Crypto** | `BTC-USD`, `ETH-USD`, `SOL-USD` |
| **Indices** | `^BVSP` (Ibovespa), `^GSPC` (S&P 500) |
| **Forex** | `USDBRL=X`, `EURUSD=X` |

---

## 🚀 Deploy

Can be published for free on:
- **Streamlit Community Cloud** — [share.streamlit.io](https://share.streamlit.io)
- **Render**, **Railway** — self-hosted options

---

## ✅ Requirements

- Python **3.11** or higher

---

## 👤 Author

<div align="center">

**Wagner Lacerda** — Senior Software Engineer | Python, Backend, AI Apps, Automation & Systems

[![GitHub](https://img.shields.io/badge/GitHub-LacerdaTraderCode-181717?logo=github&logoColor=white)](https://github.com/LacerdaTraderCode)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Wagner%20Lacerda-0077B5?logo=linkedin&logoColor=white)](https://linkedin.com/in/wagner-lacerda-da-silva-958b9481)
[![YouTube](https://img.shields.io/badge/YouTube-LacerdaTraderCode-FF0000?logo=youtube&logoColor=white)](https://youtube.com/@LacerdaTraderCode)
[![Telegram](https://img.shields.io/badge/Telegram-LacerdaTraderCode-26A5E4?logo=telegram&logoColor=white)](https://t.me/LacerdaTraderCode)
[![Telegram Bots](https://img.shields.io/badge/Telegram-Bots-26A5E4?logo=telegram&logoColor=white)](https://t.me/LacerdaTraderCode_bots)

📍 Rio Grande do Sul, Brazil

</div>

---

## 📄 License

Distributed under the MIT license. See [LICENSE](LICENSE) for more details.
