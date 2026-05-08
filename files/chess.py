board = [["empty" for x in range(8)] for y in range(8)]

# filling out board
board[0][0] = "blackRook";
board[0][1] = "blackKnight";
board[0][2] = "blackBishop";
board[0][3] = "blackQueen";
board[0][4] = "blackKing";
board[0][5] = "blackBishop";
board[0][6] = "blackKnight";
board[0][7] = "blackRook";
for x in range(8):
   board[1][x] = "blackPawn";
for x in range(8):
   board[6][x] = "whitePawn";
board[7][0] = "whiteRook";
board[7][1] = "whiteKnight";
board[7][2] = "whiteBishop";
board[7][3] = "whiteQueen";
board[7][4] = "whiteKing";
board[7][5] = "whiteBishop";
board[7][6] = "whiteKnight";
board[7][7] = "whiteRook";

for space in board:
   print(space);

