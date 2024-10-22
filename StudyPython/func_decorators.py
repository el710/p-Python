from os import system
system('cls')

"""
decorators...
"""
# def decorate(func):
#     def sur(*args):
#         original_func = func
#         #  some additional code
          # ...
#         res = func(*args)
#         # ...
#         return sur

# ## variant 1   
# def func():
#     pass
# func = decorate(func)
# ##  variant 2
# @decorate
# def func():
#     pass

print("simple null decorator...\n")
def null_decorator(func):
    return func

def greet():
    print('Hello')

greet = null_decorator(greet)
greet()

print("\n...added...\n")

def uppercase(func):
    def mrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    
    return mrapper
    
@uppercase
def greet():
    return "Hello"

# ## like this
# greet_up = uppercase(greet())
# print(greet_up())

print(greet())

print("\n...more...\n")
import time, sys

def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at =  time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f"{func.__name__}() work time: {elapsed} sec")
        return result
    return surrogate

@time_track
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))

sys.set_int_max_str_digits(100_000) ## increase the limit for string length
result = digits(3141, 5926, 2718, 2818)
print(result)


print("\n...online decorator.......\n")

def func_gen_dec(precision):
    print(f'{func_gen_dec.__name__}: get precision')
    print(f'{func_gen_dec.__name__}: make decorator')
    def dec(func):
        print(f'{dec.__name__}: start decoration')
        print(f'{dec.__name__}: make wrapper')
        def wrapper(*args, **kwargs):
            print(f'{wrapper.__name__}: start wrapper')
            start = time.time()
            print(f'{wrapper.__name__}: call {func.__name__}')
            result = func(*args, **kwargs)
            end = time.time()
            elapsed = round(end-start, precision)
            print(f'{func.__name__}() work time: {elapsed} sec')
            print(f'{wrapper.__name__}: return result')
            return result
        print(f'{dec.__name__}: return wrapper')
        return wrapper
    print(f'{func_gen_dec.__name__}: return decorator')
    return dec

@func_gen_dec(5)
def digits(*args):
    total = 1
    for i in args:
        total *= i ** 5000
    return len(str(total))

sys.set_int_max_str_digits(100000)

# time_track = func_gen_dec(5)
# digits = time_track(digits)
result = digits(3141, 5926, 2718, 2818)
print(result)