import os

os.system("cls")
print("Home work with argument's parcing...")

def print_params(a=1, b='string', c=True):
    print(f"print_param: a = {a}, b = {b}, c = {c}")
    return None


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 'a', False]
values_dict = {'a': True, 'b': 3.5, 'c': 'life'}

print_params(*values_list)
print_params(**values_dict)

values_tuple = ('True is', True)
print_params(*values_tuple, 42)

def func_(m_list = [], m_pointer = None): ## call this fucntion will make immortal!!! m_list[]
    if m_pointer == None:
        m_pointer = (1) ## make local tuple

    print(f" func_: {type(m_list)} {id(m_list)} ") 

    return m_list

new_list = func_()
print(f" new_list: {type(new_list)} {id(new_list)} ")
func_()

input("\nPress <Enter> to leave...")