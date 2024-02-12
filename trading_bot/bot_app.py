# Import my classes of functions.
import os
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime
from dotenv import load_dotenv

#trade_bot = bot_trade.Trade()
load_dotenv()
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

trade_api = StockHistoricalDataClient(api_key=api_key, secret_key=api_secret)
def get_stock_bar():
    request_param = StockBarsRequest(
        type = 'market',
        symbol_or_symbols = ["SPY"],
        timeframe = TimeFrame.Day,
        start= datetime(2024, 1, 30),
        end_date = datetime(2024, 2, 9)
    )
    bars = trade_api.get_stock_bars(request_param)
    return bars
# get_bars = [bar for bar in get_stock_bar()]
# print((get_bars[0][1]['SPY'][-3:]))

def signal():
    # for loop the dataframe (df) provided
    df = [bar for bar in get_stock_bar()]

    # bar data values for the firs bar
    df_open_bar_one = ((df[0][1]['SPY'][-3:][0].open))
    df_high_bar_one = ((df[0][1]['SPY'][-3:][0].high))
    df_low_bar_one = ((df[0][1]['SPY'][-3:][0].low))
    df_close_bar_one = ((df[0][1]['SPY'][-3:][0].close))
    df_timestamp_one =((df[0][1]['SPY'][-3:][0].timestamp))

    # bar data values for the second bar
    df_open_bar_two = ((df[0][1]['SPY'][-3:][1].open))
    df_high_bar_two = ((df[0][1]['SPY'][-3:][1].high))
    df_low_bar_two = ((df[0][1]['SPY'][-3:][1].low))
    df_close_bar_two = ((df[0][1]['SPY'][-3:][1].close))
    df_timestamp_two = ((df[0][1]['SPY'][-3:][1].timestamp))

    # bar data values for the third bar
    df_open_bar_three = ((df[0][1]['SPY'][-3:][2].open))
    df_high_bar_three = ((df[0][1]['SPY'][-3:][2].high))
    df_low_bar_three = ((df[0][1]['SPY'][-3:][2].low))
    df_close_bar_three = ((df[0][1]['SPY'][-3:][2].close))
    df_timestamp_three = ((df[0][1]['SPY'][-3:][2].timestamp))

    # get the last bar before the previous three bars
    df_open_bar_for_last_close_bar = ((df[0][1]['SPY'][-4].open))
    df_high_bar_for_last_close_bar = ((df[0][1]['SPY'][-4].high))
    df_low_bar_for_last_close_bar = ((df[0][1]['SPY'][-4].low))
    df_close_bar_for_last_close_bar = ((df[0][1]['SPY'][-4].close))
    df_timestamp_last = ((df[0][1]['SPY'][-4].timestamp))

    bearish_body_size = abs(df_open_bar_for_last_close_bar) - df_close_bar_for_last_close_bar
    bullish_body_size = abs(df_open_bar_one) - df_open_bar_one


    # bullish pattern


    # bearish

    # print(f"Three Dataset: {df_open_bar_three}, {df_high_bar_three}, {df_low_bar_three},{df_close_bar_three}, {df_timestamp_three}")
    # print(f"Second Dataset: {df_open_bar_two}, {df_high_bar_two}, {df_low_bar_two},{df_close_bar_two} , {df_timestamp_two}")
    # print(f"One Dataset: {df_open_bar_one}, {df_high_bar_one}, {df_low_bar_one},{df_close_bar_one}, {df_timestamp_one} ")
    #
    # print(f"Last Bar: {df_open_bar_for_last_close_bar}, {df_high_bar_for_last_close_bar}, {df_low_bar_for_last_close_bar}, {df_close_bar_for_last_close_bar}, {df_timestamp_last}")

signal()


