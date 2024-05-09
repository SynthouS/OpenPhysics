#импорт модулей:
import pygame as pg
from random import randrange
import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False

# параметры PyGame
RES = WIDTH, HEIGHT = 800, 600
FPS = 60
pg.display.set_caption('OpenPhysics2D')
icon = pg.image.load('img/icon.png')
pg.display.set_icon(icon)

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

# настройки Pymunk
space = pymunk.Space()
space.gravity = 0, 8000

# платформа
segment_shape = pymunk.Segment(space.static_body, (2, HEIGHT), (WIDTH, HEIGHT), 26)
space.add(segment_shape)
segment_shape.elasticity = 0.8
segment_shape.friction = 1.0



# квадратики
body = pymunk.Body()
def create_square(space, pos):
    square_mass, square_size = 1, (60, 60)
    square_moment = pymunk.moment_for_box(square_mass, square_size)
    square_body = pymunk.Body(square_mass, square_moment)
    square_body.position = pos
    square_shape = pymunk.Poly.create_box(square_body, square_size)
    square_shape.elasticity = 0.4
    square_shape.friction = 1.0
    square_shape.color = [randrange(256) for i in range(4)]
    space.add(square_body, square_shape)

# круги
def create_circle(space, pos):
    circle_mass, circle_radius = 1, 30
    circle_moment = pymunk.moment_for_circle(circle_mass, 0, circle_radius)
    circle_body = pymunk.Body(circle_mass, circle_moment)
    circle_body.position = pos
    circle_shape = pymunk.Circle(circle_body, circle_radius)
    circle_shape.elasticity = 0.5
    circle_shape.friction = 1.0
    circle_shape.color = [randrange(256) for i in range(4)]
    space.add(circle_body, circle_shape)


# текст
def draw_text(surface, text, position, font_size=30):
    font = pg.font.Font(None, font_size)
    text_surface = font.render(text, True, pg.Color('white'))
    surface.blit(text_surface, position)

# Отрисовка
while True:
    surface.fill(pg.Color('black'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        # спавн кубиков и кругов
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                create_square(space, i.pos)
            elif i.button == 3:  # Правая кнопка мыши для создания круга
                create_circle(space, i.pos)
            print(i.pos)
    draw_text(surface, f'Objects: {len(space.shapes) - 1}', (10, 10))
    draw_text(surface, f'FPS: {clock.get_fps():.2f}', (10, 30))

    space.step(1 / FPS)
    space.debug_draw(draw_options)

    pg.display.flip()
    clock.tick(FPS)

print('end')