import alpaca_trade_api as tradeapi
from alpaca.data.live import StockDataStream
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, GetOrdersRequest, QueryOrderStatus
from alpaca.trading.stream import TradingStream
from alpaca.trading.enums import OrderSide, TimeInForce
from dotenv import load_dotenv
import os
import json

# Load .env files that stores the API key, API secret, and base URL
load_dotenv()

# Import the API key, API secret, and the base URL
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
base_url = os.getenv('BASE_URL')

# Instantiate my REST API connection
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
trading_client = TradingClient(api_key=api_key, secret_key=api_secret, paper=True)
trading_stream = TradingStream(api_key=api_key, secret_key=api_secret, paper=True)
# This function returns the user account details

# trade app class

class Trade:
    def get_user_account(self):
        try:
            account = api.get_account()
            print(account)
        except Exception as e:
            print(e)

    # This function will buy a stock in the market
    def buy_Sell_market_stock(self,stock_symbol, quantity, stock_side, time_enforce):

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

    # Sell stock

    def limit_buy_sell_stock(self,symbol, limit_price, quantity,order_side,time_in_force):

        """
        If you have a specific target price at which you want to buy or sell an asset,
        a limit order allows you to specify that price and wait for the market to reach it.
        This is particularly useful when you have a target entry or exit point based on your
        analysis or trading strategy.

        type: str("Limit")
        symbol: "SPY", "AAPL"
        limit_price: float
        qty: float
        side: OrderSide.BUY, OrderSide.SELL #This returns a function
        time_in_force: TimeInForce.DAY, TimeInFocrc.FOK # this returns a function
        :return 0:
        """
        limit_order_data = LimitOrderRequest(
            type="Limit", # value: Limit
            symbol=symbol, # value: SPY, AAPL
            limit_price=int(limit_price), # the limit price of the stock
            qty=int(quantity), # value: 1, 10, or 200
            side=order_side, # this takes a function of OrderSide.BUY or orderSide.SELL
            time_in_force=time_in_force # this takes a function of TimeInForce.DAY, TimeInForce.FOK, TimeInForce.GTC etc
        )
        # Limit order
        limit_order = trading_client.submit_order(
            order_data=limit_order_data
        )

    def query_all_order(self, order_status, order_side):
        """
        status: QueryOrderStatus.OPEN, QueryOrderStatus.CLOSED #This requires a function
        side: OrderSide.SELL, OrderSide.BUY #This requires a functions
        :return:
        """
        # params to filter orders by
        request_params = GetOrdersRequest(
            status=order_status,  # value: QueryOrderStatus.CLOSED or QueryOrderStatus.OPEN
            side=order_side  # value: OrderSide.SELL or OrderSide.BUY
        )
        # orders that satisfy params
        orders = trading_client.get_orders(filter=request_params)
        print(orders)

    def cancel_submitted_orders(self):
        # attempt to cancel all open orders
        cancel_statuses = trading_client.cancel_orders()
        return cancel_statuses

    def stream_order_data(self):
        """
            which allows you to stream order updates.
            Whenever an order is submitted, filled, cancelled, etc,
            you will receive a response on the client.
        :return:
        """
        async def get_data(data):
            print(data)
        trading_order_stream = trading_stream.subscribe_trade_updates(get_data)
        print(trading_order_stream)
        trading_stream.run()

    #Getting all Positions in a user account
    def get_all_position(self):
        print(trading_client.get_all_positions())

    #Cancelling all positions including orders
    def close_all_position(self):
        # closes all position AND also cancels all open orders
        trading_client.close_all_positions(cancel_orders=True)

    # Get my candles from Alpaca broker
    def get_candles(self):
        symbol = 'TSLA'
        candles = api.get_bars(symbol=symbol, timeframe='1D')
        for bar in candles:
            print(bar)

    # Get candles in real time using async function
    def get_bars_in_real_time(self):
        try:
            wss_client = StockDataStream(api_key=api_key, secret_key=api_secret) # This create a websocket connection to the Alpaca API and return data in realtime
            async def bar_data_handler(data):
                # bars data will arrive here.
                # print(f"Symbol: {data['symbol']}, Open: {data['open']}, Close: {data['close']}")
                # data_values = json.dumps(data)
                print(data)

            wss_client.subscribe_bars(bar_data_handler, "SPY")
            wss_client.run()
        except Exception as e:
            print(e)

trade_bot = Trade()
trade_bot.get_bars_in_real_time()
#trade_bot.buy_Sell_market_stock("SPY", 1, OrderSide.SELL, TimeInForce.DAY)
