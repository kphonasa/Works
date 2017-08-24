
#open text and read
file=open('emailList.txt', 'r')
txt=(file.read())
#close file so that we can write a new one
file.close()
#.split() to get rid of whitspace
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

#make it into a list
newfile = list()
for length, word in t:
    newfile.append(word)
    
print(newfile)

#imported csv to separate the file based on the comma
import csv
def makeTuple(file):
    output= []
    #have csv read and split the file based on @ and got rid of the @
    csv_reader = csv.reader(file, delimiter='@')
    for row in csv_reader:
        #append it as a tuple
        output.append(tuple(row))
    return output

tlist=(makeTuple(newfile))
#print(tlist)
#Sort by the second index in the tuple list
sortDomain = sorted(tlist, key=lambda tup: tup[1])
print(sortDomain)
#make sortDomain into a string to write into a file)
#write the file
sortedEmails=open("sortedEmails.txt","w")
sortedEmails.write(str(sortDomain))
sortedEmails.close()