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

def grover3():
    cG = Circuit(12, 3)
    cG.setInput(Qubit(1, 0), 0)
    cG.setInput(Qubit(1, 0), 1)
    cG.setInput(Qubit(1, 0), 2)

    cG.setGate(H(), 0, 0)
    cG.setGate(H(), 0, 1)
    cG.setGate(H(), 0, 2)

    #circuit for 101 and 110 oracle
    #cG.setGate(SWAP(), 1, 0)
    #cG.setGate(CZ(), 2, 1)
    #cG.setGate(SWAP(), 3, 0)
    #cG.setGate(CZ(), 4, 1)

    #generic oracle that can be set in Gate.py (-1 values are the values we are looking for)
    cG.setGate(G3(), 1, 0)


    cG.setGate(H(), 5, 0)
    cG.setGate(H(), 5, 1)
    cG.setGate(H(), 5, 2)

    cG.setGate(X(), 6, 0)
    cG.setGate(X(), 6, 1)
    cG.setGate(X(), 6, 2)

    # multicontrolled Z from H MCT H
    cG.setGate(H(), 7, 2)
    cG.setGate(MCT(), 8, 0)
    cG.setGate(H(), 9, 2)

    cG.setGate(X(), 10, 0)
    cG.setGate(X(), 10, 1)
    cG.setGate(X(), 10, 2)

    cG.setGate(H(), 11, 0)
    cG.setGate(H(), 11, 1)
    cG.setGate(H(), 11, 2)

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
print(groverCircuit)

R, inbetweenResults = groverCircuit.run()
print("Result: ")
print(R)

print("-----------------------------------------------------------------------")
groverCircuit = grover3()
print(groverCircuit)

R, inbetweenResults = groverCircuit.run()
print("Result: ")
print(R)