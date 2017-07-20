import math
import random

TAU = 2 * math.pi

class BrownianModifier(object):
	"""Each iteration it adds noise selected uniformly at random from the
	   interval [-magnitude, magnitude] to the variable."""

	def __init__(self, variable, magnitude):
		self.variable = variable
		self.magnitude = magnitude

	def iterate(self):
		delta = random.randint(-self.magnitude, self.magnitude)
		self.variable.modify(delta)

class SinusoidModifier(object):
	"""Over a period of period iterations adds to the variable an amount
	   determined by a sinusoid of amplitude height."""

	def __init__(self, variable, amplitude, period, offset = 0):
		self.variable = variable
		self.amplitude = amplitude
		self.period = period
		self.offset = offset

	def iterate(self):
		radians = float(self.offset) / self.period * TAU

		delta = math.sin(radians) * self.amplitude

		self.variable.modify(delta)

		self.offset += 1
		if self.offset == self.period:
			self.offset = 0