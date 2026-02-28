from src.tasks.task import Task

def test_task():
    task = Task(12, "some_payload")
    assert task.__repr__() == f"Task(id={task.id}, payload={task.payload})"
