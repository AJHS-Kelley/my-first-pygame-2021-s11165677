#PyGame Collision Detection, Antonio Gonzales, January 25, 2022,9:19am, v0.3 

import pygame, sys, random
from pygame.locals import *

# Setup PyGame 
pygame.init()
mainClock = pygame.time.Clock()

#Setup the PyGame Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('CollisionDetection 2022')

# Setup colors.
BLACK = (0, 0, 0)
GREEN = (0, 255,0)
WHITE = (255, 255, 255)
