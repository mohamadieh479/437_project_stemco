from FigureGenerator.Traces._Trace import _Trace
from plotly import graph_objs as go

class ScatterLineTrace(_Trace):

    def __init__(self):
        super().__init__()
        self.set_size(None)
        self.set_line_width(None)
        self.line_dash=None
    
    def make_dashLine(self):
        self.line_dash='dash'
    def make_dotLine(self):
        self.line_dash='dot'
    def make_dashdotLine(self):
        self.line_dash='dashdot'
        
    def set_size(self, size):
        self.marker_size = size

    def set_line_width(self, width):
        self.line_width = width
    

    def generate(self):
        return go.Scatter(x=self.x,
                          y=self.y,
                          name=self.name,
                          marker_color=self.marker_color,

                          line_dash=self.line_dash,
                          line_width = self.line_width,
                          marker_size=self.marker_size,
                          mode='lines+markers'
                          )