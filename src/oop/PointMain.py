
# from <package>.<filename> import <class_name>
from oop.Point2D import Point2D


if __name__ == '__main__':

    p1 = Point2D(3, 6)  # Python omits the new keyword
    p1.x = 5

    print("(" + str(p1.x) + ", " + str(p1.y) + ")")