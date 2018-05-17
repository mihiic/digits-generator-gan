import os
import time

import yaml
import cv2 as cv
from nimblenet.activation_functions import sigmoid_function
from nimblenet.data_structures import Instance
from nimblenet.neuralnet import NeuralNet

from gui_elements.section_title import SectionTitle
from gui_elements.state_title import StateTitle
from interface.state import State


class DiscriminativeTopology(State):
    def __init__(self, name, machine):
        super().__init__(name, machine)

        self.add_drawable(
            StateTitle('Properties given for discriminative network', self)
        )

        self.action = SectionTitle(
            'Constructing neural network..', self, self.width / 4, self.height - 120
        )
        self.add_drawable(self.action)

        with open('config.yml') as config:
            self.config = yaml.load(config)

        self.network = None
        self.dataset = []

    def resume(self):
        self.machine.config = self.config
        self.config = self.config['discriminative']

        self.construct_neural_network()
        self.prepare_dataset()

    def prepare_dataset(self):
        self.action.change_title('Preparing dataset...')
        for i in range(0, 10):
            for j in range(1, 13):
                img = cv.imread('{}_{}.png'.format(i, j))

                inputs = []
                for x in range(28):
                    for y in range(28):
                        inputs.append(img[x][y])
                outputs = []
                for x in range(10):
                    if x == i:
                        outputs.append(1)
                    else:
                        outputs.append(0)

                self.dataset.append(Instance(inputs, outputs))
        self.action.change_title('Training network')

    def construct_neural_network(self):
        input_neurons = self.config['input_x'] * self.config['input_y']
        neurons_per_layer = self.config['neurons_in_hidden_layer']
        layers = []
        for i in range(self.config['hidden_layers']):
            layers.append((neurons_per_layer, sigmoid_function))

        layers.append((self.config['output'], sigmoid_function))

        settings = {
            'n_inputs': input_neurons,
            'layers': layers
        }

        self.network = NeuralNet(settings)
        time.sleep(0.5)
