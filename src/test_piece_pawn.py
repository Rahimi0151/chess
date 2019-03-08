from Board import Board
from Piece_Pawn import Piece_Pawn
import pytest

def test_pawn_can_not_go_more_than_one_square_at_a_time():
    # Black
    black_pawn = Piece_Pawn( Board() , "Black" , 2 , 7 )
    assert black_pawn.get_position() == ( 2 , 7 )

    black_pawn.go_to( 2 , 6 )
    assert black_pawn.get_position() == ( 2 , 6 )

    black_pawn.go_to( 2 , 5 )
    assert black_pawn.get_position() == ( 2 , 5 )

    with pytest.raises(Exception):
        black_pawn.go_to( 2 , 3 )
    assert black_pawn.get_position() == ( 2 , 5 )
 
    # White
    white_pawn = Piece_Pawn( Board() , "White" , 2 , 2 )
    assert white_pawn.get_position() == ( 2 , 2 )

    white_pawn.go_to( 2 , 3 )
    assert white_pawn.get_position() == ( 2 , 3 )

    white_pawn.go_to( 2 , 4 )
    assert white_pawn.get_position() == ( 2 , 4 )

    with pytest.raises(Exception):
        white_pawn.go_to( 2 , 6 )
    assert white_pawn.get_position() == ( 2 , 4 )

def test_pawn_can_go_two_square_at_the_beginning():
    # Black
    black_pawn = Piece_Pawn( Board() , "Black" , 2 , 7 )
    assert black_pawn.get_position() == ( 2 , 7 )

    black_pawn.go_to( 2 , 5 )
    assert black_pawn.get_position() == ( 2 , 5 )

    # White
    white_pawn = Piece_Pawn( Board() , "White" , 2 , 2 )
    assert white_pawn.get_position() == ( 2 , 2 )

    white_pawn.go_to( 2 , 4 )
    assert white_pawn.get_position() == ( 2 , 4 )

def test_pawn_cant_go_backward():
    # Black
    black_pawn = Piece_Pawn( Board() , "Black" , 2 , 7 )
    assert black_pawn.get_position() == ( 2 , 7 )
    
    black_pawn = Piece_Pawn( Board() , "Black" , 2 , 6 )
    assert black_pawn.get_position() == ( 2 , 6 )

    with pytest.raises(Exception):
        black_pawn.go_to( 2 , 7 )
    assert black_pawn.get_position() == ( 2 , 6 )

    # White
    white_pawn = Piece_Pawn( Board() , "White" , 2 , 2 )
    assert white_pawn.get_position() == ( 2 , 2 )
    
    white_pawn = Piece_Pawn( Board() , "White" , 2 , 3 )
    assert white_pawn.get_position() == ( 2 , 3 )

    with pytest.raises(Exception):
        white_pawn.go_to( 2 , 2 )
    assert white_pawn.get_position() == ( 2 , 3 )
