class Moves:
     
     def __init__(self , intial, final) -> None:
       #intial and final scores
          self.intial =  intial
          self.final =  final
          
     def __str__(self):
          s = ''
          s +=f'({self.intial.col} , {self.intial.row})'
          s +=f'({self.final.col} , {self.final.row})'
          return s
    
     def __eq__(self, other):
          return self.intial  == other.intial and self.final ==  other.final
          
          