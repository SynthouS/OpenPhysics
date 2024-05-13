import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False
import settings as st

# Pymunk settings
space = pymunk.Space()
space.gravity = 0, 8000