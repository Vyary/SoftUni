from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in [delicacy.name for delicacy in self.delicacies]:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in ["Gingerbread", "Stolen"]:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacies = {
            "Gingerbread": Gingerbread(name, price),
            "Stolen": Stolen(name, price),
        }

        self.delicacies.append(delicacies[type_delicacy])
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in [booth.booth_number for booth in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ["Open Booth", "Private Booth"]:
            raise Exception(f"{type_booth} is not a valid booth!")

        booths = {
            "Open Booth": OpenBooth(booth_number, capacity),
            "Private Booth": PrivateBooth(booth_number, capacity),
        }

        self.booths.append(booths[type_booth])
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return (
                    f"Booth {booth.booth_number} has been reserved for "
                    f"{number_of_people} people."
                )

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)

        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = next((d for d in self.delicacies if d.name == delicacy_name), None)

        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next(b for b in self.booths if b.booth_number == booth_number)
        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)
        self.income += bill

        booth.is_reserved = False
        booth.price_for_reservation = 0
        booth.delicacy_orders = []

        return f"Booth {booth.booth_number}:\n" f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
