import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *

gravity = .1

def load_png(name):
    # load image and return image object
    fullname = os.path.join('data',name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print('Cannot load image:', fullname)
        raise 
    return image, image.get_rect()

class Turkey(pygame.sprite.Sprite):
    """Player Object, Can move left, right and jump some number of times
    controled """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('Turkey.png')
        self.speed = 3
        self.velocity = [0,0]
        self.state = "rest"
        self.rect = self.rect.move(x,y)
        #TODO initialize all veriables here

    def update(self, platforms):
        #check if falling
        for wall in platforms:
            if self.rect.colliderect(wall) == 1 and not self.state == "jumping":
                self.velocity[1] = 0
                if (self.rect.top < wall.rect.top):
                    offset = self.rect.bottom - wall.rect.top
                    self.rect = self.rect.move(0,-offset + 1)
                break
            else:
                self.velocity[1] += gravity
                
        self.rect = self.rect.move(tuple(self.velocity))
        #TODO add all update logic here

    def moveleft(self):
        self.velocity[0] = -self.speed
        self.state = 'moving'

    def moveright(self):
        self.velocity[0] = self.speed
        self.state = 'moving'

    def movestop(self):
        self.velocity[0] = 0

    def jump(self):
        #TODO make turkey move up some
        #TODO only allow this action some number of times after leaving the ground

        self.state = "jumping"

class Platform(pygame.sprite.Sprite):
    """Object that other objects can stand on. """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('wall.png')
        self.rect = self.rect.move(x,y)

        #TODO put any other initialization data here

    #TODO add other methods here

#TODO add items like wepons, powerups and such