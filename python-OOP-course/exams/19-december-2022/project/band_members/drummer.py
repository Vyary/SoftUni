from project.band_members.musician import Musician


class Drummer(Musician):
    learnable_skills = [
        "play the drums with drumsticks",
        "play the drums with drum brushes",
        "read sheet music",
    ]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def learn_new_skill(self, new_skill: str):
        return super().learn_new_skill(new_skill)

    def can_play_rock(self):
        if "play the drums with drumsticks" in self.skills:
            return True
        return False

    def can_play_metal(self):
        if "play the drums with drumsticks" in self.skills:
            return True
        return False

    def can_play_jazz(self):
        if "play the drums with drum brushes" in self.skills:
            return True
        return False
