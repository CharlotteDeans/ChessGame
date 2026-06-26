class Square():
   def __init__(self, type=None, colour=None):
      self.type = type
      self.colour = colour
      self.symbol = '▢'
      self.pieceMoved = False
      self.enPassantable = False
      
      # movement logic - each piece needs different logic made in board to determine where they can move
      # king can move anywhere one space around it
      # queen can move anywhere so long as either x or y (but not both) doesnt change or the different between x and y is the same and a piece isnt in the way
      # bishop can move where either x or y doesnt change and a piece isnt in the way
      # knight can move anywhere where x+-2 and y+-1 or x+-1 and y+-2
      # pawn moves up 1 or 2 spaces the first time it moves, 1 after the first time it moves and can move up left or right diagonally if a piece is left or right to it
      # black pawn is the same but opposite directions
      
      if (self.colour == None):
         self.symbol = '▢'
      elif (self.colour == "black"):
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
   
   def getEnPassantable(self):
      return self.enPassantable
   
   def switchPieceMoved(self):
      self.pieceMoved = True

   def hasPieceMoved(self):
      return self.pieceMoved
   
   def switchEnPassantOn(self):
      self.enPassantable = True

   def switchEnPassantOff(self):
      self.enPassantable = False
