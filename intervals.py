import threading

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
        self.event = threading.Event()
        
        def run():
            if self.start > 0:
                self.event.wait(self.start)
            while self.times != 0:
                self.func()
                if self.times > 0:
                    self.times -= 1
                if self.times != 0:
                    self.event.wait(self.delay)

        threading.Thread(target = run).start()

    def stop(self):
        self.times = 0
        self.event.set()

timeout = lambda delay, func: Interval(0, func, delay, 1)
