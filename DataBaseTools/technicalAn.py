import pandas as pd
from ta.volatility import BollingerBands, AverageTrueRange
from ta.momentum import rsi
from ta.utils import _sma,_ema
from getStockPrice import getStockPrice

#Bollinger Bands
#this function takes as input a ticker and returns a dataframe of the bollingerband values (upper_band, moving_average, lower_band)
#Naming BB to not have conflict with library naming
def BB(ticker):
    data= getStockPrice(ticker)
    bb_indicator = BollingerBands(data['Close'])
    data['upper_band'] = bb_indicator.bollinger_hband()
    data['lower_band'] = bb_indicator.bollinger_lband()
    data['moving_average'] = bb_indicator.bollinger_mavg()
    return data[['upper_band','moving_average','lower_band']]

#RSI
#this function takes as input a ticker and returns a dataframe of the RSI values
def RSI(ticker):
    data= getStockPrice(ticker)
    data['RSI'] = rsi(data['Close'])
    return data['RSI']



#movingAverage
#this function takes as input a ticker and the size of the window and returns a dataframe of the moving average
def movingAverage(ticker,window):
    data= getStockPrice(ticker)
    data['movingAverage'] = _sma(data['Close'],window)
    return data['movingAverage']


#exponential moving Average
#this function takes as input a ticker and the size of the window and returns a dataframe of the exponential moving average
def exponentialMovingAverage(ticker,window):
    data= getStockPrice(ticker)
    data['exponentialMovingAverage'] = _ema(data['Close'],window)
    return data['exponentialMovingAverage'] 

#AverageTrueRange
#this function takes as input a ticker and returns a dataframe of the average true range
def ATR(ticker):
    data= getStockPrice(ticker)
    atr_indicator = AverageTrueRange(data['High'],data['Low'],data['Close'])
    data['ATR'] = atr_indicator.average_true_range()
    return data['ATR']

