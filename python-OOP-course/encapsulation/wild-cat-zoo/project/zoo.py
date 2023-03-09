from project.vet import Vet
from project.caretaker import Caretaker
from project.keeper import Keeper
from project.animal import Animal
from project.worker import Worker
from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah


class Zoo:
    def __init__(
        self, name: str, budget: int, animal_capacity: int, workers_capacity: int
    ):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: float) -> str:
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        if price > self.__budget:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        match = next(
            (worker for worker in self.workers if worker.name == worker_name), None
        )

        if match is None:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(match)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        salaries_total = sum(worker.salary for worker in self.workers)

        if salaries_total > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries_total
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        tend_total = sum(animal.money_for_care for animal in self.animals)

        if tend_total > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= tend_total
        return (
            f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        )

    def profit(self, amount: float):
        self.__budget += amount

    def animals_status(self) -> str:
        output = f"You have {len(self.animals)} animals\n"

        for animal_class in [Lion, Tiger, Cheetah]:
            animal_type = animal_class.__name__

            animals_of_type = [
                animal for animal in self.animals if isinstance(animal, animal_class)
            ]

            amount_of_animals = len(animals_of_type)
            animal_names = "\n".join([str(animal) for animal in animals_of_type])
            output += f"----- {amount_of_animals} {animal_type}s:\n{animal_names}\n"

        return output[:-1]

    def workers_status(self) -> str:
        output = f"You have {len(self.workers)} workers\n"

        for worker_class in [Keeper, Caretaker, Vet]:
            worker_type = worker_class.__name__

            workers_of_type = [
                worker for worker in self.workers if isinstance(worker, worker_class)
            ]

            amount_of_workers = len(workers_of_type)
            worker_names = "\n".join([str(worker) for worker in workers_of_type])
            output += f"----- {amount_of_workers} {worker_type}s:\n{worker_names}\n"

        return output[:-1]
