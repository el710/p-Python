from os import system
from time import sleep

system('cls')
print("Work with classes...\n")

class House():
    def __init__(self, name='building', floors=1) -> None:
        self.name = name
        self.floors = floors
    
    def go_to(self, floor):
        print(f"\nWellcome to {self.name}")
        if floor < 1:   ##or floor > self.floors:
            print('There is no such floor')
        else:
            for i in range(1, self.floors + 1):
                if i == floor:
                    print(f"You have got the floor number '{floor}'")
                else:
                    print(f"{i} floor...")
                    sleep(1)

            if floor > self.floors:
                print("You are on the roof :)")
            

stages = int(input("Let's build a house. what floors number: "))

one_house = House('Elbrus', stages)

go_floor = int(input(f"Which floor do you need [1..{stages}]: "))

one_house.go_to(go_floor)

input("\npress <Enter> to leave...")