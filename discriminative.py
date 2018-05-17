from dill import dill
from mnist import MNIST
from sklearn.preprocessing import OneHotEncoder
from neupy import algorithms, layers, environment, storage
import numpy as np
from neupy import plots
import theano


mndata = MNIST('mnist')
mndata.gz = True
target_scaler = OneHotEncoder()


def prepare_data(data_set):
    d, t = data_set
    d, t = np.array(d), np.array(t)
    d = d / 255.
    d = d - d.mean(axis=0)

    t = target_scaler.fit_transform(t.reshape(-1, 1))
    t = t.todense()
    return d, t


theano.config.floatX = 'float32'

data, target = prepare_data(mndata.load_training())
y_data, y_target = prepare_data(mndata.load_testing())

environment.reproducible()

network = algorithms.Momentum(
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

network.train(data, target, y_data, y_target, epochs=20)

with open('discriminative-network.dill', 'wb') as file:
    dill.dump(network, file)

plots.error_plot(network)
