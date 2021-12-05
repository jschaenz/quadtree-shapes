#pragma once
#include "Actor.hpp" 
#include "Rectangle.hpp"

class Player : public Actor 
{
    private:
        Shape *shape; //Pointer to shape of Player

    public:
    Player(Rectangle *r); //constructor
    Shape *getBoundingShape(); //returns shape of Player
};