#Calculates maximum height reached by a ladder
import math
def Ladder():
    ladder=int(input("What is the length of the ladder?:"))
    print(math.sqrt((ladder**2)-((ladder/4)**2)))