from typing import List, Union
from project.band_members.drummer import Drummer
from project.band_members.singer import Singer
from project.band_members.guitarist import Guitarist


class Band:
    def __init__(self, name: str):
        self.name = name
        self.members: List[Union[Drummer, Singer, Guitarist]] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Band name should contain at least one character!")

        self.__name = value

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."
