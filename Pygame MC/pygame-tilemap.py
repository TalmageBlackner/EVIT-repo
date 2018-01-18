import pygame, sys
from pygame.locals import * 

DIRT = 0
GRASS = 1
WATER = 2
COAL =3
LAVA = 4
ROCK = 5

BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (0, 0, 128)

tilemap = [
	[GRASS,COAL,DIRT,GRASS,ROCK],
	[WATER,WATER,GRASS,DIRT,COAL],
	[COAL,GRASS,WATER,LAVA,ROCK],
	[DIRT,WATER,COAL,LAVA,LAVA],
	[GRASS,WATER,DIRT,COAL,WATER]
]

colors = {
	DIRT : BROWN,
	GRASS : GREEN,
	WATER : BLUE,
	COAL : BLACK,
	LAVA : RED,
	ROCK : GRAY
	}

TILESIZE = 40
MAPWIDTH = 5
MAPHEIGHT = 5

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

pygame.display.set_caption('I\'m so tired... all the time... please help me...')

while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			pygame.draw.rect(DISPLAYSURF,colors[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
	
	pygame.display.update()
