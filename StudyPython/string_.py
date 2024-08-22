import os
os.system('cls')


print('Here is about strings & print()')

string_a = 'Hello'
string_b = "World"
string_c = '"quots"' # or "'quots'"

print(string_a, string_b, string_c)
print(string_a[0], string_a[-1])

#срез
print(string_b[0:3])  ## begin(def = 0) : last(ex def = len) : step

print(string_b[0:5:2])

print(string_b[::-1])

# methods

print("string in upper register".upper())
print("STRING in lower register".lower())
print("string in upper register".replace("upper", "lower"))

print('Hello') # ASCII
print(ord('a')) # code

_a = 'Hello'
chars = []
for i in _a:
    chars.append(ord(i))
print(chars)

s = ''
for i in chars:
    s += chr(i)
print(s)

## byte
_b = b'\x68' ## give Hex code 'h' - 0x68
print(_b, type(_b))
print(_b.decode())

print("print always ended line with '\n'")  ## '\n' - default
print("but we can change it - ", end='')

# making
print("Hello, " + string_b)
print("hello" * 4)
print('my name is %s' % 'Denis' ) ## % needs only one parameter
## so we can...
print('my name is %s i am %x' % ('Denis', 14) ) ## % takes from cortage... make from 0x14 - str 'e'
## or 
print('my name is %(name)s i am %(age)s' % {'name': 'Denis', 'age': 14}) ## % takes from dictionary

print('i am learning in {} {}'.format('Urban', 'university'))
print('position {0} {1} and {0}'.format('here', 'there'))
print('position {first} {second} and {first}'.format(first = 'here', second = 'there'))
print(f'position {"<any python code>"} ')



#input("\npress <Enter> if you dare...")

'''
import module_7_bonus.py
'''

