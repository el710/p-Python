
class Vehicle():

    __COLOR_VARIANTS = ['White', 'Black', 'Blue', 'Red']

    def __init__(self, owner, model, engine, color) -> None:
        self.owner = owner
        self.__model = model
        self.__engine_power = engine
        self.__color = color
    
    def get_model(self):
        return f"Model: {self.__model}"
    
    def get_horsepower(self):
        return f"Power: {self.__engine_power}"
    
    def get_color(self):
        return f"Color: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Owner: {self.owner}")

    def set_color(self, new_color):
        for i in self.__COLOR_VARIANTS:
            if new_color.upper() == i.upper():
                self.__color = new_color
        if self.__color != new_color:
            print(f"Can't change color for {new_color}")



class Sedan(Vehicle):
    __PASSANGER_LIMIT = 5


from os import system
system('cls')

print("Work with special class's attributes...\n")

sedan = Sedan('Mickle', 'VolksWagen', 300, 'White')
sedan.print_info()

sedan.set_color('Green')
sedan.set_color('red')
sedan.owner = "Ingis"
sedan.print_info()

input("\n press <Enter> to leave...")