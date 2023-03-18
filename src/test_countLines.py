# test_countLines.py
# Purpose:
#   Ensures that given a file, properly counts the lines for that
#   given file.

import unittest
import main
from main import TOTAL_LINE_COUNTER
import os
import io
import sys


testCase003 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase003.txt')
testCase004 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase004.txt')
testCase009 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase009.txt')

class TestArguments(unittest.TestCase):
    # clear the global FOUNDWORDS so tests do not
    # interfere with one another
    def setUp(self):
        main.TOTAL_LINE_COUNTER = 0
        main.FOUNDWORDS = {}
    
    # Given an empty file, with no new lines, 
    # TOTAL_LINE_COUNTER should be 0 and not increment
    def test_countEmptyFileNoLines(self):
        main.readFile(testCase003)
        self.assertEqual(main.TOTAL_LINE_COUNTER, 0)
        self.assertNotEqual(main.TOTAL_LINE_COUNTER, 1)
        
    # Given an empty file, with many blank new lines, 
    # TOTAL_LINE_COUNTER should be 15 as it counts
    # "\n" characters
    def test_countEmptyFileWithLines(self):
        main.readFile(testCase009)
        self.assertEqual(main.TOTAL_LINE_COUNTER, 15)
        self.assertNotEqual(main.TOTAL_LINE_COUNTER, 0)
        self.assertNotEqual(main.TOTAL_LINE_COUNTER, 16)
        self.assertNotEqual(main.TOTAL_LINE_COUNTER, 14)
        
    # Given a valid file with valid words, ensures 
    # words do not mess with counting of lines
    def test_countLinesWithValidWords(self):
        main.readFile(testCase004)
        self.assertEqual(main.TOTAL_LINE_COUNTER, 10)
        self.assertNotEqual(main.TOTAL_LINE_COUNTER, 0)

    # Test to ensure that if print works correctly
    # depending on the value of TOTAL_LINE_COUNTER
    def test_lineCounterPrint(self):
        main.TOTAL_LINE_COUNTER = 5
        expectedString = "Total number of lines counted in document: 5"
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        main.printLineCount()        
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        output = output.rstrip()
        self.assertEqual(output, expectedString)
        badString = "Total number of lines counted in document: 4"
        self.assertNotEqual(output, "")
        self.assertNotEqual(output, badString)
        
    # Given a valid file with lines, see if lineCounter
    # properly counts lines and prints
    def test_lineCounterPrintWithFile(self):
        main.readFile(testCase004)
        expectedString = "Total number of lines counted in document: 10"
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        main.printLineCount()        
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        output = output.rstrip()
        self.assertEqual(output, expectedString)
    
        
if __name__ == '__main__':
    unittest.main()