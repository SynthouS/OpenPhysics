import settings as st
import pygame as pg
from physics import space
from settings import surface, clock

def draw_text(surface, text, position, font_size=30, alpha=255, center=False):
    font = pg.font.Font(None, font_size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_surface.set_alpha(alpha)
    surface.blit(text_surface, position)

def text_render():
    draw_text(surface, f'Objects: {len(space.shapes) - 1}', (10, 30), font_size=30),
    draw_text(surface, 'by gooseURL - v3.0', (500, 10), font_size=40, alpha=128),
    draw_text(surface, f'FPS: {clock.get_fps():.2f}', (10, 10), font_size=30,),