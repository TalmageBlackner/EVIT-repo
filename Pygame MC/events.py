import pygame, sys, random
from pygame.locals import * 

#Sets the measurments for the game screen
TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

#gives each resources a variable number to define it
DIRT = 0
GRASS = 1
WATER = 2
COAL =3
LAVA = 4
ROCK = 5
DIAMOND = 6

#Gives each resource a personal texture
textures = {
	DIRT : pygame.image.load('Pictures/dirt.png'),
	GRASS : pygame.image.load('Pictures/grass.png'),
	WATER : pygame.image.load('Pictures/water.png'),
	COAL : pygame.image.load('Pictures/coal.png'),
	LAVA : pygame.image.load('Pictures/lava.png'),
	ROCK : pygame.image.load('Pictures/rock.png'),
	DIAMOND : pygame.image.load('Pictures/diamond.png')
	}

#Creates a list containing each resource to be randomly choses and assigned a point on the display
resources = [DIRT, GRASS, WATER, COAL, LAVA, ROCK, DIAMOND]
tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPWIDTH)]

inventory = {
		
}
#Begin program, set display size, and label the window caption
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
pygame.display.set_caption('Resetti\'s Adventure!')

#Loads the player into the program
PLAYER = pygame.image.load('Pictures/Resetti_ingame.png').convert_alpha()
playerPos = [0,0]

#Goes through each square on the program window and assigns it a resource randomly
for rw in range(MAPHEIGHT):
	for cl in range(MAPWIDTH):
		randomNumber = random.randint(0,20)
		if randomNumber == 0:
			randNumber_2 = random.randint(0,3)
			if randNumber_2 == 0:
				title = DIAMOND
			elif randNumber_2 > 0:
				title = WATER
		elif randomNumber == 1:
			title = COAL
		elif randomNumber == 2 or randomNumber == 3:
			title = WATER
		elif randomNumber >=4 and randomNumber <= 7:
			title = GRASS
		elif randomNumber >= 8 and randomNumber <= 10:
			title = LAVA
		elif randomNumber >=11 and randomNumber <= 14:
			title = ROCK
		else:
			title = DIRT
			
		tilemap[rw][cl] = title

#Main loop to 
while True:
	
	#Allows for events to be assigned 
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			print(event)
			#Allows for movement. NOT FINISHED
			if (event.key == K_RIGHT) and playerPos[0] < MAPWIDTH - 1:
				playerPos[0] += 1
			if (event.key == K_LEFT) and playerPos[0] > 0:
				playerPos[0] -= 1
			if (event.key == K_UP) and playerPos[1] > 0:
				playerPos[1] -= 1
			if (event.key == K_DOWN) and playerPos[1] < MAPHEIGHT - 1:
				playerPos[1] += 1
	
	#Places the assigned resources on the correct spaces
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
	
	#Displays the player avatar
	DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))
	#updates the total display
	pygame.display.update()
