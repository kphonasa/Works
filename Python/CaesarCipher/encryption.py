def encrypt(message,shift):
    encrypted=""

    for char in message:
        letter = ord(char)
        if ( 97 <= letter <= 122 ):
            letter = letter + shift
            if( letter > 122 ):
                letter = (letter - 26)
        elif (65 <= letter <=90):
            letter = letter + shift
            if (letter > 90):
                letter = (letter - 26)
        else:
            letter==letter

        encrypted = encrypted + chr(letter)

    print(encrypted)
