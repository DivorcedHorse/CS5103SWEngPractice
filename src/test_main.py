import unittest
from unittest.mock import patch
import main
import io
import sys

class TestStringandWords(unittest.TestCase):
    # clear the global FOUNDWORDS so tests do not
    # interfere with one another
    def setUp(self):
        main.FOUNDWORDS = {}
        
    # Given a bad input file, raise error
    def test_invalidInputFile(self):
        with self.assertRaises(IOError) as error:
            main.readFile("FILEDOESNOTEXIST.txt")
        self.assertEqual(str(error.exception), "ERROR: Unable to Open Given Input File.  Terminating Process.")
        
    # Given an empty array, check to see
    # if no words are counted.
    def test_countEmptyWords(self):
        words = []
        main.countUniqueWords(words)
        self.assertDictEqual(main.FOUNDWORDS, {})
        self.assertNotEqual(main.FOUNDWORDS, {"word":1})

    # Given an array of the same word, 
    # check to see if count works as intended
    def test_countIdenticalWords(self):
        words = ["word", "word", "word"]
        main.countUniqueWords(words)
        self.assertDictEqual(main.FOUNDWORDS, {'word': 3})
        self.assertNotEqual(main.FOUNDWORDS, {'word': 4})
        
    # Given array of different words, 
    # check to see if counted properly
    def test_countUniqueWords(self):
        words = ["word", "anotherWord", "word", "anotherWord"]
        main.countUniqueWords(words)
        self.assertDictEqual(main.FOUNDWORDS, {'anotherWord': 2, 'word': 2})
        self.assertNotEqual(main.FOUNDWORDS, {'word': 4})
        self.assertNotEqual(main.FOUNDWORDS, {'anotherWord': 2, 'word': 3})
        
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