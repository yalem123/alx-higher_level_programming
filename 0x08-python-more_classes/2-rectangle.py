#!/usr/bin/python3
"""
this progam defines a rectangle class with private attributes width and height
"""


class Rectangle():
    """
    A Rectangle Class with the private instance attributes width and height
    """

    def __init__(self, width=0, height=0):
        """
        constructor of the class Rectangle
          Args:
             - width (default = 0): int
             - height (default = 0): int
        """
        self.height = height
        self.width = width

        def area(self):
            """calculate the area of rectangle"""
            return self.__width * self.__height

        def perimeter(self):
            """returns the rectangle perimeter"""
            if (self.__width == 0 or self.__height == 0):
                return 0

            return (self.__width * 2) + (self.__height * 2)

        @property
        def width(self):
            """Get property of the width"""
            return self.__width

        @width.setter
        def width(self, value):
            """
            Getter of the property value
              Args:
                - value: int
            """
            if not isinstance(value, int):
                raise TypeError('width must be an integer')

            if value < 0:
                raise ValueError('width must be >= 0')

            self.__width = value

            @property
            def height(self):
                """Getter of the property height"""
                return self.__height

            @height.setter
            def height(self, value):
                """
                Getter of the property value
                  Args:
                    - value: int
                """
                if not isinstance(value, int):
                    raise TypeError('height must be an integer')

                if value < 0:
                    raise ValueError('height must be >= 0')

                self.__height = value
