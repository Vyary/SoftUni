from typing import List
from project.subscription import Subscription
from project.exercise_plan import ExercisePlan
from project.equipment import Equipment
from project.trainer import Trainer
from project.customer import Customer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) -> None:
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int) -> str:
        sub = next(sub for sub in self.subscriptions if sub.id == subscription_id)
        customer = next(cust for cust in self.customers if cust.id == sub.customer_id)
        trainer = next(t for t in self.trainers if t.id == sub.trainer_id)
        plan = next(ex for ex in self.plans if ex.id == sub.exercise_id)
        equipment = next(eq for eq in self.equipment if eq.id == plan.equipment_id)

        return (
            f"{str(sub)}\n"
            f"{str(customer)}\n"
            f"{str(trainer)}\n"
            f"{str(equipment)}\n"
            f"{str(plan)}\n"
        )
