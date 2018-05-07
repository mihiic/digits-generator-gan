import pyglet


class WindowEventHandler(object):
    def __init__(self, state_machine, window):
        self.state_machine = state_machine
        self.window = window

    def on_close(self):
        self.state_machine.destroy()

        self.window.pop_handlers()
        self.window.has_exit = True
        self.window.close()
        return pyglet.event.EVENT_HANDLED

    def on_draw(self):
        self.window.clear()
        self.state_machine.draw()
