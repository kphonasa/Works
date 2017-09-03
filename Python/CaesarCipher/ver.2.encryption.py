import string
def encryption(message,shift):
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    
    shifted_lower = lowercase[shift:] + lowercase[:shift]
    shifted_upper = uppercase[shift:] + uppercase[:shift]

    alphabet = lowercase + uppercase
    shifted = shifted_lower + shifted_upper
    
    table = str.maketrans(alphabet, shifted)
    return message.translate(table)
