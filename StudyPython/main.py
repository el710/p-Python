# Comments
## ctrl + /  - comment selected rows

### https://docs.python.org/

### https://www.youtube.com/watch?v=R4WF9xad_EI - 10 вопросов Python-разработчику

### https://habr.com/ru/companies/ruvds/articles/500296/ - 41 вопрос о работе со строками в Python

### https://www.reg.ru/blog/5-klassnyh-veschej-kotorye-vy-mozhete-osvoit-s-python/ - 5 вещей, которые вы можете освоить с Python

import os
from time import sleep

#os.system('cls')

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

while True:
  os.system('cls')
  number = int(input("Input integer number: "))

  if number % 2 == 0:
    print(f" {number} is even")
    sleep(2)
    continue # no need to process...
  else:
    print(f"{number} is odd number")
    if number == 7:
      break
  
  print("processing odd number...")
  sleep(4)

print("cycle is off")







input("\npress <Enter> to leave...")


