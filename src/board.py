from const import *
from square import Square
from piece import *
from moves import Moves

#lib
import copy

class Board:
    def __init__(self) -> None:
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self.last_move  = None
        self._create()
        self._add_piece('white')
        self._add_piece('black')  # Fixed typo here
        
    def move(self ,piece , move):
         intial =  move.intial
         final =  move.final
         
         # console move update
         self.squares[intial.row][intial.col].piece = None
         self.squares[final.row][final.col].piece =  piece
         
         # pawn promotion
         if isinstance(piece ,Pawn):
              self.check_promotion(piece , final)
         
         #king castling
         if isinstance(piece , King):
             if self.castling(intial , final):
                  diff = final.col - intial.col
                  rook = piece.left_rook if (diff <0) else piece.right_rook
                  self.move(rook , rook.moves[-1])
         
         # move on board
         piece.moved  =  True
         
         #clear moves on the piece
         piece.clear_moves()
         #save tga last moves
         self.last_move = move
  
    def valid_move(self ,piece , move):
         return move in piece.moves
 
    def check_promotion( self , piece , final):
         if final.row == 7 or final.row == 0 :
               self.squares[final.row][final.col].piece = Queen(piece.color) 
    
    def castling(self , intial , final):
        return abs(intial.col - final.col) == 2
  
    def in_check(self , piece, move ):
       temp_piece =  copy.deepcopy(piece)
       temp_board = copy.deepcopy(self)
       temp_board.move(temp_piece , move)
       
       #after moving a board check if there is a checkor not
       for row in range(ROWS):
           for col in range(COLS):
               if temp_board.squares[row][col].has_enemy_piece(piece.color):
                    p =  temp_board.squares[row][col].piece
                    temp_board.calc_moves(p , row , col , bool =  False)
                    for m in piece.moves:
                         if isinstance(m.final.piece , King):
                               return True
                    
       return False
    def calc_moves(self , piece , row , col , bool = True):
            """  
                calulayte all the possibke moves for each piece
            """
            # we usulay use mfun inside a funtion 
            def pawn_moves():
                #count no of moves
                steps = 1 if piece.moved else 2
                # vertical moves
                start =  row +piece.dir
                end = row  + (piece.dir *(1 + steps))
                
                for possible_move_row in range(start , end , piece.dir):
                      if Square.in_range(possible_move_row):
                             if self.squares[possible_move_row][col].is_empty():
                                   #create a initisl  and final pos
                                   initial = Square(row, col)
                                   final =  Square(possible_move_row , col)
                                   #Create na new moves
                                   move = Moves(initial , final)
                                   
                                   #CHECK IF THE MOVE LEAADS TOANY CHECK  
                                   if bool :
                                      if not self.in_check(piece , move):
                                         piece.add_move(move)
                                   else:
                                        piece.add_move(move)
                            #blocked
                             else:
                                  break
                      # not in range
                      else: break
                                
                #diagonal moves
                possible_move_row =  row  +  piece.dir
                possible_move_cols= [col -1 , col+1]
                for possible_move_col  in possible_move_cols:
                    if Square.in_range(possible_move_row , possible_move_col):
                         if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                                #create a initaqil and final square
                                initial =  Square(row , col)
                                final_piece =  self.squares[possible_move_row][possible_move_col].piece
                                final  =  Square(possible_move_row , possible_move_col , final_piece)
                                #Create  a new moves
                                move = Moves(initial , final)
                                
                                #CHECK IF THE MOVE LEAADS TOANY CHECK  
                                if bool :
                                   if not self.in_check(piece , move):
                                      piece.add_move(move)
                                else:
                                      piece.add_move(move)
            def knight_moves():
                # max 8 moves
                possibe_moves = [
                   (row-2, col+1),
                   (row-1, col+2),
                   (row+1, col+2),
                   (row+2, col+1),
                   (row+2, col-1),
                   (row+1, col-2),
                   (row-1, col-2),
                   (row-2, col-1),
                ]
                
                for posssible_move in possibe_moves:
                    possible_move_row , possible_move_col =  posssible_move
                    if Square.in_range(possible_move_row , possible_move_col):
                             #check for empty sqaure
                             if self.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.color):
                                  #create squares of new moves
                                  initial =  Square(row, col)
                                  final_piece =  self.squares[possible_move_row][possible_move_col].piece
                                  final =  Square(possible_move_row , possible_move_col , final_piece)
                                  #create  new moves
                                  move = Moves(initial , final)
                                  # append the new valid move
                                  #CHECK IF THE MOVE LEAADS TOANY CHECK  
                                  if bool :
                                     if not self.in_check(piece , move):
                                      piece.add_move(move)
                                     else:
                                         break
                                  else:
                                     piece.add_move(move) 
                                                     
            def straight_line_moves(incrs):
                  for incr in incrs:
                      row_incr  , col_incr = incr
                      possible_move_row = row + row_incr
                      possible_move_col = col + col_incr
                      
                      while True:
                        if Square.in_range(possible_move_row , possible_move_col):
                            #create a initaqil and final square
                            initial =  Square(row , col)
                            final_piece =  self.squares[possible_move_row][possible_move_col].piece
                            final  =  Square(possible_move_row , possible_move_col , final_piece)
                            #create  new moves
                            move = Moves(initial , final)
                            if self.squares[possible_move_row][possible_move_col].is_empty():
                                # append the new valid move
                               #CHECK IF THE MOVE LEAADS TOANY CHECK  
                                if bool :
                                   if not self.in_check(piece , move):
                                      piece.add_move(move)
                                   else:
                                       break
                                else:
                                      piece.add_move(move)      
                            elif self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                                    # append the new valid move
                                #CHECK IF THE MOVE LEAADS TOANY CHECK  
                                if bool :
                                   if not self.in_check(piece , move):
                                      piece.add_move(move)
                                   else:
                                      break
                                else:
                                      piece.add_move(move)
                                break 
                            elif self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                                #has a team piece
                                break 
                        else: break        
                        possible_move_row , possible_move_col =  possible_move_row + row_incr , possible_move_col + col_incr
            
            def king_moves():
                adjs = [
                (row-1, col+0), # up
                (row-1, col+1), # up-right
                (row+0, col+1), # right
                (row+1, col+1), # down-right
                (row+1, col+0), # down
                (row+1, col-1), # down-left
                (row+0, col-1), # left
                (row-1, col-1), # up-left
                        ]
                # normal moves
                for possibile_move in adjs:        
                    possible_move_row , possible_move_col = possibile_move
                     
                    if Square.in_range(possible_move_row , possible_move_col):
                           if self.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.color):
                                   #create squares of new moves
                                  initial =  Square(row, col)
                                  final =  Square(possible_move_row , possible_move_col)
                                  #create  new moves
                                  move = Moves(initial , final)
                                  # append the new valid move
                                  piece.add_move(move)       
                #castling
                
                #castling moves
                if not piece.moved:
                    # queen side 
                    left_rook  =  self.squares[row][0].piece
                    if isinstance(left_rook , Rook):
                        if not left_rook.moved:
                              for c in range(1, 4):
                                 # has a pice in btw them
                                  if self.squares[row][c].has_piece():
                                         break
                                  if c == 3:
                                      #adds left rook to king
                                       piece.left_rook  = left_rook
                                       #rook move
                                       intial =  Square(row , 0)
                                       final = Square(row, 3)
                                       move = Moves(intial , final)
                                       left_rook.add_move(move)
                                       
                                       #king move
                                       intial =  Square(row , col)
                                       final = Square(row, 2)
                                       move = Moves(intial , final)
                                       piece.add_move(move)
                                      # queen side 
                    right_rook  =  self.squares[row][7].piece
                    if isinstance(right_rook , Rook):
                        if not right_rook.moved:
                              for c in range(5, 7):
                                 # has a pice in btw them
                                  if self.squares[row][c].has_piece():
                                         break
                                  if c == 6:
                                      #adds left rook to king
                                       piece.right_rook  = right_rook
                                       #rook move
                                       intial =  Square(row , 7)
                                       final = Square(row, 5)
                                       move = Moves(intial , final)
                                       right_rook.add_move(move)
                                       
                                       #king move
                                       intial =  Square(row , col)
                                       final = Square(row, 6)
                                       move = Moves(intial , final)
                                       piece.add_move(move)
                                       
            
            if isinstance(piece , Pawn):  #if piece.name == "Pawn"
                     pawn_moves()
            if isinstance(piece , Knight):  
                     knight_moves()          
            elif isinstance(piece, Bishop): 
               straight_line_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
            ])

            elif isinstance(piece, Rook): 
               straight_line_moves([
                (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1), # left
            ])

            elif isinstance(piece, Queen): 
                straight_line_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
                (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1), # left
            ])
            if isinstance(piece , King):  
                  king_moves()
                              
    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_piece(self, color):
        row_pawn, row_other = (6, 7) if color == "white" else (1, 0)
        
        """ For pawns """
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
            """  self.squares[5][1] = Square(5, 1, Pawn(color)) """
            
        """ Knights """
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        """ self.squares[4][4] = Square(4 , 6 ,Knight(color )) """
        
        """ Bishops """
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
        """  self.squares[4][4] = Square(4, 4, Bishop(color)) """
        
        """ Rooks """
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        """ self.squares[4][4] = Square(4, 4, Rook(color)) """
        
        """ Queen """
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        """ self.squares[4][4] = Square(4, 4, Queen(color)) """
        
        """ King """
        self.squares[row_other][4] = Square(row_other, 4, King(color))
        """ self.squares[2][3] = Square(2, 3, King(color)) """