import os
os.system('cls')

print("\n --- Tuple ---")
immutable_var = (1, 2.5, "title", True, [3, 4])
print("multi type tuple: ", immutable_var)

immutable_var[4][0] = 7
print("we can change element [4]: ", immutable_var, "because its type is: ", type(immutable_var[4]) )
print("but we can't change element[0] =", immutable_var[0], "because it's simple element of tuple")

print("\n --- List ---")
mutable_list = [1, 2.5, "title", True] + [3, 4]
print("create multi type list: ", mutable_list)
mutable_list[0] = [3, 4]
mutable_list[1] = False
mutable_list[2] = "changable"
mutable_list[3] = 2.5
mutable_list[4] = 1
mutable_list[5] = "*!*"
print("change multi type list: ", mutable_list)

input("\n press <Enter> to leave....")