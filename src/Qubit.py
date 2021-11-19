import numpy as np


class Qubit():
    def __init__(self, state0=None, state1=None):
        self.state0 = state0
        self.state1 = state1
        self.vector = np.array([state0, state1])
        self.mat = self.vector

    def __str__(self):
        return "Qubit: " + str(self.vector)

    def normalize(self):
        norm = np.linalg.norm(self.vector)
        self.vector = self.vector / norm
        return self
