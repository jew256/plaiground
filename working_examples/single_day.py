

import yfinance as yf
import matplotlib.pyplot as plt

# 1. use the yahoo finance api to get any stock data
data = yf.download('AAPL', start='2022-12-20', end='2022-12-21', interval='5m')

# 2. Create a figure and set the style to dark
plt.style.use('dark_background')
fig = plt.figure()

# 3. graph apple's closing price for december 20th to 21st, 2022 on a 5 minute timescale
plt.plot(data['Close'], label='AAPL')

# 4. Add axes, title, and legend
plt.xlabel('Time')
plt.ylabel('Closing Price')
plt.title('Apple Closing Price (Dec 20-21, 2022)')
plt.legend()

# 5. Save the graph as test0.png
plt.savefig('test0.png')

# 6. Close the graph automatically
plt.close(fig)