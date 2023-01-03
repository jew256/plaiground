

import matplotlib.pyplot as plt
import yfinance as yf

try:
    # use the yahoo finance api to get any stock data
    data = yf.Ticker("AAPL").history(start="2020-01-01", end="2020-12-31")

    # Create a figure and set the style to dark
    plt.style.use('dark_background')
    fig = plt.figure()

    # graph apple's closing price for 2020
    plt.plot(data.index, data['Close'], label="Apple's Closing Price")

    # Add axes, title, and legend
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Apple\'s Closing Price in 2020')
    plt.legend()

    # Save the graph as test0.png
    plt.savefig('test0.png')

    # Close the graph automatically
    plt.close(fig)

    # write "Successful" to output.txt
    with open('output.txt', 'w') as f:
        f.write('Successful')

except Exception as e:
    # graph an error symbol and write 'Error: ', and the error to output.txt
    plt.style.use('dark_background')
    fig = plt.figure()
    plt.text(0.5, 0.5, 'Error', fontsize=50, ha='center')
    plt.savefig('test0.png')
    plt.close(fig)

    with open('output.txt', 'w') as f:
        f.write('Error: ' + str(e) + '\n')
        f.write('Hint: Make sure to provide a valid stock ticker and a readable date format.')