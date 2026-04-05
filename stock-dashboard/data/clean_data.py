import pandas as pd

def clean_stock_data(file_path):
    df = pd.read_csv(file_path)

    # Missing values hatao
    df = df.dropna()

    # Date format sahi karo
    df['Date'] = pd.to_datetime(df['Date'])

    # Index reset karo
    df.reset_index(drop=True, inplace=True)

    return df
def add_metrics(df):

    # Daily Return
    df['Daily Return'] = (df['Close'] - df['Open']) / df['Open']

    # 7-day Moving Average
    df['MA7'] = df['Close'].rolling(window=7).mean()

    # 52-week High/Low
    df['52W High'] = df['Close'].max()
    df['52W Low'] = df['Close'].min()

    return df


if __name__ == "__main__":
    df = clean_stock_data("INFY.csv")
    df = add_metrics(df)
    df.to_csv("INFY_cleaned.csv", index=False)