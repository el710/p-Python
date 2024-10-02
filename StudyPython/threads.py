"""
pip install requests
"""

import requests
from datetime import datetime

print('...simple line program...\n')

THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre'
res = []

time_start = datetime.now()

for _ in range(3):
    response = requests.get(THE_URL)
    page_response = response.json() ## format
    res.append(page_response)

time_end = datetime.now()

print(res)
print(f'time: {time_end - time_start}')

print('\n...upgrade with threads...\n')

from threading import Thread

t_res = []
urls = (THE_URL, )

def func(url):
    response = requests.get(url)
    page_response = response.json() ## format
    t_res.append(page_response)

## make threads
thr_first  = Thread(target=func, args=urls)
thr_second = Thread(target=func, args=urls)
thr_third  = Thread(target=func, args=urls)

time_start = datetime.now()

## start threads
thr_first.start()
thr_second.start()
thr_third.start()

# wait for ends of threads
thr_first.join()
thr_second.join()
thr_third.join()

time_end = datetime.now()

print(t_res)
print(f'time: {time_end - time_start}')

print('\n...upgrade with thread Class...\n')

class Getter(Thread):
    res = []

    def __init__(self, url) -> None:
        super().__init__()
        self.THE_URL = url

    def run(self):
        response = requests.get(self.THE_URL)
        Getter.res.append(response.json())


Threads = []
num_of_ganre = 10

for i in range(num_of_ganre):
    thread = Getter('https://binaryjazz.us/wp-json/genrenator/v1/genre')
    thread.start()
    Threads.append(thread)

for thread in Threads:
    thread.join()

print(Getter.res)

assert len(Getter.res) == num_of_ganre ## call error exception if condition not True


"""
sinchronize threads - race condition...
"""

x = 0

def Inc_task():
    global x
    for _ in range(10_000_000):
        x = x + 1 ## non atomic operation can cycling threads
        """
          without sync
          few threads may increase x the wrong way:
          thread_1: get x <- 23
          thread_1: stop
          thread_2: get x <- 23
          thread_2: stop
          thread_1: 23 + 1
          thread_1: x = 24
          thread_1: get x = 24
          thread_1: 24 + 1
          thread_1: x = 25 !!!
          thread_1: stop
          thread_2: 23 + 1
          thread_2: x = 24 !!!
          thread_2: stop
          e.t.c...
        """

def main():
    global x
    thread_1 = Thread(target=Inc_task)
    thread_2 = Thread(target=Inc_task)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

for _ in range(10):
    main()
    print(x)
"""
    python after v3.9 keep out threads from cycling in non atomic operation
    # atomic operatoin:
    - list.append()
    - list.extend([])
    - list.sort()
    - a = 10
"""

from threading import Lock

x = 0
lock = Lock()

def sync_task():
    global x
    for _ in range(10_000_000):
        lock.acquire() ## take lock
        x = x + 1 ## non atomic operation can cycling threads
        lock.release()
    """
       or
    """
    #    with lock:
    #         x = x + 1
    """
        algorithm of 'with':
        try:
            lock.asquire()
            ...
        fynally: ## release lock whatever errors or exceptions in block try...
            lock.release()
    """


def main():
    global x
    thread_1 = Thread(target=sync_task)
    thread_2 = Thread(target=sync_task)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

for _ in range(10):
    main()
    print(x)


"""
 Global Interpreter Lock (GIL) simplifies thread management
 It is a locking mechanism that ensures that only one thread can execute Python code at a time, even on multi-core processors\
 it is good for I/O bound but not for CPU bound threads
 It is going to be gone soon...
"""
from random import randint
from threading import Thread

print('---pseudo multithreads...\n')
def count_on(name, n):
    for i in range(n):
        print(f"{name}: {i}")

th1 = Thread(target=count_on, args=('Thread1', 3))
th2 = Thread(target=count_on, args=('-Thread2', 3))
th1.start()
th2.start()
th1.join()
th2.join()

print("\n--- GIL's work - time limit thread manage...\n")
def count_on(name, n):
    for i in range(n):
        print(f"{name}: {i}")

th1 = Thread(target=count_on, args=('Thread1', 10))
th2 = Thread(target=count_on, args=('-Thread2', 10))
th1.start()
th2.start()
th1.join()
th2.join()
    
print("\n--- sequential I/O bound work ...\n")
from datetime import datetime
import json

res = []
files = ['file1.json', 'file2.json', 'file3.json', 'file4.json', ]
## generate
# for f in files:
#     for _ in range(100_000):
#         res.append(randint(0, 10000))
#     with open(f, 'w', encoding='utf-8') as file:
#         json.dump(res, file)
#     res.clear()


res_to_count = []
start = datetime.now()

for file in files:
    with open(file, 'r') as f:
        data = json.load(f)
        res_to_count.extend(data)

end = datetime.now()

print(sum(res_to_count))
print(end-start)

print("\n--- multithreading I/O bound work ...\n")    

res.clear()
res_to_count.clear()
threads = []

def worker(file):
    with open(file, 'r') as f:
        data = json.load(f)
        res_to_count.extend(data)

start = datetime.now()

for i in range(len(files)):
    t = Thread(target=worker, args=(files[i], ))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = datetime.now()

print(sum(res_to_count))
print(end-start)

"""
    Catch errors in threads...
"""
# from threading import Thread, excepthook
from time import sleep 
import threading
import sys

print('--- catch by exception...\n')

def some_func():
    sleep(4)
    raise Exception

def thread_func():
    try:
        some_func()
    except Exception as exc:
        print('---Exception!!!')

t1 = threading.Thread(target=thread_func)
t2 = threading.Thread(target=thread_func)
t1.start()
t2.start()
t1.join()
t2.join()

print('\n--- catch by Threading.excepthook...\n')

def m_excepthook(args):
    print(f'excepthook(): {args.thread.is_alive()}')
    print(f'excepthook(): {args.thread.name}')

threading.excepthook = m_excepthook  ## function to handle exceptions in threads
## doesn't work as:
##    from threading import excepthook
##     ...
##    excepthook = m_excepthook 
## don't mix up with sys.excepthook

t1 = threading.Thread(target=some_func)
t2 = threading.Thread(target=some_func)
t1.start()
t2.start()
t1.join()
t2.join()

print('\n--- sys.excepthook...\n')

def exc_sys_hook(args, a, b): ## 3 args
    print(f'My handle...<{args}>, <{b}>, <{a}>')

sys.excepthook = exc_sys_hook

raise Exception


"""
import modules 10
"""