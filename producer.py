from resource import Resource
import time

class Producer(object):
    def __init__(self, buffer, interval):
        self.buffer = buffer
        self.interval = interval

    def produce(self, id):
        if len(self.buffer.queue) < self.buffer.max_buffer:
            resource = Resource(id)
            self.buffer.add_resource(resource)
            return True
        else:
            print("%s - buffer full, cannot produce resource\n" % time.ctime(time.time()))
            return False
    
    def auto_produce(self):
        id = 1
        while 1:
            if self.produce(id):
                id += 1
            time.sleep(self.interval)