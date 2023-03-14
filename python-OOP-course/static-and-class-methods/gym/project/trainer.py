class Trainer:
    id = 0

    def __init__(self, name: str):
        self.name = name
        self.id: int = Trainer.get_next_id()

    @classmethod
    def get_next_id(cls) -> int:
        cls.id += 1
        return cls.id

    def __repr__(self) -> str:
        return f"Trainer <{self.id}> {self.name}"
