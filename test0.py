

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from pandas_datareader import data

try:
    # get stock data
    start_date = datetime.now() - timedelta(days=1825)
    end_date = datetime.now()
    stocks = ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'FB']
    df = data.DataReader(stocks, data_source='yahoo', start=start_date, end=end_date)

    # create figure and set style
    plt.style.use('dark_background')
    fig = plt.figure()

    # graph stock prices
    for stock in stocks:
        df[f'Adj Close {stock}'].plot(label=stock)

    # add axes, title, and legend
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('FAANG Stock Prices')
    plt.legend()

    # save graph
    plt.savefig('test1.png')

    # close graph
    plt.close(fig)

    # write success to output.txt
    with open('output.txt', 'w') as f:
        f.write('Successful')

except Exception as e:
    # write error to output.txt
    with open('output.txt', 'w') as f:
        f.write(f'Error: {e}\nHint: Make sure to use the correct stock symbols and to use the free version of the Yahoo Finance API.')