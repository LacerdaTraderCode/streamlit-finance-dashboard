<div align="center">

# 📈 Streamlit Finance Dashboard

**Dashboard interativo de análise financeira com candlestick e indicadores técnicos**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/python/)
[![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-orange)](https://github.com/LacerdaTraderCode/streamlit-finance-dashboard/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-LacerdaTraderCode-181717?logo=github)](https://github.com/LacerdaTraderCode/streamlit-finance-dashboard)

</div>

---

## 📌 Sobre o projeto

Dashboard interativo de análise financeira construído com **Streamlit** e **Plotly**. Permite analisar ações, criptomoedas e índices com gráficos de candlestick, indicadores técnicos (SMA, EMA, RSI, MACD, Bollinger) e comparação entre múltiplos ativos — tudo rodando localmente sem necessidade de infraestrutura.

### Funcionalidades

- ✅ **Cotações em tempo real** via Yahoo Finance (yfinance)
- ✅ **Gráfico de candlestick** interativo com Plotly
- ✅ **Indicadores técnicos** — SMA, EMA, RSI, MACD, Bandas de Bollinger
- ✅ **Comparação multi-ativos** normalizada
- ✅ **Filtros por período** — 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, max
- ✅ **Métricas rápidas** — variação, volatilidade, volume médio
- ✅ **Download dos dados** em CSV
- ✅ **Interface responsiva** e visual moderno

---

## 🖼️ Preview

```
┌─────────────────────────────────────────────────┐
│  📈 Finance Dashboard                           │
├─────────────────────────────────────────────────┤
│  [Ticker: PETR4.SA ▼]  [Período: 6mo ▼]        │
│                                                 │
│  Preço: R$ 38,42  ↑ +2,15%  Vol: 45M           │
│                                                 │
│  ╭─────────────────────────────────────────╮   │
│  │        [Gráfico Candlestick]            │   │
│  ╰─────────────────────────────────────────╯   │
│                                                 │
│  ╭─────────────────────────────────────────╮   │
│  │        [RSI + MACD]                     │   │
│  ╰─────────────────────────────────────────╯   │
└─────────────────────────────────────────────────┘
```

---

## 🛠️ Tecnologias

- **Streamlit** — Framework para dashboards rápidos
- **Plotly** — Gráficos interativos
- **yfinance** — Dados financeiros do Yahoo Finance
- **Pandas** — Manipulação de dados
- **NumPy** — Cálculos dos indicadores técnicos

---

## 📁 Estrutura

```
streamlit-finance-dashboard/
├── app.py              # Dashboard principal (ponto de entrada)
├── indicators.py       # Cálculo dos indicadores técnicos
├── data_loader.py      # Busca de dados via yfinance
├── requirements.txt
└── README.md
```

---

## 📦 Instalação

```bash
git clone https://github.com/LacerdaTraderCode/streamlit-finance-dashboard.git
cd streamlit-finance-dashboard

python -m venv venv
source venv/bin/activate      # Linux/Mac
# venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

---

## ⚡ Uso

```bash
streamlit run app.py
```

Abre automaticamente em `http://localhost:8501`

---

## 💡 Exemplos de tickers

| Mercado | Exemplos |
|---------|----------|
| **Ações BR** | `PETR4.SA`, `VALE3.SA`, `ITUB4.SA`, `MGLU3.SA` |
| **Ações US** | `AAPL`, `MSFT`, `TSLA`, `GOOGL`, `AMZN` |
| **Cripto** | `BTC-USD`, `ETH-USD`, `SOL-USD` |
| **Índices** | `^BVSP` (Ibovespa), `^GSPC` (S&P 500) |
| **Forex** | `USDBRL=X`, `EURUSD=X` |

---

## 🚀 Deploy

Pode ser publicado gratuitamente em:
- **Streamlit Community Cloud** — [share.streamlit.io](https://share.streamlit.io)
- **Render**, **Railway** — opções self-hosted

---

## ✅ Requisitos

- Python **3.11** ou superior

---

## 👤 Autor

<div align="center">

**Wagner Lacerda** — Python Backend Developer | APIs REST • Automação • Data Engineering

[![GitHub](https://img.shields.io/badge/GitHub-LacerdaTraderCode-181717?logo=github&logoColor=white)](https://github.com/LacerdaTraderCode)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Wagner%20Lacerda-0077B5?logo=linkedin&logoColor=white)](https://linkedin.com/in/wagner-lacerda-da-silva-958b9481)
[![YouTube](https://img.shields.io/badge/YouTube-LacerdaTraderCode-FF0000?logo=youtube&logoColor=white)](https://youtube.com/@LacerdaTraderCode)
[![Telegram](https://img.shields.io/badge/Telegram-LacerdaTraderCode-26A5E4?logo=telegram&logoColor=white)](https://t.me/LacerdaTraderCode)
[![Telegram Bots](https://img.shields.io/badge/Telegram-Bots-26A5E4?logo=telegram&logoColor=white)](https://t.me/LacerdaTraderCode_bots)

📍 Rio Grande do Sul, Brasil

</div>

---

## 📄 Licença

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.
