import board
import square

# LIST_OF_VALID_COLUMNS = list(map(chr,range(97, 105))) # a to h
LIST_OF_VALID_ROWS = list(range(0,8)) # 0 to 7
COLUMN_EQUIVILENT_NO = {
   'a': 0,
   'b': 1,
   'c': 2,
   'd': 3,
   'e': 4,
   'f': 5,
   'g': 6,
   'h': 7
}

def returnActualYValue(pieceInput):
   return int(pieceInput[1]) - 1

def returnActualXValue(pieceInput):
   return COLUMN_EQUIVILENT_NO[pieceInput[0].lower()]

def isRowOrColumnInBounds(num):
   if num < 0 or num > 7:
      return False
   return True

def inputLoop(text, colour):
   loop = True
   while (loop):
      print(text,  end=" ")
      pieceInput = input()

      if pieceInput == "":
         print("No input, try again.")
         continue
      try:
         xValue = returnActualXValue(pieceInput)
      except:
         print("Invalid column, try again.")
         continue

      try:
         yValue = returnActualYValue(pieceInput)
      except:
         print("Invalid row, try again.")
         continue

      if myBoard.returnPieceColour(xValue, yValue) is not colour:
         print("Wrong colour, pick a colour of your side.")
         continue
      
      if not myBoard.isThereAPieceHere(xValue, yValue):
         print ("No piece here.")
         continue

      if not myBoard.canPieceMove(xValue, yValue):
         print("Piece cannot move. Try another piece.")
         continue

      loop = False

   xAndYInputs = []
   xAndYInputs.append(xValue)
   xAndYInputs.append(yValue)
   return xAndYInputs

def inputMoveTo(text, x, y):
   loop = True
   while (loop):
      print(text,  end=" ")
      pieceInput = input()

      if pieceInput == "":
         print("No input, try again.")
         continue

      try:
         newXValue = returnActualXValue(pieceInput)
      except:
         print("Invalid column, try again.")
         continue

      if not isRowOrColumnInBounds(newXValue):
         print("Column is out of bounds.")
         continue

      try:
         newYValue = returnActualYValue(pieceInput)
      except:
         print("Invalid row, try again.")
         continue

      if not isRowOrColumnInBounds(newYValue):
         print("Row is out of bounds.")
         continue
      # check piece type and return equivilent available spaces
      # compare available spaces with input space
      
      arrayOfSpaces = myBoard.returnListOfAvailableSpaces(x,y)
      pieceType = myBoard.returnPieceType(x, y)
      arrayOfSpacesEnPassant = []
      if pieceType is 'pawn':
         arrayOfSpacesEnPassant = myBoard.returnEnPassantAvailableSpaces(x, y)
      
      print(arrayOfSpaces)
      newSpace = [newXValue,newYValue]
      if newSpace in arrayOfSpaces:
         myBoard.movePiece(x, y, newXValue, newYValue)
         loop = False
      elif newSpace in arrayOfSpacesEnPassant:
         killOppWithEnPassant(x,y,newXValue, newYValue)
         myBoard.movePiece(x,y,newXValue,newYValue)
         loop = False
      else:
         print("Can't move here.")
         continue

def killOppWithEnPassant(x,y,newAllyXSpace,newAllyYSpace):
   pieceColour = myBoard.returnPieceColour(x, y)
   oppY = newAllyYSpace
   if pieceColour == 'white':
      oppY -= 1
   else:
      oppY += 1
   oppX = newAllyXSpace
   myBoard.killPiece(oppX,oppY)
   pass

def gameLoop():
   currentColour = 'white'
   while True:
      if currentColour is 'white':
         xAndYInputs = inputLoop("White's turn. Pick a square in chess notation (column + row):", currentColour)
      else:
         xAndYInputs = inputLoop("Black's turn. Pick a square in chess notation (column + row):", currentColour)
      x = xAndYInputs[0]
      y = xAndYInputs[1]
      inputMoveTo("Pick a square to move your piece:", x, y)
      myBoard.printBoard()
      if currentColour is 'white':
         currentColour = 'black'
      else:
         currentColour = 'white'
      if myBoard.checkForCheck(currentColour):
         print("Check!")

myBoard = board.Board()
myBoard.printBoard()
gameLoop()