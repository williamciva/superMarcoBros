import pygame
from pygame.locals import *
from libsGame import game, images
import time


## [START] Start Mapping
def mappedKeys():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        ## [START] Map Key Arrows and K_a , K_d
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT and game.marioPositionX >= 0:
                images.mm.getMovimentForAnimation('K_LEFT')
                game.marioMovimentX = - 18
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                images.mm.getMovimentForAnimation('K_RIGHT')
                game.marioMovimentX = 18
        ## [END] Map Key Arrows and K_a , K_d

        ## [START] Map Key Arrows and K_s , K_w , K_SPACE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                game.marioMovimentY = - 18
                break
            if event.type == pygame.K_s or event.key == pygame.K_DOWN:
                print('abaixa')
                break
        ## [END] Map Key Arrows and K_s , K_w , K_SPACE

        if event.type == pygame.KEYUP:
            images.mm.getMovimentForAnimation('False')
            game.marioMovimentX = 0
            game.marioMovimentY = + 18

## [END] Start Mapping