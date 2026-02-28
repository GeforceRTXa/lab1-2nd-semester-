from src.tasks.task import Task
from typing import List
from uuid import uuid4
from random import choice
from src.protocols.protocols import TaskProtocol

class FakeApiSource:
    def __init__(self, url: str) -> None:
        self.url: str = url
        self.id: int = 0

    def get_tasks(self) -> List[TaskProtocol]:
        tasks: List[TaskProtocol] = []
        for i in range(10):
            self.id += 1
            tasks.append(Task(uuid4().int, {"id": self.id,
                                            "role": choice(["user", "admin"]),
                                            "name": choice(["John", "Michael", "Alex", "Kpylov"])}))
        return tasks
