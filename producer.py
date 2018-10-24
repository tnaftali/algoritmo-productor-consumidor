from resource import Resource
import time
import random

class Producer(object):
    def __init__(self, buffer, monitor, interval = 1):
        self.buffer = buffer
        self.interval = interval
        self.monitor = monitor

    def produce(self, id):
        resource = Resource(id)
        self.buffer.add_resource(resource)
    
    def auto_produce(self):
        id = 1
        while 1:
            self.monitor.check_full()
            self.produce(id)
            id += 1
            random_interval = float(random.randrange(0, 500))/100
            time.sleep(random_interval)