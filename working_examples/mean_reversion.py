

import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime

try:
    # use the yahoo finance api to get any stock data
    stock_data = yf.Ticker("MSFT").history(start="2015-01-01", end="2020-01-01")

    # Create a figure and set the style to dark
    plt.style.use('dark_background')
    fig = plt.figure()

    # write an algorithmic trading script using a mean reversion strategy that accesses the yahoo finance api to get financial data, on microsoft stock and a 20-day moving average. then run this strategy on the past 5 years of data and plot the profit gained from the strategy. use a starting account balance of $100,000
    # calculate the 20-day moving average
    stock_data['20d_ma'] = stock_data['Close'].rolling(window=20).mean()
    # set the starting account balance
    account_balance = 100000
    # create a list to store the profits
    profits = []
    # loop through the data
    for index, row in stock_data.iterrows():
        # if the stock price is below the 20-day moving average, buy
        if row['Close'] < row['20d_ma']:
            # buy the stock
            account_balance -= row['Close']
        # if the stock price is above the 20-day moving average, sell
        elif row['Close'] > row['20d_ma']:
            # sell the stock
            account_balance += row['Close']
        # append the profits to the list
        profits.append(account_balance)

    # Add axes, title, and legend
    plt.plot(stock_data.index, profits, label="Profits")
    plt.title("Mean Reversion Strategy Profits")
    plt.xlabel("Date")
    plt.ylabel("Profits")
    plt.legend()

    # Save the graph as test0.png
    plt.savefig("test0.png")

    # Close the graph automatically
    plt.close(fig)

    # write "Successful" to output.txt
    with open("output.txt", "w") as f:
        f.write("Successful")

except Exception as e:
    # graph an error symbol
    plt.style.use('dark_background')
    fig = plt.figure()
    plt.plot([], [], marker="x", label="Error")
    plt.title("Error")
    plt.xlabel("Date")
    plt.ylabel("Error")
    plt.legend()
    plt.savefig("test0.png")
    plt.close(fig)

    # write 'Error: ', and the error to output.txt
    with open("output.txt", "w") as f:
        f.write("Error: " + str(e))
        f.write("\nHint: Make sure to provide a valid stock ticker, start date, and end date in the format YYYY-MM-DD")