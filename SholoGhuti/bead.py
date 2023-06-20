import pygame
from .constants import RED,WHITE,SQUARE_SIZE,GREY

class Piece:
   PADDING = 25
   OUTLINE = 2
   
   
   def __init__(self, row, col, color):
      self.row = row
      self.col = col
      self.color = color
      self.x = 0
      self.y = 0
      self.calc_pos()
      
   def calc_pos(self):
      self.x = self.col*SQUARE_SIZE + SQUARE_SIZE//2
      self.y = self.row*SQUARE_SIZE + SQUARE_SIZE//2
   
   def draw(self,win):
      radius = SQUARE_SIZE//2-self.PADDING
      pygame.draw.circle(win, GREY, (self.x,self.y), radius=radius+self.OUTLINE)
      pygame.draw.circle(win, self.color, (self.x, self.y), radius=radius)
      
   def __repr__(self):
      return str(self.color)
   
   def move(self, row, col):
      self.row = row
      self.col = col
      self.calc_pos()
   
   