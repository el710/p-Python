"""
home work for class inheritance 
"""
from os import system
from random import randint
from time import sleep


class Animal():
    def __init__(self, name) -> None:
        self.alive = True
        self.fed = False
        self.name = name
    
    def __str__(self) -> str:
        return f"animal {self.name}"
    
    def eat(self, food):
        if food.edible:
            print(f"{self.name} has eaten {food.name}")
            self.fed = True
        else:
            print(f"{self.name} hasn't eat {food.name}")
            self.alive = False

    def state(self):
        if self.alive:
            return f"{self.name} is alive"
        else:
            return f"{self.name} is dead"
    

class Plant():
    def __init__(self, name) -> None:
        self.edible = False
        self.name = name

class Mammal(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
class Predator(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

class Flower(Plant):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.edible = False

class Fruit(Plant):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.edible = True


if __name__ == '__main__':
    system('cls')

    a1 = Predator('Bear')
    a2 = Mammal('Hatiko')
    p1 = Flower('Romashko')
    p2 = Fruit('Orange')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)

    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)
