import board
import square

LIST_OF_VALID_COLUMNS = list(map(chr,range(97, 105)))
LIST_OF_VALID_ROWS = list(range(1,9))
COLUMN_EQUIVILENT_NO = {
   'a': 1,
   'b': 2,
   'c': 3,
   'd': 4,
   'e': 5,
   'f': 6,
   'g': 7,
   'h': 8
}

def checkForValidSquare(row, column):
   try:
      if column in LIST_OF_VALID_COLUMNS:
         if row in LIST_OF_VALID_ROWS:
            print("Valid piece")
            return True
         else:
            print("Invalid row")
      else:
         print("Invalid column")
   except:
      print("Invalid row")
   return False

myBoard = board.Board()
myBoard.printBoard()

print(myBoard.whereCanQueenMove(3,0))

loop = True
while (loop):
   print("White's turn. Pick a square:",  end=" ")
   pieceInput = input()
   try:
      row = int(pieceInput[1])
      column = pieceInput[0].lower()
      if checkForValidSquare(row, column) == True:
         actualRow = row - 1
         actualColumn = COLUMN_EQUIVILENT_NO[column] - 1
         if myBoard.isThereAPieceHere(actualRow, actualColumn) == True:
            loop = False
   except:
      print("Invalid row")

## pick a spot, if tile with the same piece, can't move. Overtake opposite piece.
loop = True
while (loop):
   print("Pick a spot to move your piece. Pick a square:",  end=" ")
   pieceInput = input()
   try:
      newRow = int(pieceInput[1])
      newColumn = pieceInput[0].lower()
      if checkForValidSquare(newRow, newColumn) == True:
         actualNewRow = newRow - 1
         actualNewColumn = COLUMN_EQUIVILENT_NO[newColumn] - 1
         print(1)
         if myBoard.canIMoveHere(actualRow, actualColumn, actualNewRow, actualNewColumn) == True:
            myBoard.movePiece(actualRow, actualColumn, actualNewRow, actualNewColumn)
            loop = False
         else:
            print("Can't move here. ")
      else:
         print("Invalid tile, try again.")
   except:
      print("Invalid row")