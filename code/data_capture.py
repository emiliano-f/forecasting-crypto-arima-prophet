"""
time-series-forecasting-crypto
"""
import pandas as pd
import pandas_datareader as web

# It will allow us to define start and end dates for our data pull
import datetime

import matplotlib.pyplot as plt
import seaborn as sns

# ARIMA, SARIMAX models
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima.model import ARIMA

# Relax the display limits on columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


btc = web.get_data_yahoo(['BTC-USD'], start=datetime.datetime(2020, 1, 1), end=datetime.datetime(2022, 1, 10))
eth = web.get_data_yahoo(['ETH-USD'], start=datetime.datetime(2020, 1, 1), end=datetime.datetime(2022, 1, 10))
ada = web.get_data_yahoo(['ADA-USD'], start=datetime.datetime(2020, 1, 1), end=datetime.datetime(2022, 1, 10))

# Only closing price
btc = btc['Close']
eth = eth['Close']
ada = ada['Close']

# Saving
path = "../data/"
btc.to_csv(path + "btc.csv")
eth.to_csv(path + "eth.csv")
ada.to_csv(path + "ada.csv")
