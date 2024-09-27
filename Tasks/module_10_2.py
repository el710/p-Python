from threading import Thread
from time import sleep

ENEMY_GROUP = 100
class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = ENEMY_GROUP

    def run(self):
        battle_days = 0
        print(f"{self.name}: We have been atacked")
        while self.enemy > 0:
            battle_days += 1
            sleep(1)
            self.enemy -= self.power
            if self.enemy > 0:
                print(f'{self.name} fight {battle_days} days..., {self.enemy} enemies are left')
        print(f'Knight {self.name} win after {battle_days} days!')
        

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('\n The battles are over')


        