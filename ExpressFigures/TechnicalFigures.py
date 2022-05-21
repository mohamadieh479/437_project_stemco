from asyncio.windows_events import NULL
from FigureGenerator import Figure
from FigureGenerator.Traces import LineTrace,CandleStickTrace

from Analysis.technicalAn import *

def genRSIFigure(ticker):
    fig = Figure()
    fig.set_Title(str(ticker)+" Relative strength index")
    fig.set_xLabel("Date")

    df = RSI(ticker)
    trace = LineTrace.LineTrace()
    trace.add_X_values(df["Date"])
    trace.add_Y_values(df["RSI"])
    trace.set_color("goldenrod")
    trace.set_name(str(ticker)+" RSI")

    upper = [70 for i in df["Date"]]
    lower = [30 for i in df["Date"]]

    tu= LineTrace.LineTrace()
    tu.add_X_values(df["Date"])
    tu.add_Y_values(upper)
    tu.set_color("grey")
    tu.make_dashLine()
    tu.set_name("70%")

    tl = LineTrace.LineTrace()
    tl.add_X_values(df["Date"])
    tl.add_Y_values(lower)
    tl.set_color("grey")
    tl.make_dashLine()
    tl.set_name("30%")

    fig.add_trace(tu)
    fig.add_trace(trace)
    fig.add_trace(tl)

    return fig

def genATRFigure(ticker):
    fig = Figure()
    fig.set_Title(str(ticker)+" Average True Range")
    fig.set_xLabel("Date")

    df = ATR(ticker)
    trace = LineTrace.LineTrace()
    trace.add_X_values(df["Date"])
    trace.add_Y_values(df["ATR"])
    trace.set_color("red")
    trace.set_name(str(ticker)+" ATR")

    fig.add_trace(trace)

    return fig

def genCandleStickWithInd(ticker,bb=False,moving_average=False,exponential_moving_average=False,avg_window=10):
    df = getStockPrice(ticker)

    fig = Figure()
    fig.set_Title(str(ticker)+" stock history")
    fig.set_xLabel("Date")
    fig.set_yLabel("Price")

    trace = CandleStickTrace.CandleStickTrace()
    trace.set_name(str(ticker))
    trace.add_X_values(df["Date"].tolist())
    trace.add_open_values(df["Open"].tolist())
    trace.add_low_values(df["Low"].tolist())
    trace.add_high_values(df["High"].tolist())
    trace.add_close_values(df["Close"].tolist())
    trace.set_increasing_line_color("green")
    trace.set_decreasing_line_color("red")


    if(bb==True):
        dfbb = BB(ticker)
        bbu = LineTrace.LineTrace()
        bbu.add_X_values(df["Date"])
        bbu.add_Y_values(dfbb["upper_band"])
        bbu.set_color("blue")
        bbu.set_name(str(ticker)+" upper Bollinger band")
        bbu.set_line_width(1)
        fig.add_trace(bbu)

    fig.add_trace(trace)

    if(moving_average==True):
        dfma = movingAverage(ticker,avg_window)
        ma = LineTrace.LineTrace()
        ma.add_X_values(df["Date"])
        ma.add_Y_values(dfma)
        ma.set_color("midnightblue")
        ma.set_name(str(ticker)+" moving average")
        ma.set_line_width(1)
        fig.add_trace(ma)
    if(exponential_moving_average==True):
        dfema = exponentialMovingAverage(ticker,avg_window)
        ema = LineTrace.LineTrace()
        ema.add_X_values(df["Date"])
        ema.add_Y_values(dfema)
        ema.set_color("blueviolet")
        ema.set_name(str(ticker)+"exponential moving average")
        ema.set_line_width(1)
        fig.add_trace(ema)
    if(bb==True):
            bbm = LineTrace.LineTrace()
            bbm.add_X_values(df["Date"])
            bbm.add_Y_values(dfbb["moving_average"])
            bbm.set_color("orange")
            bbm.set_name(str(ticker)+" Bollinger moving average")
            bbm.set_line_width(1)
            fig.add_trace(bbm)
            bbl = LineTrace.LineTrace()
            bbl.add_X_values(df["Date"])
            bbl.add_Y_values(dfbb["lower_band"])
            bbl.set_color("blue")
            bbl.set_name(str(ticker)+" lower Bollinger band")
            bbl.set_line_width(1)
            fig.add_trace(bbl)

    return fig