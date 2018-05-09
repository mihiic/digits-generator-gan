import pyglet
from math import *


class Marker:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.circle = self.make_circle()

    def draw(self):
        pyglet.gl.glColor3f(1, 0, 0)
        pyglet.gl.glLineWidth(3)
        self.circle.draw(pyglet.gl.GL_LINE_LOOP)

    def make_circle(self):
        verts = []
        for i in range(4):
            angle = radians(float(i) / 4 * 360.0)
            x = 5 * cos(angle) + self.x
            y = 5 * sin(angle) + self.y
            verts += [x, y]

        return pyglet.graphics.vertex_list(4, ('v2f', verts))