"""
home work for class inheritance 
"""
from os import system
from random import randint
from time import sleep


class Bio():
    def __init__(self, name) -> None:
        self.name = name
    
    def __repr__(self) -> str:
        return f"class <Bio> name: '{self.name}'"

class Animal(Bio):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.alive = True
        self.fed = False
    
    def __str__(self) -> str:
        return f"animal {self.name}"
    
    def eat(self, food):
        if isinstance(food, Fruit):
            print(f"{self.name} has eaten {food.name}")
            self.fed = True
        elif isinstance(food, Flower):
            if isinstance(self, Herbivore) and food.edible:
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
    

class Plant(Bio):
    edible = False
    def __init__(self, name) -> None:
        super().__init__(name)

class Herbivore(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
class Preditor(Animal):
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

    # bio_object = Bio('anylive')
    # print(bio_object.__repr__())

    # animal = Animal('anime')
    # print(animal)

    cow = Herbivore('Cow')
    bear = Preditor('Bear')
    flora = [Flower('Hydrangea'), Fruit('Apple'), Flower('Atropa'), Fruit('Ananas')]


    print(f'''{cow} and {bear}
          have field of destiny:''')
    for i in flora:
        print(i)

    print("Let's go...\n")
    challenger = cow
    while cow.alive and bear.alive and len(flora) > 0:
        chance = randint(0, len(flora) - 1)
        food = flora.pop(chance)

        print(f"{challenger.name} made a step and met {food}")
        challenger.eat(food)
        sleep(1)

        if isinstance(challenger, Herbivore):
            challenger = bear
        else:
            challenger = cow        
    
    print(cow.state())
    print(bear.state())
    
    input("\n press <Enter> to leave...")