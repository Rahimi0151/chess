from Piece import Piece
import pytest

def test_pieces_should_have_color():
    piece = Piece( "Black" )
    piece = Piece( "White" )

def test_piece_has_a_position():
    piece = Piece( "Black" )
    assert piece.get_position() == ( None , None )

def test_piece_can_move():
    piece = Piece( "Black" )
    piece.move( 1 , 5 )
    assert piece.get_position() == ( 1 , 5 )

def test_piece_can_not_go_out_of_game_board():
    piece = Piece( "Black" )
    with pytest.raises(Exception):
        piece.move( 0 , 0 )
    