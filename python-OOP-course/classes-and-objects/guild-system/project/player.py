class Player:
    NO_AFFILIATION = "Unaffiliated"

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = Player.NO_AFFILIATION

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name in self.skills.keys():

            return "Skill already added"

        if skill_name not in self.skills:
            self.skills[skill_name] = 0

        self.skills[skill_name] = mana_cost

        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        skills = "\n".join(
            [f"==={skill} - {mana}" for skill, mana in self.skills.items()]
        )

        return (
            f"Name: {self.name}\n"
            f"Guild: {self.guild}\n"
            f"HP: {self.hp}\n"
            f"MP: {self.mp}\n"
            f"{skills}\n"
        )
