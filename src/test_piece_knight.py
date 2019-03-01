from Piece_Knight import Piece_Knight
import pytest

def test_knight_can_go_in_L_shaped_line():
    knight = Piece_Knight( "Black" , 1 , 2 )
    assert knight.get_position() == ( 1 , 2 )

    knight.go_to( 3 , 3 )
    assert knight.get_position() == ( 3 , 3 )

    knight.go_to( 5 , 2 )
    assert knight.get_position() == ( 5 , 2 )

    with pytest.raises(Exception):
        knight.go_to( 3 , 5 )
    assert knight.get_position() == ( 5 , 2 )
