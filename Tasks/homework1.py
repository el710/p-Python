# Home work & tasks
import os
os.system('cls')

print('*Strings & indexation*')

str_exemple = input("Type some string: ")
print('Here is the first symbol - ', str_exemple[0])
print('Here is the last symbol - ', str_exemple[-1])
print('Here is the second part - ', str_exemple[len(str_exemple)//2:])
print('Here is mirror view - ', str_exemple[::-1])
print('Here is each second char  - ', str_exemple[1::2])

input("press <Enter> for the end...")
####################
# end task 2