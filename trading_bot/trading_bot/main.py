import alpaca_trade_api as tradeapi
import pandas as pd
from dotenv import load_dotenv
import yfinance as yf
import os

# Load .env files that stores the API key, API secret, and base URL
load_dotenv()

# Import the API key, API secret, and the base URL
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
base_url = os.getenv('BASE_URL')

# Instantiate my REST API connection
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

# This function returns the user account details
def get_user_account():
    try:
        account = api.get_account()
        print(account)
    except Exception as e:
        print(e)

# This function will buy a stock in the market
def buy_market_stock(stock_symbol, quantity, stock_side, time_enforce):

    # the try block catches any error at runtime and the except block print the message to the console
    try:
        # Market order Request properties
        order_details = {
            'symbol': stock_symbol,
            'qty': quantity,
            'side': stock_side,
            'type': 'market',  # Specify order type as 'market'
            'time_in_force': time_enforce
        }

        # Create the market order
        order_stock = api.submit_order(**order_details)
        print(order_stock)
    except Exception as e:
        print(e)


def sell_market_stock(stock_symbol, quantity, stock_side, time_enforce):
    # the try block catches any error at runtime and the except block print the message to the console
    try:
        # Market order Request properties
        order_details = {
            'symbol': stock_symbol,
            'qty': quantity,
            'side': stock_side,
            'type': 'market',  # Specify order type as 'market'
            'time_in_force': time_enforce
        }

        # Create the market order
        order_stock = api.submit_order(**order_details)
        print(order_stock)
    except Exception as e:
        print(e)


# Get my candles from Alpaca broker

def get_candles():
    symbol = 'TSLA'
    candles = api.get_bars(symbol=symbol, timeframe='1D')
    for bar in candles:
        print(bar)




# This function defined our signal. this determines when to buy a stock or sell.
# This code uses the engulfing patterns to determine when to buy or sell

def sign_generator(df):
    open = df.Open.iloc[-1]
    close = df.Close.iloc[-1]
    previous_open = df.Open.iloc[-2]
    previous_close = df.Close.iloc[-2]

    # Defining my bearish pattern
    # Handle my Bearish pattern: This is a selling signal
    if(open > close and previous_open < previous_close and close < previous_open and open >= previous_close):
        return 1

    # Handling my bullish pattern: This is a buying signal
    elif(open < close and previous_open > previous_close and close > previous_open and open <= previous_close):
        return 2

    #if no pattern
    else:
        return


get_candles()

# if __name__ == '__main__':
#     pd.set_option('display.max_columns', None)
#     # Get my data from yfinance database
#     symbol = 'AAPL'
#     start_date = '2021-06-01'
#     end_date = '2023-06-01'
#     time_frame = 15
#     data_frame = yf.download(symbol, start_date, end_date)
#     #print(data_frame.head())
#
#     signal = []
#     signal.append(0)
#     for i in range(1, len(data_frame)):
#         df = data_frame[:i+1]
#         signal.append(sign_generator(df))
#
#     data_frame['signal'] = signal
#     print(data_frame.signal.value_counts())
#     #print(data_frame)













# get_user_account()  # Call this function to get user account details
# Example usage of buy_market_stock function
#sell_market_stock('TSLA', 2, 'sell', 'gtc')
