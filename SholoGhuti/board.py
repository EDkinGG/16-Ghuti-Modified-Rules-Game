import pygame
from .bead import Piece
from .constants import BLACK, BLUE, COLS, RADIUS, RED, ROWS, SQUARE_SIZE, WHITE, GREY, GREEN, BG


class Board:
   def __init__(self):
      self.board = []
      self.selected_piece = None
      self.red_left = self.blue_left = 16
      # self.background = pygame.image.load('background.jpg')
      self.top = (1,1)
      self.down = (11,1)
      
      invalid_list = [(1,0),(1,8),(2,0),(2,1),(2,3),(2,5),(2,7),(2,8),(3,0),(3,1),(3,2),(3,6),(3,7),(3,8),(4,1),(4,7),(5,0),(5,8),(7,0),(7,8),(8,1),(8,7),(9,0),(9,1),(9,2),(9,6),(9,7),(9,8),(10,0),(10,1),(10,3),(10,5),(10,7),(10,8),(11,0),(11,8)]
      
      self.st_top = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                     (1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)]
      self.st_down = [(12,0),(12,1),(12,2),(12,3),(12,4),(12,5),(12,6),(12,7),(12,8),
                  (11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7)]
      
      default1 = [(2,2),(2,4),(2,6),
                      (3,3),(3,4),(3,5),
                      (4,0),(4,2),(4,3),(4,4),(4,5),(4,6),(4,8),
                      (5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),
                      (6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),
                      (7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),
                      (8,0),(8,2),(8,3),(8,4),(8,5),(8,6),(8,8),
                      (9,3),(9,4),(9,5),
                      (10,2),(10,4),(10,6)
                      ]
      default2 = [(2,2),(2,4),(2,6),
                  (3,3),(3,4),(3,5),
                  (4,0),(4,2),(4,3),(4,4),(4,5),(4,6),(4,8),
                  (5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),
                  (6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),
                  (7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),
                  (8,0),(8,2),(8,3),(8,4),(8,5),(8,6),(8,8),
                  (9,3),(9,4),(9,5),
                  (10,2),(10,4),(10,6)
                  ]
      # default1 = [(2,2),(2,4),(2,6),
      #                 (3,3),(3,4),(3,5),
      #                 (4,0),(4,2),(4,3),(4,4),(4,5),(4,6),(4,8),
      #                 (5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),
      #                 (6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8)
      #                 ]
      # default2 = [(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),
      #             (7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),
      #             (8,0),(8,2),(8,3),(8,4),(8,5),(8,6),(8,8),
      #             (9,3),(9,4),(9,5),
      #             (10,2),(10,4),(10,6)
      #             ]
      # default1 = [(2,2),(2,4),(2,6),
      #             (3,3),(3,4),(3,5),
      #             ]
      # default2 = [(9,3),(9,4),(9,5),
      #             (10,2),(10,4),(10,6)
      #             ]
      
      self.valids = {
         (0,0):default1,
         (0,1):default1,
         (0,2):default1,
         (0,3):default1,
         (0,4):default1,
         (0,5):default1,
         (0,6):default1,
         (0,7):default1,
         (0,8):default1,
         (1,1):default1,
         (1,2):default1,
         (1,3):default1,
         (1,4):default1,
         (1,5):default1,
         (1,6):default1,
         (1,7):default1,
         (2,2):[(2,4),(3,3)],
         (2,4):[(2,2),(2,6),(3,4)],
         (2,6):[(2,4),(3,5)],
         (3,3):[(2,2),(3,4),(4,4)],
         (3,4):[(3,3),(3,5),(4,4),(2,4)],
         (3,5):[(3,4),(2,6),(4,4)],
         (4,0):[(5,1),(6,0)],
         (4,2):[(4,3),(5,3),(5,2)],
         (4,3):[(4,2),(4,4),(5,3)],
         (4,4):[(3,3),(3,4),(3,5),(4,3),(5,3),(5,4),(5,5),(4,5)],
         (4,5):[(4,4),(4,6),(5,5)],
         (4,6):[(4,5),(5,5),(5,6)],
         (4,8):[(5,7),(6,8)],
         (5,1):[(4,0),(6,2),(6,1)],
         (5,2):[(4,2),(5,3),(6,2)],
         (5,3):[(4,2),(4,3),(4,4),(5,2),(5,4),(6,2),(6,3),(6,4)],
         (5,4):[(4,4),(5,3),(5,5),(6,4)],
         (5,5):[(4,4),(4,5),(4,6),(5,4),(5,6),(6,4),(6,5),(6,6)],
         (5,6):[(4,6),(5,5),(6,6)],
         (5,7):[(6,6),(6,7),(4,8)],
         (6,0):[(4,0),(6,1),(8,0)],
         (6,1):[(6,0),(5,1),(7,1),(6,2)],
         (6,2):[(5,1),(5,2),(5,3),(6,1),(6,3),(7,1),(7,2),(7,3)],
         (6,3):[(5,3),(6,2),(6,4),(7,3)],
         (6,4):[(5,3),(5,4),(5,5),(6,3),(6,5),(7,3),(7,4),(7,5)],
         (6,5):[(5,5),(6,4),(6,6),(7,5)],
         (6,6):[(5,5),(5,6),(5,7),(6,5),(6,7),(7,5),(7,6),(7,7)],
         (6,7):[(5,7),(6,6),(6,8),(7,7)],
         (6,8):[(6,7),(4,8),(8,8)],
         (7,1):[(6,1),(8,0),(6,2)],
         (7,2):[(6,2),(7,3),(8,2)],
         (7,3):[(6,2),(6,3),(6,4),(7,2),(7,4),(8,2),(8,3),(8,4)],
         (7,4):[(6,4),(7,3),(7,5),(8,4)],
         (7,5):[(6,4),(6,5),(6,6),(7,4),(7,6),(8,4),(8,5),(8,6)],
         (7,6):[(6,6),(7,5),(8,6)],
         (7,7):[(6,6),(6,7),(8,8)],
         (8,0):[(6,0),(7,1)],
         (8,2):[(7,2),(7,3),(8,3)],
         (8,3):[(8,2),(8,4),(7,3)],
         (8,4):[(8,3),(7,3),(7,4),(7,5),(8,5),(9,3),(9,4),(9,5)],
         (8,5):[(8,4),(8,6),(7,5)],
         (8,6):[(8,5),(7,5),(7,6)],
         (8,8):[(7,7),(6,8)],
         (9,3):[(8,4),(9,4),(10,2)],
         (9,4):[(8,4),(9,3),(9,5),(10,4)],
         (9,5):[(9,4),(8,4),(10,6)],
         (10,2):[(9,3),(10,4)],
         (10,4):[(9,4),(10,2),(10,6)],
         (10,6):[(9,5),(10,4)],
         (11,1):default2,
         (11,2):default2,
         (11,3):default2,
         (11,4):default2,
         (11,5):default2,
         (11,6):default2,
         (11,7):default2,
         (12,0):default2,
         (12,1):default2,
         (12,2):default2,
         (12,3):default2,
         (12,4):default2,
         (12,5):default2,
         (12,6):default2,
         (12,7):default2,
         (12,8):default2
      }
      self.create_board()
      
      
      
   def draw_line(self,point1,point2,win):
      y1,x1 = point1
      y2,x2 = point2
      pygame.draw.line(win, BLACK, (x1*SQUARE_SIZE + SQUARE_SIZE//2 , y1*SQUARE_SIZE + SQUARE_SIZE//2), (x2*SQUARE_SIZE + SQUARE_SIZE//2, y2*SQUARE_SIZE + SQUARE_SIZE//2),3)
         
   def draw_points(self,win):
      PADDING = 15
      OUTLINE = 2
      # win.fill(WHITE)
      win.blit(BG,(0,0))
      point_list = []
      point_list1 = [(0,0),(1,1),(2,2),(2,4),(2,6),(3,3),(4,0),(4,2),(4,3),(4,5),(4,6),(4,8),(5,1),(5,2),(5,7),(6,0),(7,2),(8,2),(9,3),(10,2),(11,1),(12,0)]
      
      point_list2 = [
         [(0,8)],
         [(1,7)],
         [(8,8),(2,6)],
         [(10,4)],
         [(8,0)],
         [(3,5)],
         [(8,0),(10,6)],
         [(4,6),(8,2),(8,6)],
         [(8,3)],
         [(8,5)],
         [(8,6),(8,2)],
         [(8,8,),(10,2)],
         [(7,1)],
         [(5,6)],
         [(7,7)],
         [(6,8)],
         [(7,6)],
         [(8,6)],
         [(9,5)],
         [(10,6)],
         [(11,7)],
         [(12,8)]
      ]
      
      blank_list = [(1,0),(1,8),(2,0),(2,1),(2,3),(2,5),(2,7),(2,8),(3,0),(3,1),(3,2),(3,6),(3,7),(3,8),(4,1),(4,7),(5,0),(5,8),(7,0),(7,8),(8,1),(8,7),(9,0),(9,1),(9,2),(9,6),(9,7),(9,8),(10,0),(10,1),(10,3),(10,5),(10,7),(10,8),(11,0),(11,8)]
      
      
      for row in range(ROWS):
         for col in range(COLS):
            # point_list.append((col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2))
            if (row,col) not in blank_list:
               pygame.draw.circle(win, GREY, (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2), radius= RADIUS)
            else:
               continue
            
      for i in range(len(point_list1)):
         point1 = point_list1[i]
         point2_list= point_list2[i]
         for point2 in point2_list:
               self.draw_line(point1,point2,win)
               
   def get_piece(self, row, col):
      # print("hello")
      # print(row,col)
      return self.board[row][col]
            
   def create_board(self):
      invalid_list = [(1,0),(1,8),(2,0),(2,1),(2,3),(2,5),(2,7),(2,8),(3,0),(3,1),(3,2),(3,6),(3,7),(3,8),(4,1),(4,7),(5,0),(5,8),(7,0),(7,8),(8,1),(8,7),(9,0),(9,1),(9,2),(9,6),(9,7),(9,8),(10,0),(10,1),(10,3),(10,5),(10,7),(10,8),(11,0),(11,8)]
      
      for row in range(ROWS):
         self.board.append([])
         for col in range(COLS):
            if row == 0:
               self.board[row].append(Piece(row,col,BLUE))
            elif row == 1:
               if col == 0 or col == 8:
                  self.board[row].append(-1)
               else:
                  self.board[row].append(Piece(row,col,BLUE))
            elif row == 12:
               self.board[row].append(Piece(row,col,RED))
            elif row == 11:
               if col == 0 or col == 8:
                  self.board[row].append(-1)
               else:
                  # self.board[row].append(0)
                  self.board[row].append(Piece(row,col,RED))
            else:
               if (row,col) in invalid_list:
                  self.board[row].append(-1)
               else:
                  self.board[row].append(0)
                  
                  
   def draw(self, win):
      self.draw_points(win)
      for rows in range(ROWS):
         for cols in range(COLS):
            piece = self.board[rows][cols]
            if piece != -1 and piece != 0:
               piece.draw(win)
               
   def evaluate(self):
      return self.blue_left - self.red_left
   
   def get_all_pieces(self, color):
      pieces = []
      for row in self.board:
         for piece in row:
               if piece!=0 and piece!=-1 and piece.color == color:
                  pieces.append(piece)
      return pieces
   
   def move(self, piece, row, col):
      self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
      piece.move(row,col)
      
   
   def remove(self, piece):
      self.board[piece.row][piece.col] = 0
      if piece != 0:
         if piece.color == RED:
               self.red_left -= 1
         else:
               self.blue_left -= 1
    
   def winner(self):
      if self.red_left <= 0:
         return BLUE
      elif self.blue_left <= 0:
         return RED
      return None
   
   def get_valid_moves(self, piece):
      current_pos = (piece.row,piece.col)
      moves = self.valids[current_pos]
      
      if current_pos in self.st_top:
         if current_pos == self.top:
            # print(self.top)
            pass
            # print('rs1',end='')
            # print(moves)  
         else:
            moves = []
            # print('rs2',end='')
            # print(self.top)
            # print(moves)  
               
      if current_pos in self.st_down:
         if current_pos == self.down:
            pass
            # print('rs3',end='')
            # print(self.down)
            # print(moves) 
         else:
            moves = []
            pass
            # print('rs4',end='')
            # print(self.down)
            # print(moves)
      
      valid_moves = self._traverse(moves, piece.color, piece)
      return valid_moves
      
   
   def _traverse(self, moves, color, piece):
      valids = []
      catch = 0
      skipped = {}
      
      for move in moves:
         r = move[0]
         c = move[1]
         
         current = self.board[r][c]
         if current == 0:
            valids.append(move)
            skipped[move] = 0
         elif current != -1 and current != 0 and current.color != color:
            direction = [move[0]-piece.row, move[1]-piece.col]
            
            if move[0] + direction[0] >= 2 and move[1] + direction[1] >= 0 and move[0] + direction[0] < ROWS-2 and move[1] + direction[1] < COLS and (move[0] + direction[0],move[1] + direction[1]) in self.valids[(move[0],move[1])]:
               next = self.board[move[0]+direction[0]][move[1]+direction[1]]
               if next == 0:
                  catch += 1
                  valids.append((move[0]+direction[0], move[1]+direction[1]))
                  skipped[(move[0]+direction[0], move[1]+direction[1])] = (move[0],move[1])
                  
      return [valids,skipped,catch]
                  
      
   
      
               
            
               