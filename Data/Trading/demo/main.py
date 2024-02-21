import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import pandas_ta as ta

# define the ticker symbol
ticker_symbol = "AAPL"

# Create a ticker object
ticker = yf.Ticker(ticker_symbol)

# Download historical data
# historical_data = ticker.history(start="1990-01-01", end="2022-12-31", interval= '1d')
historical_data = ticker.history(period="7d", interval="1d")

df = pd.read_csv("candlestick.csv")
data["EMA"] = ta.ema(df.Close, length=10)
data["RSI_IO"] = ta.rsi(df.Close, lenght=10)
volume = df[df["Volume"] != 0]
#print(df)

#data = yf.download(tickers="BTC-USD", period="max", interval="1d")

data.tail()
data.reset_index(inplace=True)
dfpl = data[0:150]

fig = go.Figure(
    data=[
        go.Candlestick(
            x=dfpl.index,
            open=dfpl["Open"],
            high=dfpl["High"],
            low=dfpl["Low"],
            close=dfpl["Close"],
        ),
        go.Scatter(
            x=dfpl.index, y=dfpl.EMA, line=dict(color="red", width=2), name="EMA"
        ),
    ]
)

fig.show()
print(data)
