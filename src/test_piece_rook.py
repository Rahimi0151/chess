from Piece_Rook import Piece_Rook
import pytest

def test_rook_can_go_in_straight_line():
    rook = Piece_Rook( "Black" , 1 , 2 )
    assert rook.get_position() == ( 1 , 2 )

    with pytest.raises(Exception):
        rook.go_to( 3 , 5 )
    assert rook.get_position() == ( 1 , 2 )


