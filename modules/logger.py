from console import console
from rich.progress import Progress
import time
from typing import Callable


class Logger:

    def __init__(self) -> None:
        self.console = console

    def show_status(self, callback: Callable):
        with self.console.status("Working"):
            callback()

    def show_progress(self, callback: Callable):
        with Progress(console=self.console) as progress:
            for _ in progress.track(range(20), description="Processing..."):
                callback()


if __name__ == '__main__':
    logger = Logger()

    def sleep():
        time.sleep(1)


    # logger.show_progress(sleep)
    # logger.show_status(sleep)

    tasks = [f'task {n}' for n in range(1,11)]
    with console.status("Working!!!") as status:
        while tasks:
            task = tasks.pop(0)
            time.sleep(1)
            console.log(f'{task} complete!')
