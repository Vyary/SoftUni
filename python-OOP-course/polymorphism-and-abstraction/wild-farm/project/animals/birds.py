from project.animals.animal import Bird
from project.food import Fruit, Meat, Seed, Vegetable


class Owl(Bird):
    eats = [Meat]
    weight_gain = 0.25

    def make_sound(self) -> str:
        return "Hoot Hoot"


class Hen(Bird):
    eats = [Vegetable, Fruit, Meat, Seed]
    weight_gain = 0.35

    def make_sound(self) -> str:
        return "Cluck"
