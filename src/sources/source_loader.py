from typing import List

from src.protocols.protocols import TaskSource
from src.config import config

def load_sources() -> List[TaskSource]:
    sources = []
    for source in config:
        if isinstance(source, TaskSource):
            sources.append(source)
    return sources
