# Comments
## ctrl + /  - comment selected rows

### https://docs.python.org/

### https://www.youtube.com/watch?v=R4WF9xad_EI - 10 вопросов Python-разработчику

### https://habr.com/ru/companies/ruvds/articles/500296/ - 41 вопрос о работе со строками в Python

### https://www.reg.ru/blog/5-klassnyh-veschej-kotorye-vy-mozhete-osvoit-s-python/ - 5 вещей, которые вы можете освоить с Python

### https://drive.google.com/file/d/1SUOHiI5Qicp0clk9OLIwkdySWluNbWJZ/view?usp=drive_link

import os                 ## include library 'os' - function call need full path  os.system()
from math import *        ## link all from library 'math' - function call sin()
from time import sleep    ## link only function sleep() from library 'time' - function call sleep()
## from <path>.<filename> import < filename / function / *(all) >

'''
from ..Tasks import module_4_1
'''

os.system('cls')

import this ## python programming rules

print('Freedom Worth')

# x = 43
# y = 32
# print(x * y)
# print("End line")

# name = input("Input your name: ")
# if name == "Urban":
#    print("Hello admin")
# else:
#      print("Hello,", name)

#current_year = 2024
#date_of_birth = input("input your birth year: ")
#age = current_year - int(date_of_birth)
#print("....")
#sleep(5)
#print("You are", age, "old")

# age = int(input("enter your code: "))
# if age % 3 == 0 and age % 5 == 0:
#  print("FizzBuzz")
# elif age % 3 == 0:
#  print("Fizz")
# elif age % 5 == 0:
#   print("Buzz")
# else:
#  print("wrong code!!!")

###################################

# print("'While' example ")
# while True:
#   os.system('cls')
#   number = int(input("Input integer number: "))

#   if number % 2 == 0:
#     print(f" {number} is even")
#     sleep(2)
#     continue # no need to process...
#   else:
#     print(f"{number} is odd number")
#     if number == 7:
#       break
  
#   print("processing odd number...")
#   sleep(4)

# print("cycle is off")

#########################

# print("'For' example ")
# print("\n Ex1")
# for i in 1, 2, 3, 4: ## var in every iteration will get next element from list
#   print(i)

# print("\n Ex2")
# for i in range(5): ## range(start, STOP, step)
#   print(i)

# print("\n Ex3")
# for i in "hello": ## var from list
#   print(i)

# print("\n Ex4")
# my_list = ['one', 'two', 'three']
# for i in my_list: ## var from list
#   if i == 'three':
#     my_list.remove(i)
# print(my_list)

# print("\n Ex5")
# for i in range(len(my_list)):
#   print(my_list[i])

# print("\n Ex6")
# dict_ = {'a': 1, "b": 2, "c": 3}
# for i in dict_:
#   print(i, dict_[i])

# print("\n Ex7")
# dict_ = {'a': 1, "b": 2, "c": 3}
# for i, e in dict_.items():
#   print(i, e)

strings = ["Text for tell.",
        "Используйте кодировку utf-8.",
        "Because there are 2 languages!",
        "Спасибо!"
    ]

strings_positions = {}

for idx, item in enumerate(strings):
    _key = (idx + 1, len(item))
    strings_positions[_key] = item

print(strings_positions)


input("\npress <Enter> to continue...")

#########################

# print("'Functions' example ")

# import random

# ## define
# def simple():
#     print("simple(): this are some functions...")

# def get_data(a, b):               ## function takes arguments
#     print(f"get_data(): get arguments a: {a} b: {b}")

# def get_ini_data(a = 1, b = True):  ## function takes arguments with initialised means
#     print(f"get_ini_data(): ini arguments a: {a} b: {b}")

# def get_any_data(*args):          ## function takes any simple arguments and returns data
#     print(f"get_any_data(): any arguments: {args}", *args)
#     return args[0]

# def get_any_named_data(**kwargs):          ## function takes any named arguments
#     print("get_any_named_data(): any arguments: ", kwargs['a'], kwargs['b']) 

# def lottery(mon, thue):
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(tickets)
#     tickets.remove(win1) ## to avoid coincidence

#     win2 = random.choice(tickets)
#     print(f"lottery(): {mon}, {thue}")
#     return win1, win2

def hello_func(name, age):
    '''
    Documentation: simple function
    '''
    return (f"Hello {name} at {age}")

print(help(hello_func))
## or
print(hello_func.__doc__)

def info(pos_value, *any_values, named=3.14, **any_named): ## all types of args and declaration order
    print(pos_value)
    print(any_values)
    print(named)
    print(any_named)
    return None


## lambda function
## only one string
## <name> = lambda <args>: <function>
result = lambda x, y: x + y
print(result(5, 7))


### there is recursion
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)

print(f"Calc sum by recursive: sum(5) = {sum(5)}")

# ## call
# simple()

# get_data(1, "string")
# get_data(True, {'a', 'b', 'c'})

# get_ini_data()
# get_ini_data([1, 2]) # give one argument 'list'
# get_ini_data(b=10) # set value by key
# get_ini_data(*[1, False]) # give list of arguments
# get_ini_data(*('tuple', 'allowed')) # give tuple of arguments
# get_ini_data(**{'a': 'set', 'b': 'dictionary'}) # give dictionary of arguments

# get_any_data([1, 2, 3])

# fun_back = get_any_data("string", "word")
# print("result:", fun_back)

# vars = {'a': 'alfa', 'b': 'beta'}
# get_any_named_data(**vars)

# win1, win2 = lottery('mon', 'thue')
# print(win1, win2)

# print(hello_func('Ann', 23))


# m_list = list(range(1,10))
# print(m_list)

# num = 1
# print("%02d" % num)
# num += 2


'''
from ..Tasks import module_3_2, module_3_3, module_3_4, module_3_5
'''



################### area of variables

print(globals()) ## list of global namespace
print(locals())  ## list of local namespace

## global 
a = 10
b = 20

def func(f, *, s, t):   # * - means i must set values after that (s & t) namelly
    global a, b # use global variables
    a = "hell"
    b = "ow"
## there are local
    c = 30
    d = 40
    print("View namespaces", c, d) 

print(a, b)
func(1, s=2, t=3) # s & t keword-only, because of '*' in function definition
print(a, b)
## print(c, d) we can't use it here

g = 6              ## global g
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

  
args = (1, 2, 3, 4, 5, 6)

for i in range(6):
    print("for by index: - ", args[i])

for i in args:
    print("for by element: - ", i)

'''
from ..Tasks import module_4_2
'''



############################################
input("\npress <Enter> to leave...")


## to make exe need:
## install package:  pip install pyinstall (in terminal)
## > pyinstaller --onefile -w 'file.py'

## pip install auto-py-to-exe - window interface
## > auto-py-to-exe