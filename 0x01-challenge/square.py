#!/usr/bin/python3
"""
Square class
"""


class square():
    """ Documentation"""

    def __init__(self, size=0):
        """ Documentation """
        self.size = size

    def area_of_my_square(self):
        """ Area of the square """
        return self.size ** 2

    def PermiterOfMySquare(self):
        """ Documentation """
        return (self.size * 4)

    def __str__(self):
        """ Documentation """
        return "{}/{}".format(self.size, self.size)


if __name__ == "__main__":

    s = square(size=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
