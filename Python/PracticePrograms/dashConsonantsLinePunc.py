#Print out vowel (include 'y' in the set of vowels) pattern2 in the poem
#For every consonant print a single dash ('-') 
#For every punctuatcion (includes space) print a vertical ('|')
#Print each vowel as is
#Took the poem and created indentations in them so they would stay in its original
#Formation 
Virgillo=(
"lily:\n"
"out of the water\n"
"out of itself\n"
"bass\n"
"picking bugs\n"
"off the moon\n")
print(Virgillo)

Wordsworth=(
"Up! up! my Friend, and quit your books;\n"
"Or surely you'll grow double:\n"
"Up! up! my Friend, and clear your looks;\n"
"Why all this toil and trouble?\n"
"The sun, above the mountain's head,\n"
"A freshening lustre mellow\n"
"Through all the long green fields has spread,\n"
"His first sweet evening yellow.\n"
"Books! 'tis a dull and endless strife:\n"
"Come, hear the woodland linnet,\n"
"How sweet his music! on my life,\n"
"There's more of wisdom in it.\n"
"And hark! how blithe the throstle sings!\n"
"He, too, is no mean preacher:\n"
"Come forth into the light of things,\n"
"Let Nature be your Teacher.\n"
"She has a world of ready wealth,\n"
"Our minds and hearts to bless—\n"
"Spontaneous wisdom breathed by health,\n"
"Truth breathed by cheerfulness.\n"
"One impulse from a vernal wood\n"
"May teach you more of man,\n"
"Of moral evil and of good,\n"
"Than all the sages can.\n"
"Sweet is the lore which Nature brings;\n"
"Our meddling intellect\n"
"Mis-shapes the beauteous forms of things:—\n"
"We murder to dissect.\n"
"Enough of Science and of Art;\n"
"Close up those barren leaves;\n"
"Come forth, and bring with you a heart\n"
"That watches and receives.\n")
print(Wordsworth)

#Import re for replacement
#include punctuations to be replaced and capitalized letters
#Punctuations must be in a different bracket. Used a new string to make easier
import re 
new_str = re.sub('[BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz]', '-', Virgillo)
new_str2=re.sub("[ :]", "|", new_str)
print (new_str2)

import re 
new_str = re.sub('[BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz]', '-', Wordsworth)
new_str2=re.sub("[ !,:;]", "|", new_str)
print (new_str2)