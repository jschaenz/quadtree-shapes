#pragma once
#include "Actor.hpp" 
#include "Circle.hpp"

class Ball : public Actor 
{
    private:
        Shape *shape; //pointer to shape of ball

    public:
    Ball(Circle *c); //constructor
    Shape *getBoundingShape(); //reutns shape of ball
};