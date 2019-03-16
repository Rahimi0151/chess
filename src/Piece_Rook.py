from Piece import Piece

class Piece_Rook ( Piece ):

    def is_going_horizental( self , toX , toY ):
        return ( self.getY() == toY )

    def is_going_vertical( self , toX , toY ):
        return ( self.getX() == toX )

    def is_allowed_move ( self , toX , toY ):
        fromX = self.getX()
        fromY = self.getY()

        if not( ( fromX - toX == 0 ) or ( fromY - toY == 0 ) ):
            raise Exception("invalid move: rook can only move in a straght line")

        if self.is_not_jumping( toX , toY ):
            return True

    def is_not_jumping( self , toX , toY ):
        fromX = self.getX()
        fromY = self.getY()

        if ( self.is_going_horizental( toX , toY ) ):
            for x in range( fromX , toX ):
                if not ( self.board.item[x][toY] == None ):
                    raise Exception("invalid move: rook can't jump over any piece")

        if ( self.is_going_vertical( toX , toY ) ):
            for y in range( fromY , toY ):
                if not ( self.board.item[toX][y] == None ):
                    raise Exception("invalid move: rook can't jump over any piece")
        return True

    def go_to( self , X , Y ):
        if self.is_allowed_move( X , Y ):
            self.move( X , Y )











