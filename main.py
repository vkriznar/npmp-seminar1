from src.Qubit import Qubit
from src.Gate import *
from src.Circuit import Circuit


def grover2():
    cG = Circuit(6, 2)
    cG.setGate(H(), 0, 0)
    cG.setGate(H(), 0, 1)

    #oracle, in this example we are looking for |11>, so the oracle is a controlled-z gate.
    cG.setGate(CZ(), 1, 0)

    cG.setGate(H(), 2, 0)
    cG.setGate(H(), 2, 1)

    cG.setGate(Z(), 3, 0)
    cG.setGate(Z(), 3, 1)

    cG.setGate(CZ(), 4, 0)

    cG.setGate(H(), 5, 0)
    cG.setGate(H(), 5, 1)

    cG.setInput(Qubit(1, 0), 0)
    cG.setInput(Qubit(1, 0), 1)

    return cG

#print(Qubit())
#print(Qubit(1, 0))
#print(Qubit(0, 1))
#print(Qubit(1, 1).normalize())


#print(I())
#print(X())
#print(H())
#print(SWAP())
#print(CNOT())

c0 = Circuit(sizeX=1, sizeY=1)
c0.setInput(Qubit(1, 0), 0)
c0.setGate(X(), 0, 0)
r0, inbetweenResults = c0.run()
print(c0)
print(r0)
print("-----------------------------------------------------------------------")

c1 = Circuit(sizeX=3, sizeY=4)
c1.setInput(Qubit(1, 0), 0)
c1.setInput(Qubit(1, 0), 1)
c1.setInput(Qubit(0, 1), 2)
c1.setInput(Qubit(1, 0), 3)

c1.setGate(Y(), 0, 0)
c1.setGate(X(), 0, 1)
c1.setGate(CNOT(), 0, 1)

c1.setGate(CNOT(), 1, 0)
c1.setGate(H(), 1, 2)

c1.setGate(I(), 2, 0)
c1.setGate(H(), 2, 1)
c1.setGate(CNOT(), 2, 2)
print(c1)

R, inbetweenResults = c1.run()
print(R)
print("-----------------------------------------------------------------------")

groverCircuit = grover2()
R, inbetweenResults = groverCircuit.run()
print(R)