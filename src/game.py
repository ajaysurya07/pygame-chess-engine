# rendering of games  take place
import pygame as pg
from const import *
from board import Board 
from dragger import Dragger
from config import Config
from square import Square
class Game:
     def __init__(self) -> None:
          self.nextplayer = 'white' 
          self.hover_sqr = None
          self.board = Board()
          self.Dragger = Dragger()
          self.config = Config()
          
          
     def show_bag(self , surface):
           theme =  self.config.theme
           
           for row in range(ROWS):
                for col in range(COLS):
                         
                         color =  (theme.bg.light) if (row +  col) %2 ==0 else theme.bg.dark
                         
                         """  if(row + col)%2 ==0:
                               color = (234 , 235 , 200) #light g
                         else:
                               color = (119 , 154 , 88)  #dark g

                         """
                         rect = (col * SQSIZE , row * SQSIZE , SQSIZE , SQSIZE)
                        

                         pg.draw.rect(surface , color , rect)
                         #row coordinater (1 - 8)
                         if col == 0:
                               #color
                               color =  theme.bg.dark if row%2 ==0 else theme.bg.light
                               #label
                               lbl = self.config.font.render(str(ROWS - row) , 1, color) 
                               lbl_pos = (5, 5+ row *SQSIZE)
                               #blit
                               surface.blit(lbl , lbl_pos)
                          #col coordinater (a- g)
                         if  row== 7:
                               #color
                               color =  theme.bg.dark if (row + col)%2 ==0 else theme.bg.light
                               #label
                               lbl = self.config.font.render(Square.get_alphacol(col) , 1, color) 
                               lbl_pos = (col *SQSIZE + SQSIZE - 20 , HEIGHT -20)
                               #blit
                               surface.blit(lbl , lbl_pos)
                         
     def show_piece(self , surface):
           for row in range(ROWS):
                for col in range(COLS):
                      if self.board.squares[row][col].has_piece():
                             piece = self.board.squares[row][col].piece
                             # all piece expect  dragging 
                             if piece is not self.Dragger.piece:
                                    piece.set_texture(size = 80)
                                    img = pg.image.load(piece.texture)
                                    img_center = col * SQSIZE  + SQSIZE //2 ,  row * SQSIZE +SQSIZE //2
                                    piece.texture_rect = img.get_rect(center = img_center)
                                    surface.blit(img , piece.texture_rect)      
     def show_moves(self , surface):
            theme =  self.config.theme
            if self.Dragger.Dragging:
                  piece = self.Dragger.piece
                  
                  for move in piece.moves:
                        #color
                        color = theme.moves.light if (move.final.row * move.final.col)%2 == 0 else  theme.moves.dark
                        #rect
                        rect  = (move.final.col * SQSIZE ,move.final.row* SQSIZE , SQSIZE ,SQSIZE )
                        #blit
                        pg.draw.rect(surface , color , rect)
                        
     
      # didplaay the last move
     def show_last_move(self , surface):
        theme = self.config.theme

        if self.board.last_move:
             intial  =  self.board.last_move.intial
             final = self.board.last_move.final
             
             for pos  in  [intial , final]:
                       #color
                        color = theme.trace.light if (pos.row * pos.col)%2 == 0 else theme.trace.dark
                        #rect
                        rect  = (pos.col * SQSIZE ,pos.row* SQSIZE , SQSIZE ,SQSIZE )
                        #blit
                        pg.draw.rect(surface , color , rect)
    #designing
     def show_hover(self , surface) :
          if self.hovered_sqr:
                #color
                        color = (180 , 180 , 180 )
                        #rect
                        rect  = (self.hovered_sqr.col * SQSIZE ,self.hovered_sqr.row* SQSIZE , SQSIZE ,SQSIZE )
                        #blit
                        pg.draw.rect(surface , color , rect)
    #designing
                    
    #other method
     def next_turn(self): # not a render method
          self.nextplayer = 'white' if self.nextplayer == 'black' else 'black'                       
      
     def  hover_set(self , row ,col):
           self.hovered_sqr =  self.board.squares[row][col]
      
      
     def change_theme(self):
           self.config.change_theme() 
           
     def sound_effect(self , capture = False):
            if capture:
                  self.config.capture_sound.play()
            else:
                  self.config.move_sound.play()
     
     def reset(self):
         self.__init__()    
                                                                                                      