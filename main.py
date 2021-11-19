from src.Qubit import Qubit
from src.Gate import *
from src.Circuit import Circuit


print(Qubit())
print(Qubit(1, 0))
print(Qubit(0, 1))
print(Qubit(1, 1).normalize())


print(I())
print(X())
print(H())
print(SWAP())
print(CNOT())


c = Circuit()
c.addInput(Qubit(1, 0))
c.addPhase()
c.addGate(H(), 0)
c.run()
