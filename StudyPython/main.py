# Comments
## ctrl + /  - comment selected rows

### https://docs.python.org/

### https://www.youtube.com/watch?v=R4WF9xad_EI - 10 вопросов Python-разработчику

### https://habr.com/ru/companies/ruvds/articles/500296/ - 41 вопрос о работе со строками в Python

### https://www.reg.ru/blog/5-klassnyh-veschej-kotorye-vy-mozhete-osvoit-s-python/ - 5 вещей, которые вы можете освоить с Python

import os                 ## include library 'os' - function call need full path  os.system()
from math import *        ## link all from library 'math' - function call sin()
from time import sleep    ## link only function sleep() from library 'time' - function call sleep()
## from <path>.<filename> import < filename / function / *(all) >

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



############################################
input("\npress <Enter> to leave...")


'''
from ..Tasks import module_3_2, module_3_3, module_3_4, module_3_5, module_4_2
'''


## to make exe need:
## install package:  pip install pyinstall (in terminal)
## > pyinstaller --onefile -w 'file.py'

## pip install auto-py-to-exe - window interface
## > auto-py-to-exe