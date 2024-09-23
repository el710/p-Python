from os import system
system('cls')

def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        for i in range(2, res):
            if (res % i) == 0:
                print("Complicated")
                return res
        print("Simple")
        return res

    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)