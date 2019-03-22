from Piece import Piece

class Piece_Bishop ( Piece ):

    def is_going_diagonal( self , toX , toY ):
        fromX = self.getX()
        fromY = self.getY()

        return abs(abs(toX)-abs(fromX)) == abs(abs(toY)-abs(fromY)) 

    def is_jumping( self , toX , toY ):
        fromX = self.getX()
        fromY = self.getY()

        for x in range ( fromX , toX ):
            for y in range ( fromY , toY ):
                if ( abs(abs(x)-abs(fromX)) == abs(abs(y)-abs(fromY)) 
                and not (x == fromX) 
                and not self.board.item[x][y] == None
                ):
                    return True

    def is_allowed_move ( self , toX , toY ):

        if not self.is_going_diagonal( toX , toY ):
            raise Exception("invalid move: bishop can only move in a diagonal line")
        if self.is_jumping( toX , toY ):
            raise Exception("invalid move: bishop can't jump over any piece")
        return True

    def go_to( self , X , Y ):
        if self.is_allowed_move( X , Y ):
            self.move( X , Y )











