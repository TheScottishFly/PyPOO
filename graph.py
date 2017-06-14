from abc import ABC
import matplotlib as mil
mil.use('TkAgg')
import matplotlib.pyplot as plt


class BaseGraph(ABC):
    """Classe abstraite qui sert de base pour les graphiques"""

    def __init__(self):
        self.title = "Your graph title"
        self.x_label = "X-axis label"
        self.y_label = "X-axis label"
        self.show_grid = True

    def xy_values(self, zones):
        raise NotImplementedError

    def show(self, zones):
        x_values, y_values = self.xy_values(zones)
        plt.plot(x_values, y_values, '.')
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.grid(self.show_grid)
        plt.show()