import time
from abc import ABC, abstractmethod


class IWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class IEater(ABC):
    @abstractmethod
    def eat(self):
        pass


class Worker(IWorker, IEater):
    def work(self) -> None:
        print("I'm normal worker. I'm working.")

    def eat(self) -> None:
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(IWorker, IEater):
    def work(self) -> None:
        print("I'm super worker. I work very hard!")

    def eat(self) -> None:
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(IWorker):
    def work(self) -> None:
        print("I'm a robot. I'm working....")


class WorkManager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker: IWorker) -> None:
        if not isinstance(worker, IWorker):
            raise TypeError(f"`worker` must be of type {IWorker}")

        self.worker = worker

    def manage(self) -> None:
        self.worker.work()


class BreakManager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker: IEater) -> None:
        if not isinstance(worker, IEater):
            raise TypeError(f"`worker` must be of type {IEater}")

        self.worker = worker

    def lunch_break(self) -> None:
        self.worker.eat()


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass
