from copy import deepcopy
import pygame

RED = (255,0,0)
BLUE = (0,0,255)


#position-> board object(current board situation)
#depth -> how depth the tree will be (depth of search)
#max_player -> player ki result max korte chay na minimum korte chay
#game -> main game object

def minimax(position, depth, max_player, game):
   if depth == 0 or position.winner() != None :
      return position.evaluate(), position
   
   if max_player:
      maxEval = float('-inf')
      best_move = None
      for move in get_all_moves(position, BLUE, game):
         evaluation = minimax(move, depth-1, False, game)[0]
         maxEval = max(maxEval,evaluation)
         print('maxv ', maxEval)
         if maxEval == evaluation:
            best_move = move
      return maxEval, best_move
   else:
      minEval = float('inf')
      best_move = None
      for move in get_all_moves(position, RED, game):
         evaluation = minimax(move, depth-1, True , game)[0]
         minEval = min(minEval,evaluation)
         print('minv ', minEval)
         if minEval == evaluation:
            best_move = move
      return minEval, best_move
   
   
   
def simulate_move(piece, move ,board,game ,skipped):
   current_pos = (piece.row,piece.col)
   if current_pos == board.top:
      x,y = board.top
      if x == 1 and y+1 <= 7 :
         y = y+1
      else:
         if x == 1:
            x = 0
            y = 0
         else:
            y = y+1
      board.top = (x,y)
   if current_pos == board.down:
      x,y = board.down
      if x == 11 and y+1 <= 7 :
         y = y+1
      else:
         if x == 11:
            x = 12
            y = 0
         else:
            y = y+1
      board.down = (x,y)
   # print(row,col)
   board.move(piece,move[0],move[1])
   if (skipped[(move[0], move[1])] != 0):
      (r, c) = skipped[move[0], move[1]]
      piece = board.get_piece(r, c)
      board.remove(piece)
   
   if(skipped[(move[0],move[1])] != 0):
      piece = board.get_piece(move[0],move[1])
      x_valid ,x_skip, catch = board.get_valid_moves(piece)
      if catch != 0:
         for mv in x_valid:
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(move[0],move[1])
            if x_skip[(mv[0],mv[1])] != 0:
               board = simulate_move(temp_piece,mv,temp_board,game,x_skip)
   return board
   
   
   
def get_all_moves(board, color, game):
   moves = []
   for piece in board.get_all_pieces(color):
      [valid_moves, skipped, catch] = board.get_valid_moves(piece)
      for move in valid_moves:
         temp_board = deepcopy(board)
         temp_piece = temp_board.get_piece(piece.row, piece.col)
         new_board = simulate_move(temp_piece,move,temp_board,game,skipped)
         moves.append(new_board)
   return moves


def draw_moves(game, board, piece):
   valid_moves,_,_ = board.get_valid_moves(piece)
   board.draw(game.win)
   pygame.draw.circle(game.win,(0,255,255),(piece.x,piece.y),50, 5)
   game.draw_valid_moves(valid_moves)
   pygame.display.update()
   pygame.time.delay(100)