"""
time-series-forecasting-crypto
"""

import yfinance as yf

data = yf.download("BTC ETH ADA", start="2022-01-05", end="2022-01-10")#, interval="5m")
print(data.head())
