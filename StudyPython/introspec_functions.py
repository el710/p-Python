"""
introspection...
ability of object to give information about itself

- help()
- __name__
- __doc__
- dir()
- type()
- hasattr()
- getattr()
- setattr()
- callable()
- isinstance()

e.t.c
"""

import pprint
import requests

"""
get description of request...
"""
# help(requests)

def some_function():
    """
        just print function
    """
    print('hello')

print(some_function.__name__)
print(some_function.__doc__)

some_variable = 34
print(type(some_variable), type(some_variable) is float)
print(type(some_function))
print(type(requests))

"""
get consistance...
"""
print(dir(some_variable),'\n')

class SomeClass():
    atttr = 5

    def __init__(self) -> None:
        self.attr_1 = 33

    def class_method(self,value):
        self.attr_1 = value

print(dir(SomeClass),'\n')

## get inner classes, methods, attributes...
pprint.pprint(dir(requests))

print("\nare there some attribute...\n")
some_object = SomeClass()
print(hasattr(some_object, 'atttr'))
print(hasattr(some_object, 'atttttr'))

print(help(getattr))
print(f" get: {getattr(some_object, 'attr_1')} ")
print(f" get: {getattr(some_object, 'attttr', 'there is no such one')} ")

try:
    getattr(some_object, 'shmatr')
except Exception as exc: 
    print(f'error - {exc}\n')


for attr_name in dir(requests):
    attr = getattr(requests, attr_name, )
    print(f"Attr: {attr_name} - {type(attr)} ")
    

print(f"\n check callable() \n")
print(callable(some_variable))
print(callable(some_function))
print(callable(some_object.attr_1))
print(callable(some_object.class_method))

print(f"\n check isinstance() \n")
print(isinstance(some_variable, int))
print(isinstance(some_variable, str))
print(isinstance(some_object, SomeClass))

import inspect
print(f"\n check inspect \n")
print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))
print(inspect.isbuiltin(requests))


some_module = inspect.getmodule(some_function)
print(type(some_module), some_module)