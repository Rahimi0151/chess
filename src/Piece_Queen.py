from Piece import Piece

class Piece_Queen ( Piece ):

    def is_going_horizental( self , toX , toY ):
        return ( self.getY() == toY )

    def is_going_vertical( self , toX , toY ):
        return ( self.getX() == toX )

    def is_going_diagonal( self , toX , toY ):
        fromX = self.getX()
        fromY = self.getY()

        return abs(abs(toX)-abs(fromX)) == abs(abs(toY)-abs(fromY)) 

    def is_going_correctly( self , toX , toY ):
        return ( self.is_going_horizental( toX , toY ) 
        or self.is_going_vertical( toX , toY ) 
        or self.is_going_diagonal( toX , toY ) )

    def is_jumping( self , toX , toY ):
        fromX = self.getX()
        fromY = self.getY()

        if ( self.is_going_diagonal( toX , toY ) ):
            for x in range ( fromX , toX ):
                for y in range ( fromY , toY ):
                    if ( abs(abs(x)-abs(fromX)) == abs(abs(y)-abs(fromY)) 
                    and not (x == fromX) 
                    and not self.board.item[x][y] == None
                    ):
                        return True
        
        elif ( self.is_going_horizental( toX , toY ) ):
            for x in range( fromX , toX ):
                if x == fromX:
                    continue
                if not ( self.board.item[x][toY] == None and not(x==fromX)):
                    return True

        elif ( self.is_going_vertical( toX , toY ) ):
            for y in range( fromY , toY ):
                if y == fromY:
                    continue
                if not ( self.board.item[toX][y] == None ):
                    return True

    def is_allowed_move ( self , toX , toY ):

        if not( self.is_going_correctly( toX , toY ) ):
            raise Exception("invalid move: queen can only move in a straght or diagonal line")
        if self.is_jumping( toX , toY ):
            raise Exception("invalid move: queen can't jump over any piece")
        return True


    def go_to( self , X , Y ):
        if self.is_allowed_move( X , Y ):
            self.move( X , Y )











