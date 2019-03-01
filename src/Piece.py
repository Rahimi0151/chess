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

    def __init__( self , color , X = None , Y = None ):
        self.set_color( color )
        self.move( X , Y )

    def get_position ( self ):
        return ( self.X , self.Y )

    def is_on_board( self , X , Y ):
        if ( ( X == None ) or ( Y == None) ):
            return True

        if not ( 
            ( X >= 1 ) and ( X <= 8 ) and
            ( Y >= 1 ) and ( Y <= 8 )
         ):
            raise Exception( "invalid move: not on board" )
        return True

    def move ( self , X , Y ):
        if self.is_on_board( X , Y ):
            self.X = X
            self.Y = Y

    def is_black( self ):
        return self.color == self.BLACK

    def is_white( self ):
        return self.color == self.WHITE







