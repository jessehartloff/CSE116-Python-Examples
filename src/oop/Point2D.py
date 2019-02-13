

class Point2D:

    # __init__ defines the constructor
    # first parameter of Python methods is always a reference to the calling object (this in Scala)
    def __init__(self, x, y):
        # define state variables using self.<name> in the constructor
        self.x = x
        self.y = y