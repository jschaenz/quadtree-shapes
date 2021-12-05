#pragma once
#include "./headers/Point.hpp"

Point::Point(int sx, int sy) //constructor
{
    x = sx;
    y = sy;
};

int Point::getX() //get x value
{
    return this->x;
}

int Point::getY() //get y value
{
    return this->y;
}