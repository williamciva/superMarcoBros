import pygame
from pygame.locals import *
from libsGame import game


icon = pygame.image.load('assets/superMarcosBrosIcoPng.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Super Marcos Bros')


backgroundMini = pygame.image.load('assets/world/word1x1_232.png')
backgroundMini = pygame.transform.scale(backgroundMini, (10176, 696))


class movimentMario(object):
    sideArrows = False
    # Mario Images Import *
    # Mario Moviment Animation
    mario1 = pygame.image.load('assets/marcos/mario1.png')
    mario1 = pygame.transform.scale(mario1, (45, 51))
    mario2 = pygame.image.load('assets/marcos/mario2.png')
    mario2 = pygame.transform.scale(mario2, (45, 51))
    mario3 = pygame.image.load('assets/marcos/mario3.png')
    mario3 = pygame.transform.scale(mario3, (45, 51))
    mario4 = pygame.image.load('assets/marcos/mario4.png')
    mario4 = pygame.transform.scale(mario4, (45, 51))
    animation = mario1

    def getMovimentForAnimation(self,keyDown):
        if keyDown == 'K_LEFT' or keyDown == 'K_RIGHT':  
            self.sideArrows = True
        else:
            self.sideArrows = False 

    def animateMovimentSide(self):

        if self.sideArrows == True:
            if self.animation == self.mario1:
                self.animation = self.mario2
                return self.animation

            elif self.animation == self.mario2:
                self.animation = self.mario3
                return self.animation

            elif self.animation == self.mario3:
                self.animation = self.mario4
                return self.animation

            elif self.animation == self.mario4:
                self.animation = self.mario1
                return self.animation

        elif self.sideArrows == False:
            return self.mario1

mm = movimentMario()