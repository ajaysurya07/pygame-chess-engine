
import os
           
""" texture is img url """
class Piece:
     def __init__(self ,name ,  color , value, texture = None, texture_rect=None ) -> None:
          self.name = name
          self.color = color

          value_sign = 1 if color == "white" else -1
          self.value =  value * value_sign
          
          self.moves = []
          self.moved =False 
          
          self.texture = texture
          self.texture_rect = texture_rect
          self.set_texture() 
     
     # setting the size of the piece
     def set_texture(self ,size = 80):
           self.texture = os.path.join(
            os.path.dirname(__file__), '..', 'assets', 'images', f'imgs-{size}px', f'{self.color}_{self.name}.png'
        )
     def add_move(self , move):
            self.moves.append(move) 
     def clear_moves(self):
            self.moves = [] 
class Pawn(Piece):
     
     def __init__(self, color) -> None:
            self.dir = -1 if color == "white" else 1
            super().__init__("pawn" , color , 1.0)

class Knight(Piece):
     
     def __init__(self, color) -> None:
            super().__init__("knight" , color , 3.0)

class Bishop(Piece):
     
     def __init__(self, color) -> None:
            super().__init__("bishop" , color , 3.001)

class Rook(Piece):
     
     def __init__(self, color) -> None:
            super().__init__("rook" , color , 5.0)

class Queen(Piece):
     
     def __init__(self, color) -> None:
            super().__init__("queen" , color , 6.0)

class King(Piece):
     
     def __init__(self, color) -> None:
            self.left_rook= None
            self.right_rook = None
            super().__init__("king" , color , 100000.0)
      
