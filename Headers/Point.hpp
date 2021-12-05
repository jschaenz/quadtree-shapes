#pragma once
class Point
{
    int x;
    int y;

public:
    Point() = default; //default constructor
    Point(int sx, int sy); //constructor
    int getX(); //get x value
    int getY(); //get y value
};