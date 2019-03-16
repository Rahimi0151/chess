from Board import Board
from Piece_Rook import Piece_Rook
import pytest

def test_rook_can_go_in_straight_line():
    rook = Piece_Rook( Board() , "Black" , 1 , 2 )
    assert rook.get_position() == ( 1 , 2 )

    with pytest.raises(Exception):
        rook.go_to( 3 , 5 )
    assert rook.get_position() == ( 1 , 2 )

def test_rook_cant_jump_over_any_piece():
    board = Board()
    rook1 = Piece_Rook( board , "Black" , 1 , 3)
    rook2 = Piece_Rook( board , "Black" , 1 , 4)

    with pytest.raises(Exception):
        rook1.go_to( 1 , 5 )
    assert rook1.get_position() == ( 1 , 3 )




