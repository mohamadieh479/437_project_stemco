from FigureGenerator._tools import plot_to_html
from plotly import graph_objs as go


class Figure:

    def __init__(self):
        self.traces = []
        self.set_Title(None)
        self.set_Title_font_size(None)
        self.set_xLabel(None)
        self.set_yLabel(None)

    def set_Title(self, title):
        self.layout_title_text=title

    def set_Title_font_size(self, size):
        self.layout_title_font_size=size

    def set_xLabel(self,label):
        self.layout_xaxis_title=label
        
    def set_yLabel(self,label):
        self.layout_yaxis_title=label

    def add_trace(self,trace):
        self.traces.append(trace)

    def render(self):
        fig = go.Figure(
            layout_title_text=self.layout_title_text,
            layout_title_font_size=self.layout_title_font_size,
            layout_xaxis_title=self.layout_xaxis_title,
            layout_yaxis_title=self.layout_yaxis_title
        )
        for i in self.traces:
            fig.add_trace(i.generate())
        return plot_to_html(fig)

    @staticmethod
    def GenTest():
        from plotly.subplots import make_subplots
        fig = make_subplots(rows=1, cols=2)
        fig.add_bar(y=[2, 1, 3], marker_color="red",marker_line_color="green",marker_line_width=10,
                    name="b", row=1, col=1)

        return plot_to_html(fig)
