import pytest #type: ignore
from src.sources.file_source import FileSource
from src.protocols.protocols import TaskProtocol
from src.sources.generator_source import GeneratorSource
from src.sources.fake_api_source import FakeApiSource
from src.main import get_tasks


@pytest.mark.usefixtures("env")
def test_file_source(tmp_path):
    source = FileSource("temp_file1.txt")
    tasks = source.get_tasks()
    for task in tasks:
        if not isinstance(task, TaskProtocol):
            assert False
    assert True

def test_generator_source():
    source = GeneratorSource()
    tasks = get_tasks(source)
    for task in tasks:
        if not isinstance(task, TaskProtocol):
            assert False
    assert True


def test_api_source():
    source = FakeApiSource("any_url")
    tasks = get_tasks(source)
    for task in tasks:
        if not isinstance(task, TaskProtocol):
            assert False
    assert True
