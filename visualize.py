# This is the master file that manages the visual chocolate and will show it
# when run. It makes use of the pygame framework for managing rendering.

import pygame
import random

import modifier
import square
import variable

WIDTH = 500
HEIGHT = 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
done = False

modifiers = []

square = square.Square(30, 30, 60, 60, (0, 128, 255))
# Modifiers that move the square.
modifiers.append(modifier.BrownianModifier(square.getX(), 8))
modifiers.append(modifier.BrownianModifier(square.getY(), 8))
modifiers.append(modifier.SinusoidModifier(square.getW(), 3, 60))
modifiers.append(modifier.SinusoidModifier(square.getH(), 3, 60))
# Additional constraints to keep the square inside the box.
variable.mustBeGreaterThan(square.getX(), variable.Constant(0))
variable.mustBeGreaterThan(square.getY(), variable.Constant(0))
variable.mustSumToNoMoreThan(variable.Constant(WIDTH), [square.getX(), square.getW()])
variable.mustSumToNoMoreThan(variable.Constant(HEIGHT), [square.getY(), square.getH()])

while not done:
	# Clear the screen.
	screen.fill((255, 255, 255))

	for modifier in modifiers:
		modifier.iterate()

	square.render(screen)

	# Manage the game's events.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()
	clock.tick(60)