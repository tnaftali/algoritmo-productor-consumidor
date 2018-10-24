from buffer import Buffer
import time
import random
from logger import Logger

class Consumer(object):
    def __init__(self, buffer, monitor, interval = 1):
        self.buffer = buffer
        self.interval = interval
        self.monitor = monitor

    def consume(self):
        self.buffer.remove_resource()

    def auto_consume(self):
        while 1:
            self.monitor.check_empty()
            self.consume()
            random_interval = float(random.randrange(0, 500))/100
            time.sleep(random_interval)