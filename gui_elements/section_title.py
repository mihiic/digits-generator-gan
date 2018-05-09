import pyglet
from gui_elements.drawable import Drawable


class SectionTitle(Drawable):
    def __init__(self, title, state, x, y):
        self.label = pyglet.text.Label(
            title,
            font_name='Roboto',
            font_size=24,
            anchor_x='center',
            anchor_y='center',
            width=state.width / 4,
            x=x,
            y=y,
            color=(100, 100, 100, 255)
        )

    def draw(self):
        self.label.draw()

    def change_title(self, new_title):
        self.label.text = new_title
