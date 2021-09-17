import numpy as np
import pandas as pd

import yfinance as yf
Data viz library





EURUSD


fig = go.Figure()


fig.add_trace(go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'market data'))


fig.update_layout(
    title='EURUSD')

fig.show()
high=data.iloc[-2,1]
low=data.iloc[-2,2]
close=data.iloc[-2,3]
data=data.round(4)



if data.iloc[-1,0]:
    status.append('buy')
   
elif data.iloc[-1,0]:
    status.append('sell')
  
           
         
           
          ------------------------------------------------------

'GBPUSD

fig = go.Figure()


fig.add_trace(go.Candlestick(x=data1.index,
                open=data1['Open'],
                high=data1['High'],
                low=data1['Low'],
                close=data1['Close'], name = 'market data'))


fig.update_layout(
    title='GBPUSD')

fig.show()
high=data1.iloc[-2,1]
low=data1.iloc[-2,2]
close=data1.iloc[-2,3]


if data1.iloc[-1,0]>close:
   
elif data1.iloc[-1,0]<=low:
  





'AUDUSD

fig = go.Figure()


fig.add_trace(go.Candlestick(x=data2.index,
                open=data2['Open'],
                high=data2['High'],
                low=data2['Low'],
                close=data2['Close'], name = 'market data'))


fig.update_layout(
    title='AUDUSD')

fig.show()

high=data2.iloc[-2,1]
low=data2.iloc[-2,2]
close=data2.iloc[-2,3]
data2=data2.round(4)

   
elif data2.iloc[-1,0]<=low:
    status2.append('sell')
   




EURGBP

fig = go.Figure()


fig.add_trace(go.Candlestick(x=data3.index,
                open=data3['Open'],
                high=data3['High'],
                low=data3['Low'],
                close=data3['Close'], name = 'market data'))


fig.update_layout(
    title='EURGBP')

fig.show()

high=data3.iloc[-2,1]
low=data3.iloc[-2,2]
close=data3.iloc[-2,3]
