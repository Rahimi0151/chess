from Board import Board
from Piece_King import Piece_King as King
from Piece_Pawn import Piece_Pawn as Pawn
from Piece_Rook import Piece_Rook as Rook
from Piece_Queen import Piece_Queen as Queen
from Piece_Knight import Piece_Knight as Knight
from Piece_Bishop import Piece_Bishop as Bishop

def initialize_board( board ):

    board.item[1][8] = Rook     ( board , "Black" , 1 , 8 )
    board.item[2][8] = Knight   ( board , "Black" , 2 , 8 )
    board.item[3][8] = Bishop   ( board , "Black" , 3 , 8 )
    board.item[4][8] = King     ( board , "Black" , 4 , 8 )
    board.item[5][8] = Queen    ( board , "Black" , 5 , 8 )
    board.item[6][8] = Bishop   ( board , "Black" , 6 , 8 )
    board.item[7][8] = Knight   ( board , "Black" , 7 , 8 )
    board.item[8][8] = Rook     ( board , "Black" , 8 , 8 )
    board.item[1][7] = Pawn     ( board , "Black" , 1 , 7 )
    board.item[2][7] = Pawn     ( board , "Black" , 2 , 7 )
    board.item[3][7] = Pawn     ( board , "Black" , 3 , 7 )
    board.item[4][7] = Pawn     ( board , "Black" , 4 , 7 )
    board.item[5][7] = Pawn     ( board , "Black" , 5 , 7 )
    board.item[6][7] = Pawn     ( board , "Black" , 6 , 7 )
    board.item[7][7] = Pawn     ( board , "Black" , 7 , 7 )
    board.item[8][7] = Pawn     ( board , "Black" , 8 , 7 )

    board.item[1][1] = Rook     ( board , "White" , 1 , 1 )
    board.item[2][1] = Knight   ( board , "White" , 2 , 1 )
    board.item[3][1] = Bishop   ( board , "White" , 3 , 1 )
    board.item[4][1] = King     ( board , "White" , 4 , 1 )
    board.item[5][1] = Queen    ( board , "White" , 5 , 1 )
    board.item[6][1] = Bishop   ( board , "White" , 6 , 1 )
    board.item[7][1] = Knight   ( board , "White" , 7 , 1 )
    board.item[8][1] = Rook     ( board , "White" , 8 , 1 )
    board.item[1][2] = Pawn     ( board , "White" , 1 , 2 )
    board.item[2][2] = Pawn     ( board , "White" , 2 , 2 )
    board.item[3][2] = Pawn     ( board , "White" , 3 , 2 )
    board.item[4][2] = Pawn     ( board , "White" , 4 , 2 )
    board.item[5][2] = Pawn     ( board , "White" , 5 , 2 )
    board.item[6][2] = Pawn     ( board , "White" , 6 , 2 )
    board.item[7][2] = Pawn     ( board , "White" , 7 , 2 )
    board.item[8][2] = Pawn     ( board , "White" , 8 , 2 )


board = Board()

initialize_board( board )

for i in board.item:
    print(i)
    print()

