from buffer import Buffer
import time

class Consumer(object):
    def __init__(self, buffer, interval):
        self.buffer = buffer
        self.interval = interval

    def consume(self):
        if len(self.buffer.queue) > 0:
            self.buffer.remove_resource()
        else:
            print("%s - buffer empty, cannot consume resource\n" % time.ctime(time.time()))

    def auto_consume(self):
        while 1:
            self.consume()
            time.sleep(self.interval)