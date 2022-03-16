# Accuracy metrics
import numpy as np
from statsmodels.tsa.stattools import acf

def forecast_accuracy(forecast, actual,
                      mape = False, me = False, mae = False,
                      mpe = False, rmse = False, corr = False,
                      acf1 = False, minmax = False, smape = False):
    """
    forecast: Future
    actual: Actual
    """
    values: dict = {}
    if mape:
        _mape = np.mean(np.abs(forecast - actual)/np.abs(actual))  # MAPE
        values['mape'] = _mape
    if me:
        _me = np.mean(forecast - actual)             # ME
        values['me'] = _me
    if mae:
        _mae = np.mean(np.abs(forecast - actual))    # MAE
        values['mae'] = _mae
    if mpe:
        _mpe = np.mean((forecast - actual)/actual)   # MPE
        values['mpe'] = _mpe
    if rmse:
        _rmse = np.mean((forecast - actual)**2)**.5  # RMSE
        values['rmse'] = _rmse
    if corr:
        _corr = np.corrcoef(forecast, actual)[0,1]   # corr
        values['corr'] = _corr
    if minmax:
        mins = np.amin(np.hstack([forecast[:,None],
                              actual[:,None]]), axis=1)
        maxs = np.amax(np.hstack([forecast[:,None],
                              actual[:,None]]), axis=1)
        _minmax = 1 - np.mean(mins/maxs)             # minmax
        values['minmax'] = _minmax
    if acf1:
        _acf1 = acf(fc-test)[1]                      # ACF1
        values['acf1'] = _acf1
    if smape:
        _smape = 1/actual.size * np.sum(np.abs(forecast - actual) / (np.abs(actual) + np.abs(forecast))*100) #SMAPE Adjusted
        values['smape'] = _smape
    return values
