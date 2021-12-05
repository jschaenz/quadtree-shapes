#pragma once
#include "ITreeElement.hpp"
#include "Rectangle.hpp"

class Quadtree
{
public:
    class T : public ITreeElement
    {
    public:
        virtual Shape *getBoundingShape();//returns shape of current element
        T() = default; //constructor
    };
    Quadtree(int maxE, Rectangle *a);
    Quadtree()=default;
    int count(Quadtree *QT); //calculate size of tree
    void insert(T *s);       //insert element into tree
    void remove(T *s);       //remove element from tree
    void split();            //splits tree into 4 quadrants
    void merge();            //merges child nodes and deletes children
    bool inside(T *s);       //check if element is inside tree
    T *collisions(T *s);     //finds all ITreeElement e that collide with passed ITreeElement

private: 
    int maxDepth; //maximum depth of Quadtree, used in remove and insert Element methods
    int currDepth; //current depth of Quadtree, used in remove, split and insert
    Quadtree *children; //Pointer to array of Quadtree children of current Quadtree layer, used in split and merge
    T *elements; //pointer to array of elements, used in count, insert, remove, split, merge, collisions
    Rectangle area; //stores area of current Quadtree as rectangle, used in split, inside
    int maxElements; //maximum amount of Elements in one tree before it needs to be split
};