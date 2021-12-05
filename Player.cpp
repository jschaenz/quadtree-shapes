#pragma once
#include "./headers/Player.hpp"

Player::Player(Rectangle *r){ //constructor 
    Shape *s;
    *s = dynamic_cast<Shape &>(*r);
    this->shape = s;
    delete s;
}   

Shape *Player::getBoundingShape(){ //returns shape of Player
    return this->shape;
}