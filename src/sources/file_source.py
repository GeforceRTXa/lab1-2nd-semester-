import os
from typing import List
from src.tasks.task import Task
from uuid import uuid4
from typing import TextIO
from src.protocols.protocols import TaskProtocol


class FileSource:
    def __init__(self, path: str) -> None:
        self.path = path

    def get_tasks(self) -> List[TaskProtocol]:
        if not os.path.isfile(self.path):
            raise FileNotFoundError(f"File not found: {self.path}")
        file: TextIO  = open(self.path, 'r', encoding='utf-8')
        tasks: List[TaskProtocol] = [Task(uuid4().int, line.strip()) for line in file]
        file.close()
        return tasks
