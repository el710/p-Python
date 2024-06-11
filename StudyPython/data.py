
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

print("\n", "*** variables")
PersonName = "Maxitron" # str
print('string variable "PersonName" - ', PersonName)


print("\n", "*** dynamic type - in python variable can change its type")
name = "Urban" # str
print(name, type(name))
name = 5
print(name, type(name))
name = 5.5
print(name, type(name))
name = [1,2]
print(name, type(name))


print("\n", "*** Lists[] - indexable, changable, extansionable, multitype elements")

food = ["apple", "coconut", "banana"] ## create
print("create list -", food)

elem = food[0]  ## take element by index
print("get element [0] -", elem, type(elem))

food[0] = "peach" # change element
print("change elements [0] -", food)

food.append(True) # add to end
print("add new element with other type to the end -", food)

food.extend("string") # add string as a set of symbols
print("add string as a set of symbols -", food)

food.extend(["string", 2]) # add list
print("add several elements -", food)

food.remove("string") # delete set
print("delete element [string] -", food)

result = "coconut" in food
print("is 'coconut' in lists -", result) # checkout for elements
result = "apple" not in food
print("is 'apple' not in lists -", result) # checkout for elements

print("slice from [0] to [5] over 2 -",food[0:5:2])

print("\n", "*** Tuples - indexable, locked elements & subchangable, nonextansionable, multitype elements, memory lighter")
tuple_1 = 1, 2, 3, 4
tuple_2 = (5, 6, 7, 8) + (5, 6)
tuple_3 = tuple([9, 10, True, "string"])

print("create tuple -", tuple_1, type(tuple_1))
print("take element [2]: ", tuple_2[2], "from ", tuple_2)
print("multitype elements:", tuple_3) ## any types

### tuple[0] = 77 # it's error. can't change element of tuple
tuple_4 = ([1, 2], 3) # tuple with changeble element
print("before subchange:", tuple_4)
tuple_4[0][0] = 5
print("after subchange: ", tuple_4)

tuple_1 = tuple_2 * 2
print("multi tuple: ", tuple_1)

##memory using
food = [9, 10, True, "string"]
print("List size - ", food.__sizeof__())
print("Tuple size - ", tuple_3.__sizeof__())











input("press <Enter> to leave...")