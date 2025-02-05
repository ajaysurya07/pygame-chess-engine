import pygame as pg;

from const import *
class Dragger :
     def __init__(self) -> None:
          self.mouseX = 0
          self.mouseY = 0
          self.inital_row = 0
          self.inital_col = 0
          self.piece = None 
          self.Dragging = False
      
     def update_mouse(self , pos) ->None:
         self.mouseX , self.mouseY = pos 
    
    
     def safe_initial(self , pos) ->None:
          self.inital_row =  pos[1] //SQSIZE
          self.inital_col = pos[0] // SQSIZE
         
    
     def drag_piece(self , piece):
           self.piece = piece
           self.Dragging = True
           
     def undrag(self):
            self.piece = None
            self.Dragging = False
     
     
     #blit method       
     def update_blit(self , surface):
           # increasing the size of the piece while dragging
           self.piece.set_texture(128)
           texture = self.piece.texture
           #image
           img = pg.image.load(texture)
           #rect
           img_center= (self.mouseX , self.mouseY)
           self.piece.texture_rect = img.get_rect(center = img_center)
           surface.blit(img , self.piece.texture_rect)
                      
      
               
          
          
          
          