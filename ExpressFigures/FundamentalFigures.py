from DataBaseTools.getStockPrice import getStockPrice
from FigureGenerator import Figure
from FigureGenerator.Traces import BarTrace

from DataBaseTools.fundamentalAn import *


def genEPSFigure(ticker):
    fig = Figure()
    fig.set_Title(str(ticker)+" Earnings Per Share")
    fig.set_xLabel("Date")

    df = EPS(ticker)
    trace = BarTrace.BarTrace()
    trace.add_X_values(df["Date"])
    trace.add_Y_values(df["EPS"])
    trace.set_color("darkturquoise")
    trace.set_name(str(ticker)+" EPS")

    fig.add_trace(trace)

    return fig


def genPEFigure(ticker):
    fig = Figure()
    fig.set_Title(str(ticker)+" Price / EPS")
    fig.set_xLabel("Date")

    df = PE(ticker)
    trace = BarTrace.BarTrace()
    trace.add_X_values(df["Date"])
    trace.add_Y_values(df["PE"])
    trace.set_color("midnightblue")
    trace.set_name(str(ticker)+" PE")

    fig.add_trace(trace)

    return fig


def genQuickRatioFigure(ticker):
    fig = Figure()
    fig.set_Title(str(ticker)+" QuickRatio")
    fig.set_xLabel("Date")

    df = QuickRatio(ticker)
    trace = BarTrace.BarTrace()
    trace.add_X_values(df["Date"])
    trace.add_Y_values(df["QuickRatio"])
    trace.set_color("goldenrod")
    trace.set_name(str(ticker)+" QuickRatio")

    fig.add_trace(trace)

    return fig


def genWorkingCapitalRatioFigure(ticker):
    fig = Figure()
    fig.set_Title(str(ticker)+" WorkingCapitalRatio")
    fig.set_xLabel("Date")

    df = WorkingCapitalRatio(ticker)
    trace = BarTrace.BarTrace()
    trace.add_X_values(df["Date"])
    trace.add_Y_values(df["WorkingCapitalRatio"])
    trace.set_color("olive")
    trace.set_name(str(ticker)+" WorkingCapitalRatio")

    fig.add_trace(trace)

    return fig


def genROEFigure(ticker):
    fig = Figure()
    fig.set_Title(str(ticker)+" Rate of exchange")
    fig.set_xLabel("Date")

    df = ROE(ticker)
    trace = BarTrace.BarTrace()
    trace.add_X_values(df["Date"])
    trace.add_Y_values(df["ROE"])
    trace.set_color("darksalmon")
    trace.set_name(str(ticker)+" Rate of exchange")

    fig.add_trace(trace)

    return fig


def genVolumeFigure(ticker):
    fig = Figure()
    fig.set_Title(str(ticker)+" Volume")
    fig.set_xLabel("Date")

    df = getStockPrice(ticker)
    trace = BarTrace.BarTrace()
    trace.add_X_values(df["Date"])
    trace.add_Y_values(df["Volume"])
    trace.set_color("blue")
    trace.set_name(str(ticker)+" Volume")

    fig.add_trace(trace)

    return fig
