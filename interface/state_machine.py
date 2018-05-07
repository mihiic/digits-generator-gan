class StateMachine:
    def __init__(self, window):
        self.states = []
        self.active_state = None
        self.window = window

    def add_state(self, state):
        self.states.append(state)

    def activate_state(self, state_name):
        if self.active_state is not None:
            self.active_state.pause()

        self.active_state = self.get_state(state_name)
        self.active_state.resume()

    def remove_state(self, state_name):
        if state_name == self.active_state.name:
            raise Exception('Can\'t remove currently active state')

        self.states.remove(self.get_state(state_name))

    def get_state(self, state_name):
        for state in self.states:
            if state.name == state_name:
                return state

        return None

    def update(self):
        if self.active_state is not None:
            self.active_state.update()

    def draw(self):
        if self.active_state is not None:
            self.active_state.draw()

    def destroy(self):
        if self.active_state is not None:
            self.active_state.destroy()
