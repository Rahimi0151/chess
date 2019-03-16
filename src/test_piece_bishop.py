from Board import Board
from Piece_Bishop import Piece_Bishop
import pytest


def test_bishop_can_go_in_diagonal_line():
    bishop = Piece_Bishop( Board() , "Black" , 1 , 2 )
    assert bishop.get_position() == ( 1 , 2 )

    with pytest.raises(Exception):
        bishop.go_to( 3 , 5 )
    assert bishop.get_position() == ( 1 , 2 )

    bishop.go_to( 3 , 4 )
    assert bishop.get_position() == ( 3 , 4 )
