# -*- coding: utf-8 -*-
"""Untitled26.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h6W7SIfLPoDMStOYnDVNk-jaeb3nxw3J
"""

pip install yfinance

import yfinance as yf

stock_symbol="AAPL"

stock_data=yf.Ticker(stock_symbol)

historical_prices=stock_data.history(period="1d",start="2023-01-01",end="2023-08-19")

print(historical_prices)

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA


stock_symbol="AAPL"
stock_data=yf.Ticker(stock_symbol)

historical_data=stock_data.history(period="1y")
closing_prices=historical_data['Close']

train_size=int(len(closing_prices)*0.8)
train_data,test_data=closing_prices[:train_size],closing_prices[train_size:]

order=(5,1,0)
model=ARIMA(train_data,order=order)
model_fit=model.fit()

forecast_steps=len(test_data)
forecast=model_fit.forecast(steps=forecast_steps)

forecast_index=pd.date_range(start=closing_prices.index[train_size],periods=forecast_steps,freq='D')
forecast_series=pd.Series(forecast,index=forecast_index)

plt.figure(figsize=(12,6))
plt.plot(closing_prices,label='Actual Prices')
plt.plot(train_data.index,model_fit.fittedvalues,color='red',label='Fitted values')
plt.plot(forecast_series.index,forecast_series,color='g',label='Forecasted Prices')
plt.xlabel('Date')
plt.xlabel('Price')
plt.title(f'Stock Price Prediction for {stock_symbol}')
plt.legend()
plt.show()

import yfinance as yf

stock_symbol = "AMZN"

stock_data = yf.Ticker(stock_symbol)

historical_prices = stock_data.history(period="1d", start="2023-01-01", end="2023-08-19")

print(historical_prices)

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA


stock_symbol="AMZN"
stock_data=yf.Ticker(stock_symbol)

historical_data=stock_data.history(period="1y")
closing_prices=historical_data['Close']

train_size=int(len(closing_prices)*0.8)
train_data,test_data=closing_prices[:train_size],closing_prices[train_size:]

order=(5,1,0)
model=ARIMA(train_data,order=order)
model_fit=model.fit()

forecast_steps=len(test_data)
forecast=model_fit.forecast(steps=forecast_steps)

forecast_index=pd.date_range(start=closing_prices.index[train_size],periods=forecast_steps,freq='D')
forecast_series=pd.Series(forecast,index=forecast_index)

plt.figure(figsize=(12,6))
plt.plot(closing_prices,label='Actual Prices')
plt.plot(train_data.index,model_fit.fittedvalues,color='red',label='Fitted values')
plt.plot(forecast_series.index,forecast_series,color='g',label='Forecasted Prices')
plt.xlabel('Date')
plt.xlabel('Price')
plt.title(f'Stock Price Prediction for {stock_symbol}')
plt.legend()
plt.show()

import yfinance as yf

stock_symbol = "NFLX"

stock_data = yf.Ticker(stock_symbol)

historical_prices = stock_data.history(period="1d", start="2023-01-01", end="2023-08-19")

print(historical_prices)

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA


stock_symbol="NFLX"
stock_data=yf.Ticker(stock_symbol)

historical_data=stock_data.history(period="1y")
closing_prices=historical_data['Close']

train_size=int(len(closing_prices)*0.8)
train_data,test_data=closing_prices[:train_size],closing_prices[train_size:]

order=(5,1,0)
model=ARIMA(train_data,order=order)
model_fit=model.fit()

forecast_steps=len(test_data)
forecast=model_fit.forecast(steps=forecast_steps)

forecast_index=pd.date_range(start=closing_prices.index[train_size],periods=forecast_steps,freq='D')
forecast_series=pd.Series(forecast,index=forecast_index)

plt.figure(figsize=(12,6))
plt.plot(closing_prices,label='Actual Prices')
plt.plot(train_data.index,model_fit.fittedvalues,color='red',label='Fitted values')
plt.plot(forecast_series.index,forecast_series,color='g',label='Forecasted Prices')
plt.xlabel('Date')
plt.xlabel('Price')
plt.title(f'Stock Price Prediction for {stock_symbol}')
plt.legend()
plt.show()

import yfinance as yf

stock_symbol = "CSCO"

stock_data = yf.Ticker(stock_symbol)

historical_prices = stock_data.history(period="1d", start="2023-01-01", end="2023-08-19")

print(historical_prices)

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA


stock_symbol="CSCO"
stock_data=yf.Ticker(stock_symbol)

historical_data=stock_data.history(period="1y")
closing_prices=historical_data['Close']

train_size=int(len(closing_prices)*0.8)
train_data,test_data=closing_prices[:train_size],closing_prices[train_size:]

order=(5,1,0)
model=ARIMA(train_data,order=order)
model_fit=model.fit()

forecast_steps=len(test_data)
forecast=model_fit.forecast(steps=forecast_steps)

forecast_index=pd.date_range(start=closing_prices.index[train_size],periods=forecast_steps,freq='D')
forecast_series=pd.Series(forecast,index=forecast_index)

plt.figure(figsize=(12,6))
plt.plot(closing_prices,label='Actual Prices')
plt.plot(train_data.index,model_fit.fittedvalues,color='red',label='Fitted values')
plt.plot(forecast_series.index,forecast_series,color='g',label='Forecasted Prices')
plt.xlabel('Date')
plt.xlabel('Price')
plt.title(f'Stock Price Prediction for {stock_symbol}')
plt.legend()
plt.show()

import yfinance as yf

stock_symbol = "V"

stock_data = yf.Ticker(stock_symbol)

historical_prices = stock_data.history(period="1d", start="2023-01-01", end="2023-08-19")

print(historical_prices)

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA


stock_symbol="V"
stock_data=yf.Ticker(stock_symbol)

historical_data=stock_data.history(period="1y")
closing_prices=historical_data['Close']

train_size=int(len(closing_prices)*0.8)
train_data,test_data=closing_prices[:train_size],closing_prices[train_size:]

order=(5,1,0)
model=ARIMA(train_data,order=order)
model_fit=model.fit()

forecast_steps=len(test_data)
forecast=model_fit.forecast(steps=forecast_steps)

forecast_index=pd.date_range(start=closing_prices.index[train_size],periods=forecast_steps,freq='D')
forecast_series=pd.Series(forecast,index=forecast_index)

plt.figure(figsize=(12,6))
plt.plot(closing_prices,label='Actual Prices')
plt.plot(train_data.index,model_fit.fittedvalues,color='red',label='Fitted values')
plt.plot(forecast_series.index,forecast_series,color='g',label='Forecasted Prices')
plt.xlabel('Date')
plt.xlabel('Price')
plt.title(f'Stock Price Prediction for {stock_symbol}')
plt.legend()
plt.show()