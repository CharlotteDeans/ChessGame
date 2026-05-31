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

def inputLoop(text):
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

      if myBoard.isThereAPieceHere(xValue, yValue):
         loop = False
         print("Input valid")

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
      ## doesnt check specific piece type and such. Need to replace
      if not myBoard.canIMoveHere(x, y, newXValue, newYValue):
         print("Can't move here.")
         continue

      myBoard.movePiece(x, y, newXValue, newYValue)
      loop = False

myBoard = board.Board()
myBoard.printBoard()

# fix so inputLoop returns row and column
xAndYInputs = inputLoop("White's turn. Pick a square in chess notation (column + row):")
x = xAndYInputs[0]
y = xAndYInputs[1]
print(myBoard.whereCanKnightMove(x, y))
inputMoveTo("Pick a square to move your piece:", x, y)
myBoard.printBoard()
