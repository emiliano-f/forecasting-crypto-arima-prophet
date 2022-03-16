"""
time-series-forecasting-crypto
"""
import pandas as pd
import yfinance as yf

# It will allow us to define start and end dates for our data pull
import datetime

def distribute(data):
    btc = data['BTC-USD']['Adj Close']
    eth = data['ETH-USD']['Adj Close']
    ada = data['ADA-USD']['Adj Close']
    return (btc,eth,ada)

def save(coins, txt=''):
    names = ["btc", "eth", "ada"]
    path = "../data/"    
    for _ in range(len(coins)):
        coins[_].to_csv(path + names[_] + "_" + txt + ".csv")
    
# Daily
data = yf.download("BTC-USD ETH-USD ADA-USD", start="2017-11-09", group_by='tickers')
coins = distribute(data)
save(coins, "1d")

# 30min
data = yf.download("BTC-USD ETH-USD ADA-USD", start="2022-02-09", interval='30m', group_by='tickers')
coins = distribute(data)
save(coins, "30m")

# 15min
#data = yf.download("BTC-USD ETH-USD ADA-USD", start="2022-01-09", interval='15m', group_by='tickers')
#coins = distribute(data)
#save(coins, "15m")

# 5min
#data = yf.download("BTC-USD ETH-USD ADA-USD", start="2022-01-09", interval='5m', group_by='tickers')
#coins = distribute(data)
#save(coins, "5m")

