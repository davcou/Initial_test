import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen_size = (800, 600)
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Slipther")

apples = []


clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)

class apple:
    def __init__(self):
	self.x_pos = random.randrange(0,display_width-10)
	self.y_pos = random.randrange(0,display_height-10)
	self.size = 10
    def spawn(self, color):
	pygame.draw.rect(gameDisplay, color, [self.x_pos, self.y_pos, 10, 10])

def draw_apple(data, id1, id2):
    apples = data
    x_pos = apples[0]
    y_pos = apples[1]
    #print(x_pos)
    pygame.draw.rect(gameDisplay, green, [x_pos, y_pos, 10, 10])  
    pygame.display.update()

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

def gameLoop():

	gameExit = False
	gameOver = False
	
	apples = []

	FPS = 15
	
	lead_x = display_width/2
	lead_y = display_height/2
	lead_x_change = 0
	lead_y_change = 0
	block_size = 10	
	
	apple_pos = None	

	randAppleX = random.randrange(0,display_width-block_size)
	randAppleY = random.randrange(0,display_height-block_size)

	while not gameExit:

	    while gameOver == True:
		gameDisplay.fill(white)
		message_to_screen("Game over, press C to play again or Q to quit", red)
		pygame.display.update()
		
		for event in pygame.event.get():
		    if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
			    gameExit = True
			    gameOver = False #must be here to get out of while loop
			if event.key == pygame.K_c:
			    gameLoop()


	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
		    gameExit = True
		elif event.type == pygame.KEYDOWN:
		    if event.key == pygame.K_LEFT:
			lead_x_change = -block_size
			lead_y_change = 0
		    elif event.key == pygame.K_RIGHT:
			lead_x_change = block_size
			lead_y_change = 0
		    elif event.key == pygame.K_UP:
			lead_y_change = -block_size
			lead_x_change = 0
		    elif event.key == pygame.K_DOWN:
			lead_y_change = block_size
			lead_x_change = 0
		    elif event.key == pygame.K_a:
			apple2 = apple()
	    		apple2.spawn(blue)
			apples.append(apple2.x_pos)
			apples.append(apple2.y_pos)

	    if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
		gameOver = True
	
	    if len(apples) > 0:
		#print((apples[0]))
		#print(apples[1])
		draw_apple(apples, 0, 1)

	    lead_x += lead_x_change
	    lead_y += lead_y_change
	
	    gameDisplay.fill(white)
	    pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])
	    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])    
	    
	    #apple2 = apple()
	    #apple2.spawn(blue)


	    pygame.display.update()
	
	    clock.tick(FPS)
	
	
	pygame.quit()
	quit()

gameLoop()