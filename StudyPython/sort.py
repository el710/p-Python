from os import system
from random import randint


system('cls')

print("Practice: sorting and stuff....\n") 
67
size = int(input("input size for list: "))
sort_list = []
for i in range(size):
    sort_list.append(randint(1, size + 1))

print(f"Here is out list for practice: {sort_list}")

def select_sort(lst):
    w_list = list(lst)
    print(f"for select - {w_list}")
    for i in range(len(w_list) - 1, 0 ,-1):
        for j in range(i):
            if w_list[j] > w_list[j + 1]:
                w_list[j], w_list[j + 1] = w_list[j + 1], w_list[j]
    return w_list

def buble_sort(lst):
    print(f"\nfor buble - {lst}")
    for i in range(len(lst) - 1):
        min_item = i
        # print(f"{i}: ----")
        for j in range(i + 1, len(lst)):
            # print(f"[{j}]: {lst[min_item]} ? {lst[j]}")
            if lst[min_item] > lst[j]:
                lst[min_item], lst[j] = lst[j], lst[min_item]
                min_item = j
                
                # print(f"--- change min {min_item}")
                # print(lst)
    return lst
    
#print("Selecting sorting:", select_sort(sort_list))
dt = [9, 7, 4, 5,]

print("Buble sorting:", buble_sort(dt))

input("\npress <Enter> to leave...")
