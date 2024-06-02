import os
os.system('cls')

print('Here are examples with print() type() & data types')

# constant values
print(5,type(5))  # int (integer)
print(3.14,type(3.14))  # float
print("string", type("string"))  # str (string)

print("'Hello' " + '"world"')

print(True, False, type(True)) # bool (boolean)

# logic operands
print('5 > 10', 5 > 10)  # >, <
print('7 <= 7', 7 <= 7)
print("'c' != 'd'", 'c' != 'd')
print('3 == 3', 3 == 3)

print("True and False = ", True and False)
print("True or False = ", True or False)

print("string number to integer number ", int('5'))