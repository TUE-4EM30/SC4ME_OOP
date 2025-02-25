class MyObject:

def __init__( self, arg ):
    self.myprop = arg

# equals (a == b)
def __eq__( self, other ):
    return isinstance(other, MyObject)\
        and self.myprop == other.myprop

# addition (a + b)
def __add__( self, other ):
    assert isinstance( other, MyObject )
    return MyObject( self.myprop + other.myprop )