import pandas as pd, matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import os
from datetime import timedelta
import random
from accuracy_metrics import forecast_accuracy

clear = lambda: os.system('clear')
clear()
hist = pd.read_csv('eth_1d.csv') 
hist = hist.set_index('Date')
hist.index = pd.to_datetime(hist.index, yearfirst=True)

# Metrics
data: list = []

for _ in range(10):
    
    # Train
    aleatory_row = random.randint(0, len(hist)-31)
    print(aleatory_row)
    df = hist[aleatory_row:aleatory_row+31]
    model = ARIMA(df[:len(df)-1]['Adj Close'], order = (2,1,1))
    model_fit = model.fit()
    output = model_fit.forecast()
    model_predictions = []
    model_predictions.append(output[0])
    inicio = df.index[-2].date()
    fin = inicio + timedelta(1)
    
    # Ignore
    to_app = pd.DataFrame()
    to_app['Date'] = [fin]
    to_app['Adj Close'] = list(model_predictions)
    to_app.set_index('Date',inplace = True)
    
    # Future, Actual sets
    future = df[:len(df)-1]
    future = future.append(to_app)
    future.drop(future.index[range(29)], inplace = True)
    
    actual = df.drop(df.index[range(29)])
    
    # Plot
    plt.figure(figsize=(9,4))
    plt.grid(True)
    plt.xlabel("Date")
    plt.ylabel("Price [USD]")
    plt.title("Historical Price and Forecast [ETH]")
    plt.plot(df[:]['Adj Close'],"blue",label="Training")
    plt.plot(df[len(df)-2:]['Adj Close'],"Green",label="Actual")
    plt.plot(future[:]['Adj Close'],"red",label="Future Prediction")
    plt.legend()
    plt.show()
    
    # Metrics
    future = future.rename(columns={'Adj Close': 'Close'})
    actual = actual.rename(columns={'Adj Close': 'Close'})
    future.drop(future.index[0],inplace=True)
    actual.drop(actual.index[0],inplace=True)
    data.append(forecast_accuracy(future.Close, actual.Close, rmse=True, mae=True, smape=True))
