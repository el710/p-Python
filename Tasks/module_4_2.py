from os import system
system('cls')

print("Work with namespaces...")

def test_function():
    def inner_function(l):
        print(f"inner_function({l}): I am in test_function() namespace")
    
    inner_function("local")

    return inner_function

## inner_function() - is not defined here

d = test_function()
print(d("global"))

input("press <Enter> to leave...")
