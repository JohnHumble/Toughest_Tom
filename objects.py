import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *

gravity = .03

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
        
        self.spriteLeft, trash = load_png('TurkeyL.png')
        self.spriteRight, self.rect = load_png('TurkeyR.png')
        self.image = self.spriteLeft

        self.speed = 1
        self.velocity = [0,0]
        self.rect = self.rect.move(x,y)
        self.jumpForce = 10

        #boolean command veriables
        self.right = False
        self.left = False
        self.onground = False
        self.faceleft = True
        #TODO initialize all veriables here

    def update(self, platforms):
        self.rect = self.rect.move(tuple(self.velocity))
        
        #check if falling
        for wall in platforms:
            if self.rect.colliderect(wall) == 1: 
                self.velocity[1] = 0
                self.jumpForce = 10
                self.onground = True
                if (self.rect.top < wall.rect.top):
                    offset = self.rect.bottom - wall.rect.top
                    self.rect = self.rect.move(0,-offset + 1)
                break
            else:
                self.velocity[1] += gravity
        
        #check if moving
        maxspeed = 6
        if not self.onground:
            maxspeed = 10
        if self.right:
            self.faceleft = False
            self.image = self.spriteRight
            if self.velocity[0] < maxspeed:
                self.velocity[0] += self.speed
            else:
                self.movestop()
        if self.left:
            self.faceleft = True
            self.image = self.spriteLeft
            if self.velocity[0] > - maxspeed:
                self.velocity[0] -= self.speed
            else:
                self.movestop()
        if not self.left and not self.right:
            self.movestop()
        #TODO add all update logic here

    def moveleft(self):
        self.left = True

    def moveright(self):
        self.right = True

    def movestop(self):
        dampening = 1
        if self.onground:
            if self.velocity[0] > dampening:
                self.velocity[0] -= dampening
            elif self.velocity[0] < -dampening:
                self.velocity[0] += dampening
            else:
                self.velocity[0] = 0

    def jump(self):
        if self.jumpForce > 0:
            self.velocity[1] = -self.jumpForce
            self.jumpForce -= 2
            self.onground = False

    #method to handle getting hit by something
    def hit(self, power, up):
        self.velocity[0] += power
        self.velocity[1] -= up

    def kick(self,turkies):
        for turkey in turkies:
            if self.rect.colliderect(turkey) == 1:
                turkey.onground = False
                if self.faceleft:
                    turkey.hit(-5,2)
                else:
                    turkey.hit(5,2)

class Platform(pygame.sprite.Sprite):
    """Object that other objects can stand on. """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('wall.png')
        self.rect = self.rect.move(x,y)

        #TODO put any other initialization data here

    #TODO add other methods here

#TODO add items like wepons, powerups and such