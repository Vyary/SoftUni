import math
from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return 1 / 2 * self.base * self.height


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2


class AreaCalculator:
    def __init__(self, shapes: List[Shape]):
        for shape in shapes:
            if not isinstance(shape, Shape):
                raise TypeError("All items in `shapes` must be of type `Shape`.")

        self.shapes = shapes

    @property
    def total_area(self):
        return sum(shape.area() for shape in self.shapes)


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)
