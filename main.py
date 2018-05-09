import pyglet
from interface.image_loader_state import ImageLoaderState
from interface.image_perspective_state import ImagePerspectiveState
from interface.image_tweaker_state import ImageTweakerState
from interface.state_machine import StateMachine
from window_events import WindowEventHandler

window = pyglet.window.Window(
    1280, 720, 'GAN Digits Generator'
)

state_machine = StateMachine(window)

image_loader_state = ImageLoaderState('image-loader-state', state_machine)
state_machine.add_state(image_loader_state)
state_machine.activate_state('image-loader-state')

image_perspective_state = ImagePerspectiveState('image-perspective-state', state_machine)
state_machine.add_state(image_perspective_state)

image_tweaker_state = ImageTweakerState('image-tweaker-state', state_machine)
state_machine.add_state(image_tweaker_state)

event_handler = WindowEventHandler(state_machine, window)
window.push_handlers(event_handler)


def update(delta):
    state_machine.update()


print('[Log] Initializing application.')

pyglet.font.add_file('assets/roboto-medium-font.ttf')
pyglet.clock.schedule_interval(update, 1.0 / 60.0)
pyglet.app.run()

print('[Log] Closing application.')
