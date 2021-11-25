import pygame
from pygame.locals import *


class movimentMario(object):
    sideArrows = False
    # marco Images Import *
    # Marco Moviment animationMarco
    marco1 = pygame.image.load('assets/marcos/marco1.png')
    marco1 = pygame.transform.scale(marco1, (45, 51))
    marco2 = pygame.image.load('assets/marcos/marco2.png')
    marco2 = pygame.transform.scale(marco2, (45, 51))
    marco3 = pygame.image.load('assets/marcos/marco3.png')
    marco3 = pygame.transform.scale(marco3, (45, 51))
    marco4 = pygame.image.load('assets/marcos/marco4.png')
    marco4 = pygame.transform.scale(marco4, (45, 51))
    animationMarco = marco1

    jumpMarco = pygame.image.load('assets/marcos/marco_jump.png')
    jumpMarco = pygame.transform.scale(jumpMarco, (45, 51))


    def getMovimentForAnimationMarco(self,keyDown):
        if keyDown == 'K_LEFT' or keyDown == 'K_RIGHT':  
            self.sideArrows = True
        else:
            self.sideArrows = False 

    def animateMovimentSide(self):

        if self.sideArrows == True:
            if self.animationMarco == self.marco1:
                self.animationMarco = self.marco2
                return self.animationMarco

            elif self.animationMarco == self.marco2:
                self.animationMarco = self.marco3
                return self.animationMarco

            elif self.animationMarco == self.marco3:
                self.animationMarco = self.marco4
                return self.animationMarco

            elif self.animationMarco == self.marco4:
                self.animationMarco = self.marco1
                return self.animationMarco

        elif self.sideArrows == False:
            return self.marco1



    def getJumpForAnimationMarco(self,keyDown):
        if keyDown == 'K_UP':  
            self.upArrows = True
        else:
            self.upArrows = False 

    def animateMovimentUp(self):
        return self.jumpMarco

mm = movimentMario()