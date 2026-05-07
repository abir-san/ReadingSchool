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
		
		if keys[pygame.K_w]:
			running = False


# I did a bit of copy and paste, so the variables didn't match perfectly, and yes, more keys will get added later. This was just so it was possible to close the pygame program.
# Otherwise, since it loads in fullscreen, it's actually very annoying to try and close. - Victor