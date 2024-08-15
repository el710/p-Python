## pip install arcade
## works with pyton v3.11.9


import arcade
import os

import arcade.key

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'PingPong'


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('D:\EL710\p-Python\StudyPython\ArcadeGame\Bar.png', 0.5)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        elif self.left <= 0:
            self.change_x = 0
        

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('D:\EL710\p-Python\StudyPython\ArcadeGame\Ball.png', 0.5)
        self.change_x = 7
        self.change_y = 7
    
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH or self.left <= 0:
            self.change_x = - self.change_x
        if self.top >= SCREEN_HEIGHT or self.bottom <= 0:
            self.change_y = - self.change_y
        

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()
   
    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def update(self, delta_time: float):
        if arcade.check_for_collision(self.ball, self.bar):
            self.ball.change_y = - self.ball.change_y

        self.ball.update()
        self.bar.update()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT or symbol == arcade.key.LEFT:
            self.bar.change_x = 0

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.bar.change_x = 6
        if symbol == arcade.key.LEFT:
            self.bar.change_x = -6


    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()


if __name__ == "__main__":

    os.system('cls')
    
    #dir_path = os.path.dirname(os.path.realpath(__file__))
    #print(dir_path)

    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) 
    arcade.run()