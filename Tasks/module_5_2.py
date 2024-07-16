from os import system
from time import sleep

system('cls')
print("Work with classes...\n")

class House():
    def __init__(self, name='building', floors=1) -> None:
        self.name = name
        self.floors = floors

    def __len__(self):
        return self.floors
    
    def __str__(self) -> str:
        return f"Name: {self.name}, floors: {len(self)}"
    
    def go_to(self, floor):
        print(f"\nWellcome to {self.name}")
        if floor < 1:   ##or floor > self.floors:
            print('There is no such floor')
        else:
            for i in range(1, len(self) + 1):
                if i == floor:
                    print(f"You have got the floor number '{floor}'")
                else:
                    print(f"{i} floor...")
                    sleep(1)

            if floor > len(self):
                print("You are on the roof :)")
            

house_name = input("Let's build a house. What is the name: ")

stages = int(input("How much floors should be: "))
one_house = House(house_name, stages)

print(f"it'll has {len(one_house)} floors")
print(one_house)


go_floor = int(input(f"\nWhich floor do you need [1..{stages}]: "))

one_house.go_to(go_floor)

input("\npress <Enter> to leave...")