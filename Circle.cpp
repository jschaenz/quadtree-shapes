#pragma once
#include "./headers/Circle.hpp"
#include "./headers/Point.hpp"
#include "./headers/Rectangle.hpp"
#include <typeinfo>
#include <math.h>

Circle::Circle(float r, Point c) //constructor
{
    radius = r;
    center = c;
};

Point Circle::getCenter() //returns center point of circle
{
    return this->center;
}

float Circle::getRadius() //returns radius of circle
{
    return this->radius;
}

bool Circle::intersects(Shape *other) //returns true if other intersects with this Circle
{
    if (typeid(*other) == typeid(Circle)) // circle circle intersection check
    {   
        Circle *c;
        *c = dynamic_cast<Circle &>(*other); //downcast to Cirle

        float x = this->center.getX() - c->center.getX();
        float y = this->center.getY() - c->center.getY();

        float max = this->getRadius() - c->getRadius();

        return sqrt(x * x + y * y) >= max;
    }
    else if(typeid(*other) == typeid(Rectangle)){ // circle rectangle intersection check
        
        Rectangle *r;
        *r = dynamic_cast<Rectangle &>(*other); //downcast to Rectangle
        r->intersects(this);
    }
};