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
#create pipe and make them randomized
def createpipe():
        offset = window_height/3
        pipeheight = game_images['pipeimage'][0].get_height()
        y2 = offset + random.randrange(0, int(window_height - game_images['sea_level'].get_height() - 1.1 * offset))
        pipex = window_width + 10
        y1 = pipeheight - y2 + offset
        #top pipe then bottom pipe  
        pipe = [{'x': pipex, 'y': -y1}, {'x': pipex, 'y': y2]  
        return pipe  
#creating game over function
#is the bird over sealevel
def isGameOver(horizontal, vertical, up_pipes, down_pipes):
  if vertical > elevation - 25 or vertical < 0:
    return true
#did bird hit top pipe
for pipe in up_pipes:
  pipeHeight = game_images['pipeimage'][0].get_height()
  if(vertical < pipeheight + pipe['y']
     and abs(horizontal - pipe['x']) < game_images['pipeimage'][0].get_width()
       return true
 #did bird hit bottom pipe
 for pipe in down_pipes:
   if (vertical + game_images['flappybird'].get_height() > pipe['y'])
   and abs(horizontal - pipe['x']) < game_images ['pipe_image'][0].get_width():
     return true
  return false
def flappygame(): 
    your_score = 0
    horizontal = int(window_width/5) 
    vertical = int(window_width/2) 
    ground = 0
    mytempheight = 100
    #making sure their are two pipes each window 
    first_pipe = createPipe() 
    second_pipe = createPipe() 
    #list of lower pipes 
    down_pipes = [ 
        {'x': window_width+300-mytempheight, 
         'y': first_pipe[1]['y']}, 
        {'x': window_width+300-mytempheight+(window_width/2), 
         'y': second_pipe[1]['y']},]
    #list of upper pipes  
    up_pipes = [ 
        {'x': window_width+300-mytempheight, 
         'y': first_pipe[0]['y']}, 
        {'x': window_width+200-mytempheight+(window_width/2), 
         'y': second_pipe[0]['y']},]
  pipeVelX = -4 #pipe velocity along x 
    bird_velocity_y = -9  # bird velocity 
    bird_Max_Vel_Y = 10   
    bird_Min_Vel_Y = -8
    birdAccY = 1
     #velocity while flapping 
    bird_flap_velocity = -8
    #it is true only if the bird is flapping 
    bird_flapped = False  
    while True: 
        #dealing with the key pressing events 
        for event in pygame.event.get(): 
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE): 
                pygame.quit() 
                sys.exit() 
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP): 
                if vertical > 0: 
                    bird_velocity_y = bird_flap_velocity 
                    bird_flapped = True
                  


        
