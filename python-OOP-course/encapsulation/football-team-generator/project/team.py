from typing import List, Union
from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    @property
    def name(self) -> str:
        return self.__name

    @property
    def rating(self) -> int:
        return self.__rating

    def add_player(self, player: Player) -> str:
        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name: str) -> Union[str, Player]:
        match = next(
            (player for player in self.__players if player.name == player_name), None
        )

        if match is None:
            return f"Player {player_name} not found"

        self.__players.remove(match)
        return match
