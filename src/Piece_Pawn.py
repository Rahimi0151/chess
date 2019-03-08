
from Piece import Piece

class Piece_Pawn ( Piece ):
    def is_allowed_move ( self , toX , toY ):
        fromX = self.get_position()[0]
        fromY = self.get_position()[1]

        if ( self.is_black() ):
                    
            if ( toY - fromY > 0 ):
                raise Exception("invalid move: black pawn can't move upward")

            if ( fromY == 7 ) and ( toY < 5 ) :
                raise Exception("invalid move: pawn can't move further than 2 squares")

            if( abs ( fromY - toY ) > 1  ) and ( not fromY == 7 ):
                raise Exception("invalid move: pawn can't move further than 1 squares")

        if ( self.is_white() ):
                    
            if( fromY - toY > 0 ):
                raise Exception("invalid move: white pawn can't move downward")

            if ( fromY == 2 ) and ( toY > 4 ) :
                raise Exception("invalid move: pawn can't move further than 2 squares")

            elif( abs ( fromY - toY ) > 1 ) and ( not fromY == 2 ):
                raise Exception("invalid move: pawn can't move further than 1 squares")

        return True

    def go_to( self , X , Y ):
        if self.is_allowed_move( X , Y ):
            self.move( X , Y )











