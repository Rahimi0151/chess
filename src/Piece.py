from Board import Board

class Piece():

    BLACK = "Black"
    WHITE = "White"
    X = None
    Y = None

    def set_color( self , color ):
        if color == "Black":
            self.color = self.BLACK
        if color == "White":
            self.color = self.WHITE

    def __init__( self , board , color , X = None , Y = None ):
        self.board = board
        self.set_color( color )
        self.move( X , Y )

    def get_position ( self ):
        return ( self.X , self.Y )

    def is_black( self ):
        return self.color == self.BLACK

    def is_white( self ):
        return self.color == self.WHITE

    def getX ( self ):
        return self.X
        
    def getY ( self ):
        return self.Y

    def is_on_board( self , X , Y ):
        if ( ( X == None ) or ( Y == None) ):
            return True

        if not ( 
            ( X >= 1 ) and ( X <= 8 ) and
            ( Y >= 1 ) and ( Y <= 8 )
         ):
            raise Exception( "invalid move: not on board" )
        return True

    def has_piece( self , X , Y ):
        if not ( ( X == None ) or ( Y == None ) ):
            if ( self.board.item[X][Y] ):
                return True
        return False
    
    def is_ally( self , X , Y ):
        if self.has_piece( X , Y ):
            return self.color == self.board.item[X][Y].color
        return False

    def capture( self , X , Y ):
        if ( self.is_ally( X , Y ) ):
            raise Exception("invalid move: yoe can't capture your own piece")
        del self.board.item[X][Y]       
        
    def move ( self , X , Y ):
        if self.is_on_board( X , Y ):
            if not ( X == None or Y == None ):
                if self.board.item[X][Y]:
                    self.capture( X , Y )
                self.X = X
                self.Y = Y
                self.board.item[self.X][self.Y] = self








