import os
os.system("cls")

print("Example about sort Prime & not prime numbers from list. let's go...\n")

list_size = int(input("Give me a size of the list: "))

numbers = list()
for i in range(list_size + 1):
    if i != 0:
        numbers.append(i)
print("Source list: ", numbers)

primes = []
not_primes = []

def isPrime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


for item in numbers[1: list_size]:
##    is_prime = True

    # for dev in range(2, item // 2 + 1):        ## range to (item / 2) is enough
    #     if item % dev == 0:   
    #        is_prime = False
    #        break

    if isPrime(item):
        primes.append(item)
    else:
        not_primes.append(item)

    # if is_prime:
    #     primes.append(item)
    # else:
    #     not_primes.append(item)

print("Here are prime numbers: ", primes)
print("and not prime numbers: ", not_primes)

input("\npress <Enter> to leave...")

'''
точно не делится на 
3:                2  > 3//2
4:                3  > 4//2
5:             4, 3  > 5//2
6:             5, 4  > 6//2
7:          6, 5, 4  > 7//2 
8:          7, 6, 5  > 8//2
e.t.c



'''