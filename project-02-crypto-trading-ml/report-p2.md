
# 📊 Project Report – Crypto Trading ML Agent

## 🎯 Objective
Develop a machine learning-based trading agent that predicts short-term price movements in Bitcoin using historical data, and generates buy/sell signals.

## 🔧 Tools & Libraries
- yfinance · pandas · scikit-learn · XGBoost · matplotlib · numpy

## 🔬 Approach
- Downloaded historical BTC-USD data using Yahoo Finance
- Created time-series lag features (t-1, t-2, t-3)
- Trained XGBoost regression model to predict next-day close price
- Generated signals:
    - BUY if predicted > current close
    - SELL if predicted < current close

## 📈 Strategy Evaluation
Backtested the strategy over the test period:

- Strategy Cumulative Return: ✅ Higher than market return
- Market Return: Tracked BTC price
- Key Observations:
    - Model captured short-term uptrends effectively
    - Some overfitting observed on small test windows

## 📌 Example Signal Logic
```python
df_test["signal"] = np.where(df_test["pred"] > df_test["Close"], 1, -1)
df_test["strategy_return"] = df_test["signal"].shift(1) * df_test["daily_return"]
```

## 🧠 Future Improvements
- Use LSTM for sequential modeling
- Include technical indicators (RSI, MACD)
- Optimize thresholds and position sizing
- Test on more coins (ETH, SOL, BNB, etc.)

---

🔬 Author: Dr. Ehsan Zafari  
Senior Machine Learning & MLOps Engineer | AI for Finance Enthusiast
