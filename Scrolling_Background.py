import pygame
from pygame.locals import *
pygame.init()
# Imports pygame library and initialises.

# Sets screen resolution to 1080x720 and makes it fullscreen.
screen = pygame.display.set_mode((1080, 720), FULLSCREEN)

# Declaring variables required for movement.
x = 100
y = 100
speed = 20
width = 50
height = 50

# Sets variable for main loop to true, so loop runs.
running = True

while running:
	keys = pygame.key.get_pressed()
	colour = (255, 0, 0)
	screen.fill(pygame.Color(255, 255, 123))
	pygame.draw.rect(screen, colour, (x, y, width, height))

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			running = False

		if keys[pygame.K_ESCAPE]:
			running = False
			# bear in mind we need WASD and arrow, arrow for players who dont use WASD (cough cough, Me)
			# All right, fine
			# Also, please only use tabs for indentation, not spaces. Python has problems if you mix the two. - Victor
				
		if keys[pygame.K_w] and y > 0 or keys[pygame.K_UP] and y > 0:
			y -= speed

		if keys[pygame.K_s] and y < 720 - height or keys[pygame.K_DOWN] and y < 720 - height:
			y += speed

		if keys[pygame.K_a] and x > 0 or keys[pygame.K_LEFT] and x > 0:
			x -= speed

		if keys[pygame.K_d] and x < 1080 - width or keys[pygame.K_RIGHT] and x < 1080 - width:
			x += speed

	pygame.display.update()
	pygame.display.flip()

