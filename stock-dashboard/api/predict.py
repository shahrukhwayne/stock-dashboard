import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression

def predict_price(symbol="INFY"):
    df = yf.download(symbol + ".NS", period="60d")

    df = df.reset_index()
    df['Day'] = np.arange(len(df))

    X = df[['Day']]
    y = df['Close']

    model = LinearRegression()
    model.fit(X, y)

    next_day = [[len(df)]]
    prediction = model.predict(next_day)

    return float(prediction[0])