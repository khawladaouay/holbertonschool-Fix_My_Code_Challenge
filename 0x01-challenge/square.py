#!/usr/bin/python3
"""square class"""


class Square():
    """A class that returns the area of a Square"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ initialazation """
        for key, value in kwargs.items():
            if value > 0:
                setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ permiter of my square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ string function """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiterofmysquare())
