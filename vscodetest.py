import yfinance as yf
import pandas as pd

def get_stock_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d", start=start_date, end=end_date)
    data["Moving_Avg"] = data["Close"].rolling(window=20).mean()
    return data

# Example Usage
data = get_stock_data("AAPL", "2024-01-01", "2025-06-01")
print(data.tail())