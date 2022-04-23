from inspect import trace
from FigureGenerator import Figure
from FigureGenerator.Traces import BarTrace

from DataBaseTools.fundamentalAn import EPS, PE


def genEPSFigure(ticker):
    fig = Figure()
    fig.set_Title("Earnings Per Share")

    df = EPS(ticker)
    trace = BarTrace.BarTrace()
    trace.add_X_values(df["Date"])
    trace.add_Y_values(df["EPS"])
    trace.set_color("aquamarine")
    trace.set_name(str(ticker)+"EPS")

    fig.add_trace(trace)

    return fig

def genPEFigure(ticker):
    fig = Figure()
    fig.set_Title("Price / EPS")

    df = PE(ticker)
    trace = BarTrace.BarTrace()
    trace.add_X_values(df["Date"])
    trace.add_Y_values(df["PE"])
    trace.set_color("crimson")
    trace.set_name(str(ticker)+"PE")

    fig.add_trace(trace)

    return fig