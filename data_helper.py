import numpy as np
from sklearn import preprocessing


def prepare_data(data_set):
    target_scaler = preprocessing.OneHotEncoder()
    d, t = data_set
    d, t = np.array(d), np.array(t)
    d = d / 255.
    d = d - d.mean(axis=0)

    t = target_scaler.fit_transform(t.reshape(-1, 1))
    t = t.todense()
    return d, t
