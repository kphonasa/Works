#Checks if arguments of division is empty
#Checks to makes sure result returned by division is in range 1-50

def div (numbers, weight):
    '''numbers is a list of numbers
    weight is a number'''
    assert weight!=0, "List must contain numbers"
    x = [elt/float(weight) for elt in numbers]

    result = 0
    for i in x:
        result += i
    assert 0<result<51, "Results must be between 1 and 50" 
    return result




def answer(listn):
    '''listn is a list of numbers
    '''

    return div(listn,len(listn))

