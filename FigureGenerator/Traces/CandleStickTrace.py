from plotly import graph_objs as go

class CandleStickTrace():

    def __init__(self):
        self.set_name(None)
        self.set_increasing_line_color(None)
        self.set_decreasing_line_color(None)
        self.add_X_values(None)
        self.add_open_values(None)
        self.add_low_values(None)
        self.add_high_values(None)
        self.add_close_values(None)
        
        
    def set_name(self, name):
        self.name = name
        
    def add_X_values(self, x):
        self. x = x
    
    def add_open_values(self, x):
        self.open = x
        
    def add_low_values(self, x):
        self.low = x
        
    def add_high_values(self, x):
        self.high = x
        
    def add_close_values(self, x):
        self.close = x
        
    def set_increasing_line_color(self,color):
        self.increasing_line_color=color
        
    def set_decreasing_line_color(self,color):
        self.decreasing_line_color=color
        
    def generate(self):
        return go.Candlestick(
                            name=self.name,
                            x=self.x,
                            open=self.open,
                            low=self.low,
                            high=self.high,
                            close=self.close,
                            increasing_line_color=self.increasing_line_color,
                            decreasing_line_color=self.decreasing_line_color
                          )
        
    