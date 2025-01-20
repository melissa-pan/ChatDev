'''
Timer class for managing the timing of the Typing Practice Game.
'''
import time
class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = None
    def start(self):
        self.start_time = time.time()
    def get_elapsed_time(self):
        if self.start_time is None:
            return 0
        return time.time() - self.start_time