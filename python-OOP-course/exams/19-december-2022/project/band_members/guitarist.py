from project.band_members.musician import Musician


class Guitarist(Musician):
    learnable_skills = ["play metal", "play rock", "play jazz"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def learn_new_skill(self, new_skill: str):
        return super().learn_new_skill(new_skill)

    def can_play_rock(self):
        if "play rock" in self.skills:
            return True
        return False

    def can_play_metal(self):
        if "play metal" in self.skills:
            return True
        return False

    def can_play_jazz(self):
        if "play jazz" in self.skills:
            return True
        return False
