import string
def decrypt(message):
    shift=1
    while shift<27:
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
    
        shifted_lower = lowercase[(26-shift):] + lowercase[:(26-shift)]
        shifted_upper = uppercase[(26-shift):] + uppercase[:(26-shift)]

        alphabet = lowercase + uppercase
        shifted = shifted_lower + shifted_upper
    
        table = str.maketrans(alphabet, shifted)
        print("Key " + str(shift) + ": "+message.translate(table))
        shift+=1
