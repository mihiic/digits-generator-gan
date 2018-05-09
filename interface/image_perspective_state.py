import pyglet
import numpy as np
import cv2 as cv

from gui_elements.image_tweaker.marker import Marker
from gui_elements.section_title import SectionTitle
from gui_elements.state_title import StateTitle
from interface.state import State


class ImagePerspectiveState(State):
    def __init__(self, name, machine):
        super().__init__(name, machine)
        self.filename = None
        self.sprite = None
        self.tweaked = None
        self.machine = machine

        self.add_drawable(StateTitle('Change Perspective', self))
        self.add_drawable(
            SectionTitle('Select Corners CCW', self,
                         self.width / 4, self.height - 120)
        )
        self.add_drawable(
            SectionTitle('Preview', self,
                         self.width / 4 * 3, self.height - 120)
        )

        self.targets = []

    def resume(self):
        self.filename = self.machine.seed_file
        print('[Log] Selected Seed File: ' + self.filename)
        self.load_seed_image()

    def update(self):
        if self.machine.clicked:
            self.add_marker(self.machine.mouseX, self.machine.mouseY)
            self.machine.clicked = False

    def load_seed_image(self):
        sprite_image = pyglet.image.load(self.filename)
        sprite_image.anchor_x = 0
        sprite_image.anchor_y = 0
        self.sprite = pyglet.sprite.Sprite(sprite_image)
        self.calculate_scale()
        self.sprite.x = self.width / 4 - self.sprite.width / 2
        self.sprite.y = self.height / 2 - self.sprite.height / 2 - 60

        self.add_drawable(self.sprite)

    def add_marker(self, x, y):
        sx = self.sprite.x
        sy = self.sprite.y
        sw = self.sprite.width
        sh = self.sprite.height

        if len(self.targets) >= 4:
            self.machine.activate_state('image-tweaker-state')
            return
        elif x < sx or x > sx + sw or y < sy or y > sy + sh:
            return

        self.screen_to_img_coordinates(x, y)
        self.add_drawable(Marker(x, y))

    def screen_to_img_coordinates(self, x, y):
        image_w = self.sprite.image.width

        ratio = image_w / self.sprite.width

        current_x = x - self.sprite.x
        current_y = y - self.sprite.y
        current_y = self.sprite.height - current_y

        current_x *= ratio
        current_y *= ratio

        self.targets.append([int(current_x), int(current_y)])
        if len(self.targets) == 4:
            self.apply_perspective()

    def apply_perspective(self):
        img = cv.imread(self.filename)
        points_1 = np.float32(self.targets)
        points_2 = np.float32([[0, 0], [0, 416], [320, 416], [320, 0]])

        M = cv.getPerspectiveTransform(points_1, points_2)
        dst = cv.warpPerspective(img, M, (320, 416))

        cv.imwrite('workdata/seedfile.png', dst)
        print('[Log] Created seed file')
        self.display_tweaked_file()

    def display_tweaked_file(self):
        sprite_image = pyglet.image.load('workdata/seedfile.png')
        sprite_image.anchor_x = 0
        sprite_image.anchor_y = 0
        self.tweaked = pyglet.sprite.Sprite(sprite_image)
        self.tweaked.x = self.width / 4 * 3 - self.tweaked.width / 2
        self.tweaked.y = self.height / 2 - self.tweaked.height / 2 - 60

        self.add_drawable(self.tweaked)

    def calculate_scale(self):
        max_w = self.width / 2 - 80
        max_h = self.height - 200

        scale_x = max_w / self.sprite.width
        scale_y = max_h / self.sprite.height

        self.sprite.scale = min(scale_x, scale_y)
