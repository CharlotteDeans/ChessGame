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

def inputLoop(text):
   loop = True
   while (loop):
      print(text,  end=" ")
      pieceInput = input()

      if pieceInput == "":
         print("No input, try again.")
         continue
      try:
         row = returnActualRowValue(pieceInput)
      except:
         print("Invalid row, try again.")
         continue

      try:
         column = returnActualColumnValue(pieceInput)
      except:
         print("Invalid column, try again.")
         continue

      if myBoard.isThereAPieceHere(row, column):
         loop = False
         print("Input valid")

def isRowOrColumnInBounds(num):
   if num < 0 or num > 7:
      return False
   return True

def inputMoveTo(text, row, column):
   loop = True
   while (loop):
      print(text,  end=" ")
      pieceInput = input()

      if pieceInput == "":
         print("No input, try again.")
         continue
      try:
         newRow = returnActualRowValue(pieceInput)
      except:
         print("Invalid row, try again.")
         continue
      try:
         newColumn = returnActualColumnValue(pieceInput)
      except:
         print("Invalid column, try again.")
         continue

      if not isRowOrColumnInBounds(newRow):
         print("Row is out of bounds.")
         continue

      if not isRowOrColumnInBounds(newColumn):
         print("Column is out of bounds.")
         continue
      
      if not myBoard.canIMoveHere(row, column, newRow, newColumn):
         print("Can't move here.")
         continue

      myBoard.movePiece(row, column, newRow, newColumn)
      loop = False

      # try:
      #    newRow = int(pieceInput[1])
      #    newColumn = pieceInput[0].lower()
      #    if checkForValidSquare(newRow, newColumn) == True:
      #       actualNewRow = newRow - 1
      #       actualNewColumn = COLUMN_EQUIVILENT_NO[newColumn] - 1
      #       print(1)
      #       if myBoard.canIMoveHere(actualRow, actualColumn, actualNewRow, actualNewColumn) == True:
      #          myBoard.movePiece(actualRow, actualColumn, actualNewRow, actualNewColumn)
      #          loop = False
      #       else:
      #          print("Can't move here. ")
      #    else:
      #       print("Invalid tile, try again.")
      # except:
      #    print("Invalid row")
def returnActualRowValue(pieceInput):
   return int(pieceInput[1]) - 1

def returnActualColumnValue(pieceInput):
   return COLUMN_EQUIVILENT_NO[pieceInput[0].lower()]

myBoard = board.Board()
myBoard.printBoard()

# fix so inputLoop returns row and column
inputLoop("White's turn. Pick a square:")
inputMoveTo("Pick a spot to move your piece. Pick a square:")
