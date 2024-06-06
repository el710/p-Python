import os
os.system('cls')

print("Here is task with strings")

my_string = input("input any text: ")
print(f"String '{my_string}' has length = {len(my_string)} symbols")

print(f"Up register - '{my_string.upper()}'")
print(f"Low register - '{my_string.lower()}'")
print(f"Without whitespaces - '{my_string.replace(' ', '')}'")
print(f"First symbol  - '{my_string[0]}'")      
print(f"Last symbol  - '{my_string[len(my_string) - 1]}'")      


input("Press <Enter> to leave...")