from os import system
system('cls')

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_string = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(item) for item in first_strings if len(item) >= 5 ]
second_result = [(x, y) for x in first_strings for y in second_string if len(x) == len(y)]
third_result = {x: len(x) for x in list(first_strings + second_string) if  not len(x) % 2}

print(first_result)
print(second_result)
print(third_result)
