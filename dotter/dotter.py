# A dotter while I'm thinking

import itertools
import sys
import threading
import time

piano = ['▉▁▁▁▁▁', '▉▉▂▁▁▁', '▉▉▉▃▁▁', '▉▉▉▉▅▁', 
         '▉▉▉▉▉▇', '▉▉▉▉▉▉', '▉▉▉▉▇▅', '▉▉▉▆▃▁', 
         '▉▉▅▃▁▁', '▉▇▃▁▁▁', '▇▃▁▁▁▁', '▃▁▁▁▁▁', 
         '▁▁▁▁▁▁', '▁▁▁▁▁▉', '▁▁▁▁▃▉', '▁▁▁▃▅▉', 
         '▁▁▃▅▇▉', '▁▃▅▇▉▉', '▃▅▉▉▉▉', '▅▉▉▉▉▉',
         '▇▉▉▉▉▉', '▉▉▉▉▉▉', '▇▉▉▉▉▉', '▅▉▉▉▉▉', 
         '▃▅▉▉▉▉', '▁▃▅▉▉▉', '▁▁▃▅▉▉', '▁▁▁▃▅▉',
         '▁▁▁▁▃▅', '▁▁▁▁▁▃', '▁▁▁▁▁▁', '▁▁▁▁▁▁', 
         '▁▁▃▁▁▁', '▁▃▅▃▁▁', '▁▅▉▅▁▁', '▃▉▉▉▃▁', 
         '▅▉▁▉▅▃', '▇▃▁▃▇▅', '▉▁▁▁▉▇', '▉▅▃▁▃▅', 
         '▇▉▅▃▅▇', '▅▉▇▅▇▉', '▃▇▉▇▉▅', '▁▅▇▉▇▃', 
         '▁▃▅▇▅▁', '▁▁▃▅▃▁', '▁▁▁▃▁▁', '▁▁▁▁▁▁',
        ]

slash = ["\\","|","/", "-"]

class dotter:

    # A dotter while I'm thinking

    def __init__(self, message: str = "Thinking", delay: float = 0.5,cycle:list[int]=["", ".", ". .", ". . ."]) -> None:
        
        self.spinner = itertools.cycle(cycle)
        self.delay = delay
        self.message = message
        self.running = False
        self.dotter_thread = None

    def dot(self):
        while self.running:
            sys.stdout.write(f"{self.message} {next(self.spinner)} \r")
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write(f"\r{' ' * (len(self.message) + 6)}\r")

    def update_message(self, new_message, delay=0.1):
        time.sleep(delay)
        sys.stdout.write(
            f"\r{' ' * (len(self.message) + 6)}\r"
        )  # Clear the current message
        sys.stdout.flush()
        self.message = new_message

    def __enter__(self):
        self.running = True
        self.dotter_thread = threading.Thread(target=self.dot)
        self.dotter_thread.start()

    def __exit__(self,*args) -> None:
        self.running = False
        if self.dotter_thread is not None:
            self.dotter_thread.join()
        sys.stdout.write(f"\r{' ' * (len(self.message) + 2)}\r")
        sys.stdout.flush()


if __name__ == "__main__":
    from time import sleep

    with dotter(cycle = piano, message="Loading", delay=0.1) as d:
        sleep(20)
