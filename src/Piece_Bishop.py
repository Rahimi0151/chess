from Piece import Piece

class Piece_Bishop ( Piece ):
    def is_allowed_move ( self , toX , toY ):
        fromX = self.get_position()[0]
        fromY = self.get_position()[1]

        if not( ( abs( fromX - toX ) - abs( fromY - toY) ) == 0 ) :
            raise Exception("invalid move: bishop can only move in a diagonal line")
        return True

    def go_to( self , X , Y ):
        if self.is_allowed_move( X , Y ):
            self.move( X , Y )











