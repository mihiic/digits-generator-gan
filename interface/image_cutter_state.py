import pyglet
import numpy as np
import cv2 as cv
import os

from gui_elements.section_title import SectionTitle
from gui_elements.state_title import StateTitle
from interface.state import State


class ImageCutterState(State):
    def __init__(self, name, machine):
        super().__init__(name, machine)

        self.add_drawable(StateTitle('Cutting Images', self))

        self.action = SectionTitle(
            'Cutting Images...', self, self.width / 4, self.height - 120
        )
        self.add_drawable(self.action)

    def resume(self):
        original_image = cv.imread('workdata/seedfile.png')

        for i in range(0, 10):
            for j in range(0, 13):
                self.cut_image(original_image, i, j)

        self.action.change_title('Continue')

    def cut_image(self, original, i, j):
        start_x = i * 32 + 2
        start_y = j * 32 + 2
        end_x = (i + 1) * 32 - 2
        end_y = (j + 1) * 32 - 2

        cut_img = original[start_y:end_y, start_x:end_x]

        filename = "workdata/neural/{}_{}.png".format(i+1, j+1)
        cv.imwrite(filename, cut_img)
        self.action.change_title('Cutting {}%...'.format((i * 10 + j) / 130.0))

        sprite_image = pyglet.image.load(filename)
        sprite_image.anchor_y = 24
        sprite_image.anchor_x = 24
        sprite = pyglet.sprite.Sprite(sprite_image)
        sprite.scale = 1.5
        sprite.x = 150 + j * 80
        sprite.y = self.height - 150 - i * 50

        self.add_drawable(sprite)

