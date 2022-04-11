from Application import app

from FigureGenerator import Figure
from FigureGenerator.Traces.ScatterTrace import ScatterTrace
from FigureGenerator.Traces.BarTrace import BarTrace
from FigureGenerator.Traces.LineTrace import LineTrace
from FigureGenerator.Traces.ScatterLineTrace import ScatterLineTrace

from flask import render_template

@app.route("/testing_figures")
def testing_figures():
    fig1 = Figure()
    fig1.set_Title("Testing fig1") # overall title
    fig1.set_Title_font_size(50) # title font size
    
    fig2 = Figure()
    fig2.set_Title("Testing fig2")

    trace = ScatterLineTrace() #also use LineTrace() for line only or ScatterTrace() for dots only
    trace.add_X_values([1,2,3,4,5])
    trace.add_Y_values([2,3,5,3,2])
    trace.set_size(20)  #size of dots
    trace.set_line_width(10) #size of line
    trace.make_dashdotLine() # also use make_dashLine() or make_dotLine()
    trace.set_color("rgba(20,200,200,200)") #set color for both line and dots, can be set as color name
    trace.set_name("ScatRandom") #set name in legend, only shows when multiple traces are on same figure

    trace2 = BarTrace()
    trace2.add_X_values([1, 2, 3, 4, 5])
    trace2.add_Y_values([1, 2, 4, 2, 1])
    trace2.set_color("green") #sets bar color
    trace2.set_name("BarRandom") #set name in legend, only shows when multiple traces are on same figure
    trace2.set_border_width(5) #Used to give borders to the bars
    trace2.set_border_color("purple") #Color of the border line

    fig1.add_trace(trace)
    fig2.add_trace(trace2)

    return render_template("test_templates/testing_figures.html",title="hello",figure1=fig1.render(),figure2=fig2.render())
