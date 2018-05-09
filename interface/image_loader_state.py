import pyglet
from os import listdir

from gui_elements.image_loader.file_handler import FileHandler
from gui_elements.section_title import SectionTitle
from gui_elements.state_title import StateTitle
from interface.state import State


class ImageLoaderState(State):
    def __init__(self, name, machine):
        super().__init__(name, machine)
        self._set_layout()
        self.add_file_handlers()

        self.files = []
        self.current_file = None

        self.mouseX = machine.mouseX
        self.mouseY = machine.mouseY

    def resume(self):
        super().resume()
        pyglet.gl.glClearColor(1, 1, 1, 1)

    def update(self):
        self.mouseX = self.machine.mouseX
        self.mouseY = self.machine.mouseY

    def toggle_file(self, filename):
        self.machine.seed_file = filename
        self.machine.activate_state('image-perspective-state')

    def add_file_handlers(self):
        current_y = 220
        for file in listdir('dataset'):
            self.add_drawable(
                FileHandler(file, self, 40, self.height - current_y)
            )

            current_y += 50

    def _set_layout(self):
        self.add_drawable(StateTitle('Load Dataset', self))

        self.add_drawable(
            SectionTitle('Select Seed File', self,
                         self.width / 4, self.height - 120)
        )

        self.add_drawable(
            SectionTitle('File Preview', self,
                         self.width / 4 * 3, self.height - 120)
        )

        self.add_drawable(
            pyglet.text.Label(
                'Files in ./dataset directory...', font_name='Roboto',
                anchor_y='center',
                x=40, y=self.height - 170,
                color=(64, 64, 64, 255)
            )
        )
