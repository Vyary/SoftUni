from typing import List
from project.band_members.drummer import Drummer
from project.band_members.singer import Singer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        musician_types = {
            "Guitarist": Guitarist(name, age),
            "Drummer": Drummer(name, age),
            "Singer": Singer(name, age),
        }

        if musician_type not in musician_types.keys():
            raise ValueError("Invalid musician type!")

        if name in [n.name for n in self.musicians if n.name == name]:
            raise Exception(f"{name} is already a musician!")

        self.musicians.append(musician_types[musician_type])
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name in [n.name for n in self.bands if n.name == name]:
            raise Exception(f"{name} band is already created!")

        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(
        self,
        genre: str,
        audience: int,
        ticket_price: float,
        expenses: float,
        place: str,
    ):
        if place in [c.place for c in self.concerts if c.place == place]:
            concert_genre = [c.genre for c in self.concerts if c.place == place][0]
            raise Exception(
                f"{place} is already registered for {concert_genre} concert!"
            )

        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next((m for m in self.musicians if m.name == musician_name), None)

        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")

        band = next((b for b in self.bands if b.name == band_name), None)

        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = next((b for b in self.bands if b.name == band_name), None)

        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        musician = next((m for m in band.members if m.name == musician_name), None)

        if musician is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next(b for b in self.bands if b.name == band_name)

        drummers = [d for d in band.members if isinstance(d, Drummer)]
        singers = [s for s in band.members if isinstance(s, Singer)]
        guitarists = [g for g in band.members if isinstance(g, Guitarist)]

        if len(drummers) < 1 or len(singers) < 1 or len(guitarists) < 1:
            raise Exception(
                f"{band_name} can't start the concert because it doesn't have enough members!"
            )

        concert = next(c for c in self.concerts if c.place == concert_place)

        if concert.genre == "Rock":
            if not all(member.can_play_rock() for member in band.members):
                raise Exception(
                    f"The {band_name} band is not ready to play at the concert!"
                )

        if concert.genre == "Metal":
            if not all(member.can_play_metal() for member in band.members):
                raise Exception(
                    f"The {band_name} band is not ready to play at the concert!"
                )

        if concert.genre == "Jazz":
            if not all(member.can_play_jazz() for member in band.members):
                raise Exception(
                    f"The {band_name} band is not ready to play at the concert!"
                )

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
