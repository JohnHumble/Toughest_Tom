#impot libraries

import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *

from objects import *

#put files here to import


# function to load files here
# function to load in an image

def main ():
    #initialize enviornment screen and background
    pygame.init()
    screen = pygame.display.set_mode((1024,640))
    pygame.display.set_caption('Toughest Tom')
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((135,206,235)) #sky blue background

    #initialize the background (use an algoritm to create platfoms and such)
    #TODO create terriain
    numPlat = 20
    platforms = pygame.sprite.Group()
    for x in range(0,numPlat):
        platform = Platform(x * 32 + 200,500)
        platforms.add(platform)

    #initialize players 
    #TODO make this changeable in a menue
    player1 = Turkey(400,400)

    #initialize sprites
    #TODO initialize sprites
    platformSprites = pygame.sprite.RenderPlain(platforms)
    playersprites = pygame.sprite.RenderPlain(player1)

    #Blit everything to the background
    screen.blit(background,(0,0))
    platformSprites.draw(screen)
    playersprites.draw(screen)
    pygame.display.flip()

    #Initialize clock
    clock = pygame.time.Clock()

    #event loop
    while 1:
        #cap the framerate
        clock.tick(60)

        # event loop check user input and update
        for event in pygame.event.get():
            if event.type == QUIT:
                return
      
            #user input keydown
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    player1.moveleft()
                elif event.key == K_RIGHT:
                    player1.moveright()

            #user input keyup
            elif event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    player1.movestop()
                    player1.state = "rest"
            #TODO check user input and move acordingly KeyDOwn, KeyUP

        #blit out the objects
        screen.blit(background,player1.rect,player1.rect)

        #update moving objects
        player1.update(platforms)
        #TODO update all objects that need it

        #draw the updated locations
        playersprites.draw(screen)
        platformSprites.draw(screen)
        #TODO blite objects here

        pygame.display.flip()

if __name__ == '__main__': main()