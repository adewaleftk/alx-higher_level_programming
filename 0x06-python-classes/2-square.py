#!/usr/bin/python3
""" Defining a Square class with size """


class Square:
    """ Square class """

    def __init__(self, size=0):
        """
        initializing a class instance
        Args:
            size (int): size of the square
        """

        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
