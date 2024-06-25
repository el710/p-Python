import os
from time import sleep

os.system('cls')
print("Work with variable's area...\n")


calls = {}

def count_calls(name):
    global calls
    if name in calls.keys():
        calls[name] += 1
    else:
        calls[name] = 1

def string_info(in_str):
    count_calls("string_info")
    return (len(in_str), in_str.upper(), in_str.lower())

def is_contains(in_str, in_list):
    count_calls("is_contains")
    for i in in_list:      
        if in_str.lower() in i.lower():
            ## print(f"{in_str.lower()} is in the {i.lower()}")
            return True

    return False

user_str="test"

while len(user_str) > 0:
    os.system('cls')
    user_str = input("Type some string (just <Enter> for ending): ")
    u_list = []
    
    if len(user_str) > 0:
        print("Length, Upcase, Lowcase")
        print("String info():", string_info(user_str))

        while True:
            str = input("input any string to compare (or just <Enter> if enough): ")
            if len(str) > 0:
                u_list.append(str)
            else:
                break
        
        print(f"is_contains(): '{user_str}' in {u_list} - ", is_contains(user_str, u_list))
        input("\npress <Enter> to continue...")


print("\nYour calls: ", calls)
print("Summary: ", sum(calls.values()))

input("\npress <Enter> to leave...")
