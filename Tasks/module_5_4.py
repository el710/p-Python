from os import system
from time import sleep

system('cls')
print("Work with classes...\n")

class House():

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, floors) -> None:
        self.name = name
        self.floors = floors

    def __len__(self):
        return self.floors
    
    def __str__(self) -> str:
        return f"{self.name} {len(self)}[f]"
    
    ## overloaded
    def __eq__(self, value: object) -> bool: ## '=='
        if isinstance(value, House):
            return len(self) == len(value)
        return False
    
    def __lt__(self, other: object) -> bool: ## '<'
        return len(self) < len(other)
    
    def __le__(self, other: object) -> bool: ## '<='
        return  len(self) < len(other) or len(self) == len(other)
    
    def __gt__(self, other: object) -> bool: ## '>'
        return len(self) > len(other)
    
    def __ge__(self, other: object) -> bool: ## '<'
        return len(self) > len(other) or len(self) == len(other)
    
    def __ne__(self, value: object) -> bool: ## '!='
        return len(self) != len(value)
    
    def __add__(self, value) -> object: ## '+ value'
        print('add:', value)
        if isinstance(value, int):
            self.floors += value
        return self
    
    def __radd__(self, value) -> object: ## 'value +'
        print('radd:')
        return self + value

    def __iadd__(self, value) -> object: ## '+='
        print('iadd:')
        return self.__add__(value)
    
    def __del__(self) -> None:
        print(f"{self.name} has demolished")
        print(f"But it'll stay in history: {self.houses_history}")
        

    ## addition
    def go_to(self, floor):
        print(f"\nWellcome to {self.name}")
        if floor < 1:   ##or floor > self.floors:
            print('There is no such floor')
        else:
            for i in range(1, len(self) + 1):
                if i == floor:
                    print(f"You have got the floor number '{floor}'")
                    sleep(2)
                else:
                    print(f"{i} floor...")
                    sleep(1)

            if floor > len(self):
                print("You are on the roof :)")
            
example = House('Prototype', 15)
print(House.houses_history)

house_name = input("Let's build a house. What is the name: ")
stages = int(input("How much floors should be: "))
one_house = House(house_name, stages)
print(House.houses_history)

two_house = House("Lulubyes", 7)
print("Just buid one more", House.houses_history)

print(example, f"has {len(example)} floors")
print(one_house, f"has {len(one_house)} floors")

print(f"\n{one_house} == {example}:", one_house == example)
one_house = one_house + 2
print(f"{one_house} > {example}:", one_house > example)
one_house = 2 + one_house
print(f"{one_house} >= {example}:", one_house >= example)
one_house += 2
print(f"\n{one_house} < {example}:", one_house < example)
print(f"{one_house} <= {example}:", one_house <= example)
print(f"{one_house} != {example}", one_house != example)



go_floor = int(input(f"\nWhich floor in '{one_house}' do you need [1..{len(one_house)}]: "))

one_house.go_to(go_floor)

del one_house
del two_house

input("\npress <Enter> to leave...")