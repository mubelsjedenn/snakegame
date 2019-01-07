import pygame
import random
import time
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
display_height=800
display_width=600
gameDisplay = pygame.display.set_mode((display_height,display_width))
full_screen=pygame.display.toggle_fullscreen()
pygame.display.set_caption('Snakes')
clock=pygame.time.Clock()
def snake(snake_width,snakelist):
	for xny in snakelist:
		pygame.draw.rect(gameDisplay,green,[xny[0],xny[1],snake_width,snake_width])
def message_to_screen(msg,colour):
	screen_text=font.render(msg,True,colour)
	gameDisplay.blit(screen_text,[display_height/2,display_width/2])
def gameLoop():
		count=5
		snakelist=[]
		crashed=False
		lead_x=display_height/2
		lead_y=display_width/2
		lead_xchange=0
		lead_ychange=0
		food_x=random.randrange(0,display_height,10)
		food_y=random.randrange(0,display_width,10)
		snake_width=10
		food_width=30
		food_counter=0
		gameOver=False
		while not crashed:
			for XnY in snakelist[:-1]:
				if XnY == snakehead:
					gameOver=True
			while gameOver==True:
				message_to_screen('You lose, press r to play again or press q to quit.',white)
				message_to_screen('Your final score was {}'.format(food_counter),white)
				pygame.display.update()
				for event in pygame.event.get():
					if event.type==pygame.KEYDOWN:
						if event.key==pygame.K_q:
							crashed=True
							gameOver=False
						elif event.key==pygame.K_r:
							gameLoop()
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					crashed=True
				elif event.type==pygame.KEYDOWN:
					if event.key==pygame.K_a:
						lead_xchange= -snake_width
						lead_ychange=0
					elif event.key==pygame.K_d:
						lead_xchange= snake_width
						lead_ychange=0
					elif event.key==pygame.K_w:
						lead_ychange= -snake_width
						lead_xchange=0
					elif event.key==pygame.K_s:
						lead_ychange= snake_width
						lead_xchange=0
			if lead_x>=food_x and lead_x<=food_x+food_width:
				if lead_y>=food_y and lead_y<=food_y+food_width:
					food_x=random.randrange(0,display_height,food_width)
					food_y=random.randrange(0,display_width,food_width)
					count+=0.1
					food_counter+=1
			if lead_x>=display_height or lead_y>=display_width or lead_x==0 or lead_y==0:
				gameOver=True
			lead_x+= lead_xchange
			lead_y+= lead_ychange
			if len(snakelist)>food_counter:
				del snakelist[0]
			snakehead=[]
			snakehead.append(lead_x)
			snakehead.append(lead_y)
			snakelist.append(snakehead)
			gameDisplay.fill(black)
			pygame.draw.rect(gameDisplay,red,[food_x,food_y,food_width,food_width])
			snake(snake_width,snakelist)
			pygame.display.update()
			clock.tick(count)
		pygame.quit()
		quit()
gameLoop()


