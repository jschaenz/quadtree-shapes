#pragma once
#include "Point.hpp"
#include "Shape.hpp"
#include "Circle.hpp"
class Rectangle : public Shape
{
    Point *upperleft;
    float width;
    float height;

public:
    Rectangle() = default; //default constructor rectangle
    Rectangle(Point *ul, float w, float h); //constructor rectangle
    bool intersects(Shape *other) override; //checks if shapes intersect, returns true if other shape s intersects with this Rectangle r
    float getWidth(); // get width of rectangle
    float getHeight(); // get height of rectangle
    Point *getUpperLeft(); // get upper left point of rectangle 
};