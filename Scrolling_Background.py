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
			# bare in mind we need WASD and arrow, arrow for players who dont use WASD (cough cough, Me)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
			screen.fill(pygame.Color(255, 255, 123))
			
		if keys[pygame.K_s] or keys[pygame.K_DOWN]:
			screen.fill(pygame.Color(255, 255, 123))
	
	pygame.display.update()

# I did a bit of copy and paste, so the variables didn't match perfectly, and yes, more keys will get added later. This was just so it was possible to close the pygame program.
# Otherwise, since it loads in fullscreen, it's actually very annoying to try and close. - Victor
