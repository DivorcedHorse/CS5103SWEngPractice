# main.py by Daniel Tellez
# Purpose:
#   The purpose of this application will be to perform various 
#   word statistics of a given document.  The initial requirement 
#   will be to count the frequency of each unique word.

# Necessary imports
import sys

# readFile
#   Given a file, simply reads the contents and prints the contents
#   of the file.
def readFile(file):
    try:
        with open(file, 'r') as file:
            # Iterate through every single line in the file
            for line in file:
                print(line)
                         
    # File being read did not work, give simple ERROR message
    except IOError:
        print("Unable to open given input file.  Terminating Process.")
        exit()

# Simply read filename provided and call readFile function
def main():
    file = sys.argv[1]
    readFile(file)
    
# Invoke Main Function
if __name__ == "__main__":
    main()