from typing import List

from project.client import Client
from project.meals.meal import Meal
from project.meals.starter import Starter
from project.meals.main_dish import MainDish
from project.meals.dessert import Dessert


class FoodOrdersApp:
    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []
        self.receipt_id = 0

    def __check_is_menu_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return True

    def __get_client(self, client_phone_number: str):
        client = next(
            (c for c in self.clients_list if c.phone_number == client_phone_number),
            None,
        )
        return client

    def register_client(self, client_phone_number: str):
        client = self.__get_client(client_phone_number)

        if client is not None:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if isinstance(meal, (Starter, MainDish, Dessert)):
                self.menu.append(meal)

    def show_menu(self):
        self.__check_is_menu_ready()
        return "\n".join(m.details() for m in self.menu)

    def add_meals_to_shopping_cart(
        self, client_phone_number: str, **meal_names_and_quantities: int
    ):
        self.__check_is_menu_ready()
        client = self.__get_client(client_phone_number)

        if client is None:
            self.register_client(client_phone_number)
            client = self.__get_client(client_phone_number)

        for meal, order_quantity in meal_names_and_quantities.items():
            current_meal = next((m for m in self.menu if m.name == meal), None)

            if current_meal is None:
                raise Exception(f"{meal} is not on the menu!")

            if current_meal.quantity < order_quantity:
                raise Exception(
                    f"Not enough quantity of {current_meal.__class__.__name__}: {meal}!"
                )

        for meal, order_quantity in meal_names_and_quantities.items():
            current_meal = next((m for m in self.menu if m.name == meal), None)

            current_meal.quantity -= order_quantity
            client.shopping_cart.append(current_meal)
            client.bill += current_meal.price * order_quantity

        client.unfinished_order.update(meal_names_and_quantities)

        meal_names = ", ".join(m.name for m in client.shopping_cart)
        return (
            f"Client {client_phone_number} successfully ordered {meal_names} for "
            f"{client.bill:.2f}lv."
        )

    def cancel_order(self, client_phone_number: str):
        client = self.__get_client(client_phone_number)

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for meal, order_quantity in client.unfinished_order.items():
            current_meal = next((m for m in self.menu if m.name == meal), None)
            current_meal.quantity += order_quantity

        client.shopping_cart = []
        client.bill = 0
        client.unfinished_order = {}
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__get_client(client_phone_number)

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        self.receipt_id += 1
        message = (
            f"Receipt #{self.receipt_id} with total amount of {client.bill:.2f} was "
            f"successfully paid for {client_phone_number}."
        )

        client.shopping_cart = []
        client.bill = 0
        client.unfinished_order = {}

        return message

    def __str__(self):
        return (
            f"Food Orders App has {len(self.menu)} meals on the menu and "
            f"{len(self.clients_list)} clients."
        )
