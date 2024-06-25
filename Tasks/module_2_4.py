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

for item in numbers[1: list_size]:
    is_prime = True
    
    for dev in range(2, item):
        # if dev > 1 and item % dev == 0:
        if item % dev == 0:   
           is_prime = False
           break
        
    if is_prime:
        primes.append(item)
    else:
        not_primes.append(item)

print("Here are prime numbers: ", primes)
print("and not prime numbers: ", not_primes)

input("\npress <Enter> to leave...")