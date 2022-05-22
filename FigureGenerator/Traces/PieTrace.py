from plotly import graph_objs as go

class PieTrace:    
    def __init__(self):
        self.add_labels(None)
        self.add_values(None)
        self.set_borders(None)
        self.set_name(None)


    def set_name(self, name):
        self.name = name

    def add_labels(self, labels):
        self.labels = labels

    def add_values(self, values):
        self.values = values

    def set_borders(self, width):
        self.line_width = width

    def set_info(self,label=False,value=False,percent=False):
        self.textinfo = ""
        if(label):
            self.textinfo+="label"
        if(value):
            if(self.textinfo!=""):
                self.textinfo+="+"
            self.textinfo+="value"
        if(percent):
            if(self.textinfo!=""):
                self.textinfo+="+"
            self.textinfo+="percent"

    def generate(self):
        return go.Pie(values=self.values,
                          labels=self.labels,
                          name=self.name,
                          marker_line_width = self.line_width,
                          textinfo = self.textinfo,
                          insidetextorientation='radial'
                          )