from src.tasks.task import Task
from uuid import uuid4
from random import choice, choices
from string import ascii_letters, digits
from typing import List, Union, Dict
from src.protocols.protocols import TaskProtocol


class GeneratorSource:
    @classmethod
    def get_tasks(cls) -> List[TaskProtocol]:
        tasks: List[TaskProtocol] = []
        for i in range(10):
            payload_type: str = choice(["text", "json", "list"])
            payload: Union[str, Dict, List]
            match payload_type:
                case "text":
                    payload = ''.join(choices(ascii_letters + digits, k=10))
                case "json":
                    payload = {"hello": "world", "C": "power", "cc": "vv"}
                case "list":
                    payload = ["aa", "Z", "kpylov", "labs", 67, 52, 42]
            tasks.append(Task(uuid4().int, payload))
        return tasks
