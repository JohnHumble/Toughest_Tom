#impot libraries

import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals improt *

#put files here to import


# function to load files here

# object classes
class Turkey(pygame.sprite.Sprite):
    """Player Object, Can move left, right and jump some number of times
    controled """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #TODO initialize all veriables here

    def update(self):
        #TODO add all update logic here

    def moveleft(self):
        #TODO make Turkey move left

    def moveright(self):
        #TODO make Turkey move right

    def jump(self):
        #TODO make turkey move up some
        #TODO only allow this action some number of times after leaving the ground

class Platform(pygame.sprite.Sprite):
    """Object that other objects can stand on. """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #TODO put any other initialization data here

#TODO add items like wepons, powerups and such

def main ():
    #initialize enviornment screen and background
    pygame.init()
    screen = pygame.display.set_mode((1024,800))
    pygame.display.set_caption('Toughest Tom')
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((135,206,235)) #sky blue background

    #initialize the background (use an algoritm to create platfoms and such)
    #TODO create terriain

    #initialize players 
    #TODO make this changeable in a menue

    #initialize sprites
    #TODO initialize sprites

    #Blit everything to the background
    screen.blit(background,(0,0))
    pygame.flip()

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
            #TODO check user input and move acordingly KeyDOwn, KeyUP

    #update objects
    #TODO update all objects that need it

    #blit everything to the screen
    #TODO blite objects here

    pygame.display.flip()

if __name__ == '__main__': main()