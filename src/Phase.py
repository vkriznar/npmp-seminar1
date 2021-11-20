from src.Gate import Gate

import numpy as np
from itertools import islice


class Phase():
    def __init__(self, gates=list()):
        self.gates = []
        self.mat = None

    def __str__(self):
        return "-".join(map(lambda g: g.label, self.gates))

    def addGate(self, gate=Gate(), location=None):
        if location is None:
            for i in range(gate.inputSize):
                self.gates.append(gate)
        else:
            for i in range(gate.inputSize):
                self.gates.insert(location + i, gate)

    def eval(self):
        gatesIterator = iter(self.gates)
        gate = next(gatesIterator)

        self.mat = gate.mat
        gatesIterator = islice(gatesIterator, gate.inputSize - 1, None)

        for gate in gatesIterator:
            self.mat = np.kron(self.mat, gate.mat)
            gatesIterator = islice(gatesIterator, gate.inputSize - 1, None)
