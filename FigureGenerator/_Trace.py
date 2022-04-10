from abc import ABC, abstractmethod

class _Trace(ABC):

    def __init__(self):
        self.add_X_values(None)
        self.add_Y_values(None)
        self.set_name(None)
        self.set_color(None)


    def add_X_values(self, x):
        self. x = x

    def add_Y_values(self, y):
        self. y = y

    def set_name(self, name):
        self.name = name

    def set_color(self ,color):
        self.marker_color = color
        # TODO check color options

    @abstractmethod
    def generate(self):
        pass