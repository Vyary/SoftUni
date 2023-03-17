from abc import ABC, abstractmethod
from typing import Union

from project.food import Fruit, Meat, Seed, Vegetable


class Animal(ABC):
    eats = []
    weight_gain = 0

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten: int = 0

    @abstractmethod
    def make_sound(self) -> str:
        ...

    def feed(self, food: Union[Vegetable, Fruit, Meat, Seed]):
        if food.__class__ not in self.__class__.eats:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * self.weight_gain
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__} "
            f"[{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
        )


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__} "
            f"[{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
        )
