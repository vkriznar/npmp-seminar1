from src.Gate import Gate


class Phase():
    def __init__(self, operations=list()):
        self.operations = operations

    def addGate(self, gate=Gate(), location=None):
        if location is None:
            for i in range(gate.inputSize):
                self.operations.append(gate)
        else:
            for i in range(gate.inputSize):
                self.operations.insert(location + i, gate)
