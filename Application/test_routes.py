from Application import app

from FigureGenerator import Figure
from FigureGenerator.ScatterTrace import ScatterTrace
from FigureGenerator.BarTrace import BarTrace

from flask import render_template

@app.route("/testing_figures")
def testing_figures():
    fig1 = Figure()
    fig1.set_Title("Testing fig1")
    
    fig2 = Figure()
    fig2.set_Title("Testing fig2")

    trace = ScatterTrace()
    trace.add_X_values([1,2,3,4,5])
    trace.add_Y_values([2,3,5,3,2])
    trace.set_size(20)
    trace.set_color("red")
    trace.set_name("ScatRandom")

    trace2 = BarTrace()
    trace2.add_X_values([1, 2, 3, 4, 5])
    trace2.add_Y_values([1, 2, 4, 2, 1])
    trace2.set_color("green")
    trace2.set_name("BarRandom")
    trace2.set_border_width(5)
    trace2.set_border_color("purple")

    fig1.add_trace(trace)
    fig2.add_trace(trace2)

    return render_template("test_templates/testing_figures.html",title="hello",figure1=fig1.render(),figure2=fig2.render())
