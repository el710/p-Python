"""
Iterators....
https://docs.python.org/3/library/itertools.html
"""
import sys
from itertools import repeat

## mem using
ex_iterator = repeat('4', 100_000)
ex_string = '4' * 100_000

print(f'string: {ex_string} mem: {sys.getsizeof(ex_string)}')
print(f'iterator: {ex_iterator} mem: {sys.getsizeof(ex_iterator)}')

print('\n Iterator class object...\n')

class Iteratical():
    def __init__(self) -> None:
        self.first  = 'el first'
        self.second = 'el second'
        self.third  = 'el third'
        self.counter = 0
    
    def __iter__(self):
        self.counter = 0
        return self
    
    def __next__(self):
        self.counter += 1
        if self.counter == 1:
            return self.first
        elif self.counter == 2:
            return self.second
        elif self.counter == 3:
            return self.third
        
        raise StopIteration() ## method 'for' will catch this exception

obj = Iteratical()
print(obj)

for item in obj:
    ## here processor calls __next__() automatically
    print(item)
    

## 'for' process:
# try:
#    while True:
#       value = obj.__next(obj)
#       ...
#       print(value)
#       ...
# except StopIteration:
#   pass 
    
"""
for example...
"""

def fibonachi(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

for value in fibonachi(10): ## function returns list and gets memory and process time for it
    print(f'func(): {value}')

## cheapest variant with iterator
class C_fibonachi():
    def __init__(self, n) -> None:
        self.i_ter = 0
        self.a = 0
        self.b = 1 
        self.n = n
    
    def __iter__(self):
        self.i_ter, self.a, self.b = 0, 0, 1
        return self
    
    def __next__(self):
        self.i_ter += 1
        if self.i_ter > 1:
            if self.i_ter > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a

fib_iterator = C_fibonachi(10)
for value in fib_iterator:
    print(f'class(): {value}')
for value in fib_iterator:
    print(f'class(): {value}')



