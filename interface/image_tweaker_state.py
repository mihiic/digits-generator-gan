import pyglet
import cv2 as cv2

from gui_elements.section_title import SectionTitle
from gui_elements.state_title import StateTitle
from interface.state import State


class ImageTweakerState(State):
    def __init__(self, name, machine):
        super().__init__(name, machine)
        self.sprite = None
        self.current = None
        self.step = 0
        self.steps = [
            self.gaussian_blur,
            self.laplacian,
            self.threshold
        ]

        self.add_drawable(StateTitle('Tweak Seed Image', self))

        self.action = SectionTitle(
            'Apply Gaussian Blur', self, self.width / 4, self.height - 120
        )
        self.add_drawable(
            self.action
        )

    def resume(self):
        self.current = cv2.imread('workdata/seedfile.png')
        self.set_previous_sprite('workdata/seedfile.png')

    def update(self):
        if self.machine.clicked:
            if self.step == 3:
                # change state
                return
            else:
                self.machine.clicked = False
                self.steps[self.step]()
                self.step += 1

    def set_previous_sprite(self, file):
        sprite_image = pyglet.image.load(file)
        sprite_image.anchor_x = 0
        sprite_image.anchor_y = 0
        self.sprite = pyglet.sprite.Sprite(sprite_image)
        self.sprite.x = self.width / 2 - self.sprite.width / 2
        self.sprite.y = self.height / 2 - self.sprite.height / 2 - 60

        self.add_drawable(self.sprite)

    def gaussian_blur(self):
        self.action.change_title('Apply Laplacian')
        img = cv2.imread('workdata/seedfile.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (3, 3), 0)
        cv2.imwrite('workdata/seedfile.png', img)

        self.set_previous_sprite('workdata/seedfile.png')

    def laplacian(self):
        self.action.change_title('Binarize')

        img = cv2.imread('workdata/seedfile.png')
        img = cv2.Laplacian(img, cv2.CV_64F)
        cv2.imwrite('workdata/seedfile.png', img)

        self.set_previous_sprite('workdata/seedfile.png')

    def threshold(self):
        self.action.change_title('Continue')
        img = cv2.imread('workdata/seedfile.png')
        ret, img = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
        cv2.imwrite('workdata/seedfile.png', img)

        self.set_previous_sprite('workdata/seedfile.png')
