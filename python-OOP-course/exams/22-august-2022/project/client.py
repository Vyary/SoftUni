from typing import List


class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: List = []
        self.bill: float = 0.0
        self.unfinished_order = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        if not value.startswith("0") or not len(value) == 10 or not value.isnumeric():
            raise ValueError("Invalid phone number!")

        self.__phone_number = value
