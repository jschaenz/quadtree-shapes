from abc import ABC, abstractmethod
from math import sqrt


class Point:
    """
    Simple point with x and y coordinates
    """

    def __init__(self, x, y):
        """constructor for setting x and y coordinates of point"""
        self.x = x
        self.y = y


class Shape(ABC):
    """
    Abstract class for different Shapes
    """
    @abstractmethod
    def intersects(self, other) -> bool:
        """Abstract method for shapes to check if they intersect"""
        pass

    @abstractmethod
    def to_str(self) -> str:
        """Abstract method for printing out all attributes of a shape"""
        pass


class Rectangle(Shape):
    """
    Class representing the shape of a Rectangle
    """
    def __init__(self, upper_left, width, height):
        """constructor for setting the upper left point, the width and the height of a rectangle object"""
        self.upper_left = upper_left  # top left point of the rectangle
        self.width = width
        self.height = height

    def to_str(self):
        """Prints out all attributes of a Rectangle separated with whitespaces"""
        return " ".join(["r,", str(float(self.upper_left.x)), str(float(self.upper_left.y)), str(float(self.width)), str(float(self.height))])

    def intersects(self, other):
        """Checks if rectangle intersects with another given shape"""
        intersects = False
        if isinstance(other, Circle):  # Circle Rectangle intersection

            # calculate the bottom left and top right point of the Rectangle from existing data
            upper_right = Point(self.upper_left.x + self.width, self.upper_left.y)
            lower_left = Point(self.upper_left.x, self.upper_left.y - self.height)

            # adapted from author: coder001 on geeksforgeeks (20.11.2020)
            # https://www.geeksforgeeks.org/check-if-any-point-overlaps-the-given-circle-and-rectangle/ -->
            # find nearest point
            xn = max(lower_left.x, min(other.center.x, upper_right.x))
            yn = max(lower_left.y, min(other.center.y, upper_right.y))

            # distance between nearest point and center of the circle
            dx = xn - other.center.x
            dy = yn - other.center.y

            intersects = bool((dx**2+dy**2) < other.radius**2)  # change to <= if touching counts as intersect
            # <-- code adapted from source above ends here

        elif isinstance(other, Rectangle):  # Rectangle Rectangle intersection
            # get all points of the other Rectangle, if one of the points is within, they intersect
            lower_right = Point(self.upper_left.x + self.width, self.upper_left.y - self.height)

            tl = other.upper_left
            tr = Point(tl.x + other.width, tl.y)
            bl = Point(tl.x, tl.y - other.height)
            br = Point(tl.x + other.width, tl.y - other.height)

            points = [tl, tr, bl, br]

            for point in points:
                if (self.upper_left.x < point.x < lower_right.x) and (self.upper_left.y > point.y > lower_right.y):
                    intersects = True

        return intersects


class Circle(Shape):
    """
    Class representing the shape of a Circle
    """
    def __init__(self, center, radius):
        """constructor for setting the upper left point, the width and the height of a rectangle object"""
        self.center = center  # center point of the circle
        self.radius = radius

    def to_str(self):
        """Prints out all attributes of a Circle"""
        return " ".join(["c,", str(float(self.center.x)), str(float(self.center.y)), str(float(self.radius))])

    def intersects(self, other):
        """Checks if circle intersects with another given shape"""
        intersects = False

        if isinstance(other, Circle):  # Circle Circle intersection
            a = Point(self.center.x - other.center.x, self.center.y - other.center.y)
            max_r = self.radius - other.radius
            if sqrt(a.x ** 2 + a.y ** 2) <= max_r:
                intersects = True

        elif isinstance(other, Rectangle):  # Circle Rectangle intersection
            upper_right = Point(other.upper_left.x + other.width, other.upper_left.y)
            lower_left = Point(other.upper_left.x, other.upper_left.y - other.height)

            # adapted from author: coder001 on geeksforgeeks (20.11.2020)
            # https://www.geeksforgeeks.org/check-if-any-point-overlaps-the-given-circle-and-rectangle/ -->

            # find nearest point
            xn = max(lower_left.x, min(self.center.x, upper_right.x))
            yn = max(lower_left.y, min(self.center.y, upper_right.x))

            # distance between nearest point and center of the circle
            dx = xn - self.center.x
            dy = yn - self.center.y

            intersects = bool((dx ** 2 + dy ** 2) < self.radius ** 2)  # change to <= if touching counts as intersect
            # <-- code adapted from source above ends here

        return intersects
