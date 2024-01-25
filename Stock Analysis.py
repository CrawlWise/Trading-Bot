import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def stock_analysis(ticker, start_date, end_date):
    # Fetch historical data
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    # Calculate daily returns
    stock_data['Daily_Return'] = stock_data['Adj Close'].pct_change()

    # Plot stock chart
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Adj Close'], label=f'{ticker} Stock Price')
    plt.title(f'{ticker} Stock Price and Daily Returns')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.legend()

    # Plot daily returns on a secondary y-axis
    ax2 = plt.gca().twinx()
    ax2.plot(stock_data['Daily_Return'], color='red', label='Daily Returns')
    ax2.set_ylabel('Daily Returns')
    ax2.legend(loc='upper right')

    # Show the plot
    plt.show()

    # Display the first few rows of the stock data
    print("\nStock Data:")
    print(stock_data.head())

if __name__ == "__main__":
    # Replace 'AAPL' with the desired ticker symbol
    ticker_symbol = 'AAPL'
    start_date = '2022-01-01'
    end_date = '2024-01-01'

    stock_analysis(ticker_symbol, start_date, end_date)
