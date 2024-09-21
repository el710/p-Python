from os import system
from typing import Any
system('cls')

first = 'Мама мыла раму'
second = 'Рамена мало было'

res = list(map(lambda x, y: x == y, first, second))
print(res)


def get_advanced_write(file_name):
    def write_everything(*data):
        with open(file_name, 'a', encoding='utf-8') as file:
            for d in data:
                print(d)
                file.write(f'{d}\n')

    return write_everything

write = get_advanced_write('example.txt')
write('This is string', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice
class MysticBall():
    def __init__(self, *args) -> None:
        self.words = args
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return choice(self.words)
        

first_ball = MysticBall('Yes', 'No', 'Maybe')
print(first_ball())
print(first_ball())
print(first_ball()) 
print(first_ball()) 

    
