import os
os.system('cls')

print(dir())
## runned file named as default __main__
## included file named by its filename


print("Main module:....")

# import submodule1
# submodule1.hello_mod(submodule1.var_a)

# import submodule1 as sm1  ## use as mnemonic
# sm1.hello_mod(sm1.var_a)

# from submodule1 import hello_mod as hm  ## use as mnemonic
# hm(9)


from submodule1 import * ## import as include global names
hello_mod(var_a)

print(dir())

## but we can't use 
# _not_available_var_in_other_modules &
# _not_available_func_in_other_modules()

## to make package from directory
## we need make file __init__.py in this directory
## and when we import this package
import py_packet ## here will executed file __init__


