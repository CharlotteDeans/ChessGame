import square

class Board():
   def __init__(self):
      board = [[square.Square() for x in range(8)] for y in range(8)]

      # filling out board
      board[0][0] = square.Square('rook', 'black', 1)
      board[0][1] = square.Square('knight', 'black', 1)
      board[0][2] = square.Square('bishop', 'black', 1)
      board[0][3] = square.Square('queen', 'black', 0)
      board[0][4] = square.Square('king', 'black', 0)
      board[0][5] = square.Square('bishop', 'black', 0)
      board[0][6] = square.Square('knight', 'black', 0)
      board[0][7] = square.Square('rook', 'black', 0)
      for x in range(8):
         board[1][x] = square.Square('pawn', 'black', 7 - x) ## counting backwards
      for x in range(8):
         board[6][x] = square.Square('pawn', 'white', x)
      board[7][0] = square.Square('rook', 'white', 0)
      board[7][1] = square.Square('knight', 'white', 0)
      board[7][2] = square.Square('bishop', 'white', 0)
      board[7][3] = square.Square('queen', 'white', 0)
      board[7][4] = square.Square('king', 'white', 0)
      board[7][5] = square.Square('bishop', 'white', 1)
      board[7][6] = square.Square('knight', 'white', 1)
      board[7][7] = square.Square('rook', 'white', 1)
      self.board = board

   def printBoard(self):
      rowNum = 8
      for row in self.board:
         print(rowNum, end=" ")
         rowNum -= 1
         for rSquare in row:
            print(rSquare.getSymbol(), end=" ")
         print()
      print("  a b c d e f g h")

   def checkForPiece(self, letter, no):
      
      return