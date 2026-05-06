import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((500, 500), FULLSCREEN)

running = True

while running:
	
	keys = pygame.key.get_pressed()
	
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			run = False

	if keys[pygame.K_ESCAPE]:
		running = False



exit()
