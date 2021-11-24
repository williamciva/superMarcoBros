import pygame
from pygame.locals import *

pygame.init()
width = 800
height = 800
displaySet = (width,height)
gameDisplay = pygame.display.set_mode(displaySet, pygame.RESIZABLE)
FpsConfig = pygame.time.Clock()

pygame.display.set_caption('Super Marcos Bros')
icon = pygame.image.load('assets/superMarcosBrosIcoPng.png')
pygame.display.set_icon(icon)

while True:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()



    pygame.display.update()
    FpsConfig.tick(60)