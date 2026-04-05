import yfinance as yf
import pandas as pd

def get_stock_data(symbol="INFY", period="3mo"):
    df = yf.download(symbol, period=period)
    df.columns = df.columns.droplevel(1)
    df.reset_index(inplace=True)
    return df
def save_data(df, symbol):
    df.to_csv(f"{symbol}.csv",index = False)

if __name__ == "__main__":
    data = get_stock_data()
    save_data(data, "INFY")
    data2 = pd.read_csv('INFY_cleaned.csv')
    print("null values\n",data2.isnull().sum())