import pygame
from pygame.locals import *
from libsGame import images, screenConfig, keyMapping


marioMovimentX = int( 0 )
marioMovimentY = int( 0 )
marioPositionX = int( 118 )
marioPositionY = int( 552 )

def moveMarcos(x, y):
    if marioPositionX < 127.5:
        screenConfig.gameDisplay.blit(images.mm.animateMovimentSide(), (x, y))
    elif marioPositionX >= 127.5:
        screenConfig.gameDisplay.blit(images.mm.animateMovimentSide(), (127.5, y))


def moveCamera(marioPositionX):
    if marioPositionX <= 127.5:
        return 0
    elif marioPositionX > 127.5:
        return -(marioPositionX) + 127.5
    elif marioPositionX >= 3174:
        return -2916
