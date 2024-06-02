# Home work & tasks
import os
os.system('cls')

print('*Length of string*')

int_num = int(input("Type some integer number: "))
str_a = str(int_num)
length = len(str_a)
print(f'Length of "{str_a}" =', length, "\n")

input("press <Enter> to continue...")
os.system('cls')
####################

print('*Sum & different*')

first = int(input("Input first integer number: "))
second = int(input("Input second integer number: "))
sum = first + second
diff = first - second
print(f'{first} + {second} = ', str(sum))
print(f'{first} - {second} = ', str(diff), "\n")

input("press <Enter> to continue...")
os.system('cls')
####################

print('*Average*')

first = int(input("Input first integer number: "))
second = int(input("Input second integer number: "))
third = int(input("Input third integer number: "))
mean = (first + second + third) / 3
print(f'Average of [{first}, {second}, {third}] - ',str(mean), "\n")

input("press <Enter> to continue...")
os.system('cls')
####################

print('*Simple strings*')

first_string = input("Type 'Tuesday': ")
second_string = input("Type 'Monday': ")
print(second_string + ", " + first_string, "\n")

input("press <Enter> to continue...")
os.system('cls')
####################

print('*Complicate formula*')
val_a = int(input("Input first integer number: "))
val_b = int(input("Input second integer number: "))
val_c = int(input("Input third integer number: "))
val_f = (val_a * val_b) + (val_a * val_c)
print(f'((({val_a} * {val_b}) + ({val_a} * {val_c})) ^ 3) / 2 = ', val_f ** 3/2 , "\n")

input("press <Enter> for the end...")
####################
# end task 1