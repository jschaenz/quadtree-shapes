from shapes import Shape, Rectangle, Circle, Point
from geometry import ITreeElement


class Quadtree:
    """
    Quadtree is an area represented by a Rectangle. Objects such as Circle and Rectangle can be placed within
    the Quadtree. If the (specified) maximum amount of elements is reached, the Quadtree splits into 4 new Quadtrees
    """
    def __init__(self, area, max_elements, depth=1):
        """Constructor for setting the area, maximum ammount of elements and the current depth of the tree"""
        self.children = []
        self.elements = []
        self.area = area
        self.max_elements = max_elements
        self.depth = depth
        self.max_depth = 6

    def count(self, c=0) -> int:
        """ Return size of the tree """
        c += 1
        for child in self.children:
            c += child.count()
        return c

    def print_tree(self):
        """Print representation of tree with sub-quadrants and elements"""
        if not self.children:
            for element in self.elements:
                element.print_shape()
        else:
            print("-----------------------")
            print("Tree-Depth:", self.depth)
            for quad_nr, child in enumerate(self.children):
                print("--Quadrant", quad_nr+1)
                child.print_tree()

    def insert(self, s):
        """ Insert an element s into the Tree """
        if not self.children:

            # case 1: list doesn't exceed amount of max elements
            if len(self.elements) < self.max_elements:
                self.elements.append(s)
            # case 2: list is full but we're at max depth so we still accept it
            elif len(self.elements) >= self.max_elements and self.depth == self.max_depth:
                self.elements.append(s)
            # case 3: list is full so we split
            else:
                self.split()
                for child in self.children:
                    if child.inside(s):
                        child.insert(s)
        else:
            for child in self.children:
                if child.inside(s):
                    child.insert(s)

    def remove_element(self, s):
        """ Remove an element s from the Tree, renamed due to remove already existing as common python method"""
        # in case we are the node at the bottom we remove the element if we have it
        if self.elements:
            if s in self.elements:
                self.elements.remove(s)
        # in case we are not at the bottom, recursively call remove_element for all children
        else:
            if self.children:
                for child in self.children:
                    child.remove_element(s)
                self.merge()

    def split(self):
        """ Split the Quadtree into 4 children """
        x = self.area.upper_left.x
        y = self.area.upper_left.y

        w = self.area.width*0.5
        h = self.area.height*0.5

        # create new Quadtrees by using half the size of the old one, calculate new top left points and increment depth
        tl_qt = Quadtree(Rectangle(Point(x, y), w, h), self.max_elements, self.depth + 1)
        tr_qt = Quadtree(Rectangle(Point(x+w, y), w, h), self.max_elements, self.depth + 1)
        bl_qt = Quadtree(Rectangle(Point(x, y-h), w, h),  self.max_elements, self.depth + 1)
        br_qt = Quadtree(Rectangle(Point(x+w, y-h), w, h),  self.max_elements, self.depth + 1)
        qts = [tl_qt, tr_qt, bl_qt, br_qt]

        # assign existing elements to the new created Quadtrees
        for tree in qts:
            for element in self.elements:
                if tree.inside(element):
                    tree.insert(element)

        # new created Quadtrees with the elements are now our new children
        # list of elements is emptied as we moved them into the children
        self.children = qts
        self.elements = []

    def merge(self):
        """ Merges the tree from the current node downwards if max and min elements allow it """
        unique = []
        for child in self.children:
            for element in child.elements:
                if element not in unique:  # prevents duplicates
                    unique.append(element)
            if unique:
                if len(unique) < self.max_elements:
                    self.elements = unique
                    self.children = []
            else:
                child.merge()

    def inside(self, s) -> bool:
        """ Checks if element s would be located in the current quadtree if it were to be inserted """
        is_inside = False
        if self.area.intersects(s.get_bounding_shape()):
            is_inside = True
        return is_inside

    def collisions(self, s) -> list:
        """ Return all objects that element s is intersecting or colliding with
        """
        found_collisions = []
        if not self.children:
            if s in self.elements:

                print("\nTested \n" + str(self.elements.index(s)))
                print("Potential")
                # find potential elements (all elements that are in the same Quadtree as element s
                pot_elements = []
                for element in self.elements:
                    if element != s:
                        pot_elements.append(str(self.elements.index(element)))
                print(", ".join(pot_elements))
                # check if they truly intersect
                confirmed_elements = []
                for element in self.elements:
                    if element != s:
                        if s.get_bounding_shape().intersects(element.get_bounding_shape()):
                            found_collisions.append(element)  # for return value
                            confirmed_elements.append(str(self.elements.index(element)))  # for print
                print("Actual")
                print(", ".join(confirmed_elements))
        else:
            for child in self.children:
                found_collisions.extend(child.collisions(s))

        return found_collisions
