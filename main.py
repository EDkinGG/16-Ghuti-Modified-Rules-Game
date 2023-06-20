import pygame,sys
from SholoGhuti.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, BLACK, BLUE,BG, MNU, COLS, ROWS
from SholoGhuti.board import Board
from SholoGhuti.game import Game
from minimax.algo import minimax
from AlphaBetaPruning.alphabeta import alphabeta
from button import Button

FPS = 60
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('16 Ghuti')

def get_row_col_from_mouse(pos):
   x, y = pos
   row = y//SQUARE_SIZE
   col = x//SQUARE_SIZE
   # print("GG")
   # print(row,col)
   return row,col

def main():
   run = True
   clock = pygame.time.Clock()
   game = Game(WIN)
   
   def get_font():
      return pygame.font.SysFont('Corbel',35)
   
   def play():
      while True:
         PLAY_MOUSE_POS = pygame.mouse.get_pos()
         if game.turn == BLUE:
            # value, new_board = minimax(game.get_board(),2, True, game)
            value, new_board = alphabeta(game.get_board(),2, True, game,float('-inf') ,float('inf') )
            # print(game.board.top)
            game.ai_move(new_board)
            
         if game.winner() != None:
            while True:
               Back_MOUSE_POS = pygame.mouse.get_pos()
               WIN.fill("black")
               val = game.winner()
               if ( val == RED ):
                  winnertext = get_font().render("You(Red) Win !", True, "green")
               else:
                  winnertext = get_font().render("AI(Blue) Wins !", True, "red")

               winnerrect = winnertext.get_rect(center=(338,488))
               WIN.blit(winnertext, winnerrect)
               
               run = False
               backbutton = Button(pos=(338, 550),text_input="BACK", font=get_font(), base_color="white", hovering_color="red")
               
               backbutton.changeColor(Back_MOUSE_POS)
               backbutton.update(WIN)
               
               for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                  if event.type == pygame.MOUSEBUTTONDOWN:
                        if backbutton.checkForInput(Back_MOUSE_POS):
                           main_menu()
               pygame.display.update()



         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
               pos = pygame.mouse.get_pos()
               row, col = get_row_col_from_mouse(pos)
               game.select(row,col)
            game.update()

         PLAY_BACK = Button( pos=(50, 280), 
                            text_input="BACK", font=pygame.font.SysFont('Calibri',18, pygame.font.Font.bold), base_color="black", hovering_color="red")

         PLAY_BACK.changeColor(PLAY_MOUSE_POS)

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
               if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                  main_menu()

         PLAY_BACK.update(WIN)
         pygame.display.update()
         
         
   def main_menu():
      # background = pygame.image.load('background.jpg')
      while True:
         WIN.fill("BLACK")
         WIN.blit(MNU,(0,0))
         MENU_MOUSE_POS = pygame.mouse.get_pos()

         MENU_TEXT = pygame.font.SysFont('Calibri',60).render("Sholo Ghuti", True, "black")
         MENU_RECT = MENU_TEXT.get_rect(center=(338, 240))

         PLAY_BUTTON = Button(pos=(338, 427), 
                              text_input="PLAY", font=pygame.font.SysFont('Calibri',40, pygame.font.Font.bold), base_color="black", hovering_color="green")
         QUIT_BUTTON = Button(pos=(338, 550), 
                           text_input="EXIT", font=pygame.font.SysFont('Calibri',40, pygame.font.Font.bold), base_color="black", hovering_color="red")

         WIN.blit(MENU_TEXT, MENU_RECT)

         for button in [PLAY_BUTTON, QUIT_BUTTON]:
               button.changeColor(MENU_MOUSE_POS)
               button.update(WIN)

         for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
               elif event.type == pygame.MOUSEBUTTONDOWN:
                  if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                     play()
                  elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                     pygame.quit()
                     sys.exit()

         pygame.display.update()

   main_menu()

main()
   
#    while run:
#       clock.tick(FPS)
#       if game.turn == BLUE:
#          value, new_board = minimax(game.get_board(),2, True, game)
#          # value, new_board = alphabeta(game.get_board(),2, True, game,float('-inf') ,float('inf') )
#          print(game.board.top)
#          game.ai_move(new_board)
         
      
#       if game.winner() != None:
#          print(game.winner())
      
#       for event in pygame.event.get():
#          if event.type == pygame.QUIT:
#             run = False
            
#          if event.type == pygame.MOUSEBUTTONDOWN:
#             pos = pygame.mouse.get_pos()
#             row, col = get_row_col_from_mouse(pos)
#             game.select(row, col)
            
#       game.update()
      
      
#    pygame.quit()

# main()
   