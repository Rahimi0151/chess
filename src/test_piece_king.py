from Board import Board
from Piece_King import Piece_King
import pytest

def test_king_can_go_in_one_square_at_a_time():
    king = Piece_King( Board() , "Black" , 1 , 2 )
    assert king.get_position() == ( 1 , 2 )

    with pytest.raises(Exception):
        king.go_to( 3 , 5 )
    assert king.get_position() == ( 1 , 2 )

    king.go_to( 2 , 3 )
    assert king.get_position() == ( 2 , 3 )



