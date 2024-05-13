# Hello to 
# |-----------------|
# |-Open-Physics-2D-|
# |-----------------|
# source code, all make gooseURL and small help in chatgpt

import pygame as pg
from random import randrange
import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False

import settings as st
from settings import surface, clock, draw_options
import objects as obj
from physics import space
import draw

pause = False

pg.init()

# Draw
while True:
    surface.fill(pg.Color('black'))

    # check and delete objects under platfrom
    for shape in list(space.shapes):
        if shape.body.position.y > st.HEIGHT + 100:
            space.remove(shape, shape.body)

    for i in pg.event.get():
        if i.type == pg.QUIT:
                exit()
        # spawn object's
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                    obj.create_square(space, i.pos)
            elif i.button == 3:
                    obj.create_circle(space, i.pos)
            elif i.button == 2:
                    obj.create_triangle(space, i.pos)
        # deleting object use 'C'
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_c:
                # deleting objects under platform
                for shape in list(space.shapes):
                    if not hasattr(shape, 'body') or shape.body.body_type != pymunk.Body.STATIC:
                        space.remove(shape, shape.body)
            if i.key == pg.K_ESCAPE:
                pg.quit()
                exit()
            # Low Gravity
            if i.key == pg.K_g:
                if pause == False:
                    pause = True
                    space.gravity = 0, 1
            # High gravity
            if i.key == pg.K_h:
                if pause == True:
                    pause = False
                    space.gravity = 0, 8000

    draw.text_render()
    draw.draw_text(surface, f'low gravity: {pause}', (10, 50), font_size=30),

    space.step(1 / st.FPS)
    space.debug_draw(draw_options)

    pg.display.flip()
    clock.tick(st.FPS)

print('end')