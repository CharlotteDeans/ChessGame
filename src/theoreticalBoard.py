from board import Board
from square import Square

class TheoreticalBoard(Board):
   def __init__(self, newKingSpace, colour):
      super().__init__(self)
   
      newKingX = newKingSpace[0]
      newKingY = newKingSpace[1]
      kingPiece = Square('king', colour)
      for x in range(8):
         for y in range(8):
            if self.board[x][y] is kingPiece:
               self.board[x][y] = Square()
               break
      self.board[newKingX][newKingY] = kingPiece

   def returnListOfAvailableSpaces(self, x, y):
      pieceType = self.returnPieceType(x, y)
      arrayOfSpaces = []
      match pieceType:
         case 'pawn':
            arrayOfSpaces = self.whereCanPawnMove(x,y)
         case 'knight':
            arrayOfSpaces = self.whereCanKnightMove(x,y)
         case 'bishop':
            arrayOfSpaces = self.whereCanBishopMove(x,y)
         case 'rook':
            arrayOfSpaces = self.whereCanRookMove(x,y)
         case 'queen':
            arrayOfSpaces = self.whereCanQueenMove(x,y)
         # checking king again will cause infinite loop of making theoretical board instances
      return arrayOfSpaces