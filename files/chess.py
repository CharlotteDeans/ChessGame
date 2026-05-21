import board
import square

LIST_OF_VALID_COLUMNS = list(map(chr,range(97, 105)))
LIST_OF_VALID_ROWS = list(range(1,9))
COLUMN_EQUIVILENT_NO = {
   'a': 1, 'A': 1,
   'b': 2, 'B': 2,
   'c': 3, 'C': 3,
   'd': 4, 'D': 4,
   'e': 5, 'E': 5,
   'f': 6, 'F': 6,
   'g': 7, 'G': 7,
   'h': 8, 'H': 8
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

loop = True
# fix
while (loop):
   print("White's turn. Pick a square:",  end=" ")
   pieceInput = input()
   try:
      row = int(pieceInput[1])
      column = pieceInput[0].lower()
      if checkForValidSquare(row, column) == True:
         realRowValue = row - 1
         realColumnValue = COLUMN_EQUIVILENT_NO(column) - 1
         aSquare = myBoard.checkForPiece(realRowValue, realColumnValue)
         if aSquare is not None:
            loop = False
   except:
      print("Invalid row")
# -----------------------------------------------------------------------
   
