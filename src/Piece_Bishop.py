from Piece import Piece

class Piece_Bishop ( Piece ):

    def is_not_jumping( self , toX , toY ):
        fromX = self.getX()
        fromY = self.getY()

        # TODO: Add Algorithm here to pass the test.
        # 
        # test will be passed if the programp raises an exception when
        # bishop is trying to jump over any other piece
        #
        # you can check out test in test_bishop_cant_jump function of test_piece_bishop.py
        #
        raise Exception("invalid move: bishop can't jump over any piece")


    def is_allowed_move ( self , toX , toY ):
        fromX = self.get_position()[0]
        fromY = self.get_position()[1]

        if not( ( abs( fromX - toX ) == abs( fromY - toY) ) ) :
            raise Exception("invalid move: bishop can only move in a diagonal line")
        self.is_not_jumping( toX , toY )
        
        return True

    def go_to( self , X , Y ):
        if self.is_allowed_move( X , Y ):
            self.move( X , Y )











