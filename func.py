import numpy as np

def sigmod(x):
    return 1/ (1 + np.exp(-1))

treining_inputs = np.array([[0,0,1],
                           [1,1,1],
                           [1,0,1],
                           [0,1,1]])

treining_outputs = np.array([[0,1,1,0]]).T

np.rand.seed(1)

synaptic_weights = 2 * np.rand.random((3,1) - 1)

print(synaptic_weights)