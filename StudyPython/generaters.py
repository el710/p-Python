from os import system
system('cls')

"""
    one-time process generators - they returns iterator
"""

my_numbers = list(range(1, 11))
print(f"generate list : {my_numbers}")

## iterator = generator()
result = (x ** 100 for x in my_numbers) ## this is just scheme - has not any values in memory

# for item in result: ##
#     print(item) ## when item is called - it start to be computed
# ## but it doesn't work twice - there is no more 'result'
# for item in result:
#     print(f"again: {item}") 

# ## process timing different
# import time

# start_time = time.time()
# result = [x ** 500 for x in my_numbers]  ## list in memory
# for i in result:
#     print(i)
# finish_time = time.time()
# print(f'process time [] msec: {(finish_time - start_time) * 1000}')

# start_time = time.time()
# result = (x ** 500 for x in my_numbers)  ## just scheme - generator
# for i in result:
#     print(i)
# finish_time = time.time()
# print(f'process time () msec: {(finish_time - start_time) * 1000}')

# list_1 = range(1, 10)
# list_2 = range(11, 20)

#  ## these are just schemes
# rng = range(10, 31)
# zp = zip(list_1, list_2)
# mp = map(str, list_1)

# ## in list() schemes become real values
# print(list(rng)) 
# print(list(zp))
# print(list(mp))

# """
#   fast functions-generators
# """
# def func_generator(n):
#    i = 0
#    while i != n:
#       yield i ## ~ return value without exit
#       i += 1

# obj = func_generator(10)
# print(obj) ## - it is just object

# for i in obj:
#     print(i)

# def fib2(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a 
#         a, b = b, a + b

# print('\n fibonachi v2...\n')
# gen = fib2(10)
# for value in gen:
#     print(value)
# ## here gen will be deleted

# def fib3():
#     a, b = 0, 1
#     while True:
#         yield a 
#         a, b = b, a + b

# print('\n fibonachi v3... more faster then "for"\n')
# for value in fib3():
#     print(value)
#     if value > 1000 ** 6:
#         break

# """
# large files do
# """
# start_time = time.time()

# def r_file(file_name):
#     with open(file_name, 'r', encoding="utf-8") as file:
#         for line in file:
#             yield line.strip()

# for line in r_file('large.txt'):
#     print(line) 

# finish_time = time.time()
# print(f"file was readen in msec: {(finish_time - start_time) * 1000}")