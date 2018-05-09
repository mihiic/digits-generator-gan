import pyglet
from gui_elements.drawable import Drawable


class FileHandler(Drawable):
    def __init__(self, filename, state, x, y):
        self.state = state
        self.location = 'dataset/{}'.format(filename)
        self.label = pyglet.text.Label(
            filename,
            font_name='Roboto',
            font_size=20,
            anchor_x='left',
            anchor_y='center',
            x=x+40,
            y=y,
            color=(100, 100, 100, 255)
        )
        self.sprite = None
        self.load_sprite()
        self.hovered = False

    def draw(self):
        self.update()
        self.label.draw()

        if self.hovered:
            self.sprite.draw()
        self.hovered = False

    def update(self):
        if self.state.mouseX < self.state.width / 2.0 and abs(self.state.mouseY - self.label.y) < 20:
            self.label.color = (0,0,0,255)
            self.hovered = True

            if self.state.machine.clicked:
                self.state.toggle_file(self.location)
                self.state.machine.clicked = False
        else:
            self.label.color = (100, 100, 100, 255)

    def load_sprite(self):
        sprite_image = pyglet.image.load(self.location)
        self.sprite = pyglet.sprite.Sprite(sprite_image)
        self.calculate_scale()
        self.sprite.x = self.state.width / 4 * 3 - self.sprite.width / 2
        self.sprite.y = self.state.height / 2 - self.sprite.height / 2 - 60

    def calculate_scale(self):
        max_w = self.state.width / 2 - 80
        max_h = self.state.height - 200

        scale_x = max_w / self.sprite.width
        scale_y = max_h / self.sprite.height

        self.sprite.scale = min(scale_x, scale_y)
