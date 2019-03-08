from Board import Board
from Piece import Piece
from Piece_Rook import Piece_Rook
from Piece_Bishop import Piece_Bishop
import pytest

def test_pieces_should_have_color():
    piece = Piece( Board() , "Black" )
    piece = Piece( Board() , "White" )

def test_piece_has_a_position():
    piece = Piece( Board() , "Black" )
    assert piece.get_position() == ( None , None )

def test_piece_can_move():
    piece = Piece( Board() , "Black" )
    piece.move( 1 , 5 )

    assert piece.get_position() == ( 1 , 5 )

def test_piece_can_not_go_out_of_game_board():
    piece = Piece( Board() , "Black" )

    with pytest.raises(Exception):
        piece.move( 0 , 0 )

def test_you_cant_capture_your_ally():
    board = Board()
    rook1 = Piece_Rook( board , "White" , 2 , 2 )
    rook2 = Piece_Rook( board , "White" , 2 , 3 )

    with pytest.raises(Exception):
        rook1.move( 2 , 3 )
        rook2.move( 2 , 3 )

def test_if_you_move_to_an_enemies_square_you_can_capture_his_piece():
    board = Board()
    rook = Piece_Rook( board , "White" , 2 , 2 )
    bishop = Piece_Bishop( board , "Black" , 2 , 3 )

    rook.move( 2 , 3 )

    assert type( board.item[ 2 ][ 3 ] ) == type( Piece_Rook( board , "White" ) )
    assert board.item[ 2 ][ 3 ] == rook

