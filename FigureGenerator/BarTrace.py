from FigureGenerator._Trace import _Trace
from plotly import graph_objs as go

class BarTrace(_Trace):

    def __init__(self):
        super()
        self.set_border_width(None)
        self.set_border_color(None)

    def set_border_width(self, width):
        self.marker_line_width = width

    def set_border_color(self, color):
        self.marker_line_color = color


    def generate(self):
        return go.Bar(x=self.x,
                          y=self.y,
                          name=self.name,
                          marker_color=self.marker_color,

                          marker_line_width=self.marker_line_width,
                          marker_line_color=self.marker_line_color
                          )