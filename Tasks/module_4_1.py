from homework4_1.fake_math import divide as fm_dev
from homework4_1.true_math import divide as tm_dev

print('Work with import modules....\n')

first = int(input("Input Dividend: "))
print("Try to divide by zero...")
second = int(input("Input Divisor: "))

print(f"fake math: {fm_dev(first, second)}")
print(f"true math: {tm_dev(first, second)}")

input("\npress <Enter> to leave...")

