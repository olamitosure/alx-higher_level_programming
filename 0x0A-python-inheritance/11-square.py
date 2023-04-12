#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

"""This module has a class that inherits from another class.
The instantiation size, it has the method area and __str__.
"""


class Square(Rectangle):
    """Class Square.
    It inherits from Rectangle, instantiation with
    size, it has the method area and __str__.
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

