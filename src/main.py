# main.py by Daniel Tellez
# Purpose:
#   The purpose of this application will be to perform various 
#   word statistics of a given document.  The initial requirement 
#   will be to count the frequency of each unique word.

# Necessary imports
import sys

# GLOBALS
FOUNDWORDS = {}     # Stores unique words found

# printWords
#   Prints all the words in FOUNDWORDS with their 
#   respective count values
def printWords():
    for word in FOUNDWORDS.keys():
        print("\"" + word + "\"" + " has a word count of " + str(FOUNDWORDS[word]))

# countUniqueWords
#   Given a list of words, iterates through them
#   and keeps counts of new/old words 
def countUniqueWords(words):
    global FOUNDWORDS
    
    # Iterate through all words in list
    for word in words:
        # If it exists in dictionary, increment count
        if word in FOUNDWORDS:
            FOUNDWORDS[word] = FOUNDWORDS[word] + 1
        # First time seeing word, add it into dictionary and set value to 1
        else:
            FOUNDWORDS[word] = 1
            
# readFile
#   Given a file, simply reads the contents and prints the contents
#   of the file.
def readFile(file):
    try:
        with open(file, 'r') as file:
            # Iterate through every single line in the file
            for line in file:
                # strip end of line for newline
                line = line.rstrip()
                
                # split will remove all spaces, tabs, and newlines
                words = line.split()
                
                # Invoke the countUniqueWords function
                countUniqueWords(words)
                
    # File being read did not work, give simple ERROR message
    except IOError:
        print("Unable to open given input file.  Terminating Process.")
        exit()

# Simply read filename provided and call readFile function
def main():
    file = sys.argv[1]
    readFile(file)
    printWords()
    
# Invoke Main Function
if __name__ == "__main__":
    main()