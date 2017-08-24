#Prints the number of syllables in each line of the poem

Vline1="lily:\n"
Vline2="out of the water\n"
Vline3="out of itself\n"
Vline4="bass\n"
Vline5="picking bugs\n"
Vline6="off the moon\n"

Virgillo=(Vline1+Vline2+Vline3+Vline4+Vline5+Vline6)
print(Virgillo)

counter = 0
vowels = 'aeiouy'
Vline1 = Vline1.lower().strip(".:;?!")
if Vline1[0] in vowels:
    counter +=1
for index in range(1,len(Vline1)):
    if Vline1[index] in vowels and Vline1[index-1] not in vowels:
        counter +=1
if Vline1.endswith('e'):
    counter -= 1
if Vline1.endswith('le'):
    counter+=1
if counter == 0:
    counter +=1
print("Line 1:",counter)

counter = 0
vowels = 'aeiouy'
Vline2 = Vline2.lower().strip(".:;?!")
if Vline2[0] in vowels:
    counter +=1
for index in range(1,len(Vline2)):
    if Vline2[index] in vowels and Vline2[index-1] not in vowels:
        counter +=1
if Vline2.endswith('e'):
    counter -= 1
if Vline2.endswith('le'):
    counter+=1
if counter == 0:
    counter +=1
print("Line 2:",counter)

counter = 0
vowels = 'aeiouy'
Vline3 = Vline3.lower().strip(".:;?!")
if Vline3[0] in vowels:
    counter +=1
for index in range(1,len(Vline3)):
    if Vline3[index] in vowels and Vline3[index-1] not in vowels:
        counter +=1
if Vline3.endswith('e'):
    counter -= 1
if Vline3.endswith('le'):
    counter+=1
if counter == 0:
    counter +=1
print("Line 3:",counter)

counter = 0
vowels = 'aeiouy'
Vline4 = Vline4.lower().strip(".:;?!")
if Vline4[0] in vowels:
    counter +=1
for index in range(1,len(Vline4)):
    if Vline4[index] in vowels and Vline4[index-1] not in vowels:
        counter +=1
if Vline4.endswith('e'):
    counter -= 1
if Vline4.endswith('le'):
    counter+=1
if counter == 0:
    counter +=1
print("Line 4:",counter)

counter = 0
vowels = 'aeiouy'
Vline5 = Vline5.lower().strip(".:;?!")
if Vline5[0] in vowels:
    counter +=1
for index in range(1,len(Vline5)):
    if Vline5[index] in vowels and Vline5[index-1] not in vowels:
        counter +=1
if Vline5.endswith('e'):
    counter -= 1
if Vline5.endswith('le'):
    counter+=1
if counter == 0:
    counter +=1
print("Line 5:",counter)

counter = 0
vowels = 'aeiouy'
Vline6 = Vline6.lower().strip(".:;?!")
if Vline6[0] in vowels:
    counter +=1
for index in range(1,len(Vline6)):
    if Vline6[index] in vowels and Vline6[index-1] not in vowels:
        counter +=1
if Vline6.endswith('e'):
    counter -= 1
if Vline6.endswith('le'):
    counter+=1
if counter == 0:
    counter +=1
print("Line 6:",counter)

Wline1="Up! up! my Friend, and quit your books;\n"
Wline2="Or surely you'll grow double:\n"
Wline3="Up! up! my Friend, and clear your looks;\n"
Wline4="Why all this toil and trouble?\n"
Wline5="The sun, above the mountain's head,\n"
Wline6="A freshening lustre mellow\n"
Wline7="Through all the long green fields has spread,\n"
Wline8="His first sweet evening yellow.\n"
Wline9="Books! 'tis a dull and endless strife:\n"
Wline10="Come, hear the woodland linnet,\n"
Wline11="How sweet his music! on my life,\n"
Wline12="There's more of wisdom in it.\n"
Wline13="And hark! how blithe the throstle sings!\n"
Wline14="He, too, is no mean preacher:\n"
Wline15="Come forth into the light of things,\n"
Wline16="Let Nature be your Teacher.\n"
Wline17="She has a world of ready wealth,\n"
Wline18="Our minds and hearts to bless—\n"
Wline19="Spontaneous wisdom breathed by health,\n"
Wline20="Truth breathed by cheerfulness.\n"
Wline21="One impulse from a vernal wood\n"
Wline22="May teach you more of man,\n"
Wline23="Of moral evil and of good,\n"
Wline24="Than all the sages can.\n"
Wline25="Sweet is the lore which Nature brings;\n"
Wline26="Our meddling intellect\n"
Wline27="Mis-shapes the beauteous forms of things:—\n"
Wline28="We murder to dissect.\n"
Wline29="Enough of Science and of Art;\n"
Wline30="Close up those barren leaves;\n"
Wline31="Come forth, and bring with you a heart\n"
Wline32="That watches and receives.\n")

def count(line,number):
    counter = 0
    vowels = 'aeiouy'
    line = line.lower().strip(".:;?!")
    if line[0] in vowels:
        counter +=1
    for index in range(1,len(Vline6)):
    if line[index] in vowels and line[index-1] not in vowels:
        counter +=1
    if line.endswith('e'):
        counter -= 1
    if line.endswith('le'):
        counter+=1
    if counter == 0:
        counter +=1
    print("Line ",number,":",counter)

