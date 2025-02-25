#include <iostream>

class MyObject{
 
  // constructor
  MyObject(int arg){
    myprop = arg;
  }

  // method
  void printme(){
    std::cout << myprop;
  }

  // attribute
  int myprop;
};