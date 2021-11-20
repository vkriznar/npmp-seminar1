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


c1 = Circuit()
c1.addInput(Qubit(1, 0))
c1.addInput(Qubit(1, 0))
c1.addInput(Qubit(0, 1))
c1.addInput(Qubit(1, 0))

c1.addPhase()
c1.addGate(H(), 0, 0)
c1.addGate(I(), 0, 1)

c1.addPhase()
c1.addGate(CNOT(), 1, 0)
c1.addGate(H(), 1, 2)

c1.addPhase()
#c1.addGate(I(), 2, 0)
c1.addGate(H(), 2, 1)
c1.addGate(CNOT(), 2, 2)
print(c1)
