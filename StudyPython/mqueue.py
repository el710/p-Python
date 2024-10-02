"""
.... QUEUEs
"""

from threading import Thread
import queue
from time import sleep

def producer(queue):
    c = 0
    message = 'ping'
    while True:
        c += 1
        queue.put(message)
        print(f'producer: put {message} {c}')
        sleep(1)
        if c > 15:
            break

def consumer(queue):
    i = 0
    while True:
        if queue.empty():
            print(f'consumer: no messages')
            sleep(1)
            i += 1
        else:
            message = queue.get()
            print(f'consumer: get {message}')
            i = 0
        
        if i > 3:
            break

q = queue.Queue()
t1 = Thread(target=producer, args=(q, ))
t2 = Thread(target=consumer, args=(q, ))

t1.start()
t2.start()
t1.join()
t2.join()