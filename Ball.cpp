#pragma once
#include "./headers/Ball.hpp"

Ball::Ball(Circle *c){ //constructor
    Shape *s;
    *s = dynamic_cast<Shape &>(*c);
    this->shape = s;
    delete s;
}   

Shape *Ball::getBoundingShape(){ //returns shape of Ball
    return this->shape;
}