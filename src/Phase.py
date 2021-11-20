from src.Gate import Gate, I

import numpy as np
from itertools import islice
from functools import reduce


class Phase():
    def __init__(self, size):
        self.size = size
        self.nodes = size * [None]
        self.mat = np.array([1])

    def __str__(self):
        return "-".join(map(lambda g: g.label, self.nodes))

    def addGate(self, gate=Gate(), location=None):
        for i in range(gate.inputSize):
            self.nodes[location + i] = gate

    def getNormalizedGates(self):
        normalizedGates = list()
        nodesIterator = iter(self.nodes)

        for gate in nodesIterator:
            if gate is None:
                normalizedGates.append(I())
            else:
                normalizedGates.append(gate)
                _ = list(islice(nodesIterator, gate.inputSize - 1))

        return normalizedGates

    def getMaxLableLength(self):
        return reduce(lambda acc, gate: max(acc, 1 if gate is None else len(gate.label)), self.nodes, 0)

    def eval(self):
        for gate in self.getNormalizedGates():
            self.mat = np.kron(self.mat, gate.mat)

        return self.mat
