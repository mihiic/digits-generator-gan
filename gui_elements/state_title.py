import pyglet

from gui_elements.drawable import Drawable


class StateTitle(Drawable):
    def __init__(self, title, state):
        self.label = pyglet.text.Label(
            title,
            font_name='Roboto',
            font_size=36,
            anchor_x='left',
            anchor_y='center',
            x=40,
            y=state.height - 40,
            color=(0, 0, 0, 255)
        )

    def draw(self):
        self.label.draw()
