import pytest #type: ignore
import os

@pytest.fixture(scope="function")
def env(tmp_path):

    main_cwd = os.getcwd()
    os.chdir(tmp_path)

    with open("temp_file1.txt", "w") as f:
        f.write("Hello World1\nabc")
    with open("temp_file2.txt", "w") as f:
        f.write("It's me, file2!")

    with open("config.json", "w") as f:
        f.write('{"sources": [{"type": "file", "path": "temp_file1.txt"}, {"type": "file", "path": "temp_file2.txt"}]}')

    yield tmp_path
    os.chdir(main_cwd)
