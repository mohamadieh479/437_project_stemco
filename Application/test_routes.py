from ExpressFigures.FundamentalFigures import genEPSFigure, genPEFigure
from DataBaseTools.getStockPrice import getStockPrice
from Application import app

from FigureGenerator import Figure
from FigureGenerator.Traces.ScatterTrace import ScatterTrace
from FigureGenerator.Traces.BarTrace import BarTrace
from FigureGenerator.Traces.LineTrace import LineTrace
from FigureGenerator.Traces.ScatterLineTrace import ScatterLineTrace
from FigureGenerator.Traces.CandleStickTrace import CandleStickTrace

from flask import render_template, request


@app.route("/testing_figures")
def testing_figures():
    fig1 = Figure()
    fig1.set_Title("Testing fig1")  # overall title
    fig1.set_Title_font_size(50)  # title font size
    fig1.set_xLabel("X LABEL")  # x axis label
    fig1.set_yLabel("Y LABEL")  # y axis label

    fig2 = Figure()
    fig2.set_Title("Testing fig2")

    # also use LineTrace() for line only or ScatterTrace() for dots only
    trace = ScatterLineTrace()
    trace.add_X_values([1, 2, 3, 4, 5])
    trace.add_Y_values([2, 3, 5, 3, 2])
    trace.set_size(20)  # size of dots
    trace.set_line_width(10)  # size of line
    trace.make_dashdotLine()  # also use make_dashLine() or make_dotLine()
    # set color for both line and dots, can be set as color name
    trace.set_color("rgba(20,200,200,200)")
    # set name in legend, only shows when multiple traces are on same figure
    trace.set_name("ScatRandom")

    trace2 = BarTrace()
    trace2.add_X_values([1, 2, 3, 4, 5])
    trace2.add_Y_values([1, 2, 4, 2, 1])
    trace2.set_color("green")  # sets bar color
    # set name in legend, only shows when multiple traces are on same figure
    trace2.set_name("BarRandom")
    trace2.set_border_width(5)  # Used to give borders to the bars
    trace2.set_border_color("purple")  # Color of the border line

    fig1.add_trace(trace)
    fig2.add_trace(trace2)

    fig3 = Figure()
    fig3.set_Title("Testing CandleStick")

    from datetime import datetime
    dates = [datetime(year=2013, month=10, day=10),
             datetime(year=2013, month=11, day=10),
             datetime(year=2013, month=12, day=10),
             datetime(year=2014, month=1, day=10),
             datetime(year=2014, month=2, day=10)]
    #dates = ["2013-10-10","2013-11-10","2013-12-10","2014-1-10","2014-2-10"]
    # the two dates lists are identical and interchangeable

    candleTrace = CandleStickTrace()
    # Yes you can add more lines and stuff on the same graph
    candleTrace.set_name("CandleTrace")
    candleTrace.add_X_values(dates)
    # All 4 values need to be set or else you''l get an empty graph
    candleTrace.add_open_values([33.0, 33.3, 33.5, 33.0, 34.1])
    candleTrace.add_low_values([32.7, 32.7, 32.8, 32.6, 32.8])
    candleTrace.add_high_values([33.1, 33.3, 33.6, 33.2, 34.8])
    candleTrace.add_close_values([33.0, 32.9, 33.3, 33.1, 33.1])
    candleTrace.set_increasing_line_color("green")
    candleTrace.set_decreasing_line_color("black")

    fig3.add_trace(candleTrace)

    return render_template("test_templates/testing_figures.html",
                           title="hello",
                           figure1=fig1.render(),
                           figure2=fig2.render(),
                           figure3=fig3.render()
                           )

### This has been moved to the routes.py file ###


@app.route("/testing_candleStickChart")
def testing_candleStickChart():
    df = getStockPrice("MMM")

    fig = Figure()
    fig.set_Title("MMM stock history")
    fig.set_xLabel("Date")
    fig.set_yLabel("Price")

    trace = CandleStickTrace()
    trace.set_name("MMM")
    trace.add_X_values(df["Date"].tolist())
    trace.add_open_values(df["Open"].tolist())
    trace.add_low_values(df["Low"].tolist())
    trace.add_high_values(df["High"].tolist())
    trace.add_close_values(df["Close"].tolist())
    trace.set_increasing_line_color("green")
    trace.set_decreasing_line_color("red")

    fig.add_trace(trace)

    fig2 = Figure()
    fig2.set_xLabel("Date")
    fig2.set_yLabel("Volume")

    volTrace = BarTrace()
    volTrace.add_X_values(df["Date"].tolist())
    volTrace.add_Y_values(df["Volume"].tolist())
    volTrace.set_color("blue")
    volTrace.set_name("Volume")

    fig2.add_trace(volTrace)

    return render_template("test_templates/testing_figures.html",
                           title="MMM stock data",
                           figure1=fig.render(),
                           figure2=fig2.render()
                           )


@app.route("/testing_ExpressFigures")
def testing_ExpressFigures():
    return render_template("test_templates/testing_figures.html",
                           title="MMM stock data",
                           figure1=genEPSFigure("AAPL").render(),
                           figure2=genPEFigure("AAPL").render()
                           )
