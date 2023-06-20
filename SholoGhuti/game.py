import pygame
from .constants import RED,BLUE,WHITE,GREEN, SQUARE_SIZE
from SholoGhuti.board import Board

class Game:
   def __init__(self, win):
      self._init()
      self.win = win
      
      
   def update(self):
      self.board.draw(self.win)
      self.draw_valid_moves(self.valid_moves)
      #AI SCORE COUNT
      AI_SCORE_TXT = pygame.font.SysFont('Calibri',18, pygame.font.Font.bold).render(f"AI: {16-self.board.red_left}", True, "blue")
      AI_SCORE_POS = AI_SCORE_TXT.get_rect(center=(50, 220))
      self.win.blit(AI_SCORE_TXT, AI_SCORE_POS)
      #HUMAN SCORE COUNT
      HUM_SCORE_TXT = pygame.font.SysFont('Calibri',18, pygame.font.Font.bold).render(f"YOU: {16-self.board.blue_left}", True, "red")
      HUM_SCORE_POS = HUM_SCORE_TXT.get_rect(center=(50, 250))
      self.win.blit(HUM_SCORE_TXT, HUM_SCORE_POS)
      
      if self.turn == RED:
         turntextb = pygame.font.SysFont('Calibri',18, pygame.font.Font.bold).render("Your Turn", True, "red")
         turnrectb = turntextb.get_rect(center=(50, 190))
         self.win.blit(turntextb, turnrectb)
      else:
         turntextr = pygame.font.SysFont('Calibri',18, pygame.font.Font.bold).render("AI Turn", True, "blue")
         turnrectr = turntextr.get_rect(center=(50, 190))
         self.win.blit(turntextr, turnrectr)
      pygame.display.update()
      
   def _init(self):
      self.selected = None
      self.board = Board()
      self.turn = RED
      self.valid_moves = [] #impo
      self.skipped = {}#vhul korsi
      self.cnt = 0
      
   def reset(self):
      self._init()
      
   def select(self, row, col):
      if self.selected:
         # print("result")
         # print(row,col)
         result = self._move(row, col)
         if not result:
            self.selected = None
            self.select(row,col)
      piece = self.board.get_piece(row,col)
      if piece != 0 and piece != -1 and piece.color == self.turn:
         self.selected = piece
         self.valid_moves, self.skipped, self.cnt = self.board.get_valid_moves(piece)
         return True
      return False
   
   
   def _move(self, row, col):
      piece = self.board.get_piece(row, col)
      if self.selected and piece == 0 and (row, col) in self.valid_moves:
         # print('taken')
         # print(self.selected.row)
         # print(self.selected.col)
         
         current_pos = (self.selected.row,self.selected.col)
         
         if current_pos == self.board.top:
            x,y = self.board.top
            if x == 1 and y+1 <= 7 :
               y = y+1
            else:
               if x == 1:
                  x = 0
                  y = 0
               else:
                  y = y+1
            self.board.top = (x,y)
         if current_pos == self.board.down:
            x,y = self.board.down
            if x == 11 and y+1 <= 7 :
               y = y+1
            else:
               if x == 11:
                  x = 12
                  y = 0
               else:
                  y = y+1
            self.board.down = (x,y)
            
         # print(row,col)
         
         self.board.move(self.selected, row, col)
         if(self.skipped[(row,col)] != 0):
            (r,c) = self.skipped[(row,col)]
            piece = self.board.get_piece(r,c)
            self.board.remove(piece)
         
         if(self.skipped[(row,col)] != 0):
            piece = self.board.get_piece(row,col)
            _, _, catch = self.board.get_valid_moves(piece)
            if catch == 0:
               self.change_turn()
         else:
            self.change_turn()
      else:
         return False
      return True
   
   def draw_valid_moves(self, moves):
      # print(moves)
      for move in moves:
         row = move[0]
         col = move[1]
         # print(move)
         pygame.draw.circle(self.win,GREEN, (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2),7)
   
   def change_turn(self):
      self.valid_moves = []
      if self.turn == RED:
         self.turn = BLUE
         # turntextb = pygame.font.SysFont('Calibri',18, pygame.font.Font.bold).render("BLUE", True, "blue")
         # turnrectb = turntextb.get_rect(center=(50, 190))
         # self.win.blit(turntextb, turnrectb)
         # pygame.display.update()
      else:
         self.turn = RED
         # turntextr = pygame.font.SysFont('Calibri',18, pygame.font.Font.bold).render("RED", True, "red")
         # turnrectr = turntextr.get_rect(center=(50, 190))
         # self.win.blit(turntextr, turnrectr)
         # pygame.display.update()
         
   def winner(self):
      val = self.board.winner()
      if val == None:
         if self.turn == RED:
            cntv = 0
            for piece in self.board.get_all_pieces(self.turn):
               [v_moves, skd, ct ] = self.board.get_valid_moves(piece)
               cntv += len(v_moves)
            if cntv == 0:
               print("0 RED",BLUE)
               return BLUE            
         elif self.turn == BLUE:
            cntv = 0
            for piece in self.board.get_all_pieces(self.turn):
               [v_moves, skd, ct ] = self.board.get_valid_moves(piece)
               cntv += len(v_moves)   
            if cntv == 0:
               print("0 BLUE",RED)
               return RED  
      # return self.board.winner()
      print("4",val)
      return val
   
   def get_board(self):
      return self.board
   
   def ai_move(self,board):
      self.board = board
      # print('ai moved')
      # print(board.top)
      self.change_turn()
   
      
      