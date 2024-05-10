#импорт модулей:
import pygame as pg
from random import randrange
import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False

import settings as st
import objects as obj
from physics import space

pg.init()
surface = pg.display.set_mode(st.RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

# текст
def draw_text(surface, text, position, font_size=30, alpha=255, center=False):
    font = pg.font.Font(None, font_size)
    text_surface = font.render(text, True, pg.Color('white'))
    text_surface.set_alpha(alpha)  # Установка прозрачности текста
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (st.WIDTH // 2, position[1])
    else:
        text_rect.topleft = position
    surface.blit(text_surface, text_rect)

# Отрисовка
while True:
    surface.fill(pg.Color('black'))

    # Проверка и удаление объектов, которые упали ниже платформы
    for shape in list(space.shapes):
        if shape.body.position.y > st.HEIGHT + 100:  # Высота, ниже которой объекты будут удаляться
            space.remove(shape, shape.body)

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        # спавн кубиков и кругов
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                obj.create_square(space, i.pos)
            elif i.button == 3:  # Правая кнопка мыши для создания круга
                obj.create_circle(space, i.pos)
        # удаление всех объектов при нажатии на кнопку 'C'
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_c:
                # Удаление всех объектов, кроме платформы
                for shape in list(space.shapes):
                    if not hasattr(shape, 'body') or shape.body.body_type != pymunk.Body.STATIC:
                        space.remove(shape, shape.body)
            if i.key == pg.K_ESCAPE:
                pg.quit()
                exit()

    draw_text(surface, f'Objects: {len(space.shapes) - 1}', (10, 10))
    draw_text(surface, f'FPS: {clock.get_fps():.2f}', (10, 30))
    draw_text(surface, 'by gooseURL - v2.0', (640, 10), font_size=50, alpha=128)

    space.step(1 / st.FPS)
    space.debug_draw(draw_options)

    pg.display.flip()
    clock.tick(st.FPS)

print('end')