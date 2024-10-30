import pygame as pg
from pygame.sprite import Sprite
import logging


loger_move = logging.getLogger("MovingLog")

logging.basicConfig(level=logging.INFO, 
                    handlers=[logging.FileHandler(filename="move.log", mode='w', encoding="utf-8")]
)



class Tank(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill('green')
        ## or self.image = pg.image.load('tank.png')
        ## or +scale: self.image = pg.transform.scale(pg.image.load('tank.png'), (30, 30))
        self.rect = self.image.get_rect()

    def move(self):
        keys = pg.key.get_pressed() ## list of keys state

        if keys[pg.K_s]:
            self.rect.y += 1
        if keys[pg.K_w]:
            self.rect.y -= 1
        if keys[pg.K_d]:
            self.rect.x += 1
        if keys[pg.K_a]:
            self.rect.x -= 1

    def moving_logger(self):
        keys = pg.key.get_pressed() ## list of keys state
        if any([keys[pg.K_s], keys[pg.K_w], keys[pg.K_d], keys[pg.K_a]]):
            loger_move.info(f" got move: {self.rect.x}:{self.rect.y}")

    def update(self, screen):
        self.move()
        self.moving_logger()
        screen.blit(self.image, self.rect)
        pg.draw.rect(screen, 'blue', self.rect, width=5) ## color new rect(over self.rect) with size self.rect
        
