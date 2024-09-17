from os import system
system('cls')


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
       
class IncorrectCarNumber(Exception):
    def __init__(self, message):
        self.message = message

class Car():
    def __init__(self, model, vin, number):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin

        if self.__is_valid_number(number):
            self.__number = number
    
    def __is_valid_vin(self, vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber("Incorrect type of vin number")
        elif vin not in range(1000000, 100000000):
            raise IncorrectVinNumber("Incorrect range of vin number")
        return True

    def __is_valid_number(self, number):
        if not isinstance(number, str):
            raise IncorrectCarNumber("Wrong type of number")
        elif len(number) != 6:
            raise IncorrectCarNumber("Wrong length of number")
        return True

try:
    first = Car('Model_1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f'{first.model} was create') 

try:
    second = Car('Model_2', 300, 't001tp')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f'{second.model} was create') 

try:
    third = Car('Model_3', 2020202, 'no number')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f'{third.model} was create') 



