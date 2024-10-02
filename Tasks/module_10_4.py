from random import randint
from threading import Thread
from time import sleep
from queue import Queue

BUSY_MIN = 3
BUSY_MAX = 10

class Table():
    def __init__(self, number, guest=None) -> None:
        self.number = number
        self.guest = guest
      
    def put_guest(self, guest) -> bool:
        if self.guest == None:
            self.guest = guest
            return True
        return False
        
    def free(self):
        self.guest = None
    
    def is_free(self):
        return self.guest == None
    
    def get_number(self):
        return self.number
    
    def get_guest(self):
        return self.guest

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def __str__(self):
        return self.name
    
    def run(min, max):
        sleep(randint(min, max))


class Cafe():
    def __init__(self, *tables) -> None:
        self.queue = Queue()
        self.tables = tables
        self.threads = {}
      
    def __del__(self):
        for key, thread in self.threads.items():
            thread.join()  
    
    def guest_arrival(self, *guests):
        for guest in guests:
            guest_wait = True
            for table in self.tables:
                if table.put_guest(guest):
                  print(f'{guest} has got table N {table.get_number()}')
                  thread = Guest(BUSY_MIN, BUSY_MAX)
                  thread.start()
                  self.threads[guest] = thread

                  guest_wait = False
                  break
            if guest_wait:
                  self.queue.put(guest)
                  print(f'{guest} in line...')
                  
    def discuss_guest(self):
        busy_tables = True
        while not self.queue.empty() or busy_tables:
            for table in self.tables:
                if not table.is_free():
                    guest = table.get_guest()
                    if not self.threads[guest].is_alive():
                        print(f'{guest} have done and gone')
                        print(f'Table {table.get_number()} is free')
                        table.free()

                if table.is_free() and not self.queue.empty():
                    guest = self.queue.get()
                    table.put_guest(guest)
                    print(f'{guest} has out from line and got table N {table.get_number()}')
                    thread = Guest(BUSY_MIN, BUSY_MAX)
                    thread.start()
                    self.threads[guest] = thread
            
            busy_tables = False
            for table in self.tables:
                if not table.is_free():
                    busy_tables = True


tables = [Table(number) for number in range(1, 6)]
guest_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Victoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guest_names]

cafe = Cafe(*tables)
cafe.guest_arrival(*guests)    
cafe.discuss_guest()