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
    player3 = Turkey(532, 400, 'purple')
    player4 = Turkey(600, 400, 'red')

    #initialize sprites
    #TODO initialize sprites
    platformSprites = pygame.sprite.RenderPlain(platforms)
    playersprites = pygame.sprite.RenderPlain(player1,player2, player3, player4)

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

    texdis3 = "P3: " + str(score3)
    text3 = font.render(texdis3,False,(93,79,113))
    textpos3 = text3.get_rect()
    textpos3 = textpos3.move(400,10)
    screen.blit(text3,textpos2)

    texdis4 = "P4: " + str(score4)
    text4 = font.render(texdis4,False,(254,82,82))
    textpos4 = text4.get_rect()
    textpos4 = textpos4.move(600,10)
    screen.blit(text4,textpos2)

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
                    player1.kick([player2,player3,player4])

                #player2
                if event.key == K_a:
                    player2.moveleft()
                if event.key == K_d:
                    player2.moveright()
                if event.key == K_w:
                    player2.jump()
                if event.key == K_LSHIFT:
                    player2.kick([player1,player3,player4])

                #player3
                if event.key == K_g:
                    player3.moveleft()
                if event.key == K_j:
                    player3.moveright()
                if event.key == K_y:
                    player3.jump()
                if event.key == K_LCTRL:
                    player3.kick([player1,player2,player4])

                #player4
                if event.key == K_l:
                    player4.moveleft()
                if event.key == K_QUOTE:
                    player4.moveright()
                if event.key == K_p:
                    player4.jump()
                if event.key == K_RSHIFT:
                    player4.kick([player1,player2,player3])

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
                
                #player3
                if event.key == K_g:
                    player3.left = False
                if event.key == K_j:
                    player3.right = False

                #player4
                if event.key == K_l:
                    player4.left = False
                if event.key == K_QUOTE:
                    player4.right = False

            #TODO check user input and move acordingly KeyDOwn, KeyUP

        # check to see if anyone should die
        if player1.rect.top > displayHeight + 100:
            player1.alive = False
        if player2.rect.top > displayHeight + 100:
            player2.alive = False
        if player3.rect.top > displayHeight + 100:
            player3.alive = False
        if player4.rect.top > displayHeight + 100:
            player4.alive = False

        #blit out the objects
        screen.blit(background,player1.rect,player1.rect)
        screen.blit(background,player2.rect,player2.rect)
        screen.blit(background,player3.rect,player3.rect)
        screen.blit(background,player4.rect,player4.rect)

        # check to see if anyone won or they all lost
        # if so then reset the players
        if player1.alive and not player2.alive and not player3.alive and not player4.alive:
            print("Player1 Wins!")
            player1.reset(400,400)
            player2.reset(466,400)
            player3.reset(532, 400)
            player4.reset(600, 400)
            score1 += 1

            texdis1 = "P1: " + str(score1)
            text1 = font.render(texdis1,False,(255,255,255))
            textpos1 = text1.get_rect()
            textpos1 = textpos1.move(10,10)
            screen.blit(text1,textpos1)
            screen.blit(background,textpos1,textpos1)

        elif player2.alive and not player1.alive and not player3.alive and not player4.alive:
            print("Player2 Wins!")
            player1.reset(400,400)
            player2.reset(466,400)
            player3.reset(532, 400)
            player4.reset(600, 400)
            score2 += 1

            texdis2 = "P2: " + str(score2)
            text2 = font.render(texdis2,False,(232,173,83))
            textpos2 = text2.get_rect()
            textpos2 = textpos2.move(200,10)
            screen.blit(text2,textpos2) 
            screen.blit(background,textpos2,textpos2)

        elif player3.alive and not player1.alive and not player2.alive and not player4.alive:
            print("Player3 Wins!")
            player1.reset(400,400)
            player2.reset(466,400)
            player3.reset(532, 400)
            player4.reset(600, 400)
            score3 += 1

            texdis3 = "P3: " + str(score3)
            text3 = font.render(texdis3,False,(93,79,113))
            textpos3 = text3.get_rect()
            textpos3 = textpos3.move(400,10)
            screen.blit(text3,textpos2)
            screen.blit(background,textpos3,textpos3)

        elif player4.alive and not player1.alive and not player2.alive and not player3.alive:
            print("Player4 Wins!")
            player1.reset(400,400)
            player2.reset(466,400)
            player3.reset(532, 400)
            player4.reset(600, 400)
            score4 += 1

            texdis4 = "P4: " + str(score4)
            text4 = font.render(texdis4,False,(254,82,82))
            textpos4 = text4.get_rect()
            textpos4 = textpos4.move(600,10)
            screen.blit(text4,textpos2)          
            screen.blit(background,textpos4,textpos4)

        elif not player1.alive and not player2.alive and not player3.alive and not player4.alive:
            print("Draw")
            player1.reset(400,400)
            player2.reset(466,400)
            player3.reset(532, 400)
            player4.reset(600, 400)

        #update moving objects
        if player1.alive:
            player1.update(platforms, [player2,player3,player4])
        if player2.alive:
            player2.update(platforms, [player1,player3,player4])
        if player3.alive:
            player3.update(platforms, [player1,player2,player4])
        if player4.alive:
            player4.update(platforms, [player1,player2,player3])
        #TODO update all objects that need it

        #draw the updated locations
        playersprites.draw(screen)
        platformSprites.draw(screen)
        screen.blit(text1,textpos1)
        screen.blit(text2,textpos2)
        screen.blit(text3,textpos3)
        screen.blit(text4,textpos4)

        #TODO blite objects here

        pygame.display.flip()

if __name__ == '__main__': main()