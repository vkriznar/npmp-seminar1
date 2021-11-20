import math
import numpy as np


# ABSTRACT
class Gate():
    def __init__(self, label=None, inputSize=None, matSize=None):
        self.label = label
        self.mat = None
        self.inputSize = inputSize
        self.matSize = matSize

    def __str__(self):
        return str(self.label) + ": \n" + str(self.mat)


# IDENTITY
class I(Gate):
    def __init__(self):
        super().__init__('I', inputSize=1, matSize=2)
        self.mat = np.array([
            [1, 0],
            [0, 1]
        ])


# NOT
class X(Gate):
    def __init__(self):
        super().__init__('X', inputSize=1, matSize=2)
        self.mat = np.array([
            [0, 1],
            [1, 0]
        ])


# HADAMARD
class H(Gate):
    def __init__(self):
        super().__init__('H', inputSize=1, matSize=2)
        self.mat = 1/math.sqrt(2) * np.array([
            [1,  1],
            [1, -1]
        ])


# SWAP
class SWAP(Gate):
    def __init__(self):
        super().__init__("SWAP", inputSize=2, matSize=4)
        self.mat = np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ])


# CONTROLLED NOT
class CNOT(Gate):
    def __init__(self):
        super().__init__("CNOT", inputSize=2, matSize=4)
        self.mat = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ])


# CONTROLLED Z
class Z(Gate):
    def __init__(self):
        super().__init__("Z")
        self.mat = H() @ CNOT() @ H()
