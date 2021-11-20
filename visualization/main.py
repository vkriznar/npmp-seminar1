from numpy.core.shape_base import block
from qutip import Bloch, basis
import matplotlib.pyplot as plt

b = Bloch()
b.add_states(basis(2,0))
b.add_states(basis(2,1))
b.add_states((0.864 * basis(2,0) + 0.134 * basis(2,1)).unit())
b.show()
# For some reason b.show() immediately closes, as a workaround plt.show() was added
plt.show()
