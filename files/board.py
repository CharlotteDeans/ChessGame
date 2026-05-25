import square

class Board():
   def __init__(self):
      board = [[square.Square() for x in range(8)] for y in range(8)]

      # filling out board
      board[0][0] = square.Square('rook', 'white', 1)
      board[0][1] = square.Square('knight', 'white', 1)
      board[0][2] = square.Square('bishop', 'white', 1)
      board[0][3] = square.Square('queen', 'white', 0)
      board[0][4] = square.Square('king', 'white', 0)
      board[0][5] = square.Square('bishop', 'white', 0)
      board[0][6] = square.Square('knight', 'white', 0)
      board[0][7] = square.Square('rook', 'white', 0)
      for x in range(8):
         board[1][x] = square.Square('pawn', 'white', 7 - x) ## counting backwards
      for x in range(8):
         board[6][x] = square.Square('pawn', 'black', x)
      board[7][0] = square.Square('rook', 'black', 0)
      board[7][1] = square.Square('knight', 'black', 0)
      board[7][2] = square.Square('bishop', 'black', 0)
      board[7][3] = square.Square('queen', 'black', 0)
      board[7][4] = square.Square('king', 'black', 0)
      board[7][5] = square.Square('bishop', 'black', 1)
      board[7][6] = square.Square('knight', 'black', 1)
      board[7][7] = square.Square('rook', 'black', 1)
      self.board = board

   def printBoard(self):
      rowNum = 8
      for row in self.board:
         print(rowNum, end=" ")
         rowNum -= 1
         for rSquare in row:
            print(rSquare.getSymbol(), end=" ")
         print()
      print("  a b c d e f g h")

   def returnPiece(self, row, column):
      thePiece = self.board[row][column]
      if thePiece.getType() is None:
         return None
      else:
         return thePiece
      
   def isThereAPieceHere(self, row, column):
      piece = self.board[row][column]
      if piece.getType() is None:
         return False
      return True
      
   def canIMoveHere(self, oldRow, oldColumn, newRow, newColumn):
      myPiece = self.board[oldRow][oldColumn]
      pieceToOvertake = self.board[newRow][newColumn]
      if pieceToOvertake.getType() is None:
         return True
      elif pieceToOvertake.getColour() is not myPiece.getColour():
         return True
      return False
   
   def movePiece(self, oldRow, oldColumn, newRow, newColumn):
      self.board[newRow][newColumn] = self.board[oldRow][oldColumn]
      self.board[oldRow][oldColumn] = square.Square()

   def whereCanKingMove(self, row, column):
      myPiece = self.board[row][column]
      arrayOfSpaces = []
      for x in range(3):
         rowInLoop = row - 1 + x
         if rowInLoop <= 7 and rowInLoop >= 0:
            for y in range(3):
               columnInLoop = column - 1 + y
               if columnInLoop <= 7 and columnInLoop >= 0:
                  arrayOfSpaces.append([rowInLoop, columnInLoop])

      return arrayOfSpaces

   # queen can move anywhere so long as either x or y (but not both) doesnt change or the different between x and y is the same and a piece isnt in the way
   def whereCanQueenMove(self, row, column):
      myPiece = self.board[row][column]
      arrayOfSpaces = []
      for x in range(7):
         rowAboveQueen = row + x
         if rowAboveQueen > 7:
            break
         pieceHere = self.board[rowAboveQueen][column]
         if pieceHere.getColour() is None:
            arrayOfSpaces.append([rowAboveQueen, column])
         elif pieceHere.getColour() is not myPiece.getColour():
            arrayOfSpaces.append([rowAboveQueen, column])
            break
         else:
            break

      for x in range(7):
         rowBelowQueen = row - x
         if rowBelowQueen < 0:
            break
         pieceHere = self.board[rowBelowQueen][column]
         if pieceHere.getColour() is None:
            arrayOfSpaces.append([rowBelowQueen, column])
         elif pieceHere.getColour() is not myPiece.getColour():
            arrayOfSpaces.append([rowBelowQueen, column])
            break
         else:
            break
      
      for y in range(7):
         columnRightOfQueen = column + y
         if columnRightOfQueen > 7:
            break
         pieceHere = self.board[row][columnRightOfQueen]
         if pieceHere.getColour() is None:
            arrayOfSpaces.append([row, columnRightOfQueen])
         elif pieceHere.getColour() is not myPiece.getColour():
            arrayOfSpaces.append([row, columnRightOfQueen])
            break
         else:
            break

      for y in range(7):
         columnLeftOfQueen = column - y
         if columnLeftOfQueen < 0:
            break
         pieceHere = self.board[row][columnLeftOfQueen]
         if pieceHere.getColour() is None:
            arrayOfSpaces.append([row, columnLeftOfQueen])
         elif pieceHere.getColour() is not myPiece.getColour():
            arrayOfSpaces.append([row, columnLeftOfQueen])
            break
         else:
            break

      ## next: diagonals for queen