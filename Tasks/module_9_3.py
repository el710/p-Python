from os import system
system('cls')

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(item[0]) - len(item[1]) for item in zip(first, second) if len(item[0]) != len(item[1]))
second_result = (len(first[idx]) == len(second[idx]) for idx in range(len(first)))

print(list(first_result))
print(list(second_result))