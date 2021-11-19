from src.Qubit import Qubit
from src.Gate import Gate
from src.Phase import Phase

import numpy as np


class Circuit():
    def __init__(self, inputs=list()):
        self.inputs = inputs
        self.phases = list()
        self.currentPhase = None

    def addInput(self, qubit=Qubit(), location=None):
        if location is None:
            self.inputs.append(qubit)
        else:
            self.inputs.insert(location, qubit)

    def addPhase(self, phase=Phase(), location=None):
        if location is None:
            self.phases.append(phase)
        else:
            self.phases.insert(location, phase)

    def addGate(self, gate=Gate(), locationX=None, locationY=None):
        if locationX is None:
            self.phases[len(self.phases) - 1].addGate(gate, locationY)
        else:
            self.phases[locationX].addGate(gate, locationY)

    def advancePhase(self, phase):
        phase.eval()
        print("Test: ")
        print(self.currentPhase.mat)
        print(phase.mat)
        print(np.matmul(phase.mat, self.currentPhase.mat))

    def run(self):
        self.currentPhase = self.inputs[0]
        self.advancePhase(self.phases[0])

    # TODO print circuit
    # TODO JSON export for visualization and other simulators?
