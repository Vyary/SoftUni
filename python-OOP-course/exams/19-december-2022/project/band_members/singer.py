from project.band_members.musician import Musician


class Singer(Musician):
    learnable_skills = ["sing high pitch notes", "sing low pitch notes"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def learn_new_skill(self, new_skill: str):
        return super().learn_new_skill(new_skill)

    def can_play_rock(self):
        if "sing high pitch notes" in self.skills:
            return True
        return False

    def can_play_metal(self):
        if "sing low pitch notes" in self.skills:
            return True
        return False

    def can_play_jazz(self):
        if (
            "sing high pitch notes" in self.skills
            and "sing low pitch notes" in self.skills
        ):
            return True
        return False
