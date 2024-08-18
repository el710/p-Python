from os import system

system('cls')

## files
import io
from pprint import pprint


_name = 'test.txt'
_file = open(_name, 'w')
_file.write('Hellow world\n');
_file.close

_file = open(_name, 'r') ## r - read,  w - write, a - append rb - read binary file

print('\n------------------\n', _file) ## header
print(_file.tell()) ## cursor position
pprint(_file.read()) ## read end encoding - not byte-format

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

_name = "sample.txt"
# _file = open(_name, 'w')
# _file.write('Hellow world\n');
# _file.close

print("\nOpen file to watch cursor...")
_file = open(_name, 'r') # set uncoding page
print(_file.tell())
pprint(_file.read()) ## russian symbols are uncoded
print(_file.tell()) 
_file.close()

print("\nwrite to file by cursor...")
_file = open(_name, 'a')
print(_file.tell())
_file.seek(_file.tell()) ## last position by _file.tell()
_file.write("Continue...\n")
_file.close()

print("\nOpen file with encoding we need...")
_file = open(_name, 'r', encoding='utf-8') # set coding page 'cp1251' - default
pprint(_file.read())
print(_file.tell()) 

print("\nFile properties...")
print("writable: ", _file.writable()) ## can we write to opened file
print("readable: ", _file.readable())
print("seekable: ", _file.seekable())
print("closed: ", _file.closed)
print("Name: ", _file.name)
print("buffer: ", _file.buffer)