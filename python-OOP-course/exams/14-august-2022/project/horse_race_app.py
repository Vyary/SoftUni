from typing import List, Union
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace


class HorseRaceApp:
    def __init__(self):
        self.horses: List[Union[Thoroughbred, Appaloosa]] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_name in [h.name for h in self.horses if h.name == horse_name]:
            raise Exception(f"Horse {horse_name} has been already added!")

        available_horse_breeds = {
            "Appaloosa": Appaloosa,
            "Thoroughbred": Thoroughbred,
        }

        if horse_type not in available_horse_breeds:
            return

        self.horses.append(available_horse_breeds[horse_type](horse_name, horse_speed))
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [j.name for j in self.jockeys if j.name == jockey_name]:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [
            r.race_type for r in self.horse_races if r.race_type == race_type
        ]:
            raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = next((j for j in self.jockeys if j.name == jockey_name), None)
        horse_list = [h for h in self.horses if h.__class__.__name__ == horse_type and h.is_taken is False]

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if len(horse_list) == 0:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        horse = horse_list[-1]
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = next(
            (r for r in self.horse_races if r.race_type == race_type), None
        )
        jockey = next((j for j in self.jockeys if j.name == jockey_name), None)

        if horse_race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return (
                f"Jockey {jockey_name} has been already added to the {race_type} race."
            )

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = next(
            (r for r in self.horse_races if r.race_type == race_type), None
        )

        if horse_race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        best_horse_speed = 0
        best_jockey = None

        for jockey in horse_race.jockeys:
            if jockey.horse.speed > best_horse_speed:
                best_horse_speed = jockey.horse.speed
                best_jockey = jockey

        return (
            f"The winner of the {race_type} race, with a speed of "
            f"{best_horse_speed}km/h is {best_jockey.name}! "
            f"Winner's horse: {best_jockey.horse.name}."
        )
