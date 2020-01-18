import pygame
from pygame.locals import *
pygame.init()

#Display Stuff 
screenx = 1000
screeny = 900
screen = pygame.display.set_mode((screenx,screeny))
pygame.display.set_caption('Block Runner')
clock = pygame.time.Clock()
image = pygame.image.load('square.png')




#Color Stuff
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)


#Variables
x_blocky = 50
y_blocky = 750
blocky_y_move = 0
blocky_x_move = 0



#Animations
def Blocky(x_blocky, y_blocky, image):
    screen.blit(image,(x_blocky,y_blocky))

#Game Loop

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                blocky_y_move = -3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                blocky_y_move = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                blocky_y_move = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                blocky_y_move = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                blocky_x_move = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                blocky_x_move = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                blocky_x_move = -3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                blocky_x_move = 0

        if x_blocky > 870 or x_blocky < 0:
            print(' X Border')
            blocky_x_move = 0


        if y_blocky > 750 or y_blocky < 2:
            print(' Y Border')
            blocky_y_move = 0



    y_blocky += blocky_y_move
    x_blocky += blocky_x_move


    screen.fill(white)
    Blocky(x_blocky, y_blocky, image)
    pygame.display.update()
clock.tick(60)
