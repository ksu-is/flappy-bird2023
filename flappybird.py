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
game_images ('sealevel') = pygame.image.load(sealevel_image).convert_alpha()
game_images ('background') = pygame.image.load(background_image).convert_alpha()
game_images ('pipeimage') = pygame.transform.rotate(pygame.image.load(pipeimage).convert_alpha(),180),pygame.image.load(pipeimage).convert_alpha())
print("Welcome back to Flappy Bird!")
print("Press enter to start the game.")



