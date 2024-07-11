from homework4_1.fake_math import divide as fm_div
from homework4_1.true_math import divide as tm_div

print('Work with import modules....\n')

first = int(input("Input Dividend: "))
print("Try to divide by zero...")
second = int(input("Input Divisor: "))

print(f"fake math: {fm_div(first, second)}")
print(f"true math: {tm_div(first, second)}")

input("\npress <Enter> to leave...")

