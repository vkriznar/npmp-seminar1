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

        for i in range(self.sizeY):
            lines[i] = str(self.inputs.nodes[i])

        for phase in self.phases:
            last_node = None
            input = None
            for i in range(self.sizeY):
                node = phase.nodes[i]

                if node is None:
                    lines[i] += " -> " + (phase.getMaxLableLength()+2)*'-'
                else:
                    if last_node is node:
                        input += 1
                    else:
                        input = 1

                    last_node = node


                    l1 = '['
                    label = node.label
                    l2 = ']'
                    if node.inputSize > 1 and input == 1:
                        l1 = '⌈'
                        l2 = '⌉'
                    if node.inputSize > 1 and 1 < input and input < node.inputSize:
                        l1 = '|'
                        label = len(node.label)*' '
                        l2 = '|'
                    if node.inputSize > 1 and input == node.inputSize:
                        l1 = '⌊'
                        label = len(node.label)*' '
                        l2 = '⌋'

                    diff = phase.getMaxLableLength() - len(node.label)
                    lines[i] += " -> " + math.floor(diff/2)*' ' + l1 + label + l2 + math.ceil(diff/2)*' '

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
        self.inputs.setSizeY(sizeY)

        for phase in self.phases:
            phase.setSizeY(sizeY)

    def setSize(self, sizeX, sizeY):
        self.setSizeX(sizeX)
        self.setSizeY(sizeY)

    def addInput(self, qubit=Qubit(), locationY=None):
        if locationY < self.sizeY:
            self.inputs.addNode(qubit, locationY)

            self.setSizeY(self.sizeY + 1)
        else:
            self.setSizeY(locationY + 1)

            self.inputs.setNode(qubit, locationY)

    def setInput(self, qubit=None, locationY=None):
        self.inputs.setNode(qubit, locationY)

    def addPhase(self, phase=None, locationX=None):
        if phase is None:
            phase = Phase(size=self.sizeY)

        if locationX < self.sizeX:
            if locationX is None:
                self.phases.append(phase)
            else:
                self.phases.insert(locationX, phase)

            self.setSizeX(self.sizeX + 1)
        else:
            self.setSizeX(locationX + 1)

            self.setPhase(phase, locationX)

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
        vectors = []
        vectors.append(vector)

        for phase in self.phases:
            if(phase.getNormalizedGates()[0].label == "M"):
                probabilities = vector**2
                probabilities = [float(float(i) / sum(probabilities)) for i in probabilities]
                index = np.random.choice(range(len(probabilities)), p=probabilities)
                print("Measure: " + format(index, '0'+str(self.sizeY)+'b'))
                continue
            matrix = phase.eval()
            vector = np.matmul(matrix, vector)
            vectors.append(vector)

        return vector, vectors

    # TODO JSON export for visualization and other simulators?
