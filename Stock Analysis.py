# https://www.youtube.com/watch?v=8Vg8GKWrV5M
# import pandas as pd
from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.stream import TradingStream
import config

client = TradingClient(config.API_KEY, config.API_SECRETE, paper=True)
account = dict(client.get_account())
# for k,v in account.items():
#     print(f"{k:30}, {v}")

# buying an order
def trade_buy():
    # Order market requirements.
    order_details = MarketOrderRequest(
        symbol = "AAPL",
        qty = 50,
        side = OrderSide.BUY, # Decide if you are buying long or short
        time_in_force = TimeInForce.DAY
    )

    # Creating an order client
    order = client.submit_order(order_data = order_details) # This line of code automatically buys a order from the market
    trades = TradingStream(config.API_KEY, config.API_SECRETE, paper=True) #define my trade order. This shows the information on my screen. This uses websocket API

    #Subscribe to my trade
    async def trade_status(data):
        print(data)

    trades.subscribe_trade_updates(trade_status)
    trades.run()

# Get all asset
assets = [asset for asset in client.get_all_positions()]
print(assets)

client.close_all_positions(cancel_orders=True)