import dill
import numpy as np
from sklearn import datasets, preprocessing
from mnist import MNIST
from neupy import algorithms, layers, environment, storage

from data_helper import prepare_data

with open('discriminative-network.dill', 'rb') as file:
    network = dill.load(file)


mndata = MNIST('mnist')
mndata.gz = True
target_scaler = preprocessing.OneHotEncoder()

data, target = prepare_data(mndata.load_training())


gen_network = algorithms.Momentum(
    [
        layers.Input(784),
        layers.Relu(500),
        layers.Relu(300),
        layers.Softmax(10),
    ],
    error='categorical_crossentropy',
    step=0.01,
    verbose=True,
    shuffle_data=True,
    momentum=0.99,
    nesterov=True
)
