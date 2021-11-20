from src.Gate import Gate

import numpy as np
from itertools import islice
from functools import reduce


class Phase():
    def __init__(self, size):
        self.size = size
        self.gates = size * [None]
        self.mat = None

    def __str__(self):
        return "-".join(map(lambda g: g.label, self.gates))

    def addGate(self, gate=Gate(), location=None):
        for i in range(gate.inputSize):
            self.gates[location + i] = gate

    def getMaxLableLength(self):
        return reduce(lambda acc, gate: max(acc, 1 if gate is None else len(gate.label)), self.gates, 0)

    #TODO fix
    def eval(self):
        gatesIterator = iter(self.gates)
        gate = next(gatesIterator)

        self.mat = gate.mat
        gatesIterator = islice(gatesIterator, gate.inputSize - 1, None)

        for gate in gatesIterator:
            self.mat = np.kron(self.mat, gate.mat)
            gatesIterator = islice(gatesIterator, gate.inputSize - 1, None)
