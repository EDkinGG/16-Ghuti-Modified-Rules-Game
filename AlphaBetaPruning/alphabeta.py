from copy import deepcopy
import pygame

RED = (255,0,0)
BLUE = (0,0,255)


#position-> board object(current board situation)
#depth -> how depth the tree will be (depth of search)
#max_player -> player ki result max korte chay na minimum korte chay
#game -> main game object

def alphabeta(position, depth, max_player, game, alpha, beta):
   if depth == 0 or position.winner() != None :
      return position.evaluate(), position
   
   if max_player:
      maxEval = float('-inf')
      best_move = None
      for move in get_all_moves(position, BLUE, game):
         evaluation = alphabeta(move, depth-1, False, game, alpha, beta)[0]
         if( maxEval < evaluation ):
            maxEval = evaluation
            best_move = move
            alpha = max(alpha,maxEval)
            if beta <= alpha:
               break
      #    maxEval = max(maxEval,evaluation)
      #    alpha = max(alpha,maxEval)
      #    print('maxv ', evaluation)
      #    if maxEval == evaluation:
      #       best_move = move
      #    if beta <= alpha:
      #       break
      # if best_move == None:
      #    print("kire vai")
      return maxEval, best_move
   else:
      minEval = float('inf')
      best_move = None
      for move in get_all_moves(position, RED, game):
         evaluation = alphabeta(move, depth-1, True , game, alpha, beta)[0]
         if( minEval > evaluation ):
            minEval = evaluation
            best_move = move
            beta = min(beta,minEval)
            if beta <= alpha:
               break
         # minEval = min(minEval,evaluation)
         # beta = min(beta,minEval)
         # print('minv ', evaluation)
         # if minEval == evaluation:
         #    best_move = move
         # if beta <= alpha:
         #    break
      return minEval, best_move
   
   
   
def simulate_move(piece, move ,board,game ,skipped):
   # print(piece)
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
      if( piece!= 0 ):
         board.remove(piece)
   
   if(skipped[(move[0],move[1])] != 0):
      piece = board.get_piece(move[0],move[1])
      x_valid ,x_skip, catch = board.get_valid_moves(piece)
      if catch != 0:
         for mv in x_valid:
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(move[0],move[1])
            if x_skip[(mv[0],mv[1])] != 0 and temp_piece != 0:
               # print('call korse')
               # print(temp_piece)
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