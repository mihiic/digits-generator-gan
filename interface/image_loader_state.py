import pyglet
from future.moves.tkinter import filedialog

from gui_elements.state_title import StateTitle
from interface.state import State


class ImageLoaderState(State):
    def __init__(self, name, machine):
        super().__init__(name, machine)
        self.add_drawable(StateTitle('Load Dataset', self))

        self.files = []

    def resume(self):
        super().resume()
        pyglet.gl.glClearColor(0.9, 0.9, 0.9, 1)

    def update(self):
        pass
