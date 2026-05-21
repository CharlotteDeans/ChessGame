class Square():
   def __init__(self, type=None, colour=None, no=None):
      self.type = type
      self.colour = colour
      self.no = no
      self.symbol = '▢'

      if (self.colour == None):
         self.symbol = '▢'
      elif (self.colour == "white"):
         match self.type:
            case "king":
               self.symbol = '♔'
            case "queen":
               self.symbol = '♕'
            case "rook":
               self.symbol = '♖'
            case "bishop":
               self.symbol = '♗'
            case "knight":
               self.symbol = '♘'
            case "pawn":
               self.symbol = '♙'
      else:
         match self.type:
            case "king":
               self.symbol = '♚'
            case "queen":
               self.symbol = '♛'
            case "rook":
               self.symbol = '♜'
            case "bishop":
               self.symbol = '♝'
            case "knight":
               self.symbol = '♞'
            case "pawn":
               self.symbol = '♟'
      pass
   
   def getType(self):
      return self.type

   def getColour(self):
      return self.colour
   
   def getNo(self):
      return self.no

   def getSymbol(self):
      return self.symbol