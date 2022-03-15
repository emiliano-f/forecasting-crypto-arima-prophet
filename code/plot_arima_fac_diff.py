import pandas as pd, matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_squared_error,mean_absolute_error
import os

def train_test_split(df, test_size=0.1):
    split_row = len(df) - int(test_size * len(df))
    train_data = df.iloc[:split_row]
    test_data = df.iloc[split_row:]
    return (train_data, test_data)

def show(line1, line2, line3=None, 
         label1="Train Data", label2="Test Data", label3="Forecast", 
         title="", lw=2):
    fig, ax = plt.subplots(1, figsize=(9, 5))
    ax.plot(line1, label=label1, linewidth=lw)
    ax.plot(line2, label=label2, linewidth=lw)
    if not line3 is None:
        ax.plot(line3, label=label3, linewidth=lw)
    ax.set_ylabel('USD', fontsize=14)
    ax.set_xlabel('Date', fontsize=14)
    ax.set_title(title, fontsize=16)
    ax.legend(loc='best', fontsize=16);

clear = lambda: os.system('clear')
clear()

hist = pd.read_csv('../data/ada_30m.csv')
hist = hist.set_index('Date')
hist.index = pd.to_datetime(hist.index, yearfirst=True)
hist = hist.rename(columns={'Adj Close': 'Price'})
split = train_test_split(hist)
train = split[0]
test = split[1]

# Auto
"""
import pmdarima as pm

model = pm.auto_arima(test, trace=True, error_action="ignore")
model.fit(test)
num_per = 30
forecast = model.predict(n_periods = num_per)
dates = pd.date_range('03/09/2022', periods = num_per)
forecast = pd.DataFrame(forecast, index = dates, columns = ["Prediction"])
show(test, forecast)
"""
# Manual 

# d parameter
result = adfuller(train.Price.dropna())
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])

# Original Series
fig, axes = plt.subplots(4, figsize=(8, 9), sharex=True)
fig2, axes2 = plt.subplots(4, figsize=(8, 9), sharex=True)
axes[0].plot(train.Price); 
axes[0].set_title('Original Series')
plot_acf(train.Price, ax=axes2[0])

# 1st Differencing
axes[1].plot(train.Price.diff()); 
axes[1].set_title('1st Order Differencing')
plot_acf(train.Price.diff().dropna(), ax=axes2[1])

# 2nd Differencing
axes[2].plot(train.Price.diff().diff()); 
axes[2].set_title('2nd Order Differencing')
plot_acf(train.Price.diff().diff().dropna(), ax=axes2[2])

# 3rd Differencing
axes[3].plot(train.Price.diff().diff().diff()); 
axes[3].set_title('3rd Order Differencing')
plot_acf(train.Price.diff().diff().diff().dropna(), ax=axes2[3])

plt.show()

# p parameter

# PACF plot of 1st differenced series

fig, axes = plt.subplots(1, sharex=True, figsize=(8, 3))
fig2, axes2 = plt.subplots(1, sharex=True, figsize=(8, 3))
axes.plot(train.Price.diff()); axes.set_title('1st Differencing')
axes2.set(ylim=(0,5))
plot_pacf(train.Price.diff().dropna(), ax=axes2)

plt.show()

# q parameter

fig, axes = plt.subplots(1, sharex=True, figsize=(8, 3))
fig2, axes2 = plt.subplots(1, sharex=True, figsize=(8, 3))
axes.plot(train.Price.diff()); axes.set_title('1st Differencing')
axes2.set(ylim=(0,1.2))
plot_acf(train.Price.diff().dropna(), ax=axes2)
plt.show()


"""
# 1,1,2 ARIMA model
model = ARIMA(train.Price, order=(1,1,1))
model_fit = model.fit()
print(model_fit.summary())
model_fit.plot_predict(dynamic=False)
"""
