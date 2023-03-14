from typing import List
from project.dvd import DVD
from project.customer import Customer


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) != MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) != MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = next(
            customer for customer in self.customers if customer.id == customer_id
        )
        dvd = next(dvd for dvd in self.dvds if dvd.id == dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return (
                f"{customer.name} should be at least "
                f"{dvd.age_restriction} to rent this movie"
            )

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = next(
            customer for customer in self.customers if customer.id == customer_id
        )
        dvd = next(dvd for dvd in self.dvds if dvd.id == dvd_id)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self) -> str:
        customers_info = "\n".join(str(customer) for customer in self.customers)
        dvd_info = "\n".join(str(dvd) for dvd in self.dvds)

        return f"{customers_info}\n{dvd_info}"
