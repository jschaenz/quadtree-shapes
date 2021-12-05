from abc import ABC, abstractmethod
from shapes import Shape, Rectangle, Circle, Point


class ITreeElement(ABC):
    """
    Interface that is meant to assure every object that can be inserted into a Quadtree has an accessible shape
    """
    @abstractmethod
    def get_bounding_shape(self):
        """Abstract method for retuning the shape of an object"""
        pass


class Actor(ITreeElement):
    """
    Abstract class for objects that can be inserted into a Quadtree
    """
    @abstractmethod
    def __init__(self):
        """Abstract Constructor supplying print_shape with a shape attribute"""
        self.shape = Shape()

    @abstractmethod
    def get_bounding_shape(self):
        """Abstract method for retuning the shape of an object"""
        pass

    def print_shape(self):
        """Implemented method for printing a string with all attributes of the objects Shape"""
        print(self.shape.to_str())


class Player(Actor):
    """
    Player object whose shape is represented by a Rectangle object.
    Can be inserted into a Quadtree
    """
    def __init__(self, x, y, width, height):
        """Constructor setting the shape of the Player"""
        self.shape = Rectangle(Point(x,y), width, height)

    def get_bounding_shape(self) -> Rectangle:
        """Returns the Rectangle object, representing the shape of the Player"""
        return self.shape


class Ball(Actor):
    """
    Ball object whose shape is represented by a Circle object.
    Can be inserted into a Quadtree
    """
    def __init__(self, x, y, radius):
        """Constructor setting the shape of the Ball"""
        self.shape = Circle(Point(x, y), radius)

    def get_bounding_shape(self) -> Circle:
        """Returns the Circle object, representing the shape of the Ball"""
        return self.shape

