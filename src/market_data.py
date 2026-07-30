import yfinance as yf


def get_market_data(symbol, name):
    """
    Fetch market data for a given symbol.
    """

    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")

    latest = data.iloc[-1]

    return {
        "Index": name,
        "Open": round(latest["Open"], 2),
        "High": round(latest["High"], 2),
        "Low": round(latest["Low"], 2),
        "Close": round(latest["Close"], 2),
        "Volume": latest["Volume"],
    }


if __name__ == "__main__":

    nifty = get_market_data("^NSEI", "NIFTY 50")

    print(nifty)