from os import system
system('cls')

print("'Functions' examples....\n ")

import random

## define
def simple():
    '''
    Documentation: simple function
    '''
    print("simple(): this are some functions...")

print(f'function is an object of class: {type(simple)}')
print(f'function has attributes: name - {simple.__name__}')
print(simple.__doc__)
## or
print(help(simple))
simple()

print('\n--------- Arguments...\n')

def get_data(a, b):               ## function takes arguments
    print(f"get_data(): get arguments a: {a} b: {b}")

get_data(1, "string")
get_data(True, {'a', 'b', 'c'})


def get_ini_data(a = 1, b = True):  ## function takes arguments with initialised means
    print(f"get_ini_data(): ini arguments a: {a} b: {b}")

get_ini_data()
get_ini_data([1, 2]) # give one argument 'list'
get_ini_data(b=10) # set value by key
get_ini_data(*[1, False]) # give list of arguments
get_ini_data(*('tuple', 'allowed')) # give tuple of arguments
get_ini_data(**{'a': 'set', 'b': 'dictionary'}) # give dictionary of arguments


def get_any_data(*args):          ## function takes any simple arguments and returns data
    print(f"get_any_data(): any arguments: {args}", *args)
    return args[0]

get_any_data([1, 2, 3])
fun_back = get_any_data("string", "word")
print("result:", fun_back)


def get_any_named_data(**kwargs):          ## function takes any named arguments
    print("get_any_named_data(): any arguments: ", kwargs['a'], kwargs['b']) 

vars = {'a': 'alfa', 'b': 'beta'}
get_any_named_data(**vars)


def lottery(mon, thue):
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tickets)
    tickets.remove(win1) ## to avoid coincidence

    win2 = random.choice(tickets)
    print(f"lottery(): {mon}, {thue}")
    return win1, win2

win1, win2 = lottery('mon', 'thue')
print(win1, win2)


def info(pos_value, *any_values, named=3.14, **any_named): ## all types of args and declaration order
    print(pos_value)
    print(any_values)
    print(named)
    print(any_named)
    return None


def func(f, *, s, t):   # * - means i must set values after that (s & t) namelly
    c = 30
    d = 40
    print("View namespaces", c, d) 

func(1, s=2, t=3) # s & t keword-only, because of '*' in function definition


### there is recursion
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)

print(f"Calc sum by recursive: sum(5) = {sum(5)}")

g = 6 ## global
def one_slice(x):
    g = x + 6         ## local g for one_slice
    def two_slice(x):
        nonlocal g      ## use g from one_slice
        ## global g     ## use global g
        g = x + 9
        print("middle namespace", g)
    
    two_slice(g)
    return g

print(f"Slices: {g} -> ", one_slice(g))

  
print('\n--------- As object...\n')

def get_slavy_names():
    return ['Ivan', 'Mitya', 'Gunya']

def get_rome_names():
    return ['John', 'Nick', 'Harry']

func = get_slavy_names
print(func())
print(func.__name__)

name_getters = [get_slavy_names, get_rome_names]
for name_getter in name_getters:
    print(name_getter())


def adder(args):
    res = 0
    for number in args:
        res += number
    return res

def mult(args):
    res = 1
    for number in args:
        res *= number
    return res

def process_numbers(numbers, function):
    result = function(numbers)
    print(f'result = {result}')

my_numbers = list(range(1, 10))
process_numbers(my_numbers, adder)
process_numbers(my_numbers, mult)


def pow_2(arg):
    return arg * 2

new_list = map(pow_2, my_numbers)  ## call function to each item -> make map object
print(type(new_list))
print(list(new_list))

def is_odd(arg):
    return arg % 2

new_list = filter(is_odd, my_numbers)
print(type(new_list))
print(list(new_list))


## lambda function
## only one string
## <name> = lambda <args>: <function>
result = lambda x, y: x + y
print(result(5, 7))

my_func = lambda x: x + 10

print(my_func(33))

list_1 = range(1, 10)
list_2 = range(10, 20)

func = map(lambda x, y: x + y, list_1, list_2)
print(list(func))


## on-fly functions

def mult(n):
    if n == 2:
        def mult_ex(x):
            return x * 2
    elif n == 3:
        def mult_ex(x):
            return x *3
    else:
        raise Exception('Only 2 or 3 multiplayer possible')
    
    return mult_ex

by_2 = mult(2)
by_3 = mult(3)

print(f'by_2: {list(map(by_2, list_1))}')
print(f'by_3: {list(map(by_3, list_1))}')


def mult_ext(n):
    def mult_fly(x):
        return x * n
    
    return mult_fly

print(f'by_4: {list(map(mult_ext(4), list_1))}')
print(f'by_5: {list(map(mult_ext(5), list_1))}')


## classic

class Multiplyer:
    def __init__(self, m) -> None:
        self.m = m
    
    def __call__(self, x) -> Any: ## object of this clsss can call like function
        return x * self.m


multy = Multiplyer(5)

numbers = list(range(1, 11))

list_x = list(map(multy, numbers))
print(list_x)






"""
import module_9
"""