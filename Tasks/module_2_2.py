import os
os.system('cls')

print("Work with 'if' operator...\n")

first = int(input("We need three integer numbers, type the first: "))
second = int(input("input the second: "))
third = int(input("end the last one: "))

list = list([first, second, third])
print("Now we have list of tese numbers: ",list)

if first == second and first == third and second == third:
    print("result 3: all numbers are equal")
elif first == second or first == third or second == third:
    if first == second or first == third:
        print(f"result 2: there is pair of {first}")
    else: 
        print(f"result 2: there is pair of {second}")
else:
    print("result 0: there are no equal numbers at all")
  
# ### academic option
# from collections import Counter
# c = Counter([first, second, third])
# r = {e: count for e, count in c.items() if count > 1}
# print(r)    
    
input("\nThat's all folks.\nPress <Enter> to leave....")


