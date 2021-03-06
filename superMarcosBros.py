import pygame
from pygame.locals import *

from libsGame import images, screenConfig, game, keyMapping

def startGame():
    pygame.init()


    while True:
        keyMapping.mappedKeys()     
            

        game.marioPositionX += game.marioMovimentX 
        if game.marioPositionX <= 0:
            game.marioPositionX = 0
        elif game.marioPositionX >= 10176:
            game.marioPositionX = 10176
        
        game.marioPositionY += game.marioMovimentY
        if game.marioPositionY <= 0:
            game.marioPositionY = 0
        elif game.marioPositionY >= 552:
            game.marioPositionY  = 552

        positionCameraX = game.moveCamera(game.marioPositionX)

        screenConfig.gameDisplay.blit(images.backgroundMini, (positionCameraX, 0))
        game.moveMarcos(game.marioPositionX, game.marioPositionY)
        pygame.display.update()
        screenConfig.FpsConfig.tick(17)