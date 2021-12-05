from geometry import *
from quadtree import *
from shapes import *


def main():
    """Method for testing the Quadtree and Shape implementations"""

    # initialize the Quadtree
    world_area = Rectangle(Point(0, 10), 10, 10)  # 10x10 Rectangle
    world = Quadtree(world_area, 6)

    # generating some shapes
    shapes = [Player(2, 3, 2, 2),
              Ball(2, 7.5, 0.5),
              Ball(3, 5, 0.5),
              Ball(4.5, 5, 0.5),
              Ball(7.5, 7.5, 0.5),
              Ball(6, 5, 0.5),
              Ball(7.5, 5, 0.5),
              Ball(2, 1, 0.5),
              Ball(8.5, 1, 1.5),
              Ball(8.5, 3.5, 1.5),
              ]

    # print out the different shapes and insert them into the Quadtree
    for shape in shapes:
        shape.print_shape()
        world.insert(shape)
    # world.print_tree()

    world.collisions(shapes[0])


if __name__ == "__main__":
    main()
