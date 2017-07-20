import pygame

import variable

class Square(object):

	def __init__(self, x, y, w, h, color):
		self.x = variable.Variable(x)
		self.y = variable.Variable(y)
		self.w = variable.Variable(w)
		self.h = variable.Variable(h)
		self.color = variable.Variable(color)

		# Add our constraints.
		variable.mustBeGreaterThan(self.w, variable.Constant(5))
		variable.mustBeGreaterThan(self.h, variable.Constant(5))

	def render(self, screen):
		rect = pygame.Rect(self.x.get(), self.y.get(), self.w.get(), self.h.get())
		pygame.draw.rect(screen, self.color.get(), rect)

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getW(self):
		return self.w

	def getH(self):
		return self.h