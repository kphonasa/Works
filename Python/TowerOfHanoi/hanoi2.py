# tower of hanoi problem - recursive solution
# tells you what moves to make
# here A is the starting position and C is the ending position.
# B is the temporary position.

counter=0
#create counter
stack = [4,3,2,1]
def hanoi(stack,A,B,C):
            global counter
            #globally called it because if I put it in the function it kept resetting 
            if len(stack) == 1:
                        #if either peg is Y add to counter
                        if A==B or C==B:
                                    counter=counter+1
                        print ('move disc',stack[0],'from',A,'to',C)
            else:
                        #Same for in this section
                        if A==B or C==B:
                                    counter=counter+1                        
                        hanoi(stack[1:],A,C,B)
                        print ('move disc',stack[0],'from',A,'to',C)
                        hanoi(stack[1:],B,A,C)
            print("Peg B included",counter,"times.")
