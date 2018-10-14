from buffer import Buffer
from producer import Producer
from consumer import Consumer
import input
import time
import _thread
import threading

def main():
    max_buffer = input.insert_number('insert maximum buffer capacity: ')
    producer_interval = input.insert_number('insert producer seconds interval: ')
    consumer_interval = input.insert_number('insert consumer seconds interval: ')

    buffer = Buffer(max_buffer)
    producer = Producer(buffer, producer_interval)    
    consumer = Consumer(buffer, consumer_interval)

    try:
        threading.Thread(target=producer.auto_produce).start()
        threading.Thread(target=consumer.auto_consume).start()
        threading.Thread(target=buffer.auto_print).start()
    except:
        print ('%s - error: unable to start thread\n' % time.ctime(time.time()))

main()