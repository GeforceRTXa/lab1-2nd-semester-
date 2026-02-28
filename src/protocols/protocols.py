from typing import Protocol, runtime_checkable, Any, List


@runtime_checkable
class TaskProtocol(Protocol):
    id: int
    payload: Any

class TaskSource(Protocol):
    def get_tasks(self) -> List[TaskProtocol]: ...
