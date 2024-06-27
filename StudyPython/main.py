# Comments
## ctrl + /  - comment selected rows

### https://docs.python.org/

### https://www.youtube.com/watch?v=R4WF9xad_EI - 10 вопросов Python-разработчику

### https://habr.com/ru/companies/ruvds/articles/500296/ - 41 вопрос о работе со строками в Python

### https://www.reg.ru/blog/5-klassnyh-veschej-kotorye-vy-mozhete-osvoit-s-python/ - 5 вещей, которые вы можете освоить с Python

import os                 ## link library 'os' - function call need full path  os.system
##import time*             ## link all from library 'math' - function call sin()
from time import sleep    ## link only function sleep() from library 'time' - function call sleep()

os.system('cls')

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
    return (f"Hello {name} at {age}")

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

################### area of variables

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
    print(c, d) 


print(a, b)
func(1, s=2, t=3) # s & t keword-only, because of '*' in function definition
print(a, b)
## print(c, d) we can't use it here






############################################
input("\npress <Enter> to leave...")


