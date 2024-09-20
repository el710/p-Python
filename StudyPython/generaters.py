from os import system
system('cls')

"""
    one-time process generators
"""

my_numbers = list(range(1, 11))
print(my_numbers)

## generator
result = (x ** 100 for x in my_numbers) ## this is just scheme - has not any values in memory

for item in result:
    print(item) ## when item is called - it has been computed
## but it doesn't work twice - there is no more 'result'
for item in result:
    print(f"again: {item}") 

## process timing different
import time

start_time = time.time()
result = [x ** 500 for x in my_numbers]  ## list in memory
for i in result:
    print(i)
finish_time = time.time()
print(f'process time [] msec: {(finish_time - start_time) * 1000}')

start_time = time.time()
result = (x ** 500 for x in my_numbers)  ## just scheme
for i in result:
    print(i)
finish_time = time.time()
print(f'process time () msec: {(finish_time - start_time) * 1000}')

list_1 = range(1, 10)
list_2 = range(11, 20)

 ## these are just schemes
rng = range(10, 31)
zp = zip(list_1, list_2)
mp = map(str, list_1)

## in list() schemes become real values
print(list(rng)) 
print(list(zp))
print(list(mp))