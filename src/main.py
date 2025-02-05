import pygame as pg
import sys

""" from other py files   """
from const import *
from game import Game
from square import Square
from moves import Moves
class Main:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((WIDTH , HEIGHT))
        pg.display.set_caption('Chess')
        self.game = Game()
    
    def Mainloop(self):
           
            game = self.game
            screen =self.screen
            dragger = self.game.Dragger
            board = self.game.board
            while True:
                 #show methods
                game.show_bag(screen)
                game.show_last_move(screen)
                game.show_moves(screen)
                game.show_piece(screen)
                
                if dragger.Dragging :
                     dragger.update_blit(screen)

                for event in pg.event.get():
                       #click
                       if event.type == pg.MOUSEBUTTONDOWN:
                              dragger.update_mouse(event.pos)
                              #print(event.pos)
                              C_row = dragger.mouseY // SQSIZE
                              C_col = dragger.mouseX // SQSIZE
                              #print(C_row,"  , " ,C_col)
                              if board.squares[C_row][C_col].has_piece():
                                  piece = board.squares[C_row][C_col].piece
                                  if  piece.color  == game.nextplayer:
                                    board.calc_moves(piece , C_row , C_col , bool = True)
                                    dragger.safe_initial(event.pos)
                                    dragger.drag_piece(piece)
                                    #show methods
                                    game.show_bag(screen)
                                    game.show_moves(screen)
                                    game.show_piece(screen)
                              
                              
                       #mouse motion 
                       elif event.type == pg.MOUSEMOTION:
                             motion_row =  event.pos[1] //SQSIZE
                             motion_col =  event.pos[0] // SQSIZE
                             
                             game.hover_set(motion_row , motion_col)
                             
                             if dragger.Dragging :
                                   dragger.update_mouse(event.pos)
                                   game.show_bag(screen)
                                   game.show_last_move(screen)
                                   game.show_moves(screen)
                                   game.show_piece(screen)
                                   game.show_hover(screen)
                                   dragger.update_blit(screen)
                       #click release
                       elif event.type == pg.MOUSEBUTTONUP:
                              if dragger.Dragging :
                                  dragger.update_mouse(event.pos)   # update the dragger intoi the mouse postion
                                  
                                  release_row = dragger.mouseY // SQSIZE
                                  release_col =  dragger.mouseX //SQSIZE
                                  
                                  #create a possible moves
                                  initial = Square(dragger.inital_row , dragger.inital_col)
                                  final =  Square(release_row , release_col)
                                  move = Moves(initial , final)
                                  
                                  if board.valid_move(dragger.piece , move):
                                       capture = board.squares[release_row][release_col].has_piece()
                                       board.move(dragger.piece , move)
                                       #sound effect
                                       game.sound_effect(capture)
                                       #drop  
                                       game.show_bag(screen)
                                       #shopew the prev move
                                       game.show_last_move(screen)
                                       game.show_piece(screen)
                                       #game change tonect player 
                                       game.next_turn()
                                  
                              dragger.undrag()
                       
                       # key press
                       elif event.type == pg.KEYDOWN:
                           #change the theme 
                           if event.key == pg.K_t:
                                game.change_theme()
                           if event.key == pg.K_r:
                                 game.reset()
                                 game = self.game
                                 screen =self.screen
                                 dragger = self.game.Dragger
                                 board = self.game.board
                                  
                       #quit  event
                       if event.type == pg.QUIT:
                            pg.quit()
                            sys.exit()
                


                pg.display.update()


main  =  Main()
main.Mainloop() 