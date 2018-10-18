import time
from logger import Logger

class Monitor(object):
    def __init__(self, buffer, max_buffer):
        self.buffer = buffer
        self.max_buffer = max_buffer

    def check_full(self):
        while len(self.buffer.queue) == self.max_buffer:
            # Logger.info('Buffer full, producer thread suspended')
            time.sleep(1)
        # else:
            # Logger.info('Producer thread suspended')

    def check_empty(self):
        while len(self.buffer.queue) == 0:
            # Logger.info('Buffer empty, consumer thread suspended')
            time.sleep(1)
        # else:
            # Logger.info('Consumer thread resumed')