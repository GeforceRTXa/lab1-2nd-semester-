from typing import List

from src.protocols.protocols import TaskProtocol, TaskSource
from src.sources.file_source import FileSource
from src.sources.generator_source import GeneratorSource
from src.sources.fake_api_source import FakeApiSource
import json

def load_sources() -> List[TaskSource]:
    with open("config.json", "r") as sources_file:
        config = json.load(sources_file)

    sources: List[TaskSource] = []
    for source in config["sources"]:
        if source["type"] == "file":
            sources.append(FileSource(source["path"]))
        elif source["type"] == "generator":
            sources.append(GeneratorSource())
        elif source["type"] == "api":
            sources.append(FakeApiSource(source["url"]))
        else:
            raise ValueError(f"Unknown source type: {source['type']}")
    return sources

def get_tasks(source: TaskSource) -> List[TaskProtocol]:
    return source.get_tasks()


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    sources = load_sources()
    for source in sources:
        tasks = get_tasks(source)
        for task in tasks:
            try:
                if isinstance(task, TaskProtocol):
                    print(task)
                else:
                    raise TypeError("Incorrect task type")
            except TypeError:
                print("Incorrect task type")

if __name__ == "__main__":
    main()
