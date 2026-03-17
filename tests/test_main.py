import pytest #type: ignore

from src.sources.file_source import uuid4 #noqa: F401
import src.sources.file_source
from src.sources.file_source import FileSource

@pytest.mark.usefixtures("env")
def test_main(tmp_path, capsys, monkeypatch):
    class MockUUID:
        def __init__(self):
            self.int = 1

    monkeypatch.setattr(src.sources.file_source, "uuid4", lambda: MockUUID())
    test_config = [FileSource("temp_file1.txt"), FileSource("temp_file2.txt")]
    from src.main import main
    main(load=lambda: test_config)
    captured = capsys.readouterr()
    assert captured.out == "Task(id=1, payload=Hello World1)\nTask(id=1, payload=abc)\nTask(id=1, payload=It's me, file2!)\n"
