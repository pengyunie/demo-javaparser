from pathlib import Path

import seutil as su
from jsonargparse import CLI


class ParserWithProjectContext:
    def __init__(
        self,
        work_dir: su.arg.RPath = Path(__file__).parent.parent.parent / "_work",
        data_subdir: str = "data",
        projects_subdir: str = "projects",
        downloads_subdir: str = "_downloads",
    ):
        self.work_dir = work_dir
        self.data_dir = work_dir / data_subdir
        self.projects_dir = work_dir / projects_subdir
        self.downloads_dir = work_dir / downloads_subdir

    def tokenize(self): ...

    def extract_methods(self): ...

    def resolve_types(self): ...


if __name__ == "__main__":
    CLI(ParserWithProjectContext, as_positional=False)
