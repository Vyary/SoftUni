class Customer:
    id = 0

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id: int = Customer.get_next_id()

    @classmethod
    def get_next_id(cls) -> int:
        cls.id += 1
        return cls.id

    def __repr__(self) -> str:
        return (
            f"Customer <{self.id}> {self.name}; "
            f"Address: {self.address}; "
            f"Email: {self.email}"
        )
