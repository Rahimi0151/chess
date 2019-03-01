from Piece import Piece

class Piece_Knight ( Piece ):
    def is_allowed_move ( self , toX , toY ):
        fromX = self.get_position()[0]
        fromY = self.get_position()[1]

        if not( 
            ( ( abs( fromX - toX ) ) == 2 ) and ( ( abs( fromY - toY ) ) == 1 ) or
            ( ( abs( fromX - toX ) ) == 1 ) and ( ( abs( fromY - toY ) ) == 2 ) 
        ):
            raise Exception("invalid move: knight can only move in a L-shaped line")
        return True

    def go_to( self , X , Y ):
        if self.is_allowed_move( X , Y ):
            self.move( X , Y )











