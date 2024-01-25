import yfinance as yf
import pandas as pd

ticker_symbol = 'AAPL'
start_date = '2023-12-01'
end_date = '2024-01-01'
stock_data = yf.download(ticker_symbol, start_date, end_date)

with pd.option_context('display.max_row', None, 'display.max_columns', None):
    pass