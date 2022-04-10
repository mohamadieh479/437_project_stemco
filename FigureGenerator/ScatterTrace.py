from FigureGenerator._Trace import _Trace
from plotly import graph_objs as go

class ScatterTrace(_Trace):

    def __init__(self):
        super()
        self.set_size(None)

    def set_size(self, size):
        self.marker_size = size


    def generate(self):
        return go.Scatter(x=self.x,
                          y=self.y,
                          name=self.name,
                          marker_color=self.marker_color,

                          marker_size=self.marker_size
                          )