import settings as st
import pygame as pg
from physics import space
from settings import surface, clock, pause

_FONT_CACHE = {}
pg.mixer.init()
pg.font.init()

def draw_text(surface, text, position, font_size=30, alpha=255, center=False, color=(255, 255, 255)):
    font = _FONT_CACHE.get(font_size)
    if font is None:
        font = pg.font.Font('assets/font/Roboto-Bold.ttf', font_size)
        _FONT_CACHE[font_size] = font

    text_surface = font.render(text, True, color)
    text_surface.set_alpha(alpha)
    rect = text_surface.get_rect()
    if center:
        rect.center = position
    else:
        rect.topleft = position
    surface.blit(text_surface, rect)
    return text_surface  # Return the text_surface

def text_render():
    draw_text(surface, f'Objects: {len(space.shapes) - 1}', (10, 40), font_size=25)
    draw_text(surface, 'Version: 4.0', (10, 70), font_size=25,)
    draw_text(surface, 'N/Tech', (500, 10), font_size=40, alpha=50)
    draw_text(surface, f'FPS: {clock.get_fps():.2f}', (10, 10), font_size=25)

notifications = []

notification_sound = pg.mixer.Sound('assets/sounds/notf.mp3')

def spawn_notification(pos):
    notification_text = f'spawn: ({pos[0]}, {pos[1]})'
    notifications.append((notification_text, pg.time.get_ticks()))
    notification_sound.play()

def gravity_notification():
    notification_text = f'Low gravity: {pause}'
    notifications.append((notification_text, pg.time.get_ticks()))
    notification_sound.play()

def draw_notifications():
    notification_rect_height = 30
    for i, (notification_text, timestamp) in enumerate(notifications):
        notification_rect = pg.Rect(st.WIDTH - 210, st.HEIGHT - 60 - i * notification_rect_height, 200, notification_rect_height, alpha=204)
        pg.draw.rect(surface, pg.Color('#000000'), notification_rect)
        pg.draw.rect(surface, pg.Color('#000000'), notification_rect, 1)
        text_surface = draw_text(surface, notification_text, (notification_rect.x + 5, notification_rect.y + 5), font_size=20, color=pg.Color('#FFFFFF'))
        if pg.time.get_ticks() - timestamp > 3000:  # 3 seconds
            notifications.remove((notification_text, timestamp))

def main_loop():
    while True:
        object_position = (10, 20)  # define the position of the object
        spawn_notification(object_position)  # pass the position to the function
        gravity_notification()
        surface.fill((0, 0, 0))  # clear the screen
        text_render()  # render the text
        draw_notifications()  # render the notifications
        pg.display.flip()  # update the display
        clock.tick(60)  # limit the frame rate
