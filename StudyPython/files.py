from os import system
import os

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


###########
## using 'with'
## analog 'try - finally'
# with <exprassion> as <target object>
#     <action>

with open('test.txt', encoding='utf-8') as file: 
    for line in file:
        for char in line:
            print(char, end='')
## here 'with' automatically closes the file

print(f"current directory: {os.getcwd()}")

if not os.path.exists('second'):
    os.mkdir('second')
os.chdir('second') ## go to in to

print(f"current directory: {os.getcwd()}")

## make nested directory
os.makedirs(r'third\fourth') ## r - show that '\' not spec symbol
## or os.makedirs('third\\fourth') 

for i in os.walk('.'): ## walk through directory's tree
    print(i)

os.removedirs(r'third\fourth') ## delete all chain
os.chdir('..') ## go out
print(f"current directory: {os.getcwd()}")
os.removedirs('second') ## can't delete unempty dirs

## generate lists fo dirs & files
print(os.listdir()) ## like <ls> - item's list in current directory
files = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]

print(files)
print(dirs)

print(os.startfile(files[2])) ## open file in system app
print(os.stat(files[2])) ## get file properties
print(os.stat(files[2]).st_size) 

'''
import module_7_1.py, module_7_2.py module_7_3.py
'''