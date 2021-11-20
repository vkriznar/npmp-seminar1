from qutip import Bloch, basis
import matplotlib.pyplot as plt


class QubitVisualizator():
	def __init__(self, alpha, beta) -> None:
		if alpha * alpha + beta * beta != 1:
			raise Exception("Qubit has to be normalized")
		self.alpha = alpha
		self.beta = beta

	def visualize(self):
		b = Bloch()
		b.add_states(basis(2, 0))
		b.add_states(basis(2, 1))
		b.add_states((self.alpha * basis(2, 0) + self.beta * basis(2, 1)).unit())
		b.show()
		# For some reason b.show() immediately closes, as a workaround plt.show() was added
		plt.show()

	def animate(self):
		# TODO
		pass
