from typing import Protocol, runtime_checkable, Any, List


@runtime_checkable
class TaskProtocol(Protocol):
    id: int
    payload: Any

@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> List[TaskProtocol]: ...
