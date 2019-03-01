from Board import Board
import pytest


def test_can_create_a_board():
    return
    board = Board()

def test_board_is_8_x_8_spots():
    board = Board()
    assert board.get_item_in((1,1)) == None
    with pytest.raises(IndexError) as error:
        board.get_item_in( ( 9 , 9 ) )
    assert "list index out of range" == str(error.value)