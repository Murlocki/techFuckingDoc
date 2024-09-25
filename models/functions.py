import numpy as np
from abc import ABC, abstractmethod
class Functions(ABC):
    def __init__(self, x_interval_str='(-5;5)', y_interval_str='(-5;5)'):
        try:
            self.x_interval = list(map(float, x_interval_str.replace(')', '', 1).replace('(', '', 1).split(';')))
            self.y_interval = list(map(float, y_interval_str.replace(')', '', 1).replace('(', '', 1).split(';')))
        except Exception:
            self.x_interval = [-5,5]
            self.y_interval = [-5,5]
    @abstractmethod
    def get_function(self) -> tuple:
        pass
    @abstractmethod
    def get_function_point(self, x, y):
        pass
    @abstractmethod
    def get_derivative(self, x, y):
        pass
class MatiasFunction(Functions):
    def get_function(self):
        x = np.arange(self.x_interval[0], self.x_interval[1], 0.25)
        y = np.arange(self.y_interval[0], self.y_interval[1], 0.25)
        x, y = np.meshgrid(x, y)
        z = .26 * (x ** 2 + y ** 2) - .48 * x * y
        return x, y, z

    def get_derivative(self, x, y):
        return .52 * x - .48 * y, .52 * y - .48 * x

    def get_function_point(self, x, y):
        return .26 * (x ** 2 + y ** 2) - .48 * x * y
class CamelThreeHumpFunction(Functions):
    def get_function(self):
        x = np.arange(self.x_interval[0], self.x_interval[1], 0.25)
        y = np.arange(self.y_interval[0], self.y_interval[1], 0.25)
        x, y = np.meshgrid(x, y)
        z = 2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2
        return x, y, z
    def get_derivative(self, x, y):
        df_dx = x**5 - 4.2 * x**3 + 4 * x + y
        df_dy = x + 2 * y
        return df_dx, df_dy
    def get_function_point(self, x, y):
        return 2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2
class RosenbrockFunction(Functions):
    def get_function(self):
        x = np.arange(self.x_interval[0], self.x_interval[1], 0.25)
        y = np.arange(self.y_interval[0], self.y_interval[1], 0.25)
        x, y = np.meshgrid(x, y)
        z = (1 - x)**2 + 100 * (y - x**2)**2
        return x, y, z

    def get_function_point(self, x, y):
        return (1 - x)**2 + 100 * (y - x**2)**2

    def get_derivative(self, x, y):
        dx = -2 * (1 - x) - 400 * x * (y - x**2)
        dy = 200 * (y - x**2)
        return dx, dy