thelist=[1, "dff",34,"the world", 980, (5,6,7)]

#Made counter to represent the index of the list
#Counter=-1 because if I keep adding 1 the first print would be thelist[0]


def printList(thelist):
    counter=-1
    n=(len(thelist))
    n=n-1
    #n=n-1 because the index would contain one less than the length
    if n==-1:
        print("List needs to contain something.")
        #list needs to contain something
    else:
        while counter!=n:
            counter=counter+1
            print(thelist[counter])

        
print(printList(thelist))



