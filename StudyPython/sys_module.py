"""
sys module...
"""
import pprint
import sys

print(type(sys))
pprint.pprint(dir(sys))

print(f"\nWhere is python: {sys.executable}")
print(f"\npython version: {sys.version}")
print(f"\npython version about: {sys.version_info}")
print(f"\nWhich OS : {sys.platform}")

if sys.version.split(' ')[0] == '3.11.9':
    print('version of python is correct')

print(f"\nArgs of app: {sys.argv}")
print(f"\nPath to find modules: {sys.path}")
print(f"\nDictionary of used modules: {sys.modules}")


"""
__builtins__ - keeps inner objects of python
"""
print(f"\n {__builtins__}")
pprint.pprint(dir(__builtins__))