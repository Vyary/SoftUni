from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:

            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        match = next((task for task in self.tasks if task.name == task_name), None)

        if match is None:

            return f"Could not find task with the name {task_name}"

        match.completed = True

        return f"Completed task {task_name}"

    def clean_section(self) -> str:
        completed_tasks = [x for x in self.tasks if x.completed]

        for task in completed_tasks:
            self.tasks.remove(task)

        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self) -> str:
        task_details = "\n".join([task.details() for task in self.tasks])

        return f"Section {self.name}: \n{task_details}"
