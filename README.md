# 📈 Streamlit Finance Dashboard

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/python/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

Dashboard interativo de análise financeira construído com **Streamlit** e **Plotly**. Permite analisar ações, criptomoedas e índices com gráficos de candlestick, indicadores técnicos (médias móveis, RSI, MACD) e comparação entre ativos.

---

## 🎯 Funcionalidades

- ✅ **Cotações em tempo real** via Yahoo Finance (yfinance)
- ✅ **Gráfico de candlestick** interativo com Plotly
- ✅ **Indicadores técnicos**: SMA, EMA, RSI, MACD, Bandas de Bollinger
- ✅ **Comparação multi-ativos** normalizada
- ✅ **Filtros por período** (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, max)
- ✅ **Métricas rápidas** (variação, volatilidade, volume médio)
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
- **NumPy** — Cálculos dos indicadores

---

## 📁 Estrutura

```
streamlit-finance-dashboard/
├── app.py                   # Dashboard principal
├── indicators.py            # Cálculo dos indicadores técnicos
├── data_loader.py           # Busca dados via yfinance
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Instalação

```bash
git clone https://github.com/LacerdaTraderCode/streamlit-finance-dashboard.git
cd streamlit-finance-dashboard

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

## 🚀 Uso

```bash
streamlit run app.py
```

Abre automaticamente no navegador em `http://localhost:8501`

---

## 💡 Exemplos de Tickers

| Mercado | Exemplos |
|---------|----------|
| **Ações BR** | PETR4.SA, VALE3.SA, ITUB4.SA, MGLU3.SA |
| **Ações US** | AAPL, MSFT, TSLA, GOOGL, AMZN |
| **Cripto** | BTC-USD, ETH-USD, SOL-USD |
| **Índices** | ^BVSP (Ibovespa), ^GSPC (S&P 500) |
| **Forex** | USDBRL=X, EURUSD=X |

---

## 🚀 Deploy

Este dashboard pode ser publicado gratuitamente em:
- **Streamlit Community Cloud** — [share.streamlit.io](https://share.streamlit.io)
- **Render**, **Railway** — opções self-hosted

---

## 👨‍💻 Autor

**Wagner Lacerda**  
🔗 [LinkedIn](https://www.linkedin.com/in/wagner-lacerda-da-silva-958b9481)  
🐙 [GitHub](https://github.com/LacerdaTraderCode)  

---

## 📄 Licença

MIT License
