#Asks user for 2 lists of numbers (list1 and list2). 
#Then takes each element of list1 and divides by the corresponding element of list 2
#(list1[0]/list2[0], list1[1]/list2[1] etc.)
#and stores the result in a new list
#The program returns the resulting list

while True:
     try:
          a=raw_input("Please input your first list like [x,x,x]:")
          #input like such or else I get an invalid literal error
          a=a[1:len(a)-1]
          #will start taking the string and start changing it to integers
          listA = a.split(",")
          #split the , so that the intergers can be appended
          listEndA=[]
          for caseListA in listA:
               listEndA.append(int(caseListA))
               #append integers to a list so we can use
          break
     except ValueError:
          #except error for making it not in list format
          print("You must input your list like [x,x,x,x,x,x]")         
          
#Do same thing for next list
while True:
     try:
          b=raw_input("Please input your second list to divide the first list like [x,x,x]:")
          b=b[1:len(b)-1]
          listB = b.split(",")
          listEndB=[]
          for caseListB in listB:
               listEndB.append(int(caseListB))
          break
     except ValueError:
          print("You must input your list like [x,x,x,x,x,x]")
          
#use float to give back decimals if the number divided is not divided into a whole number
#zip function to divide up the lists by index and pair them together to divide easier
print([(x*1.0)/y for x, y in zip(listEndA, listEndB)])

