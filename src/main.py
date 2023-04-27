# main.py by Daniel Tellez
# Purpose:
# The purpose of this application will be to perform various
# word statistics on a given document/file.  The initial requirement
# will be to count the frequency of each unique word and print the
# results to the terminal.
# Necessary imports
import sys
import re
# GLOBALS
FOUNDWORDS = {}     # Stores unique words found
TOTAL_CHARACTER_COUNTER = 0 # Stores the count of the total number of characters in the file
TOTAL_LINE_COUNTER = 0 # Stores the total count of lines in the file
# printWords
#   Prints all the words in FOUNDWORDS with their
#   respective count values

def printWords():
    if len(FOUNDWORDS) == 0:
        print("String and Words found no valid words in the given file.")
        return

    for word in FOUNDWORDS.keys():
        print("\"" + word + "\"" + " has a word count of " + str(FOUNDWORDS[word]))

# validateWord
#   Given a word, checks to see if that word
#   will count as a valid word or not.
def validateWord(word):
    if word == "":
        return False

    # Check to see if valid word if only containing letters
    for index, char in enumerate(word):
        # If a char is not in a-zA-Z, check to see if single operator
        # If at end of the string, then count as word but remove operator.
        if not char.isalpha():
            if len(word) == 1:
                return False
            # Valid operator at the end, return True
            if (index == len(word)-1) and re.match(r"[!?\.,;:]", char):
                return True
            return False
    # Valid word, return True
    return True

# countUniqueWords
#   Given a list of words, iterates through them
#   and keeps counts of new/old words
def countUniqueWords(words):
    global FOUNDWORDS
    global TOTAL_CHARACTER_COUNTER

    # Iterate through all words in list
    for word in words:
        # count the characters for each word to add to total
        charWordCounter(word)

        # invoke validateWord to see if a good word or not
        if not validateWord(word):
            continue
        else:
            # if valid word with valid operator at end, simply remove it
            if re.match(r"[!?\.,;:]", word[-1]):
                word = word[:-1]

        # If it exists in dictionary, increment count
        if word in FOUNDWORDS:
            FOUNDWORDS[word] = FOUNDWORDS[word] + 1
        # First time seeing word, add it into dictionary and set value to 1
        else:
            FOUNDWORDS[word] = 1

# charWordCounter
    # Given a single word, regardless if valid or not,
    # counts the characters and its it to the total
    # character counter.
def charWordCounter(word):
    global TOTAL_CHARACTER_COUNTER
    charCounter = len(word)
    TOTAL_CHARACTER_COUNTER = TOTAL_CHARACTER_COUNTER + charCounter

# printCharacterCount
    # Simply prints the total number of characters
    # that were counted in the given file.
def printCharacterCount():
    print("Total number of characters counted in document: " + str(TOTAL_CHARACTER_COUNTER))

# printCharacterCount
    # Simply prints the total number of lines
    # that were counted in the given file.
def printLineCount():
    print("Total number of lines counted in document: " + str(TOTAL_LINE_COUNTER))

# validWordsCheck
    # Checks to see if there exists any valid words that was found
    # in the given document.  If words found, returns True, otherwise
    # false
def validWordsCheck():
    global FOUNDWORDS
    if len(FOUNDWORDS) > 0:
        return True
    return False

# findWordInFile
    # Checks to see if the word given by user is a valid word
    # found in FOUNDWORDS dictionary.  This ensures that
    # user is replacing a valid word found
def findWordInFile(word):
    try:
        if FOUNDWORDS[word]:
            return True
    except:
        print("Word does not exist in file.  Please Try Again.")
        return False

# getReplacementWord
    # Prompts the user to input their replacement word.  Checks
    # to ensure that the word provided by the user is a valid word
    # as well.
def getReplacementWord():
    replacementWord = 1

    while (replacementWord):
        typedWord = input("\nPlease type in your replacement word: ")

        if validateWord(typedWord):
            replacementWord = 0
        else:
            print("Invalid word provided, please try again.")
    return typedWord

# getReplacedWord
    # Prompts users if they would like to replace a word in the file
    # User can skip if they would not like to.
    # Invokes findWordInFile() to ensure word they would like to replace
    # exists in the file.
def getReplacedWord():
    replacedWord = 1

    while (replacedWord):
        inputTxt = "\nPlease type the word you would like to replace (Press Enter to Skip): "
        selectedWord = input(inputTxt)

        if selectedWord == "":
            exit("No Words Replaced.  Exiting.")
        else:
            if findWordInFile(selectedWord):
                replacedWord = 0
    return selectedWord

# replaceWord
    # Given the two words the user will be replacing with, creates a new
    # file that will print out the same contents as the previous file
    # but with the new word replacing old occurrances of the old word.
def replaceWord(selectedWord, replacementWord, file):
    # Open original file and create new file with modified name
    with open(file) as infile, open(file + "_MODIFIED", 'w') as outfile:
        # iterate through all lines in the file and grab the words
        for line in infile:
            words = line.split()
            newLine = line
            # for each word, check to see if they match word wanted to be replaced by user
            # if it does, replace that occurance with new word, otherwise keep line the same
            for word in words:
                if re.search(r"^" + selectedWord + r"[!?\.,;:]{0,1}$", word):
                    if re.match(r"[!?\.,;:]", word[-1]):
                        newLine = re.sub(word, replacementWord+word[-1], newLine, count=1)
                    else:
                        newLine = re.sub(word, replacementWord, newLine, count=1)
            outfile.write(newLine)

# readFile
#   Given a file/document, simply reads the contents of the file
#   invoking helper functions to count unique and valid words.
def readFile(file):
    global TOTAL_LINE_COUNTER
    try:
        with open(file, 'r') as infile:
            # Iterate through every single line in the file
            for line in infile:
                # increase the count
                TOTAL_LINE_COUNTER = TOTAL_LINE_COUNTER + 1
                # strip end of line for newline
                line = line.rstrip()
                # split will remove all spaces, tabs, and newlines
                words = line.split()
                # Invoke the countUniqueWords function
                countUniqueWords(words)
    # File being read did not work, give simple ERROR message
    except IOError:
        raise IOError("ERROR: Unable to Open Given Input File.  Terminating Process.")

# checkArguments
#   Ensures that the proper number of arguments is provided to the
#   String and Words application.
def checkArguments(arguments):
    if arguments == []:
        exit("ERROR : Please Provide an Input File.")
    elif len(arguments) > 1:
        exit("ERROR : Please Provide Only a Single Input File.")
    elif len(arguments) == 1:
        return

# Simply read filename provided and call readFile function
def main():
    checkArguments(sys.argv[1:])
    file = sys.argv[1]
    readFile(file)

    # print statistics to user
    printWords()
    printCharacterCount()
    printLineCount()

    # ensure there exists words to be replaced
    if (validWordsCheck()):
        selectedWord = getReplacedWord()
        replacementWord = getReplacementWord()
        replaceWord(selectedWord, replacementWord, file)

# Invoke Main Function
if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)
