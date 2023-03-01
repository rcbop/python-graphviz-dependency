import os
from glob import iglob

PYTHON_GLOB = '**/*.py'

class FileCrawler:
    def __init__(self, root_path: str) -> None:
        self.root_path = root_path

    def crawl(self) -> list[str]:
        search_path = os.path.join(self.root_path, PYTHON_GLOB)
        return list(iglob(search_path, recursive=True))
