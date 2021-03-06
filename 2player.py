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
    #veriables
    score1 = 0
    score2 = 0
    score3 = 0
    score4 = 0
    displayHeight = 640
    displayWidth = 1024

    #initialize enviornment screen and background
    pygame.init()
    screen = pygame.display.set_mode((displayWidth,displayHeight))
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
    player1 = Turkey(400, 400, 'white')
    player2 = Turkey(466, 400, 'brown')

    #initialize sprites
    #TODO initialize sprites
    platformSprites = pygame.sprite.RenderPlain(platforms)
    playersprites = pygame.sprite.RenderPlain(player1,player2)

    #initialize score display
    font = pygame.font.Font(None,34)

    texdis1 = "P1: " + str(score1)
    text1 = font.render(texdis1,False,(255,255,255))
    textpos1 = text1.get_rect()
    textpos1 = textpos1.move(10,10)
    screen.blit(text1,textpos1)

    texdis2 = "P2: " + str(score2)
    text2 = font.render(texdis2,False,(232,173,83))
    textpos2 = text2.get_rect()
    textpos2 = textpos2.move(200,10)
    screen.blit(text2,textpos2)

    #Blit everything to the background
    screen.blit(background,(0,0))
    platformSprites.draw(screen)
    playersprites.draw(screen)
    pygame.display.flip()

    #Initialize clock and game veriables
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
                #player1
                if event.key == K_LEFT:
                    player1.moveleft()
                if event.key == K_RIGHT:
                    player1.moveright()
                if event.key == K_UP:
                    player1.jump()
                if event.key == K_SPACE:
                    player1.kick([player2])

                #player2
                if event.key == K_a:
                    player2.moveleft()
                if event.key == K_d:
                    player2.moveright()
                if event.key == K_w:
                    player2.jump()
                if event.key == K_LSHIFT:
                    player2.kick([player1])


            #user input keyup
            elif event.type == KEYUP:
                #player1
                if event.key == K_LEFT:
                    player1.left = False
                if event.key == K_RIGHT:
                    player1.right = False
                
                #player2
                if event.key == K_a:
                    player2.left = False
                if event.key == K_d:
                    player2.right = False
                

        # check to see if anyone should die
        if player1.rect.top > displayHeight + 100:
            player1.alive = False
        if player2.rect.top > displayHeight + 100:
            player2.alive = False
    

        #blit out the objects
        screen.blit(background,player1.rect,player1.rect)
        screen.blit(background,player2.rect,player2.rect)

        # check to see if anyone won or they all lost
        # if so then reset the players
        if player1.alive and not player2.alive:
            print("Player1 Wins!")
            player1.reset(400,400)
            player2.reset(466,400)
            score1 += 1

            texdis1 = "P1: " + str(score1)
            text1 = font.render(texdis1,False,(255,255,255))
            textpos1 = text1.get_rect()
            textpos1 = textpos1.move(10,10)
            screen.blit(text1,textpos1)
            screen.blit(background,textpos1,textpos1)

        elif player2.alive and not player1.alive:
            print("Player2 Wins!")
            player1.reset(400,400)
            player2.reset(466,400)

            score2 += 1

            texdis2 = "P2: " + str(score2)
            text2 = font.render(texdis2,False,(232,173,83))
            textpos2 = text2.get_rect()
            textpos2 = textpos2.move(200,10)
            screen.blit(text2,textpos2) 
            screen.blit(background,textpos2,textpos2)
            
        elif not player1.alive and not player2.alive:
            print("Draw")
            player1.reset(400,400)
            player2.reset(466,400)

        #update moving objects
        if player1.alive:
            player1.update(platforms, [player2])
        if player2.alive:
            player2.update(platforms, [player1])

        #draw the updated locations
        playersprites.draw(screen)
        platformSprites.draw(screen)
        screen.blit(text1,textpos1)
        screen.blit(text2,textpos2)

        #TODO blite objects here

        pygame.display.flip()

if __name__ == '__main__': main()