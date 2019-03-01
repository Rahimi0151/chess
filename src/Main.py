from Board import Board
from Piece_King import Piece_King as King
from Piece_Rook import Piece_Rook as Rook
from Piece_Queen import Piece_Queen as Queen
from Piece_Knight import Piece_Knight as Knight
from Piece_Bishop import Piece_Bishop as Bishop

def initialize_board( board ):

    board.item[1][1] = Rook     ( "Black" , 1 , 1 )
    board.item[1][2] = Knight   ( "Black" , 1 , 2 )
    board.item[1][3] = Bishop   ( "Black" , 1 , 3 )
    board.item[1][4] = King     ( "Black" , 1 , 4 )
    board.item[1][5] = Queen    ( "Black" , 1 , 5 )
    board.item[1][6] = Bishop   ( "Black" , 1 , 6 )
    board.item[1][7] = Knight   ( "Black" , 1 , 7 )
    board.item[1][8] = Rook     ( "Black" , 1 , 8 )

    board.item[8][1] = Rook     ( "White" , 1 , 1 )
    board.item[8][2] = Knight   ( "White" , 1 , 2 )
    board.item[8][3] = Bishop   ( "White" , 1 , 3 )
    board.item[8][4] = King     ( "White" , 1 , 4 )
    board.item[8][5] = Queen    ( "White" , 1 , 5 )
    board.item[8][6] = Bishop   ( "White" , 1 , 6 )
    board.item[8][7] = Knight   ( "White" , 1 , 7 )
    board.item[8][8] = Rook     ( "White" , 1 , 8 )


board = Board()

initialize_board( board )




