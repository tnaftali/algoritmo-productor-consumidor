from buffer import Buffer
from producer import Producer
from consumer import Consumer
from monitor import Monitor
import input
import time
import _thread
import threading
import random
from logger import Logger

def main():
    # max_buffer = input.insert_number('insert maximum buffer capacity: ')

    # buffer = Buffer(max_buffer)
    monitor = Monitor()
    producer = Producer(monitor)    
    consumer = Consumer(monitor)

    try:
        threading.Thread(target=producer.auto_produce).start()
        threading.Thread(target=consumer.auto_consume).start()
    except:
        print(Logger.error('Unable to start thread'))

main()