import square

class Board():
   def __init__(self):
      board = [[square.Square() for x in range(8)] for y in range(8)]
      # filling out board
      # first is char, second is num
      # x/y - column/row - char/num
      board[0][0] = square.Square('rook', 'white')
      board[1][0] = square.Square('knight', 'white')
      board[2][0] = square.Square('bishop', 'white')
      board[3][0] = square.Square('queen', 'white')
      board[4][0] = square.Square('king', 'white')
      board[5][0] = square.Square('bishop', 'white')
      board[6][0] = square.Square('knight', 'white')
      board[7][0] = square.Square('rook', 'white')
      for x in range(8):
         board[x][1] = square.Square('pawn', 'white') ## counting backwards
      for x in range(8):
         board[x][6] = square.Square('pawn', 'black')
      board[0][7] = square.Square('rook', 'black')
      board[1][7] = square.Square('knight', 'black')
      board[2][7] = square.Square('bishop', 'black')
      board[3][7] = square.Square('queen', 'black')
      board[4][7] = square.Square('king', 'black')
      board[5][7] = square.Square('bishop', 'black')
      board[6][7] = square.Square('knight', 'black')
      board[7][7] = square.Square('rook', 'black')
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

   def returnPieceType(self,x,y):
      thePiece = self.board[x][y]
      return thePiece.getType()

   def returnPieceColour(self,x,y):
      thePiece = self.board[x][y]
      return thePiece.getColour()
   
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
   
   def movePiece(self, oldX, oldY, newX, newY):

      myPiece = self.board[oldX][oldY]
      ## when this colour moves, all pawns of this colour and un-enpassantable, apart from a piece that's just made itself susceptible (which is made enpassantable after this block)
      for x in range(8):
         for y in range(8):
            thisPiece = self.board[x][y]
            if thisPiece.getType() is 'pawn' and thisPiece.getColour() is myPiece.getColour():
               thisPiece.switchEnPassantOff()

      ## check for enpassant and turn on piece moved if
      # if my piece is pawn and oldY+2 = newY
      if myPiece.getType() is 'pawn' and oldY+2 is newY or oldY-2 is newY:
         myPiece.switchEnPassantOn()
         myPiece.switchPieceMoved()
      if myPiece.getType() is 'pawn' and oldY+1 is newY or oldY-1 is newY:
         myPiece.switchPieceMoved()
      # then move
      self.board[newX][newY] = self.board[oldX][oldY]
      self.board[oldX][oldY] = square.Square()

   def killPiece(self, x, y):
      self.board[x][y] = square.Square()

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

   def whereCanPawnMove(self, x, y):
      # if pawn's first move, can move 2 spaces
      arrayOfSpaces = []
      myPiece = self.board[x][y]
      pieceColour = myPiece.getColour()

      # without taking
      j = 1
      if not myPiece.hasPieceMoved():
         j += 1
      for i in range(j):
         if pieceColour is 'white':
            newY = y + i + 1
         else:
            newY = y - (i + 1)
         answer = self.movementPlacementLogic(x,y,x,newY)
         if self.canIMoveHere(answer):
            arrayOfSpaces.append([x,newY])
         if self.canIMoveAnymore(answer):
            break
      
      # while taking
      newX = x - 1
      if pieceColour is 'white':
         newY = y + 1
      else:
         newY = y - 1

      # up left
      answer = self.movementPlacementLogic(x,y,newX,newY)
      if self.canIMoveHere(answer) and self.canITakePiece(x,y,newX,newY):
         arrayOfSpaces.append([newX,newY])
      
      # up right
      newX = x + 1

      answer = self.movementPlacementLogic(x,y,newX,newY)
      if self.canIMoveHere(answer) and self.canITakePiece(x,y,newX,newY):
         arrayOfSpaces.append([newX,newY])

      return arrayOfSpaces
   
   def whereCanPawnEnPassant(self,x,y):
      ## where pawn can only move if it take (x-1,y+1 and x+1,y+1)
      ## and opposing pawn travelled two spaces on the previous turn
      arrayOfSpaces = []
      myPiece = self.board[x][y]
      pieceColour = myPiece.getColour()
      newX = x - 1
      oppX = x - 1
      oppY = y
      
      oppPiece = self.board[oppX][oppY]

      if pieceColour is 'white':
         newY = y + 1
      else:
         newY = y - 1

      # up left
      answer = self.movementPlacementLogic(x,y,newX,newY)

      # print(self.canIMoveHere(answer))
      # print(self.canITakePiece(x,y,oppX,oppY))
      # print(oppPiece.getEnPassantable())
      if self.canIMoveHere(answer) and self.canITakePiece(x,y,oppX,oppY) and oppPiece.getEnPassantable():
         arrayOfSpaces.append([newX,newY])
      
      # up right
      newX = x + 1
      oppX = x + 1

      oppPiece = self.board[oppX][oppY]

      answer = self.movementPlacementLogic(x,y,newX,newY)
      if self.canIMoveHere(answer) and self.canITakePiece(x,y,oppX,oppY) and oppPiece.getEnPassantable():
         arrayOfSpaces.append([newX,newY])
      
      return arrayOfSpaces

   def whereCanKnightMove(self, x, y):
      arrayOfPotentialSpaces = [ [x-2, y+1], [x-2, y-1], [x+2, y+1], [x+2, y-1], [x-1, y+2], [x+1, y+2], [x-1, y-2], [x+1, y-2] ]
      arrayOfSpaces = []
      for spaces in arrayOfPotentialSpaces:
         newX = spaces[0]
         newY = spaces[1]
         answer = self.movementPlacementLogic(x,y,newX,newY)
         if self.canIMoveHere(answer) is True:
            arrayOfSpaces.append(spaces)
      return arrayOfSpaces
   # assumes old piece is actual piece
   def canITakePiece(self,oldX, oldY, newX, newY):
      if self.isSpaceOutOfBounds(oldX, oldY) or self.isSpaceOutOfBounds(newX,newY):
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
      
   def canIMoveHere(self, answer):
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
         if self.canIMoveHere(answer):
            arrayOfSpaces.append([xRightOfPiece, y])
         if self.canIMoveAnymore(answer):
            break

      for x in range(7):
         xLeftOfPiece = x - (x + 1)
         answer = self.movementPlacementLogic(x, y, xLeftOfPiece, y)
         if self.canIMoveHere(answer):
            arrayOfSpaces.append([xLeftOfPiece, y])
         if self.canIMoveAnymore(answer):
            break

      for y in range(7):
         yAbovePiece = y + y + 1
         answer = self.movementPlacementLogic(x, y, x, yAbovePiece)
         if self.canIMoveHere(answer):
            arrayOfSpaces.append([x, yAbovePiece])
         if self.canIMoveAnymore(answer):
            break

      for y in range(7):
         xBelowPiece = y - (y + 1)
         answer = self.movementPlacementLogic(x, y, x, xBelowPiece)
         if self.canIMoveHere(answer):
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
         if self.canIMoveHere(answer):
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
         if self.canIMoveHere(answer):
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
         if self.canIMoveHere(answer):
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
         if self.canIMoveHere(answer):
            arrayOfSpaces.append([xFromPiece, yFromPiece])
         if self.canIMoveAnymore(answer):
            break

      return arrayOfSpaces