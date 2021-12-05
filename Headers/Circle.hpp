#pragma once
#include "Point.hpp"
#include "Shape.hpp"

class Circle : public Shape
{
    float radius;
    Point center;

public:
    Circle() = default; //default constructor
    Circle(float radius, Point center); //constructor
    Point getCenter(); //returns center point of circle
    float getRadius(); //returns radius of circle
    bool intersects(Shape *other) override; //checks if shapes intersect, returns true if other shape s intersects with this circle
};