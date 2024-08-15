from os import system

system('cls')

## files
from pprint import pprint

_name = 'test.py'
_file = open(_name, 'r') ## r - read,  w - write, a - append rb - read binary file

print('\n------------------\n', _file) ## header
print(_file.tell()) ## cursor position
pprint(_file.read())

print('\n------------------\n')
_file.seek(400)
pprint(_file.read())


_file.close()

_name = 'sample.txt'
_file = open(_name, 'w')
_file.write("sample file\n")
_file.close()

_name = 'sample.txt'
_file = open(_name, 'a')
_file.write("double sample file")
_file.close()