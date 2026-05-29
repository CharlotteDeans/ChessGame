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
      board[3][3] = square.Square('bishop', 'white', 2)
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
   
   def isRowOrColumnInBounds(self, num):
      if num < 0 or num > 7:
         return False
      return True

   def isThereAPieceHere(self, row, column):
      if not self.isRowOrColumnInBounds(row) or not self.isRowOrColumnInBounds(column):
         return False
      piece = self.board[row][column]
      if piece.getType() is None:
         return False
      return True
   
   ## change or delete because it's part of bad code
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
      arrayOfSpaces = self.calculateOrthogonalMovement(row,column)
      arrayOfDiagonalSpaces = self.calculateDiagonalMovement(row,column)
      for diagonalSpace in range(len(arrayOfDiagonalSpaces)):
         arrayOfSpaces.append(arrayOfDiagonalSpaces[diagonalSpace])

      return arrayOfSpaces
   
   def whereCanRookMove(self, row, column):
      arrayOfSpaces = self.calculateOrthogonalMovement(row, column)
      return arrayOfSpaces

   def whereCanBishopMove(self, row, column):
      arrayOfSpaces = self.calculateDiagonalMovement(row, column)
      return arrayOfSpaces

   ## when there is another piece 
   def canITakePiece(self,oldRow, oldColumn, newRow, newColumn):
      myPiece = self.board[oldRow][oldColumn]
      pieceHere = self.board[newRow][newColumn]
      if pieceHere.getColour() is not myPiece.getColour():
         return True
      else:
         return False

   def isSpaceFree(self, row, column):
      space = self.board[row][column]
      if space.getColour() is None:
         return True
      else:
         return False

   def isSpaceOutOfBounds(self, row, column):
      if row < 0 or row > 7 or column < 0 or column > 7:
         return True
      else:
         return False

   def movementPlacementLogic(self, oldRow, oldColumn, newRow, newColumn):
      if self.isSpaceOutOfBounds(newRow, newColumn):
         return 'OOB'
      elif self.isSpaceFree(newRow, newColumn):
         return 'SpaceIsFree'
      elif self.canITakePiece(oldRow, oldColumn, newRow, newColumn):
         return 'SpaceHasOpponentPiece'
      else:
         return 'SpaceHasPlayerPiece'
      
   def canIMoveHere2(self, answer):
         if (answer == 'SpaceIsFree' or answer == 'SpaceHasOpponentPiece'):
            return True
         else:
            return False
         
   def canIMoveAnymore(self, answer):
      if (answer == 'OOB' or answer == 'SpaceHasOpponentPiece' or answer == 'SpaceHasPlayerPiece'):
         return True
      else:
         return False

   def calculateOrthogonalMovement(self, row, column):
      arrayOfSpaces = []
      for x in range(7):
         rowAbovePiece = row + x + 1
         answer = self.movementPlacementLogic(row, column, rowAbovePiece, column)
         print(answer)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([rowAbovePiece, column])
         if self.canIMoveAnymore(answer):
            break

      for x in range(7):
         rowBelowPiece = row - (x + 1)
         answer = self.movementPlacementLogic(row, column, rowBelowPiece, column)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([rowBelowPiece, column])
         if self.canIMoveAnymore(answer):
            break

      for y in range(7):
         columnRightOfPiece = column + y + 1
         answer = self.movementPlacementLogic(row, column, row, columnRightOfPiece)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([row, columnRightOfPiece])
         if self.canIMoveAnymore(answer):
            break

      for y in range(7):
         columnLeftOfPiece = column - (y + 1)
         answer = self.movementPlacementLogic(row, column, row, columnLeftOfPiece)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([row, columnLeftOfPiece])
         if self.canIMoveAnymore(answer):
            break

      return arrayOfSpaces
   
   def calculateDiagonalMovement(self, row, column):
      # +1 to row and column until out of bounds or hit another piece
      # then +1 row and -1 column, -1 row and +1 column, -1 row and column
      arrayOfSpaces = []

      rowFromPiece = row
      columnFromPiece = column
      # up right
      for spaces in range(7):
         rowFromPiece += 1
         columnFromPiece += 1
         answer = self.movementPlacementLogic(row, column, rowFromPiece, columnFromPiece)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([rowFromPiece, columnFromPiece])
         if self.canIMoveAnymore(answer):
            break

      rowFromPiece = row
      columnFromPiece = column
      # up left
      for spaces in range(7):
         rowFromPiece -= 1
         columnFromPiece += 1
         answer = self.movementPlacementLogic(row, column, rowFromPiece, columnFromPiece)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([rowFromPiece, columnFromPiece])
         if self.canIMoveAnymore(answer):
            break

      # down right
      rowFromPiece = row
      columnFromPiece = column
      for spaces in range(7):
         rowFromPiece += 1
         columnFromPiece -= 1
         answer = self.movementPlacementLogic(row, column, rowFromPiece, columnFromPiece)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([rowFromPiece, columnFromPiece])
         if self.canIMoveAnymore(answer):
            break

      # down left
      rowFromPiece = row
      columnFromPiece = column
      for spaces in range(7):
         rowFromPiece -= 1
         columnFromPiece -= 1
         answer = self.movementPlacementLogic(row, column, rowFromPiece, columnFromPiece)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([rowFromPiece, columnFromPiece])
         if self.canIMoveAnymore(answer):
            break

      return arrayOfSpaces