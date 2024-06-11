
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


print("\n", "*** List[] - indexable, changable, extansionable, multitype elements")

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
item = food.pop(3)
print("take element with delete -", food, item)

result = "coconut" in food
print("is 'coconut' in lists -", result) # checkout for elements
result = "apple" not in food
print("is 'apple' not in lists -", result) # checkout for elements

print("slice from [0] to [5] over 2 -",food[0:5:2])

print("\n", "*** Tuple() - indexable, locked elements & subchangable, nonextansionable, multitype elements, memory lighter")
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

print("\n*** Dictionary{} - paired item, indexable, changable, extansionable, multitype values")

phone_book = {'Denis': 81002223456, 'Max': 82003334567, 'Kolya': [2354, 5646]}
print("create dictionary -", phone_book)
print("value type of 'Kolya' -", type(phone_book['Kolya']))

item = phone_book["Denis"]
print("take element by key 'Denis': ", item, " type is ", type(item))
item = phone_book.get('Kamila', "there is no such item")
print("take not existing element by key 'Kamila': ", item)

phone_book["Denis"] = 83004445678
print("change item 'Denis' -", phone_book["Denis"])
phone_book['Anton'] = 84005556789
print("add new item -", phone_book)
phone_book.update({'Sasha': 85006667890,
                  'Alex': 86007778901})
print("add set of items -", phone_book)

del phone_book["Max"]
print("delete item 'Max' -", phone_book)
item = phone_book.pop('Anton')
print("take value with delete -", phone_book, item)

items = phone_book.keys()
print("get list of keys -", items, type(items))
items = phone_book.values()
print("get list of values -", items, type(items))

items = phone_book.items()
print("get list of items -", items, type(items))


print("\n*** Set{} - uniq items, nonordered, extansionable, multitype items")
new_set = {1, 2, 3, 4, 5, 6, 3, 1, 2, "string", True, (9, 8, 7)}
print("create set with uniq items -", new_set)

new_list = ['a', 'b', 'c']
new_list = set(new_list)
print("create set from lists -", new_list)
new_list.discard('b')
print("delete item 'b' by discard('without error <not exists>') -", new_list)
res = new_list.remove('c')
print("delete item 'c' by remove('item must exists') -", res, new_list)
new_list.add("something new")
print("add new item -", new_list)

input("\n press <Enter> to leave...")