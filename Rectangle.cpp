#pragma once
#include "./headers/Rectangle.hpp"
#include "./headers/Point.hpp"
#include "./headers/Circle.hpp"
#include <typeinfo>


Rectangle::Rectangle(Point *ul, float w, float h) //constructor rectangle
{
    upperleft = ul;
    width = w;
    height = h;
};


float Rectangle::getWidth() //get width of rectangle
{
    return this->width;
};

float Rectangle::getHeight() //get height of rectangle
{
    return this->height;
};

Point *Rectangle::getUpperLeft() //get upper left point of rectangle
{
    return this->upperleft;
};

bool Rectangle::intersects(Shape *other) //checks if shapes intersect, returns true if other shape s intersects with this Rectangle r
{
    bool returnValue;

    //checks if other shape is rectangle and subsequently checks for intersections between rectangle & rectangle
    if (typeid(*other) == typeid(Rectangle)) 
    {
        Rectangle *r;
        *r = dynamic_cast<Rectangle &>(*other); //downcast

        if ((this->getUpperLeft()->getY() - this->getHeight() > r->getUpperLeft()->getY() || //r has to be above s
             this->getUpperLeft()->getY() < r->getUpperLeft()->getY() - r->getHeight()) &&   // r has to be below s
            (this->getUpperLeft()->getX() + this->getWidth() < r->getUpperLeft()->getX() ||  // r has to be left of s
             this->getUpperLeft()->getX() > r->getUpperLeft()->getX() + r->getWidth())       // r has to be right of s
        )
        {
            returnValue = false;
        }
        else
        {
            returnValue = true;
        }
    }

    //checks if other shape is circle and subsequently checks for intersections between rectangle & circle
    else if (typeid(*other) == typeid(Circle)) //based on https://www.coding-daddy.xyz/node/29
    {
        Circle *c;
        *c = dynamic_cast<Circle &>(*other); //downcast

        float closestX;
        float closestY;
        bool borderCollides;

        if (c->getCenter().getX() < this->getUpperLeft()->getX())
        {
            closestX = this->getUpperLeft()->getX();
        }
        else if (c->getCenter().getX() > this->getUpperLeft()->getX() + this->getWidth())
        {
            closestX = this->getUpperLeft()->getX() + this->getWidth();
        }

        if (c->getCenter().getY() < this->getUpperLeft()->getY() - this->getHeight())
        {
            closestX = this->getUpperLeft()->getY() - this->getHeight();
        }
        else if (c->getCenter().getY() > this->getUpperLeft()->getY())
        {
            closestX = this->getUpperLeft()->getY();
        }

        float distanceX = c->getCenter().getX() - closestX;
        float distanceY = c->getCenter().getY() - closestY;

        if (distanceX * distanceX + distanceY * distanceY < c->getRadius() * c->getRadius())
        {
            borderCollides = true;
        }

        else
        {
            borderCollides = false;
        }

        // checks if circle is inside Rectangle by using its center and checks borderCollides status
        if ((this->getUpperLeft()->getX() < c->getCenter().getX() < this->getUpperLeft()->getX() + this->getWidth() && 
            this->getUpperLeft()->getY() > c->getCenter().getX() > this->getUpperLeft()->getY() - this->getHeight()) || 
            borderCollides) 
        {
            returnValue = true;
        }
        else
        {
            returnValue = false;
        }
    }

    return returnValue;
};