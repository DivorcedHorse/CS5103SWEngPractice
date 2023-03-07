# test_printWords.py
# Purpose:
#   Ensures that given a count of words, properly
#   prints out the contents onto the terminal.

import unittest
import main
import io
import sys

class TestPrintWords(unittest.TestCase):
    # clear the global FOUNDWORDS so tests do not
    # interfere with one another
    def setUp(self):
        main.FOUNDWORDS = {}
        
    def tearDown(self):
        main.FOUNDWORDS = {}
        
     # Given an empty dictionary, prints nothing
    def test_validatePrintNone(self):
        main.FOUNDWORDS = {}
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        main.printWords()
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        output = output.rstrip()
        self.assertEqual(output, '')
        self.assertEqual(len(output), 0)
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

if __name__ == '__main__':
    unittest.main()