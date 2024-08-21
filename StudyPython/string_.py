import os
os.system('cls')


print('Here is about strings & print()')

string_a = 'Hello'
string_b = "World"
string_c = '"quots"' # or "'quots'"

print(string_a, string_b, string_c)
print("Hello, " + string_b)
print("hello" * 4)
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

input("press <Enter> if you dare...")

