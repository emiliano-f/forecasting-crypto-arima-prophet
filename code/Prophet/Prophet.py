import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib as mpl
import yfinance as yf
from fbprophet import Prophet, plot
from fbprophet.diagnostics import cross_validation, performance_metrics
from datetime import datetime
from datetime import timedelta
import os

df = pd.read_csv('Data.csv')
df = df[['Date','Adj Close']]

df.columns = ["ds","y"]
print(df)
model = Prophet()
model.fit(df)
future_dates = model.make_future_dataframe(periods=60) # Indica la cantidad de términos futuros que debe predecir, en este caso, 60 dia en el futuro
prediction = model.predict(future_dates)
print("\n\n----------------------------------PREDICCIONES----------------------------------")
print(prediction.tail())
fig = model.plot(prediction)
plt.show()

df_cv = cross_validation(model, horizon = 365, parallel="processes")

print(df_cv.tail())


df_performance = performance_metrics(df_cv)
#fig2 = plot.plot_cross_validation_metric(df_cv, metric="mape")

# yhat --> Precio predecido para una fecha en específica
# ds --> Fecha
# yhat_lower --> Precio mínimo que puede tomar la prediccion
# yhat_upper --> Precio máximo que puede tomar la prediccion
# trend_lower --> Media, valor más probable que tome la prediccion



