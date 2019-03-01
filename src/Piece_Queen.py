from Piece import Piece

class Piece_Queen ( Piece ):
    def is_allowed_move ( self , toX , toY ):
        fromX = self.get_position()[0]
        fromY = self.get_position()[1]

        if not( 
                ( fromX - toX == 0 ) or ( fromY - toY == 0 ) or
                ( abs( fromX - toX ) - abs( fromY - toY) ) == 0 
            ):
            raise Exception("invalid move: queen can only move in a straght or diagonal line")
        return True

    def go_to( self , X , Y ):
        if self.is_allowed_move( X , Y ):
            self.move( X , Y )











