import pymunk
from random import randrange
from physics import space
import settings as st

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

# Triangle
def create_triangle(space, pos):
    triangle_mass = 1
    triangle_vertices = [(0, -30), (-30, 30), (30, 30)]  # вершины треугольника
    triangle_moment = pymunk.moment_for_poly(triangle_mass, triangle_vertices)
    triangle_body = pymunk.Body(triangle_mass, triangle_moment)
    triangle_body.position = pos
    triangle_shape = pymunk.Poly(triangle_body, triangle_vertices)
    triangle_shape.elasticity = 0.6
    triangle_shape.friction = 1.0
    triangle_shape.color = [randrange(256) for i in range(4)]
    space.add(triangle_body, triangle_shape)

# platform
segment_shape = pymunk.Segment(space.static_body, (2, st.HEIGHT), (st.WIDTH, st.HEIGHT), 26)
space.add(segment_shape)
segment_shape.elasticity = 0.8
segment_shape.friction = 1.0