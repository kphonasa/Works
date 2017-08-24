// Homework 06
// Author:
// CS:3210 Programming in C++
// Due Date: December 14, 2016
// 50 points

// 25 points - part 1
// 15 points - part 2
// 10 points - code is well formatted and easy to follow



#include <iostream>
#include <vector>   // You may use vector to store the locations in part 2
#include <array>
#include <algorithm>
#include <iterator>

// Part 1:
// Write a templated search function that works with any type of array.
//
// Your function should return a pointer to the first value found in the array
// If no value is found it should return a pointer with the value nullptr.
//
// Your function should take three parameters.
// A pointer to the beginning of the array
// A pointer to the end+1 of the Array
// A value to find
// An example using int instead of templates would be:
// int* findit(int *begin, int *end, int const &value){...}

template<class InputIterator, class T>
  typename std::iterator_traits<InputIterator>::difference_type
    findit(InputIterator begin, InputIterator end, const T value)
{
  typename std::iterator_traits<InputIterator>::difference_type count=0;
  while (begin!=end)
  {
    if (*begin==value) 
    {
      //std::cout<<value<<"found in location"<<begin<<std::endl;
      ++count;
    }
    ++begin;
  }
  //std::cout<<value<<" appears "<<count<<" times."<<std::endl;
  return count;
}





// Part 2:
// Use findit<int>(..) to find the number of 8's in the myNumbers array
// Print out their locations in memory
// Note you will get different values every time you run the program,
// but their relative positions should be the same
int main()
{
    int myNumbers[] = {3,5,8,9,2,4,7,8,3,6,7,8,8,4,4,4,6,6,6};
    std::vector<int> myvector (myNumbers,myNumbers+19);
    std::vector<int>::iterator position;

   
    std::cout<<findit(myvector.begin(), myvector.end(),8)<<std::endl;
    int x=0;
    position=myvector.begin();
    while (myvector.begin()!=myvector.end())
    {
      if (*myvector.begin()==8) std::cout<<"8 found in location:"<<*position<<std::endl;
      myvector.begin()=(myvector.begin()+x);
    }

}

    // A loop that keeps searching for '8' in the array until
    // it reaches the last element, or no more is found
    // hint: it's easiest to use a std::vector of int pointers to store the locations




    // Use std::cout to print out the locations to the terminal


