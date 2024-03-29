#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a Square."""

    def __init__(self, size=0):
        """initializes a new square.

        Args:
            Size (int): The size of the new Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
