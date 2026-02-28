from dataclasses import dataclass
from typing import Any

@dataclass
class Task:
    id: int
    payload: Any

    def __repr__(self) -> str:
        return f"Task(id={self.id}, payload={self.payload})"
