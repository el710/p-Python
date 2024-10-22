"""
module for testing in testing.py
"""
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


#test helps to notice if somebody edited file:
# def add(a, b):
#     return a ** b

## ...later somebody add new functionality...
def sqrt(a):
    return a ** 0.5

def pow(a, b):
    return a**b
## ... and made new test file - test_new.py

if __name__ == '__main__':
    print(add(5, 8))
    print(sub(5, 8))
    print(mul(5, 8))
    print(div(5, 8))
