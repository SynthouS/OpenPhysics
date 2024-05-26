import pygame as pg
from random import randrange
import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False

from settings import *
import objects as obj
from physics import space
import draw

dragged_obj = None

# Set up loading screen
loading_image = pg.image.load('assets/img/loading.png')
loading_image = pg.transform.scale(loading_image, (600, 400))
loading_screen = pg.display.set_mode((600, 400))

# Show loading screen
loading_screen.blit(loading_image, (0, 0))
pg.display.flip()
pg.time.wait(1000)  # Wait for 1 second

# Draw
while True:
    # Handle window resizing
    if WIDTH != loading_screen.get_width() or HEIGHT != loading_screen.get_height():
        loading_screen = pg.display.set_mode((WIDTH, HEIGHT))
        loading_screen.blit(loading_image, (0, 0))
        pg.display.flip()
        pg.time.wait(1000)  # Wait for 1 second

    # Draw grid background
    surface.fill(pg.Color('#131313'))  # background color
    for x in range(0, WIDTH, 55):  # grid size is 55x55
        pg.draw.line(surface, pg.Color('#393939'), (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, 55):
        pg.draw.line(surface, pg.Color('#393939'), (0, y), (WIDTH, y), 1)

    # check and delete objects under platfrom
    for shape in list(space.shapes):
        if shape.body.position.y > HEIGHT + 100:
            space.remove(shape, shape.body)

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        # drag&drop
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:  # Left mouse button
                for shape in space.shapes:
                    if not hasattr(shape, 'body') or shape.body.body_type != pymunk.Body.STATIC:
                        point = i.pos
                        query = space.point_query_nearest(point, 0, pymunk.ShapeFilter())
                        if query.shape == shape:
                            dragged_obj = shape
                            break

        if i.type == pg.MOUSEMOTION:
            if dragged_obj:
                dragged_obj.body.position = i.pos

        if i.type == pg.MOUSEBUTTONUP:
            if i.button == 1:  # Left mouse button
                dragged_obj = None
                
        # spawn object's
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_1:
                pos = pg.mouse.get_pos()
                obj.create_square(space, pos)
                draw.spawn_notification(pos)
            elif i.key == pg.K_2:
                pos = pg.mouse.get_pos()
                obj.create_circle(space, pos)
                draw.spawn_notification(pos)
            elif i.key == pg.K_3:
                pos = pg.mouse.get_pos()
                obj.create_triangle(space, pos)
                draw.spawn_notification(pos)
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
                    draw.gravity_notification()
            # High gravity
            if i.key == pg.K_h:
                if pause == True:
                    pause = False
                    space.gravity = 0, 8000
                    draw.gravity_notification()

    draw.text_render()
    draw.draw_text(surface, f'Low gravity: {pause}', (10, 100), font_size=25),
    draw.draw_notifications()

    space.step(0.5 / FPS)
    space.debug_draw(draw_options)

    pg.display.flip()
    clock.tick(FPS)

print('end')