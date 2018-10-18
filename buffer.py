import time
from logger import Logger

class Buffer(object):
    def __init__(self, max_buffer):
        self.queue = []
        self.max_buffer = max_buffer
        self.print_interval = 5

    def add_resource(self, resource):
        self.queue.append(resource)
        self.print()
        
        # Logger.info('Resource {} produced'.format('{' + str(resource.id) + '}'))

    def remove_resource(self):
        resource = self.queue.pop(0)
        self.print()
        # Logger.info('Resource {} consumed'.format('{' + str(resource.id) + '}'))
    
    def print(self):
        message = "%s - Buffer: ["
        count = 0
        i = 0
        for item in self.queue:
            message += " {" + str(item.id) + "} "
            count += 1
            i += 1
        message += "]\n"
        print(message % (time.ctime(time.time())))

    def auto_print(self):
        while 1:
            self.print()
            time.sleep(self.print_interval)