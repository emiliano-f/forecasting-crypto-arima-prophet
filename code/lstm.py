from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout, LSTM
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def train_test_split(df, test_size=0.2):
    split_row = len(df) - int(test_size * len(df))
    train_data = df.iloc[:split_row]
    test_data = df.iloc[split_row:]
    return (train_data, test_data)

def line_plot(line1, line2, label1=None, label2=None, title='', lw=2):
    fig, ax = plt.subplots(1, figsize=(13, 7))
    ax.plot(line1, label=label1, linewidth=lw)
    ax.plot(line2, label=label2, linewidth=lw)
    ax.set_ylabel('USD', fontsize=14)
    ax.set_xlabel('Date', fontsize=14)
    ax.set_title(title, fontsize=16)
    ax.legend(loc='best', fontsize=16);
    
def normalise_zero_base(df):
    return df / df.iloc[0] - 1

def normalise_min_max(df):
    return (df - df.min()) / (df.max() - df.min())

def extract_window_data(df, window_len=5, zero_base=True):
    window_data = []
    for idx in range(len(df) - window_len):
        tmp = df[idx: (idx + window_len)].copy()
        if zero_base:
            tmp = normalise_zero_base(tmp)
        window_data.append(tmp.values)
    return np.array(window_data)

def prepare_data(df, target_col, window_len=10, zero_base=True, test_size=0.2):
    datasets = train_test_split(df, test_size=test_size)
    train_data = datasets[0]
    test_data = datasets[1]
    X_train = extract_window_data(train_data, window_len, zero_base)
    X_test = extract_window_data(test_data, window_len, zero_base)
    y_train = train_data[target_col][window_len:].values
    y_test = test_data[target_col][window_len:].values
    if zero_base:
        y_train = y_train / train_data[target_col][:-window_len].values - 1
        y_test = y_test / test_data[target_col][:-window_len].values - 1

    return train_data, test_data, X_train, X_test, y_train, y_test

def build_lstm_model(input_data, output_size, neurons=100, activ_func='linear',
                     dropout=0.2, loss='mse', optimizer='adam'):
    model = Sequential()
    model.add(LSTM(neurons, input_shape=(input_data.shape[1], input_data.shape[2])))
    model.add(Dropout(dropout))
    model.add(Dense(units=output_size))
    model.add(Activation(activ_func))

    model.compile(loss=loss, optimizer=optimizer)
    return model

names = ["btc", "eth", "ada"]
times = ["1d", "30m"]
target_col = 'Adj Close'

np.random.seed(42)
window_len = 5
test_size = 0.2
zero_base = True
lstm_neurons = 100
epochs = 20
batch_size = 32
loss = 'mse'
dropout = 0.2
optimizer = 'adam'

for coin in names:
    for time in times:
        # Load
        path = '../data/' + coin + "_" + time + ".csv" 
        hist = pd.read_csv(path)
        hist = hist.set_index('Date')
        hist.index = pd.to_datetime(hist.index, yearfirst=True)
        
        # Plot
        datasets = train_test_split(hist, test_size=0.2)
        train = datasets[0]
        test = datasets[1]
        title = "Historical Price " + coin.upper() + " " + time 
        line_plot(train[target_col], test[target_col], 'Training', 'Test', title)

        # Preparing data
        train, test, X_train, X_test, y_train, y_test = prepare_data(
            hist, target_col, window_len=window_len, zero_base=zero_base, test_size=test_size)

        # Create model
        model = build_lstm_model(
            X_train, output_size=1, neurons=lstm_neurons, dropout=dropout, loss=loss,
            optimizer=optimizer)
        
        # Fit
        history = model.fit(
            X_train, y_train, validation_data=(X_test, y_test), epochs=epochs, batch_size=batch_size, verbose=1, shuffle=True)


        # Plot LSTM
        #plt.plot(history.history['loss'],'r',linewidth=2, label='Train loss')
        #plt.plot(history.history['val_loss'], 'g',linewidth=2, label='Validation loss')
        #plt.title('LSTM')
        #plt.xlabel('Epochs')
        #plt.ylabel('MSE')
        #plt.show()

        # Predict
        targets = test[target_col][window_len:]
        preds = model.predict(X_test).squeeze()
        mean_absolute_error(preds, y_test)


        MAE=mean_squared_error(preds, y_test)
        MAE

        R2=r2_score(y_test, preds)
        R2

        preds = test[target_col].values[:-window_len] * (preds + 1)
        preds = pd.Series(index=targets.index, data=preds)
        line_plot(targets, preds, 'Actual', 'Prediction', title='Comparision: Actual and Predicted Prices', lw=3)
        #input("Next?")