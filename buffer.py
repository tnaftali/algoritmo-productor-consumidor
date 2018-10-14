import time

class Buffer(object):
    def __init__(self, max_buffer):
        self.queue = []
        self.max_buffer = max_buffer
        self.print_interval = 5

    def add_resource(self, resource):
        self.queue.append(resource)
        print("%s - resource {%s} produced" % (time.ctime(time.time()), str(resource.id)))

    def remove_resource(self):
        resource = self.queue.pop(0)
        print("%s - resource {%s} consumed" % (time.ctime(time.time()), str(resource.id)))
    
    def print(self):
        message = "%s - buffer: ["
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