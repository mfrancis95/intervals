import threading

class Interval:

    def __init__(self, delay, func, start = None, times = None):
        if start is None:
            start = 0
        if times is None:
            times = -1
        self.delay = delay
        self.func = func
        self.start = start
        self.times = times
        self.event = threading.Event()
        
        def run():
            if self.start > 0:
                self.event.wait(self.start)
            if self.times < 0:
                while not self.event.is_set():
                    self.func()
                    self.event.wait(self.delay)
            elif self.times > 0:
                times = self.times
                while not self.event.is_set():
                    self.func()
                    times -= 1
                    if times == 0:
                        self.event.set()
                    else:
                        self.event.wait(self.delay)
            else:
                self.event.set()

        threading.Thread(target = run).start()

    def is_running(self):
        return not self.event.is_set()

    def stop(self):
        self.event.set()

timeout = lambda delay, func: Interval(0, func, delay, 1)
