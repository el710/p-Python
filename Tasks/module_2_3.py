import os

os.system('cls')

print("Here is some example with 'While' cycle...")

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, 5]
index = 0
print("Let's take positive numbers before negative one from list: ", my_list)

while True:
    if index > len(my_list) or my_list[index] < 0:
        break
    if my_list[index] > 0:
        print(f"{index}: {my_list[index]}")
    elif my_list[index] < 0:
        continue
    
    index = index + 1

input("We have done. Press <Enter> to leave...")

     