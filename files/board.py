import piece

class Board():
   def __init__(self):
      board = [["empty" for x in range(8)] for y in range(8)]

      # images from https://github.com/lichess-org/lila/tree/master/public/piece/alpha

      # filling out board
      board[0][0] = piece.Piece('rook', 'black', 1, 'img/bR.svg')
      board[0][1] = piece.Piece('knight', 'black', 1, 'img/bN.svg')
      board[0][2] = piece.Piece('bishop', 'black', 1, 'img/bB.svg')
      board[0][3] = piece.Piece('queen', 'black', 0, 'img/bQ.svg')
      board[0][4] = piece.Piece('king', 'black', 0, 'img/bK.svg')
      board[0][5] = piece.Piece('bishop', 'black', 0, 'img/bB.svg')
      board[0][6] = piece.Piece('knight', 'black', 0, 'img/bN.svg')
      board[0][7] = piece.Piece('rook', 'black', 0, 'img/bR.svg')
      for x in range(8):
         board[1][x] = piece.Piece('pawn', 'black', 7 - x, 'img/bP.svg') ## counting backwards
      for x in range(8):
         board[6][x] = piece.Piece('pawn', 'white', x, 'img/wP.svg')
      board[7][0] = piece.Piece('rook', 'white', 0, 'img/wR.svg')
      board[7][1] = piece.Piece('knight', 'white', 0, 'img/wN.svg')
      board[7][2] = piece.Piece('bishop', 'white', 0, 'img/wB.svg')
      board[7][3] = piece.Piece('queen', 'white', 0, 'img/wQ.svg')
      board[7][4] = piece.Piece('king', 'white', 0, 'img/wK.svg')
      board[7][5] = piece.Piece('bishop', 'white', 1, 'img/bB.svg')
      board[7][6] = piece.Piece('knight', 'white', 1, 'img/bK.svg')
      board[7][7] = piece.Piece('rook', 'white', 1, 'img/bP.svg')
      self.board = board