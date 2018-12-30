import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *

gravity = .03

def noZero(value):
    if value > 0:
        return max(value,1)
    else:
        return min(value,1)

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

    def __init__(self, x, y, skin):
        pygame.sprite.Sprite.__init__(self)
        
        if skin == "white":
            self.spriteLeft, trash = load_png('TurkeyL.png')
            self.spriteRight, self.rect = load_png('TurkeyR.png')
            self.spriteKickL, trash = load_png('KickL.png')
            self.spriteKickR, trash = load_png('KickR.png')
            self.image = self.spriteLeft
        elif skin == "brown":
            self.spriteLeft, trash = load_png('TurkeyBrownL.png')
            self.spriteRight, self.rect = load_png('TurkeyBrownR.png')
            self.spriteKickL, trash = load_png('KickBrownL.png')
            self.spriteKickR, trash = load_png('KickBrownR.png')
            self.image = self.spriteLeft            
        self.step = 0
        self.speed = 1
        self.velocity = [0,0]
        self.rect = self.rect.move(x,y)
        self.jumpForce = 10

        #boolean command veriables
        self.right = False
        self.left = False
        self.onground = False
        self.faceleft = True
        self.alive = True
        #TODO initialize all veriables here

    def reset(self, x, y):
        self.image = self.spriteLeft

        self.speed = 1
        self.velocity = [0,0]
        self.rect.x = x
        self.rect.y = y
        self.jumpForce = 10

        #boolean command veriables
        self.right = False
        self.left = False
        self.onground = False
        self.faceleft = True
        self.alive = True

    def update(self, platforms, other):
        self.rect = self.rect.move(tuple(self.velocity))
        
        hitrect = self.rect.inflate(-16,-16)


        #check if colliding with platform
        for wall in platforms:
            if self.rect.colliderect(wall) == 1: 
                self.velocity[1] = 0
                if (self.rect.top - self.velocity[1] < wall.rect.top):
                    self.jumpForce = 10
                    self.onground = True
                    offset = self.rect.bottom - wall.rect.top
                    self.rect = self.rect.move(0,-offset + 1)
                else:
                    offset = self.rect.top - wall.rect.bottom
                    self.rect = self.rect.move(0,-offset)
                break
            else:
                self.velocity[1] += gravity
        

        #check if moving
        maxspeed = 6
        if not self.onground:
            maxspeed = 10

        # controled moving
        if self.right and self.step < 5:
            self.faceleft = False
            if self.velocity[0] < maxspeed:
                self.velocity[0] += self.speed
            else:
                self.movestop()
        if self.left and self.step < 10:
            self.faceleft = True
            if self.velocity[0] > - maxspeed:
                self.velocity[0] -= self.speed
            else:
                self.movestop()
        if not self.left and not self.right:
            self.movestop()

        #check if colliding with other
        if hitrect.colliderect(other) == 1:
            #self.rect.move(-self.velocity[0],-self.velocity[1])
            x = -(self.velocity[0] + other.velocity[0])
            y = -(self.velocity[1] + other.velocity[1])
            x = noZero(x)
            y = noZero(y)
            self.velocity[0] = x
            self.velocity[1] = y
            self.step = 5
            
        #kicking cooldown
        if self.step > 0:
            self.step -= 1
        else:
            if self.faceleft:
                self.image = self.spriteLeft
            else:
                self.image = self.spriteRight 

        #TODO add all update logic here

    def moveleft(self):
        self.left = True

    def moveright(self):
        self.right = True

    def movestop(self):
        dampening = .5
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
        self.step = 20 # number of tics to display the image
        if self.faceleft:
            self.image = self.spriteKickL
            hitrect = self.rect.move((-16,0))
        else:
            self.image = self.spriteKickR
            hitrect = self.rect.move((16,0))
        for turkey in turkies:
            if hitrect.colliderect(turkey) == 1:
                turkey.onground = False
                if self.faceleft:
                    turkey.hit(-10,2)
                else:
                    turkey.hit(10,2)

class Platform(pygame.sprite.Sprite):
    """Object that other objects can stand on. """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('wall.png')
        self.rect = self.rect.move(x,y)

        #TODO put any other initialization data here

    #TODO add other methods here

#TODO add items like wepons, powerups and such