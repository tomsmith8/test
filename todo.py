# todo.py

class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task:
            raise ValueError("Task cannot be empty.")
        self.tasks.append(task)
        return f"Task '{task}' added."

    def get_tasks(self):
        return self.tasks
