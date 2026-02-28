import pytest #type: ignore

from src.main import main
from src.sources.file_source import uuid4 #noqa: F401
import src.sources.file_source
import json


@pytest.mark.usefixtures("env")
def test_config(tmp_path):
    with open("config.json", "r") as sources_file:
        config = json.load(sources_file)
    assert config == {
  "sources": [
    {"type": "file", "path": "temp_file1.txt"},
      {"type": "file", "path": "temp_file2.txt"}
  ]
}

@pytest.mark.usefixtures("env")
def test_main(tmp_path, capsys, monkeypatch):
    class MockUUID:
        def __init__(self):
            self.int = 1

    monkeypatch.setattr(src.sources.file_source, "uuid4", lambda: MockUUID())
    main()
    captured = capsys.readouterr()
    assert captured.out == "Task(id=1, payload=Hello World1)\nTask(id=1, payload=abc)\nTask(id=1, payload=It's me, file2!)\n"
