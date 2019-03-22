from Board import Board
from Piece_Queen import Piece_Queen
import pytest

def test_queen_can_go_in_diagonal_or_straight_line():
    queen = Piece_Queen( Board() , "Black" , 1 , 2 )
    assert queen.get_position() == ( 1 , 2 )

    # Diagonal
    queen.go_to( 3 , 4 )
    assert queen.get_position() == ( 3 , 4 )

    # Horizental
    queen.go_to( 7 , 4 )
    assert queen.get_position() == ( 7 , 4 )

    # Vertical
    queen.go_to( 7 , 1 )
    assert queen.get_position() == ( 7 , 1 )

    # Not other types
    with pytest.raises(Exception):
        queen.go_to( 6 , 5 )
    assert queen.get_position() == ( 7 , 1 )

def test_queen_cant_jump_over_any_piece():

    # diagonal
    board = Board()
    queen1 = Piece_Queen( board , "Black" , 1 , 1)
    queen2 = Piece_Queen( board , "Black" , 2 , 2)

    with pytest.raises(Exception):
        queen1.go_to( 3 , 3 )
    assert queen1.get_position() == ( 1 , 1 )


    # vertical
    board = Board()
    queen1 = Piece_Queen( board , "Black" , 1 , 1)
    queen2 = Piece_Queen( board , "Black" , 1 , 2)
    
    with pytest.raises(Exception):
        queen1.go_to( 1 , 3 )
    assert queen1.get_position() == ( 1 , 1 )


    # horizental
    board = Board()
    queen1 = Piece_Queen( board , "Black" , 1 , 1)
    queen2 = Piece_Queen( board , "Black" , 2 , 1)
    
    with pytest.raises(Exception):
        queen1.go_to( 3 , 1 )
    assert queen1.get_position() == ( 1 , 1 )




