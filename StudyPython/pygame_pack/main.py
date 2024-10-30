import pygame as pg
from player import Tank

screen = pg.display.set_mode((500, 500))
player = Tank()

fps = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    fps.tick(80) ## slow proceessing

    
    player.update(screen)
    pg.display.update()
    