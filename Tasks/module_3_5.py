import os
os.system('cls')
print("Work with function's recurcive - multiply\n")

def get_multiplied_digits(number):
    number = str(int(number))
    
    if len(number) == 1:
        return int(number)
    
    first = int(number[0])
    
    last = get_multiplied_digits(number[1:])
    if last == 0:
        return first
    else:
        return first * last

str_number = input("input some digit's row: ")
mult = get_multiplied_digits(str_number)
print("result of multiplication =",mult)

input("\npress <Enter> to leave...")



