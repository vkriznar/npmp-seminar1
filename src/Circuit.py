import math

from src.Qubit import Qubit
from src.Gate import Gate
from src.Phase import Phase

import numpy as np
from functools import reduce


class Circuit():
    def __init__(self, sizeX=1, sizeY=1):
        self.sizeX = sizeX  # phase size
        self.sizeY = sizeY  # input size

        self.phases = list()
        self.inputs = Phase(self.sizeY)

        self.setSize(sizeX, sizeY)

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

    # n phases
    def setSizeX(self, sizeX):
        self.sizeX = sizeX

        phases = list()

        for i in range(self.sizeX):
            if i < len(self.phases):
                phases.append(self.phases[i])
            else:
                phases.append(Phase(size=self.sizeY))

        self.phases = phases

    # input size
    def setSizeY(self, sizeY):
        self.sizeY = sizeY
        self.inputs.setSize(sizeY)

        for phase in self.phases:
            phase.setSize(sizeY)

    def setSize(self, sizeX, sizeY):
        self.setSizeX(sizeX)
        self.setSizeY(sizeY)

    #def addInput(self, qubit=Qubit(), location=None):
    #    self.inputs.addGate(qubit, location)

    def setInput(self, qubit=None, locationY=None):
        self.inputs.setNode(qubit, locationY)

    #def addPhase(self, phase=None, locationX=None):
    #    if phase is None:
    #        phase = Phase(size=self.sizeY)

    #    if locationX is None:
    #        self.phases.append(phase)
    #    else:
    #        self.phases.insert(locationX, phase)

    def setPhase(self, phase=None, locationX=None):
        if phase is None:
            phase = Phase(size=self.sizeY)

        self.phases[locationX] = phase

    #def addGate(self, gate, locationX=None, locationY=None):
    #    if locationX is None:
    #        self.phases[len(self.phases) - 1].addGate(gate, locationY)
    #    else:
    #        self.phases[locationX].addGate(gate, locationY)

    def setGate(self, gate, locationX=None, locationY=None):
        self.phases[locationX].setNode(gate, locationY)

    def run(self):
        vector = self.inputs.eval()

        for phase in self.phases:
            matrix = phase.eval()
            vector = np.matmul(matrix, vector)

        return vector

    # TODO JSON export for visualization and other simulators?
