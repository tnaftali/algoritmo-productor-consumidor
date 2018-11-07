from resource import Resource
import time
import random
from urllib import request, parse
import json

class Producer(object):
    def __init__(self, monitor, interval = 1):
        self.interval = interval
        self.monitor = monitor

    def produce(self, id):
        data = { }
        req =  request.Request("http://127.0.0.1:5000/produce", data=data)
        resp = request.urlopen(req)
        print(resp.read().decode('utf-8'))
    
    def auto_produce(self):
        id = 1
        while 1:
            self.monitor.check_full()
            self.produce(id)
            id += 1
            random_interval = float(random.randrange(0, 500))/100
            time.sleep(random_interval)