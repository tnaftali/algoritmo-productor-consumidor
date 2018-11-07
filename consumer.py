from buffer import Buffer
import time
import random
from logger import Logger
from urllib import request, parse
import json

class Consumer(object):
    def __init__(self, monitor, interval = 1):
        self.interval = interval
        self.monitor = monitor

    def consume(self):
        resp = request.urlopen('https://producer-consumer-problem.herokuapp.com/consume')
        print(resp.read().decode('utf-8'))

    def auto_consume(self):
        while 1:
            self.monitor.check_empty()
            self.consume()
            random_interval = float(random.randrange(0, 500))/100
            time.sleep(random_interval)