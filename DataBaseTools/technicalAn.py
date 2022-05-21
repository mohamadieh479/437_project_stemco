import pandas as pd
from ta.volatility import BollingerBands, AverageTrueRange
from ta.momentum import rsi
from ta.utils import _sma, _ema
from DataBaseTools.getStockPrice import getStockPrice
from FigureGenerator.Traces.ScatterTrace import ScatterTrace
from FigureGenerator.Traces.ScatterLineTrace import ScatterLineTrace


# Bollinger Bands
# this function takes as input a ticker and returns a dataframe of the bollingerband values (upper_band, moving_average, lower_band)
# Naming BB to not have conflict with library naming


def BB(ticker):
    data = getStockPrice(ticker)
    bb_indicator = BollingerBands(data['Close'])
    data['upper_band'] = bb_indicator.bollinger_hband()
    data['lower_band'] = bb_indicator.bollinger_lband()
    data['moving_average'] = bb_indicator.bollinger_mavg()
    return data[['upper_band', 'moving_average', 'lower_band']]

# RSI
# this function takes as input a ticker and returns a dataframe of the RSI values


def RSI(ticker):
    data = getStockPrice(ticker)
    data['RSI'] = rsi(data['Close'])
    return data['RSI']


# movingAverage
# this function takes as input a ticker and the size of the window and returns a dataframe of the moving average
def movingAverage(ticker, window):
    data = getStockPrice(ticker)
    data['movingAverage'] = _sma(data['Close'], window)
    return data['movingAverage']


# exponential moving Average
# this function takes as input a ticker and the size of the window and returns a dataframe of the exponential moving average
def exponentialMovingAverage(ticker, window):
    data = getStockPrice(ticker)
    data['exponentialMovingAverage'] = _ema(data['Close'], window)
    return data['exponentialMovingAverage']

# AverageTrueRange
# this function takes as input a ticker and returns a dataframe of the average true range


def ATR(ticker):
    data = getStockPrice(ticker)
    atr_indicator = AverageTrueRange(data['High'], data['Low'], data['Close'])
    data['ATR'] = atr_indicator.average_true_range()
    return data['ATR']


def handleRequest(x_values, df, indicator):
    if indicator == 'BB':
        upper_band = ScatterLineTrace()
        upper_band.add_X_values(x_values)
        upper_band.add_Y_values(df['upper_band'].tolist())
        upper_band.set_name("Upper Band")
        upper_band.set_color("blue")
        upper_band.set_size(1)

        lower_band = ScatterLineTrace()
        lower_band.add_X_values(x_values)
        lower_band.add_Y_values(df['lower_band'].tolist())
        lower_band.set_name("Lower Band")
        lower_band.set_color("orange")
        lower_band.set_size(1)

        moving_average = ScatterLineTrace()
        moving_average.add_X_values(x_values)
        moving_average.add_Y_values(df['moving_average'].tolist())
        moving_average.set_name("Moving Average")
        moving_average.set_color("red")
        moving_average.set_size(1)
        return (upper_band, lower_band, moving_average)

    elif indicator == 'RSI':
        rsi = ScatterLineTrace()
        rsi.add_X_values(x_values)
        rsi.add_Y_values(df.tolist())
        rsi.set_name("Relative Strength Index")
        rsi.set_color("rgb(251,192,45)")
        rsi.set_size(1)
        return rsi

    elif indicator == 'ATR':
        atr = ScatterLineTrace()
        atr.add_X_values(x_values)
        atr.add_Y_values(df.tolist())
        atr.set_name("Average True Range")
        atr.set_color("rgb(126,87,194)")
        atr.set_size(1)
        return atr

    elif indicator == 'MA':
        ma = ScatterLineTrace()
        ma.add_X_values(x_values)
        ma.add_Y_values(df.tolist())
        ma.set_name("Moving Average")
        ma.set_color("rgb(16,295,123")
        ma.set_size(1)
        return ma
    else:
        return None
