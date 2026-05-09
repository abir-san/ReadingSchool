import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((500, 500), FULLSCREEN)

running = True
while running:
	keys = pygame.key.get_pressed()
	
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			running = False

		if keys[pygame.K_ESCAPE]:
			running = False
			# bear in mind we need WASD and arrow, arrow for players who dont use WASD (cough cough, Me)
			# All right, fine
        if keys[pygame.K_w] or keys[pygame.K_UP]:
			screen.fill(pygame.Color(255, 255, 123))
			
		if keys[pygame.K_s] or keys[pygame.K_DOWN]:
			screen.fill(pygame.Color(255, 255, 123))
	
	pygame.display.update()

