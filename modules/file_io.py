from generators import FileNameGenerator
from pathlib import Path


class FileIO:
    """Modifies files on local disk.

    This is a sample description.
    """

    def __init__(self) -> None:
        ...

    @staticmethod
    def rename_files(directory_path):
        generator = FileNameGenerator(directory_path)
        for p in generator:
            print(p)


if __name__ == '__main__':
    fileio = FileIO()
    fileio.rename_files(Path("C:\\Users\LinWin-001\Documents\Datasets\\74.220.215.205\RAW\CASME_A\Section A"))
