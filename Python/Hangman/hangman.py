# Hangman game
# Must create word list file saved as "words.txt"
# The words only need to be separated by a space

import random
import string

# Word file helper code 

WORD_LIST_FILE= "words.txt"

def loadWords():
    """
    Returns a list of valid words from the word list file. 
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    file = open(WORD_LIST_FILE, 'r')
    # line: string
    line = file.readline() # all the words of this file are in 1 line
    #print line
    wordlist = line.split() # splitting line at space
    print ("Ready! ", len(wordlist), " words loaded.")
    return wordlist


def chooseWord(gamelist):
    """
    Returns a word from wordlist at random
    """
    return random.choice(gamelist)

# End helper code
# -----------------------------------
# Begin game code

def isGuessCorrect(guess, word):
    '''
    Sees if a character guessed is in the word 
    returns True of the guess is in word
    False otherwise
    '''
    if guess in word:
        return True
    else: 
        return False


def wordGuessed(guessedChars, word):
    '''
    given a string as the first parameter, checks to see if all the characters
    of word are in guessChars. If so returns True otherwise False
    '''
    for char in word:
        if char not in guessedChars:
            return False
    return True
    
    
def buildTemplate(template, word):
    '''
    returns a string (template) which represents a template the length of word. If the character in word
    is present in template, then prints the charcter, otherwise prints a dash.
     
    '''

    currentTemplate = ''
    for char in word:
        if char in template:
            currentTemplate += char
        else:
            currentTemplate += '-'
    return currentTemplate


def getRemainingChars(guessedChars):
    '''
    returns a string containing all characters of the alphabet except for those in
    guessedChars.
    '''

    remaining = ''
    alpha = string.ascii_lowercase
    for char in alpha:
        if char not in guessedChars:
            remaining += char
            
    return remaining
    
    
def hangman(secretWord):
    '''
    secretWord: the word to guess. Chosen by the helper code
    
    Starts up an interactive game of Hangman.

    * At the start of the game, selects a random word and then
      let the user know how many letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word and
      whether the word has been guessed.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    * You should allow up to 8 guesses.
    
    '''

    numGuesses = 1
    guessedChars =''
    gameWon = False
    while numGuesses < 9:
        userGuess = input("Enter your guess: ")

        guessedChars += userGuess
        #print guessedChars

        if isGuessCorrect(userGuess, secretWord):
            print ("Correct")
            
            if wordGuessed(guessedChars, secretWord):
                print ('Congrats! Game won!')
                gameWon = True
                break

        else:
            print ("Wrong")



        gameTemplate = buildTemplate(guessedChars, secretWord)
        print ("your guesses so far ",gameTemplate)

        remainder = getRemainingChars(guessedChars)
        print ("your remaining characters are: ",remainder)
        
        print ("you have",8-numGuesses,"guesses left")
        
        numGuesses += 1

    if not gameWon:
        print ("Sorry, you lost the game")

# Run the game

gamelist = loadWords()
while (len(gamelist)!=0):
    secretWord = chooseWord(gamelist).lower()
    hangman(secretWord)
    gamelist.remove(secretWord)
    print ("New game!")
    
