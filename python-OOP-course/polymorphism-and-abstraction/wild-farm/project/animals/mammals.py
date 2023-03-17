from project.animals.animal import Mammal
from project.food import Fruit, Meat, Vegetable


class Mouse(Mammal):
    eats = [Vegetable, Fruit]
    weight_gain = 0.10

    def make_sound(self) -> str:
        return "Squeak"


class Dog(Mammal):
    eats = [Meat]
    weight_gain = 0.40

    def make_sound(self) -> str:
        return "Woof!"


class Cat(Mammal):
    eats = [Vegetable, Meat]
    weight_gain = 0.30

    def make_sound(self) -> str:
        return "Meow"


class Tiger(Mammal):
    eats = [Meat]
    weight_gain = 1

    def make_sound(self) -> str:
        return "ROAR!!!"
