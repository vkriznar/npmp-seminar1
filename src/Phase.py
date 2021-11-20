from src.Gate import Gate, I

import numpy as np
from itertools import islice
from functools import reduce


class Phase():
    def __init__(self, size):
        self.size = size
        self.gates = size * [None]
        self.mat = np.array([1])

    def __str__(self):
        return "-".join(map(lambda g: g.label, self.gates))

    def addGate(self, gate=Gate(), location=None):
        for i in range(gate.inputSize):
            self.gates[location + i] = gate

    def getNormalizedGates(self):
        normalizedGates = list()
        gatesIterator = iter(self.gates)

        for gate in gatesIterator:
            if gate is None:
                normalizedGates.append(I())
            else:
                normalizedGates.append(gate)
                _ = list(islice(gatesIterator, gate.inputSize - 1))

        return normalizedGates

    def getMaxLableLength(self):
        return reduce(lambda acc, gate: max(acc, 1 if gate is None else len(gate.label)), self.gates, 0)

    def eval(self):
        for gate in self.getNormalizedGates():
            self.mat = np.kron(self.mat, gate.mat)
