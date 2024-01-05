#!/usr/bin/python3
"""empty class called rectangle"""


class Rectangle:
    """class that does nothing"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if isinstance(value, int) and value >= 0:
            self.__width = value
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        if isinstance(value, int) and value >= 0:
            self.__height = value
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        string = ""
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(0, self.height):
            string += str(self.print_symbol) * self.width
            if i < self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

# Error case
try:
    mysquare = Rectangle.square("12")
    print("{} / {}".format(mysquare.width, mysquare.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
