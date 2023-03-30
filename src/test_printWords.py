# test_printWords.py
# Purpose:
#   Ensures that given a count of words, properly
#   prints out the contents onto the terminal.

import unittest
import main
import io
import sys
import os

testCase005 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase005.txt')

class TestPrintWords(unittest.TestCase):
    # clear the global FOUNDWORDS so tests do not
    # interfere with one another
    def setUp(self):
        main.FOUNDWORDS = {}
        main.TOTAL_CHARACTER_COUNTER = 0
        main.TOTAL_LINE_COUNTER
        
    def tearDown(self):
        main.FOUNDWORDS = {}
        main.TOTAL_CHARACTER_COUNTER = 0
        main.TOTAL_LINE_COUNTER
        
     # Given an empty dictionary, prints that no valid
     # words were found.
    def test_validatePrintNone(self):
        main.FOUNDWORDS = {}
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        main.printWords()
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        output = output.rstrip()
        self.assertEqual(output, 'String and Words found no valid words in the given file.')
        self.assertEqual(len(output), 56)
        self.assertNotEqual(len(output), 1)
        self.assertNotEqual(output, "bad string")

    # Given a dictionary of single word, ensure 
    # print is correct
    def test_validatePrintSingleWord(self):
        main.FOUNDWORDS = {"Print": 10}
        expectedString = "\"Print\" has a word count of 10"
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        main.printWords()
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        output = output.rstrip()
        self.assertEqual(output, expectedString)
        self.assertNotEqual(output, "bad string")
        self.assertNotEqual(output, "")
        self.assertNotEqual(output, "\"Print\" has a word count of 11")

    # Given a dictionary of many unique words,
    # ensure all are printed
    def test_validatePrintWords(self):
        main.FOUNDWORDS = {"Print": 10, "another": 3, "first": 5}
        expectedString = "\"Print\" has a word count of 10"
        expectedString += "\n\"another\" has a word count of 3"
        expectedString += "\n\"first\" has a word count of 5"
            
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        main.printWords()
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        output = output.rstrip()
        self.assertEqual(output, expectedString)
        self.assertNotEqual(output, "bad string")
        self.assertNotEqual(output, "")
        self.assertNotEqual(output, expectedString + ".")
        
    # running the entire system on a simple file, ensure the system
    # prints the expected lines in order and correctly.
    def test_allFinalPrints(self):
        main.FOUNDWORDS = {}

        main.readFile(testCase005)
        expectedWordString = "\"Unique\" has a word count of 10\n"
        expectedCountString = "Total number of characters counted in document: 60\n"
        expectedLineString = "Total number of lines counted in document: 6"
        expectedString = expectedWordString + expectedCountString + expectedLineString
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        main.printWords()
        main.printCharacterCount()
        main.printLineCount()        
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        output = output.rstrip()
        self.assertEqual(output, expectedString)

if __name__ == '__main__':
    unittest.main()