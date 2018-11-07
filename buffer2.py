import time
from logger import Logger
from resource import Resource

class Buffer(object):
    def __init__(self, max_buffer):
        self.queue = []
        self.max_buffer = max_buffer
        self.print_interval = 5
        self.last_id = 0

    def add_resource(self):
        resource = self.last_id + 1
        self.last_id += 1
        self.queue.append(resource)
        self.print_log()
        return resource
        
    def remove_resource(self):
        resource = self.queue.pop(0)
        self.print_log()
        return resource
    
    def print_log(self):
        message = "%s - Buffer: ["
        count = 0
        i = 0
        for item in self.queue:
            message += " {" + str(item) + "} "
            count += 1
            i += 1
        message += "]\n"
        print(message % (time.ctime(time.time())))

    def auto_print(self):
        while 1:
            self.print_log()
            time.sleep(self.print_interval)