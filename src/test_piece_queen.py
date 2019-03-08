from Board import Board
from Piece_Queen import Piece_Queen
import pytest

def test_queen_can_go_in_diagonal_or_straight_line():
    queen = Piece_Queen( Board() , "Black" , 1 , 2 )
    assert queen.get_position() == ( 1 , 2 )

    # Diagonal
    queen.go_to( 3 , 4 )
    assert queen.get_position() == ( 3 , 4 )

    # Straint
    queen.go_to( 7 , 4 )
    assert queen.get_position() == ( 7 , 4 )

    # Not other types
    with pytest.raises(Exception):
        queen.go_to( 3 , 5 )
    assert queen.get_position() == ( 7 , 4 )
