value, new_board = alphabeta(game.get_board(),2, True, game,float('-inf') ,float('inf') )


def alphabeta(position, depth, max_player, game, alpha, beta):
   if depth == 0 or position.winner() != None :
      return position.evaluate(), position-------------------><9> 
   
   if max_player:---------------------------><1>
      maxEval = float('-inf')---------------><2>maxEval = -inf,
      best_move = None----------------------><3>best_move = none,
      for move in get_all_moves(position, BLUE, game):
         evaluation = alphabeta(move, depth-1, False, game, alpha, beta)[0]----------------------><4>call1---<14>0,bestmove
         maxEval = max(maxEval,evaluation)-------------------><15> max(-inf,0)---> maxEval = 0,
         alpha = max(alpha,maxEval)--------------------------> <16> alpha = max(0,-inf)--> alpha = 0,
         print('maxv ', maxEval)
         if beta <= alpha:-----------------------------> <17> 0 <= 0
            break--------------------------------------> <18> break
         if maxEval == evaluation:
            best_move = move
      return maxEval, best_move
   else: -------------------------------------><5>
      minEval = float('inf')-------------------><6> minEval = inf
      best_move = None-------------------------> <7> best_move = none
      for move in get_all_moves(position, RED, game):
         evaluation = alphabeta(move, depth-1, True , game, alpha, beta)[0]-------------><8>call------------> 0
         minEval = min(minEval,evaluation)---------------><9> 0
         beta = min(beta,minEval)------------------------><10> 0
         print('minv ', minEval)
         if beta <= alpha:-------------------><11> 0 <= -inf
            break
         if minEval == evaluation:-----------><12> this the best move,
            best_move = move
      return minEval, best_move-------------->0,bestmove<13>