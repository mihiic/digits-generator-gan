from gui_elements.drawable import Drawable


class State:
    def __init__(self, name, machine):
        self.name = name
        self.machine = machine
        self.width = machine.window.width
        self.height = machine.window.height
        self.drawables = []

    def pause(self):
        pass

    def resume(self):
        self.width = self.machine.window.width
        self.height = self.machine.window.height

    def destroy(self):
        pass

    def update(self):
        pass

    def draw(self):
        for drawable in self.drawables:
            drawable.draw()

    def add_drawable(self, drawable):
        if drawable.draw is None:
            raise Exception('Element must implement Drawable interface')

        self.drawables.append(drawable)
