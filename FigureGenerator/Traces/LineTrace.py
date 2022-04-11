from FigureGenerator.Traces._Trace import _Trace
from plotly import graph_objs as go

class LineTrace(_Trace):

    def __init__(self):
        super()
        self.set_line_width(None)

    def set_line_width(self, width):
        self.line_width = width


    def generate(self):
        return go.Scatter(x=self.x,
                          y=self.y,
                          name=self.name,
                          marker_color=self.marker_color,

                          line_width = self.line_width,
                          mode='lines'
                          )