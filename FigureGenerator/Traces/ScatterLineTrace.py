from FigureGenerator.Traces._Trace import _Trace
from plotly import graph_objs as go

class ScatterLineTrace(_Trace):

    def __init__(self):
        super()
        self.set_size(None)
        self.set_line_width(None)
        
    def set_size(self, size):
        self.marker_size = size

    def set_line_width(self, width):
        self.line_width = width
    

    def generate(self):
        return go.Scatter(x=self.x,
                          y=self.y,
                          name=self.name,
                          marker_color=self.marker_color,

                          line_width = self.line_width,
                          marker_size=self.marker_size,
                          mode='lines+markers'
                          )