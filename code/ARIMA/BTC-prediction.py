import yfinance as yf
import numpy as np, pandas as pd, matplotlib.pyplot as plt
import math
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error,mean_absolute_error
import os
from pandas import datetime
clear = lambda: os.system('clear')
clear()
df = yf.download("BTC-USD")

plt.plot(df.index, df['Adj Close'])
#plt.show()

to_row = int(len(df)*0.9)
training_data = list(df[:to_row]['Adj Close'])
test_data = list(df[to_row:]['Adj Close'])
"""
plt.figure(figsize=(10,6))
plt.grid(True)
plt.xlabel("Dates")
plt.ylabel("Closing Prices")
plt.plot(df[:to_row]['Adj Close'],"green",label="Train Data")
plt.plot(df[to_row:]['Adj Close'],"blue",label="Test Data")
plt.legend()
plt.show()
"""
model_predictions = []
n_test_obser = len(test_data) 

for i in range(0,n_test_obser):
    model = ARIMA(training_data, order = (4,1,0))
    model_fit = model.fit()
    output = model_fit.forecast()
    yhat = output[0]
    print(yhat)
    model_predictions.append(yhat)
    print(model_predictions)
    actual_test_value = test_data[i]
    training_data.append(actual_test_value)


print(model_fit.summary())
plt.figure(figsize=(15,9))
plt.grid(True)
date_range = df[to_row:].index
plt.plot(date_range, model_predictions, color="blue", marker="o", linestyle="dashed", label="Precio de BTC predicho")
plt.plot(date_range, test_data, color="red", label="Precio de BTC real")
plt.title("Predicción del precio del bitcoin")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()

plt.figure(figsize=(10,6))
plt.grid(True)
plt.xlabel("Dates")
plt.ylabel("Closing Prices")
plt.plot(df[:to_row]['Adj Close'],"green",label="Train Data")
plt.plot(df[to_row:]['Adj Close'],"blue",label="Test Data")
plt.legend()
plt.show()

# Correlation
predictions_df = pd.DataFrame(model_predictions, columns=['Adj Close'])
test_df = pd.DataFrame(test_data, columns=['Adj Close'])
test_df['Adj Close'].corr(predictions_df.loc[0:len(predictions_df),'Adj Close'])


clear()
print(training_data)


