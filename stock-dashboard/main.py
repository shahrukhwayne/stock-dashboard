from fastapi import FastAPI
import yfinance as yf
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from api.predict import predict_price
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache





app = FastAPI()

@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/companies")
def get_companies():
    return ["INFY", "TCS", "RELIANCE"]


@app.get("/data/{symbol}")
@cache(expire=60)
def get_stock_data(symbol: str):
    try:
        df = yf.download(symbol + ".NS", period="30d")

        if df.empty:
            return {"error": "No data found"}

        df.columns = df.columns.get_level_values(0)
        df.reset_index(inplace=True)

        return df.to_dict(orient="records")

    except Exception as e:
        return {"error": str(e)}

@app.get("/summary/{symbol}")
@cache(expire=120)
def get_summary(symbol: str):
    try:
        df = yf.download(symbol + ".NS", period="1y")

        if df.empty:
            return {"error": "No data found"}

        # fix multi-index columns
        df.columns = df.columns.get_level_values(0)

        return {
            "symbol": symbol,
            "52_week_high": round(float(df['Close'].max()), 2),
            "52_week_low": round(float(df['Close'].min()), 2),
            "average_close": round(float(df['Close'].mean()), 2)
        }

    except Exception as e:
        return {"error": str(e)}

@app.get("/compare")
@cache(expire=60)
def compare(symbol1: str, symbol2: str):
    try:
        s1 = symbol1 + ".NS"
        s2 = symbol2 + ".NS"

        df1 = yf.download(s1, period="30d")
        df2 = yf.download(s2, period="30d")

        if df1.empty or df2.empty:
            return {"error": "Invalid symbol or no data found"}

        # fix multi-level columns
        df1.columns = df1.columns.get_level_values(0)
        df2.columns = df2.columns.get_level_values(0)

        return {
            "dates": df1.index.strftime("%Y-%m-%d").tolist(),
            symbol1: df1["Close"].values.tolist(),
            symbol2: df2["Close"].values.tolist()
        }

    except Exception as e:
        return {"error": str(e)}
    

@app.get("/predict/{symbol}")
def predict(symbol: str):
    return {"prediction": predict_price(symbol)}

app.mount("/", StaticFiles(directory="frontend/dist", html=True), name="static")