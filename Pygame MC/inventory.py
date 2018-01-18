import pygame, sys, random
from pygame.locals import * 

#constants representing colors
BLACK = (0,0,0)
BROWN = (153,76,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

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
	ROCK : pygame.image.load('Pictures/the_magic.jpg'),
	DIAMOND : pygame.image.load('Pictures/diamond.png')
	}

#Creates a list containing each resource to be randomly choses and assigned a point on the display
resources = [DIRT, GRASS, WATER, COAL, LAVA, ROCK, DIAMOND]
tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPWIDTH)]

inventory = {
	DIRT : 0,
	GRASS : 0,
	WATER : 0,
	COAL : 0,
	LAVA : 0,
	ROCK : 0,
	DIAMOND : 0
	}
#Begin program, set display size, and label the window caption
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE + 50))
pygame.display.set_caption('Resetti\'s Adventure!')

#Loads the player into the program
PLAYER = pygame.image.load('Pictures/Resetti_ingame.png').convert_alpha()
playerPos = [0,0]

#add a font for our inventory
INVFONT = pygame.font.Font('Fonts/FreeSansBold.ttf', 18)

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
		#Allows for movement.
			if (event.key == K_RIGHT) and playerPos[0] < MAPWIDTH - 1:
				playerPos[0] += 1
			if (event.key == K_LEFT) and playerPos[0] > 0:
				playerPos[0] -= 1
			if (event.key == K_UP) and playerPos[1] > 0:
				playerPos[1] -= 1
			if (event.key == K_DOWN) and playerPos[1] < MAPHEIGHT - 1:
				playerPos[1] += 1
			
		#Allows to check inventory
			if event.key == K_SPACE:
			#what resource is the player standing on?
				currentTile = tilemap[playerPos[1]][playerPos[0]]
			#player now has 1 more of this resource
				inventory[currentTile] +=1
			#the player is now standing on dirt
				tilemap[playerPos[1]][playerPos[0]] = DIRT
				print(inventory)
				
		#placing dirt
			if (event.key == K_1):
			#get the tile to swap with the dirt
				currentTile = tilemap[playerPos[1]][playerPos[0]]
			#if we have any dirt in our inventory
				if inventory[DIRT] > 0:
				#remove one dirt and place it
					inventory[DIRT] -= 1
					tilemap[playerPos[1]][playerPos[0]] = DIRT
				#swap the item that was there before
					inventory[currentTile] += 1
					
			#placing grass
			if (event.key == K_2):
			#get the tile to swap with the grass
				currentTile = tilemap[playerPos[1]][playerPos[0]]
			#if we have any grass in our inventory
				if inventory[GRASS] > 0:
				#remove one grass and place it
					inventory[GRASS] -= 1
					tilemap[playerPos[1]][playerPos[0]] = GRASS
				#swap the item that was there before
					inventory[currentTile] += 1
					
			#placing water
			if (event.key == K_3):
			#get the tile to swap with the water
				currentTile = tilemap[playerPos[1]][playerPos[0]]
			#if we have any water in our inventory
				if inventory[WATER] > 0:
				#remove one water and place it
					inventory[WATER] -= 1
					tilemap[playerPos[1]][playerPos[0]] = WATER
				#swap the item that was there before
					inventory[currentTile] += 1
					
			#placing COAL
			if (event.key == K_4):
			#get the tile to swap with the coal
				currentTile = tilemap[playerPos[1]][playerPos[0]]
			#if we have any dirt in our inventory
				if inventory[COAL] > 0:
				#remove one coal and place it
					inventory[COAL] -= 1
					tilemap[playerPos[1]][playerPos[0]] = COAL
				#swap the item that was there before
					inventory[currentTile] += 1
					
			#placing LAVA
			if (event.key == K_5):
			#get the tile to swap with the dirt
				currentTile = tilemap[playerPos[1]][playerPos[0]]
			#if we have any lava in our inventory
				if inventory[LAVA] > 0:
				#remove one lava and place it
					inventory[LAVA] -= 1
					tilemap[playerPos[1]][playerPos[0]] = LAVA
				#swap the item that was there before
					inventory[currentTile] += 1	
					
		#placing DIAMOND 
			if (event.key == K_7):
				#KEY SET TO 7^^^ NOT 6
			#get the tile to swap with the diamond
				currentTile = tilemap[playerPos[1]][playerPos[0]]
			#if we have any diamond in our inventory
				if inventory[DIAMOND] > 0:
				#remove one diamond and place it
					inventory[DIAMOND] -= 1
					tilemap[playerPos[1]][playerPos[0]] = DIAMOND
				#swap the item that was there before
					inventory[currentTile] += 1
					
		#placing ROCK
			if (event.key == K_6):
				#KEY SET TO 6^^^ NOT 7
			#get the tile to swap with the rock
				currentTile = tilemap[playerPos[1]][playerPos[0]]
			#if we have any rock in our inventory
				if inventory[ROCK] > 0:
				#remove= one rock and place it
					inventory[ROCK] -= 1
					tilemap[playerPos[1]][playerPos[0]] = ROCK
				#swap the item that was there before
					inventory[currentTile] += 1
					
#Places the assigned resources on the correct spaces
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
	
#Displays the inventory, starting 10 pixels in
	placePosition = 10
	for item in resources:
		#add the image
		DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 30
		#add the text showing ther amount in the inventory
		textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
		DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 50
		
#Displays the player avatar
	DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))
#updates the total display
	pygame.display.update()
