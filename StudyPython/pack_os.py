import os
import sys

os.system("cls")

print(os.getcwd())

file_path = sys.argv[0]

print(os.path.dirname(file_path))

dir, file_name = os.path.split(file_path)
print(dir, file_name)

name = os.path.splitext(file_name)[0]
print(name)