pip install pygame
import random
import sys
import pygame
from pygame.locals import *

# creating the map:
window_width = 600
window_height = 550
window = pygame.display.set_mode((window_width, window_height))
elevation = window_height *.75
game_images =
framepersecond = 30
pipe_image = 'images/pipe.png'
background_image = 'images/background.jpg'
birdplayer_image = '/images/bird.png'
sealevel_image = '/images/base.jfif'

#creating main menu
#when app starts:
if __name__ == "main":
  pygame.init()
  framepersecond_clock = pygame.time.clock()
  #menu display
  pygame.display.set_caption("Tyler's Flappy Bird Remake")           
  game_images("scoreimages") = 
    pygame.image.load('images/1.png').convert_alpha(),
    pygame.image.load('images/2.png').convert_alpha(),
    pygame.image.load('images/3.png').convert_alpha(),
    pygame.image.load('images/4.png').convert_alpha(),
    pygame.image.load('images/5.png').convert_alpha(),
    pygame.image.load('images/6.png').convert_alpha(),
    pygame.image.load('images/7.png').convert_alpha(),
    pygame.image.load('images/8.png').convert_alpha(),
    pygame.image.load('images/9.png').convert_alpha(),
    pygame.image.load('images/0.png').convert_alpha(),
    
game_images ('flappy bird') = pygame.image.load(birdplayer_image).convert_alpha()
game_images ('sea_level') = pygame.image.load(sealevel_image).convert_alpha()
game_images ('background') = pygame.image.load(background_image).convert_alpha()
game_images ('pipeimage') = pygame.transform.rotate(pygame.image.load(pipeimage).convert_alpha(),180),pygame.image.load(pipeimage).convert_alpha())
print("Welcome back to Flappy Bird!")
print("Press enter to start the game.")
#establishing the bird position + world loop
horizontal = int(window_width/4.75)
vertical = int((window_height - game_images['flappybird'].get_height())/2
ground = 0
      while True:
        for event in pygame.event.get():
            #close game function
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit() 
#start game with enter or space bar
        elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_ENTER):flappygame()
#game wont start if player doesnt press anything
        else:
        window.blit(game_images['background'], (0,0))
        window.blit(game_images['flappybird'], (horizontal, vertical))  
        window.blit(game_images['sealevel'], (ground, elevation))
        #refresh
        pygame.display.update()
        #show fps
        framepersecond_clock.tick(framepersecond)



