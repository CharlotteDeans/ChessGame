import board
import square

myBoard = board.Board()
myBoard.printBoard()
COLUMN_ASCII = list(map(chr,range(97, 104)))

loop = True
while (loop):
   try:
      print("White's turn. Pick a square:",  end=" ")
      pieceInput = input()
      
      # fix below
      if pieceInput[0] >= 'a' and pieceInput[1] <= 'h':
         if pieceInput[1] in COLUMN_ASCII:
            print("Valid piece")
         else:
            print("Invalid char")
      else:
         print("invalid num")
      # ----------------------

   except:
      print("Invalid input, try again.")