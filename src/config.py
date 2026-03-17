from src.sources.fake_api_source import FakeApiSource
from src.sources.file_source import FileSource
from src.sources.generator_source import GeneratorSource


config = [GeneratorSource,
          FileSource("file.txt"),
          FakeApiSource("some_url")]
