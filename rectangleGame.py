import pygame as pg
from random import *

pg.init()
window = pg.display.set_mode((600,300))
pg.display.set_caption("Run rectangle,run!")
run = True

x = 50
y = 50
width = 40
height = 60
speed = 6

while run:
    pg.draw.rect(window, (2, 156, 9), (45,345 ,14, 14))
    pg.time.delay(100)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            x-=speed
        if keys[pg.K_RIGHT]:
            x+=speed
        if keys[pg.K_UP]:
            y-=speed
        if keys[pg.K_DOWN]:
            y+=speed
        window.fill((0, 0, 0))


    pg.draw.rect(window, (9, 34, 100), (x, y, width, height))
    pg.display.update()
pg.quit()