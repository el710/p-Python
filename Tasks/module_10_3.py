from threading import Thread, Lock
from random import randint
from time import sleep

TRANS_COUNT = 100
TRANS_MIN = 50
TRANS_MAX = 500
TRANS_TIMEOUT = 0.001

class Bank(Thread):
    def __init__(self) -> None:
        super().__init__()
        self.balance = 0
        self.lock = Lock()
    
    def deposit(self, transaction):
        for i in range(transaction):
            value = randint(TRANS_MIN, TRANS_MAX)
            self.balance += value
            print(f'{i} Deposit: <{value}>. Balance: {self.balance}')
            if self.balance >= TRANS_MAX and self.lock.locked():
                self.lock.release()
                # print('---deposit(): lock released')
            sleep(TRANS_TIMEOUT)

    def take(self, transaction):
        for i in range(transaction):
            value = randint(TRANS_MIN, TRANS_MAX)
            print(f'{i} Request: <{value}>...')
            if value <= self.balance:
                self.balance -= value
                print(f'{i} Take: <{value}>. Balance: {self.balance}')
            else:
                print(f'{i} Request rejected: not enoght balance')
                # print(f'---take({i}): acquire lock...')
                self.lock.acquire()
                # print(f'---take({i}): lock passed')


bk = Bank()
th1 = Thread(target=bk.deposit, args=(TRANS_COUNT, ))
th2 = Thread(target=bk.take, args=(TRANS_COUNT, ))

th1.start()
th2.start()

th1.join()
th2.join()

print(f' State of balance: {bk.balance}')





