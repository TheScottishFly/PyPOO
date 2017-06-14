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


class AgreeablenessGraph(BaseGraph):

    def __init__(self):
        super().__init__()
        self.title = "Nice people live in the countryside"
        self.x_label = "population density"
        self.y_label = "agreeableness"

    def xy_values(self, zones):
        x_values = [zone.population_density() for zone in zones]
        y_values = [zone.average_agreeableness() for zone in zones]
        return x_values, y_values
