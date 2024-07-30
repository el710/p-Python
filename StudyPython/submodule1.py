



def hello_mod(x):
    print(f"{__name__}: {x}")

var_a = 5

# property of sign '_' in forvard of names
_not_available_var_in_other_modules = 666
def _not_available_func_in_other_modules():
    print(f"you can use me only in this file - {_not_available_var_in_other_modules}")
class _unavailable_class_in_other_modules():
    pass


if __name__ == '__main__':
    print("sub module runned as itself ...")
    _not_available_func_in_other_modules()
