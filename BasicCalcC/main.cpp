<<<<<<< HEAD
#include <iostream>
using namespace std;

void arithmetic(int a, int b)
  {
    int choice;
    std::cout<<"What type of arithmetic would you like to do?"<<std::endl;
    std::cout<<"1)Addition"<<std::endl;
    std::cout<<"2)Subtraction: A-B"<<std::endl;
    std::cout<<"3)Multiplication"<<std::endl;
    std::cout<<"4)Division: A/B"<<std::endl;
    std::cin>>choice;

      switch (choice)
      {
	case 1:
	  std::cout<<a<<" + "<<b<<" = "<<a+b<<std::endl;
	  break;

	case 2:
	  std::cout<<a<<" - "<<b<<" = "<<a-b<<std::endl;
	  break;

	case 3:
	  std::cout<<a<<" * "<<b<<" = "<<a*b<<std::endl;
	  break;
	  
	case 4:
	  if (b==0) 
	  {std::cout<<"You cannot divide by zero, try again."<<std::endl;}
	  else
	  {std::cout<<a<<"/"<<b<<" = "<<a/b<<std::endl;}
	  break;
      }
    }
    
int GCD(int a, int b)
{
  int gcd;
  for (int i=1; (i <= a)&&(i <= b); i++)
  {
    if (a%i==0&&b%i==0) 
    {gcd=i;}
    
  }
  
  return gcd;
}
    
int factorial (int x)
{
  if(x==0)
    return 1;
  return x*factorial(x-1);
}
  
  
// The Babylonian Method
void squareroot(int z)
{
  double n=z;
  double i=1;
  while(n>i)
  {
    n=(n+i)/2;
    i=z/n;
  }

  std::cout<<"The square root of "<<z<<" is "<<n<<std::endl;
}
  
  
int main() 
{
  int func;
    int a;
    int b;
    std::cout << "Please enter integer A:" << std::endl;
    std::cin>>a;
    if (a<0)
    {
      std::cout<<"That is not a positive integer."<<std::endl;
      std::cout<<main()<<std::endl;
    }
    
    std::cout<<"Please enter integer B:"<<std::endl;
    std::cin>>b;
    if (b<0)
    {
      std::cout<<"That is not a positive integer."<<std::endl;
      std::cout<<main()<<std::endl;
    }
    
    std::cout<<"Please select an operation:"<<std::endl;
    std::cout<<"1)Arithmetic"<<std::endl;
    std::cout<<"2)GCD"<<std::endl;
    std::cout<<"3)Factorial"<<std::endl;
    std::cout<<"4)Square root"<<std::endl;
    std::cout<<"5)EXIT"<<std::endl;
    std::cin>>func;
    
     switch (func)
     {
       case 1:
         arithmetic(a,b);
	 std::cout<<main()<<std::endl;
         break;
	 
       case 2:
	 std::cout<<"GCD("<<a<<","<<b<<") = "<<GCD(a,b)<<std::endl;
	 std::cout<<main()<<std::endl;
	 break;
	 
       case 3:
	 std::cout<<"Factorial of "<< a <<" = "<<factorial(a)<<std::endl;
	 std::cout<<"Factorial of "<< b <<" = "<<factorial(b)<<std::endl;
	 std::cout<<main()<<std::endl;
	 break;
	 
       case 4:
	 squareroot(a);
	 squareroot(b);
	 std::cout<<main()<<std::endl;
	 break;
	 
       case 5:
	 std::cout<<"Exiting!"<<std::endl;
	 break;
 
      default:
	main();
        break;
     }
  
    return 0;
}


=======
// Homework 01
// CS:3210:0001
// Author:

#include <iostream>

int main(int argc, char **argv) {

    
    return 0;
}
>>>>>>> d6c1630664aa5acc2bb0d53b4fdac3629c6e0e41
