class Player:
    def __init__(
        self, name: str, sprint: int, dribble: int, passing: int, shooting: int
    ):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self) -> str:
        return self.__name

    @property
    def sprint(self) -> int:
        return self.__sprint

    @property
    def dribble(self) -> int:
        return self.__dribble

    @property
    def passing(self) -> int:
        return self.__passing

    @property
    def shooting(self) -> int:
        return self.__shooting

    def __str__(self):
        return (
            f"Player: {self.name}\n"
            f"Sprint: {self.sprint}\n"
            f"Dribble: {self.dribble}\n"
            f"Passing: {self.passing}\n"
            f"Shooting: {self.shooting}"
        )
