import square

class Board():
   def __init__(self):
      board = [[square.Square() for x in range(8)] for y in range(8)]

      # row(num)/column(char)
      # row is y axis and column is x axis

      # # filling out board
      # board[0][0] = square.Square('rook', 'white', 1)
      # board[0][1] = square.Square('knight', 'white', 1)
      # board[0][2] = square.Square('bishop', 'white', 1)
      # board[0][3] = square.Square('queen', 'white', 0)
      # board[0][4] = square.Square('king', 'white', 0)
      # board[0][5] = square.Square('bishop', 'white', 0)
      # board[0][6] = square.Square('knight', 'white', 0)
      # board[0][7] = square.Square('rook', 'white', 0)
      # for y in range(8):
      #    board[1][y] = square.Square('pawn', 'white', 7 - y) ## counting backwards
      # for y in range(8):
      #    board[6][y] = square.Square('pawn', 'black', y)
      # board[7][0] = square.Square('rook', 'black', 0)
      # board[7][1] = square.Square('knight', 'black', 0)
      # board[7][2] = square.Square('bishop', 'black', 0)
      # board[7][3] = square.Square('queen', 'black', 0)
      # board[7][4] = square.Square('king', 'black', 0)
      # board[7][5] = square.Square('bishop', 'black', 1)
      # board[7][6] = square.Square('knight', 'black', 1)
      # board[7][7] = square.Square('rook', 'black', 1)
      # board[3][4] = square.Square('bishop', 'white', 2)

      # filling out board
      # first is char, second is num
      # x/y - column/row - char/num
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
      board[7][7] = square.Square('pawn', 'white', 8)
      self.board = board

   def printBoard(self):
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

   def returnPiece(self, x, y):
      thePiece = self.board[x][y]
      if thePiece.getType() is None:
         return None
      else:
         return thePiece
   
   def printPieceDetails(self,x,y):
      thePiece = self.board[x][y]
      print(thePiece.getType())
      print(thePiece.getColour())

   def isXOrYInBounds(self, num):
      if num < 0 or num > 7:
         return False
      return True

   def isThereAPieceHere(self, x, y):
      if not self.isXOrYInBounds(x) or not self.isXOrYInBounds(y):
         return False
      piece = self.board[x][y]
      if piece.getType() is None:
         return False
      return True
   
   ## change or delete because it's part of bad code
   def canIMoveHere(self, oldXValue, oldYValue, newXValue, newYValue):
      myPiece = self.board[oldXValue][oldYValue]
      pieceToOvertake = self.board[newXValue][newYValue]
      if pieceToOvertake.getType() is None:
         return True
      elif pieceToOvertake.getColour() is not myPiece.getColour():
         return True
      return False
   
   def movePiece(self, oldX, oldY, newX, newY):
      self.board[newX][newY] = self.board[oldX][oldY]
      self.board[oldX][oldY] = square.Square()

   def whereCanKingMove(self, x, y):
      myPiece = self.board[x][y]
      arrayOfSpaces = []
      for x in range(3):
         xInLoop = x - 1 + x
         if xInLoop <= 7 and xInLoop >= 0:
            for y in range(3):
               yInLoop = y - 1 + y
               if yInLoop <= 7 and yInLoop >= 0:
                  arrayOfSpaces.append([xInLoop, yInLoop])

      return arrayOfSpaces
   # queen can move anywhere so long as either x or y (but not both) doesnt change or the different between x and y is the same and a piece isnt in the way
   def whereCanQueenMove(self, x, y):
      arrayOfSpaces = self.calculateOrthogonalMovement(x,y)
      arrayOfDiagonalSpaces = self.calculateDiagonalMovement(x,y)
      for diagonalSpace in range(len(arrayOfDiagonalSpaces)):
         arrayOfSpaces.append(arrayOfDiagonalSpaces[diagonalSpace])

      return arrayOfSpaces
   
   def whereCanRookMove(self, x, y):
      arrayOfSpaces = self.calculateOrthogonalMovement(x, y)
      return arrayOfSpaces

   def whereCanBishopMove(self, x, y):
      arrayOfSpaces = self.calculateDiagonalMovement(x, y)
      return arrayOfSpaces
   
   def whereCanPawnMoveWithoutTaking(self, x, y):
      # if pawn's first move, can move 2 spaces
      arrayOfSpaces = []
      myPiece = self.board[x][y]
      # black moves down, white up
      pieceColour = myPiece.getColour()
      j = 1
      if not myPiece.hasPieceMoved():
         j += 1
         myPiece.switchPieceMoved()
      for i in range(j):
         if pieceColour is 'white':
            newY = y + i + 1
         else:
            newY = y - (i + 1)
         answer = self.movementPlacementLogic(x,y,x,newY)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([x,newY])
         if self.canIMoveAnymore(answer):
            break
      return arrayOfSpaces

