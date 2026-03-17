from typing import Any

from src.protocols.protocols import TaskProtocol, TaskSource
from src.sources.source_loader import load_sources

def get_tasks(source: TaskSource) -> Any:
    return source.get_tasks()


def main(load=load_sources) -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    sources = load()
    for source in sources:
        tasks = get_tasks(source)
        for task in tasks:
            try:
                if isinstance(task, TaskProtocol):
                    print(task)
                else:
                    raise TypeError(f"Incorrect task type. Task: {task}")
            except Exception as e:
                print(e)

if __name__ == "__main__":
    main()
