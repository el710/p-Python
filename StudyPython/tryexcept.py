"""
Exceptions:
    Exception
    ValueError
    TypeError
    IndexError
    KeyError
    IOError
"""


from os import system
system("cls")

print("try .. except")
# div = int(input("input number: "))
div = 0
a = 0

try:
    a = 10 / div
except:
    print("there is some error ???")
else:
    print("nothing wromg :)")
finally:
    print("this code will work forever!!!!")


print("\n get class of exception...")
try:
#    a = 10 / div
    b = a + c
# except ZeroDivisionError:  ## set classes of error  (... , ...)
#     print(f"something wrong with <10 / {div}>")  ## run if ZeroDivision only
except NameError as exc: ## save error message in 'exc'
    print(f"there is error with variable 'c' - {exc}")


print("\n get args of exception...")
try:
    file = open("text.txt")
except OSError as exc:
    print(f"{exc}: {exc.args}")


## raise - call exception

def ch_name(person):
    if person == "xthn":
        raise Exception("wrong name")
    print(f'hello {person}')


ch_name("Oleg")
try:
    ch_name("xthn")
except Exception as exc:
    print(f'got exception {exc} ({type(exc)}): {exc.args}')
    # raise # we can call it again


print('\n our own class...\n')

class CatchZero(Exception):
    def __init__(self, message, args) -> None:
        self.message = message
        self.args = args ## cant make dictionary


import logging

def fun(a, b):
    if b == 0:
        # logging.exception("Attention: error")
        raise CatchZero("division by zero", {a, b})
    else:
        return a / b
    
try:
    fun(4, 0)
except CatchZero as exc:
    logging.exception("Attention: error")
    print(f'{exc.message}, {exc.args} {type(exc.args)}')


print('\n big teasting...\n')

def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    print(f'Get: {operand_1} {operation} {operand_2}', end = '')
    if operation == '+':
        print(f' = {operand_1 + operand_2}')
    if operation == '-':
        print(f' = {operand_1 - operand_2}')
    if operation == '*':
        print(f' = {operand_1 * operand_2}')
    if operation == '/':
        print(f' = {operand_1 / operand_2}')
    if operation == '//':
        print(f' = {operand_1 // operand_2}')
    if operation == '%':
        print(f' = {operand_1 % operand_2}')



with open('matdata.txt', 'r') as file:
    for cnt, line in enumerate(file):
        try:
            calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Error in {cnt} line: not enought data  ({exc})')
            else:
                print(f'Error in {cnt} line: {exc}')



try:
     1 / 0
except ZeroDivisionError as exc:
    raise ValueError("wrong divider") from exc


""""
import module_8_1,  module_8_2,
"""