## complete here
   def whereCanPawnMoveWhileTaking(self,x,y):
      ## where pawn can only move if it take (x-1,y+1 and x+1,y+1)
      ## either piece is at this location or this location y-1
      arrayOfSpaces = []
      myPiece = self.board[x][y]
      pieceColour = myPiece.getColour()
      
      newX = x - 1
      oppX = x - 1
      oppY = y
      
      if pieceColour is 'white':
         newY = y + 1
      else:
         newY = y - 1

      # up left
      answer = self.movementPlacementLogic(x,y,newX,newY)
      if self.canIMoveHere2(answer) and self.canITakePiece(x,y,oppX,oppY):
         arrayOfSpaces.append([newX,newY])
      
      # up right
      newX = x + 1
      oppX = x + 1
      answer = self.movementPlacementLogic(x,y,newX,newY)
      if self.canIMoveHere2(answer) and self.canITakePiece(x,y,oppX,oppY):
         arrayOfSpaces.append([newX,newY])

      return arrayOfSpaces
      
   ## when there is another piece 
   # safer than old version
   # assumes old piece is actual piece
   def canITakePiece(self,oldX, oldY, newX, newY):
      if not self.isXOrYInBounds(oldX) or not self.isXOrYInBounds(oldY) or not self.isXOrYInBounds(newX) or not self.isXOrYInBounds(newY):
         return False
      piece = self.board[oldX][oldY]
      oppPiece = self.board[newX][newY]
      if piece.getColour() is not oppPiece.getColour() and oppPiece.getType() is not None:
         return True
      return False
      

   def isSpaceFree(self, x, y):
      space = self.board[x][y]
      if space.getColour() is None:
         return True
      else:
         return False

   def isSpaceOutOfBounds(self, x, y):
      if x < 0 or x > 7 or y < 0 or y > 7:
         return True
      else:
         return False

   def movementPlacementLogic(self, oldX, oldY, newX, newY):
      if self.isSpaceOutOfBounds(newX, newY):
         return 'OOB'
      elif self.isSpaceFree(newX, newY):
         return 'SpaceIsFree'
      elif self.canITakePiece(oldX, oldY, newX, newY):
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

   def calculateOrthogonalMovement(self, x, y):
      arrayOfSpaces = []
      for x in range(7):
         xRightOfPiece = x + x + 1
         answer = self.movementPlacementLogic(x, y, xRightOfPiece, y)
         print(answer)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([xRightOfPiece, y])
         if self.canIMoveAnymore(answer):
            break

      for x in range(7):
         xLeftOfPiece = x - (x + 1)
         answer = self.movementPlacementLogic(x, y, xLeftOfPiece, y)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([xLeftOfPiece, y])
         if self.canIMoveAnymore(answer):
            break

      for y in range(7):
         yAbovePiece = y + y + 1
         answer = self.movementPlacementLogic(x, y, x, yAbovePiece)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([x, yAbovePiece])
         if self.canIMoveAnymore(answer):
            break

      for y in range(7):
         xBelowPiece = y - (y + 1)
         answer = self.movementPlacementLogic(x, y, x, xBelowPiece)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([x, xBelowPiece])
         if self.canIMoveAnymore(answer):
            break

      return arrayOfSpaces
   
   def calculateDiagonalMovement(self, x, y):
      # +1 to row and column until out of bounds or hit another piece
      # then +1 row and -1 column, -1 row and +1 column, -1 row and column
      arrayOfSpaces = []

      xFromPiece = x
      yFromPiece = y
      # up right
      for spaces in range(7):
         xFromPiece += 1
         yFromPiece += 1
         answer = self.movementPlacementLogic(x, y, xFromPiece, yFromPiece)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([xFromPiece, yFromPiece])
         if self.canIMoveAnymore(answer):
            break

      xFromPiece = x
      yFromPiece = y
      # up left
      for spaces in range(7):
         xFromPiece -= 1
         yFromPiece += 1
         answer = self.movementPlacementLogic(x, y, xFromPiece, yFromPiece)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([xFromPiece, yFromPiece])
         if self.canIMoveAnymore(answer):
            break

      # down right
      xFromPiece = x
      yFromPiece = y
      for spaces in range(7):
         xFromPiece += 1
         yFromPiece -= 1
         answer = self.movementPlacementLogic(x, y, xFromPiece, yFromPiece)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([xFromPiece, yFromPiece])
         if self.canIMoveAnymore(answer):
            break

      # down left
      xFromPiece = x
      yFromPiece = y
      for spaces in range(7):
         xFromPiece -= 1
         yFromPiece -= 1
         answer = self.movementPlacementLogic(x, y, xFromPiece, yFromPiece)
         if self.canIMoveHere2(answer):
            arrayOfSpaces.append([xFromPiece, yFromPiece])
         if self.canIMoveAnymore(answer):
            break

      return arrayOfSpaces