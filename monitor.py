import time
from logger import Logger
from urllib import request, parse
import json

class Monitor(object):
    def __init__(self):
        self.max_buffer = 50
        self.length = 0

    def check_full(self):
        resp = request.urlopen('https://producer-consumer-problem.herokuapp.com/length')
        self.length = int(resp.read().decode('utf-8'))
        while self.length == self.max_buffer:
            Logger.info('Buffer full, producer thread suspended')
            time.sleep(1)
        else:
            Logger.info('Producer thread suspended')

    def check_empty(self):
        resp = request.urlopen('https://producer-consumer-problem.herokuapp.com/length')
        self.length = int(resp.read().decode('utf-8'))
        print('check empty: ' + str(self.length))
        while self.length == 0:
            Logger.info('Buffer empty, consumer thread suspended')
            time.sleep(1)
        else:
            Logger.info('Consumer thread resumed')