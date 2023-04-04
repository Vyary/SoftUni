from typing import Union
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class Jockey:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse: Union[Appaloosa, Thoroughbred] = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value.strip()) == 0:
            raise ValueError("Name should contain at least one character!")

        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 18:
            raise ValueError("Jockeys must be at least 18 to participate in the race!")

        self.__age = value
