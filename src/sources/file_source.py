import os
from typing import List
from src.tasks.task import Task
from uuid import uuid4
from typing import TextIO
from src.protocols.protocols import TaskProtocol


class FileSource:
    def __init__(self, path: str) -> None:
        if not os.path.isfile(path):
            raise FileNotFoundError(f"File not found: {path}")
        self.file: TextIO  = open(path, 'r', encoding='utf-8')

    def get_tasks(self) -> List[TaskProtocol]:
        return [Task(uuid4().int, line.strip()) for line in self.file]

    def __del__(self) -> None:
        self.file.close()
