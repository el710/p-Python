from os import system
system('cls')

def add_everything_up(el_1, el_2):
    try:
        sum = el_1 + el_2
    except TypeError:
        if isinstance(el_1, str):
            sum = el_1 + str(el_2)
        else:
            sum = str(el_1) + el_2

    return sum

print(f"123.456 + 'string' = {add_everything_up(123.456, 'string')}")
print(f"'apple' + 4215 = {add_everything_up('apple', 4215)}")
print(f"123.456 + 7 = {add_everything_up(123.456, 7):0.3f}")


