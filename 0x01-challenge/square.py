#!/usr/bin/python3

class square():

    def __init__(self, size=0):
        self.size = size

    def area_of_my_square(self):
        """ Area of the square """
        return self.size * self.size

    def PermiterOfMySquare(self):
        return (self.size * 4)

    def __str__(self):
        return "size -> {}".format(self.size)


if __name__ == "__main__":

    s = square(size=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())