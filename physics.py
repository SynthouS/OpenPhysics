import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False
import settings as st

# настройки Pymunk
space = pymunk.Space()
space.gravity = 0, 8000

# платформа
segment_shape = pymunk.Segment(space.static_body, (2, st.HEIGHT), (st.WIDTH, st.HEIGHT), 26)
space.add(segment_shape)
segment_shape.elasticity = 0.8
segment_shape.friction = 1.0