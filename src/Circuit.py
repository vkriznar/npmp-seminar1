import math

from src.Qubit import Qubit
from src.Gate import Gate
from src.Phase import Phase

import numpy as np
from functools import reduce


class Circuit():
    def __init__(self, inputSize=1):
        self.inputSize = inputSize
        self.inputs = Phase(self.inputSize)
        self.phases = list()
        self.currentPhase = None

    def __repr__(self):
        lines = dict()

        for i in range(self.inputs.size):
            lines[i] = str(self.inputs.nodes[i])

        for phase in self.phases:
            for i in range(self.inputs.size):
                if phase.nodes[i] is None:
                    lines[i] += " -> " + (phase.getMaxLableLength()+2)*'-'
                else:
                    diff = phase.getMaxLableLength() - len(phase.nodes[i].label)
                    lines[i] += " -> " + math.floor(diff/2)*' ' + '[' + phase.nodes[i].label + ']' + math.ceil(diff/2)*' '

        output = ""
        for line in lines:
            output += str(lines[line]) + '\n'

        return str(output)

    def setInputSize(self, inputSize):
        self.inputs.setSize(inputSize)

        for phase in self.phases:
            phase.setSize(inputSize)

    def addInput(self, qubit=Qubit(), location=None):
        self.inputs.addGate(qubit, location)

    def addPhase(self, phase=None, location=None):
        if phase is None:
            phase = Phase(size=self.inputs.size)

        if location is None:
            self.phases.append(phase)
        else:
            self.phases.insert(location, phase)

    def addGate(self, gate, locationX=None, locationY=None):
        if locationX is None:
            self.phases[len(self.phases) - 1].addGate(gate, locationY)
        else:
            self.phases[locationX].addGate(gate, locationY)

    def run(self):
        vector = self.inputs.eval()

        for phase in self.phases:
            matrix = phase.eval()
            vector = np.matmul(matrix, vector)

        return vector

    # TODO JSON export for visualization and other simulators?
