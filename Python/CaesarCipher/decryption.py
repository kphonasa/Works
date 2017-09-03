def decrypt(message):
    shift=1
    while shift<27:
        decrypted=""
        for char in message:
            letter = ord(char)
            if ( 97 <= letter <= 122 ):
                letter = letter - shift
                if( letter < 97 ):
                    letter = (letter + 26)
            elif (65 <= letter <=90):
                letter = letter - shift
                if (letter < 65):
                    letter = (letter + 26)
            else:
                letter==letter

            decrypted = decrypted + chr(letter)

        print("Key " + str(shift) + ": "+decrypted)
        shift+=1
