import pygame, sys, random
from pygame.locals import * 

#Sets the measurments for the game screen
TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

DIRT = 0
GRASS = 1
WATER = 2
COAL =3
LAVA = 4
ROCK = 5
DIAMOND = 6

textures = {
	DIRT : pygame.image.load('Pictures/dirt.png'),
	GRASS : pygame.image.load('Pictures/grass.png'),
	WATER : pygame.image.load('Pictures/water.png'),
	COAL : pygame.image.load('Pictures/coal.png'),
	LAVA : pygame.image.load('Pictures/lava.png'),
	ROCK : pygame.image.load('Pictures/rock.png'),
	DIAMOND : pygame.image.load('Pictures/diamond.png')
	}

resources = [DIRT, GRASS, WATER, COAL, LAVA, ROCK, DIAMOND]

tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPWIDTH)]


pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
pygame.display.set_caption('I\'m so tired... all the time... please help me...')

for rw in range(MAPHEIGHT):
	for cl in range(MAPWIDTH):
		randomNumber = random.randint(0,17)
		if randomNumber == 0:
			randNumber_2 = random.randint(0,3)
			if randNumber_2 == 0:
				title = DIAMOND
			elif randNumber_2 > 0:
				title = WATER
		elif randomNumber == 1 or randomNumber == 2:
			title = COAL
		elif randomNumber == 3 or randomNumber == 4:
			title = WATER
		elif randomNumber >=5 and randomNumber <= 8:
			title = GRASS
		else:
			title = DIRT
			
		tilemap[rw][cl] = title

while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
	
	pygame.display.update()
