import pygame

WIDTH, HEIGHT = 675, 975

x=WIDTH//2
y=HEIGHT//2

COLS ,ROWS = 9,13
SQUARE_SIZE = WIDTH//COLS

RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0, 0, 255)
GREEN = (0,255,0)
GREY = (128,128,128)
BG = pygame.image.load('background.jpg')
MNU =  pygame.image.load('gg.jpg')


PADDING = 30
OUTLINE = 2

RADIUS = 10 #SQUARE_SIZE//2-PADDING