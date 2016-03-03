from threading import Thread
from time import sleep

class Interval:

    def __init__(self, delay, func, start = None, times = None):
        if not start:
            start = 0
        if not times:
            times = -1
        self.delay = delay
        self.func = func
        self.start = start
        self.times = times
        Thread(target = self.run).start()

    def run(self):
        if self.start > 0:
            sleep(self.start)
        while self.times != 0:
            self.func()
            sleep(self.delay)
            if self.times > 0:
                self.times -= 1

timeout = lambda delay, func: Interval(0, func, delay, 1)
