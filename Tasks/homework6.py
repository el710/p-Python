import os
os.system('cls')

print("\n --- Dictionary ---")
my_dict = {"deca": 10, "kilo": 1000, "mega": 1000000}
print("create dictionary: ", my_dict)

print("get value of 'kilo': ", my_dict['kilo'])
print("get value of 'giga': ", my_dict.get('giga', "there is no 'giga'"))

my_dict.update({"giga": 1000000000, "hecto": 100})
print("add 'giga' & 'hecto': ", my_dict)

item = my_dict.pop("mega")
print("take out 'mega': ", item, my_dict)


print("\n --- Set ---")
my_set = {1, 2, 3, True, (9, False, "world"), "Hello", False, 3, 2, 1}
print("create set: ", my_set)

my_set.add(True) ## can't add True
my_set.add(99)
print("add items: ", my_set)

my_set.discard(2)
print("discard item '2': ", my_set)


input("\n press <Enter> to leave....")