import pygame, sys

from pygame.locals import * 

pygame.init()

DISPLAYSURF = pygame.display.set_mode((300,300))

pygame.display.set_caption('My First Game')

while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.draw.rect(DISPLAYSURF, (0,255,0), (100,50,20,20))
	pygame.draw.rect(DISPLAYSURF, (0,0,255), (250,75,100,20))
	pygame.draw.rect(DISPLAYSURF, (255,0,0), (177,200,20,30))
	pygame.draw.rect(DISPLAYSURF, (255,200,0), (100,250,90,70))
	pygame.display.update()
