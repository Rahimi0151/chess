class Board:
    def create_board( self ):
        self.item = [ [ None for i in range(9) ] for j in range(9) ]

    def __init__( self ):
        self.create_board()
    
    def get_item_in( self , possition ):
        return self.item[ possition[0] ][ possition[1] ]










