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

    def setSizeY(self, size):
        self.size = size
        nodes = list()

        for i in range(self.size):
            if i < len(self.nodes):
                nodes.append(self.nodes[i])
            else:
                nodes.append(None)

        self.nodes = nodes

    def addNode(self, node=None, locationY=None):
        if locationY is None:
            self.nodes.append(node)
        else:
            self.nodes.insert(locationY, node)

    def setNode(self, node=None, locationY=None):
        for i in range(node.inputSize):
            self.nodes[locationY + i] = node

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
        self.mat = np.array([1])

        for gate in self.getNormalizedGates():
            self.mat = np.kron(self.mat, gate.mat)

        return self.mat
