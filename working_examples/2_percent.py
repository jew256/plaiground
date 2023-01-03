

import matplotlib.pyplot as plt
import yfinance as yf
import datetime

try:
    # use the yahoo finance api to get any stock data
    stock_data = yf.Ticker("MSFT").history(period="5y")

    # Create a figure and set the style to dark
    plt.style.use("dark_background")
    fig = plt.figure()

    # write an algorithmic trading script using a mean reversion strategy that accesses the yahoo finance api to get financial data, on microsoft stock and a 20-day moving average, risking 2% of the portfolio. then run this strategy on the past 5 years of data and plot the gross profit earned from the strategy. use a starting account balance of $100,000
    start_balance = 100000
    risk_percent = 0.02
    stock_data["20d_ma"] = stock_data["Close"].rolling(window=20).mean()
    stock_data["position"] = None
    for row in range(20, len(stock_data)):
        if stock_data.iloc[row]["Close"] > stock_data.iloc[row]["20d_ma"]:
            stock_data.iloc[row, stock_data.columns.get_loc("position")] = "long"
        else:
            stock_data.iloc[row, stock_data.columns.get_loc("position")] = "short"
    stock_data["balance"] = start_balance
    for row in range(20, len(stock_data)):
        if stock_data.iloc[row]["position"] == "long":
            stock_data.iloc[row, stock_data.columns.get_loc("balance")] = stock_data.iloc[row-1]["balance"] + (stock_data.iloc[row-1]["balance"] * risk_percent)
        elif stock_data.iloc[row]["position"] == "short":
            stock_data.iloc[row, stock_data.columns.get_loc("balance")] = stock_data.iloc[row-1]["balance"] - (stock_data.iloc[row-1]["balance"] * risk_percent)
    stock_data["gross_profit"] = stock_data["balance"] - start_balance

    # Add axes, title, and legend
    ax = fig.add_subplot(111)
    ax.plot(stock_data.index, stock_data["gross_profit"], label="Gross Profit")
    ax.set_title("Gross Profit from Mean Reversion Strategy")
    ax.set_xlabel("Date")
    ax.set_ylabel("Gross Profit")
    ax.legend()

    # Save the graph as test0.png
    plt.savefig("test0.png")

    # Close the graph automatically
    plt.close()

    # write "Successful" to `output.txt`
    with open("output.txt", "w") as f:
        f.write("Successful")

except Exception as e:
    # graph an error symbol and write 'Error: ', and the error to `output.txt`
    plt.style.use("dark_background")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.text(0.5, 0.5, "Error", fontsize=50, ha="center")
    plt.savefig("test0.png")
    plt.close()

    # write a hint for a better prompt to `output.txt`
    with open("output.txt", "w") as f:
        f.write(f"Error: {e}\nHint: Make sure to provide a valid stock ticker and a valid date range")