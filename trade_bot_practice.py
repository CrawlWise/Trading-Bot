import alpaca_trade_api as tradeapi
import pandas as pd

#Credentials
BASE_URL = 'https://paper-api.alpaca.markets'
API_KEY = 'PKT232BC2I7MO0IIG3K7'
API_SECRETE = 'p8wHg7oMvcU5MpDdb3Her7hbwiQNVglifD3tumzp'


# Instantials REST Connection
api = tradeapi.REST(key_id=API_KEY, secret_key=API_SECRETE, base_url=BASE_URL, api_version='v2')

# fetch account details
# account = api.get_account()
# print(account)

# Get historical market data
# history_data_AAPL = api.get_bars('AAPL','1D', limit=100)
# print(history_data_AAPL.df.head())

#submitting orders
# orders = api.submit_order(symbol='AAPL', qty=1, side='buy', type='market', time_in_force='day')
# sell = api.submit_order(symbol='TSLA', qty=1, side='sell', type='market', time_in_force='day')


# Get position order
position = api.get_position('TSLA')

# Print the position
print(position)
