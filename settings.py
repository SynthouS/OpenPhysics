import pygame as pg
import pymunk
import random

pause = False

# phrases for name of game
phrases = [
    'I know the figure you want to build',
    'try build a house',
    'Squares, circles and triangles',
    'Gravity()=0',
    'oh no, where my fps!',
    'lets make a pyramide'
]

clock = pg.time.Clock()
base_title = 'OpenPhysics2D'

# параметры PyGame
RES = WIDTH, HEIGHT = 1280, 600
FPS = 120
pg.display.set_caption(f'{base_title} - {random.choice(phrases)}')
icon = pg.image.load('assets/img/icon.png')
pg.display.set_icon(icon)

surface = pg.display.set_mode(RES)
draw_options = pymunk.pygame_util.DrawOptions(surface)