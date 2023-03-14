class Subscription:
    id = 0

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id: int = Subscription.get_next_id()

    @classmethod
    def get_next_id(cls) -> int:
        cls.id += 1
        return cls.id

    def __repr__(self) -> str:
        return f"Subscription <{self.id}> on {self.date}"
