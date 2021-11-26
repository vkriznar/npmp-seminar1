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


# PAULI X (NOT)
class X(Gate):
    def __init__(self):
        super().__init__('X', inputSize=1, matSize=2)
        self.mat = np.array([
            [0, 1],
            [1, 0]
        ])


# PAULI Y
class Y(Gate):
    def __init__(self):
        super().__init__('Y', inputSize=1, matSize=2)
        self.mat = np.array([
            [0, -1j],
            [1j,  0]
        ])


# PAULI Z
class Z(Gate):
    def __init__(self):
        super().__init__('Z', inputSize=1, matSize=2)
        self.mat = np.array([
            [1,  0],
            [0, -1]
        ])


# HADAMARD
class H(Gate):
    def __init__(self):
        super().__init__('H', inputSize=1, matSize=2)
        self.mat = 1/math.sqrt(2) * np.array([
            [1,  1],
            [1, -1]
        ])

# PHASE SHIFT
class PS(Gate):
    def __init__(self, phi):
        super().__init__("PS", inputSize=1, matSize=2)
        self.mat = np.array([
            [1,  0],
            [0, math.cos(phi) + math.sin(phi)*1j]
        ])


# PHASE Z = PAULI Z
class Z(Gate):
    def __init__(self):
        super().__init__('Z', inputSize=1, matSize=2)
        self.mat = np.array([
            [1,  0],
            [0, -1]
        ])


# PHASE S
class S(Gate):
    def __init__(self):
        super().__init__('S', inputSize=1, matSize=2)
        self.mat = np.array([
            [1,  0],
            [0, 1j]
        ])


# PHASE T
class T(Gate):
    def __init__(self):
        super().__init__('T', inputSize=1, matSize=2)
        self.mat = np.array([
            [1, 0],
            [0,  1/math.sqrt(2) + (1/math.sqrt(2))*1j]
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
class CZ(Gate):
    def __init__(self):
        super().__init__("CZ", inputSize=2, matSize=4)
        self.mat = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, -1]
        ])

# MULTI CONTROLLED TOFOLLI
class MCT(Gate):
    def __init__(self):
        super().__init__("MCT", inputSize=3, matSize=8)
        self.mat = np.array([
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0]
        ])

# GROVER3 ORACLE
class G3(Gate):
    def __init__(self):
        super().__init__("G3", inputSize=3, matSize=8)
        self.mat = np.array([
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, -1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, -1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1]
        ])

class Measure(Gate):
    def __init__(self):
        super().__init__("M", inputSize=1, matSize=2)
        self.mat = np.array([
            [1, 0],
            [0, 1]
        ])