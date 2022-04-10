from flask import Markup
from json import dumps
from plotly.utils import PlotlyJSONEncoder


def plot_to_html(plt):
    pltJSON = dumps(plt, cls=PlotlyJSONEncoder)
    return json_to_html(pltJSON)


plotID = 0


def json_to_html(graphJSON):
    global plotID
    plotID += 1
    return Markup("<div id = \"chart"+str(plotID)+"\"></div>\n\
            <script src=\"https://cdn.plot.ly/plotly-latest.min.js\"></script>\n\
            <script>\n\
                var graph = "+graphJSON+"\n\
                Plotly.plot(\"chart"+str(plotID)+"\",graph,{})\n\
            </script>\n")