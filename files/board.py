import square

class Board():
   def __init__(self):
      board = [[square.Square() for x in range(8)] for y in range(8)]

      # filling out board
      board[0][0] = square.Square('rook', 'white', 1)
      board[1][0] = square.Square('knight', 'white', 1)
      board[2][0] = square.Square('bishop', 'white', 1)
      board[3][0] = square.Square('queen', 'white', 0)
      board[4][0] = square.Square('king', 'white', 0)
      board[5][0] = square.Square('bishop', 'white', 0)
      board[6][0] = square.Square('knight', 'white', 0)
      board[7][0] = square.Square('rook', 'white', 0)
      for x in range(8):
         board[x][1] = square.Square('pawn', 'white', 7 - x) ## counting backwards
      for x in range(8):
         board[x][6] = square.Square('pawn', 'black', x)
      board[0][7] = square.Square('rook', 'black', 0)
      board[1][7] = square.Square('knight', 'black', 0)
      board[2][7] = square.Square('bishop', 'black', 0)
      board[3][7] = square.Square('queen', 'black', 0)
      board[4][7] = square.Square('king', 'black', 0)
      board[5][7] = square.Square('bishop', 'black', 1)
      board[6][7] = square.Square('knight', 'black', 1)
      board[7][7] = square.Square('rook', 'black', 1)
      self.board = board

   def printBoard(self):

      ## printing the 2d array like usual will make pieces opposite in the x axis
      # but this doesnt affect actual piece locations and placement will always be 1 less than on board
      rowNum = 8
      for y in range(8):
         print(rowNum, end=" ")
         rowNum -= 1
         for x in range(8):
            # print x backwards
            thePiece = self.board[x][7 - y]
            print(thePiece.getSymbol(), end=" ")
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
         rowAboveQueen = row + x + 1
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
         rowBelowQueen = row - (x + 1)
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
         columnRightOfQueen = column + y + 1
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
         columnLeftOfQueen = column - (y + 1)
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

      # +1 to row and column until out of bounds or hit another piece
      # then +1 row and -1 column, -1 row and +1 column, -1 row and column
      rowFromQueen = row
      columnFromQueen = column
      # up right
      for spaces in range(7):
         rowFromQueen += 1
         columnFromQueen += 1
         pieceHere = self.board[rowFromQueen][columnFromQueen]
         if pieceHere.getColour() is None:
            arrayOfSpaces.append([rowFromQueen, columnFromQueen])
         elif pieceHere.getColour() is not myPiece.getColour():
            arrayOfSpaces.append([rowFromQueen, columnFromQueen])
            break
         else:
            break

      rowFromQueen = row
      columnFromQueen = column
      # up left
      for spaces in range(7):
         rowFromQueen -= 1
         columnFromQueen += 1
         pieceHere = self.board[rowFromQueen][columnFromQueen]
         if pieceHere.getColour() is None:
            arrayOfSpaces.append([rowFromQueen, columnFromQueen])
         elif pieceHere.getColour() is not myPiece.getColour():
            arrayOfSpaces.append([rowFromQueen, columnFromQueen])
            break
         else:
            break

      rowFromQueen = row
      columnFromQueen = column
      for spaces in range(7):
         rowFromQueen += 1
         columnFromQueen -= 1
         pieceHere = self.board[rowFromQueen][columnFromQueen]
         if pieceHere.getColour() is None:
            arrayOfSpaces.append([rowFromQueen, columnFromQueen])
         elif pieceHere.getColour() is not myPiece.getColour():
            arrayOfSpaces.append([rowFromQueen, columnFromQueen])
            break
         else:
            break

      rowFromQueen = row
      columnFromQueen = column
      for spaces in range(7):
         rowFromQueen -= 1
         columnFromQueen -= 1
         pieceHere = self.board[rowFromQueen][columnFromQueen]
         if pieceHere.getColour() is None:
            arrayOfSpaces.append([rowFromQueen, columnFromQueen])
         elif pieceHere.getColour() is not myPiece.getColour():
            arrayOfSpaces.append([rowFromQueen, columnFromQueen])
            break
         else:
            break
      return arrayOfSpaces
   
      ## fix issues with out of bounds spaces