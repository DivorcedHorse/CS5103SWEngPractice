# test_countChars.py
# Purpose:
#   Ensures that given a file, properly counts the total 
#   number of characters in the file.

import unittest
import main
from main import TOTAL_CHARACTER_COUNTER
import os
import io
import sys

testCase003 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase003.txt')
testCase004 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase004.txt')
testCase006 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase006.txt')
testCase007 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase007.txt')
testCase009 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase009.txt')

class TestCharCount(unittest.TestCase):
    # clear the global FOUNDWORDS and character counter
    # so tests do not interfere with each other.
    def setUp(self):
        main.TOTAL_CHARACTER_COUNTER = 0
        main.FOUNDWORDS = {}
    def tearDown(self):
        main.TOTAL_CHARACTER_COUNTER = 0
        main.FOUNDWORDS = {}
    
    # Given an empty file, with no words or characters
    # TOTAL_CHARACTER_COUNTER should be 0 and not increment
    def test_countEmptyFileNoCharacters(self):
        main.readFile(testCase003)
        self.assertEqual(main.TOTAL_CHARACTER_COUNTER, 0)
        self.assertGreaterEqual(1, main.TOTAL_CHARACTER_COUNTER)
    
    # Given a single unique word, ensures that the length 
    # is properly counted and added to total of TOTAL_CHARACTER_COUNTER
    def test_simpleCharWordCount(self):
        word = "character"
        expectedLength = 9
        main.charWordCounter(word)
        self.assertEqual(main.TOTAL_CHARACTER_COUNTER, expectedLength)
        
    # Given a various amount of words, ensures TOTAL_CHARACTER_COUNTER
    # updates properly with different characters
    def test_multipleWordsCharCount(self):
        words = ["One", "Two", "THREE", "FOUR", "fiVE"]
        totalLenghs = [3, 6, 11, 15, 19]
        for index, word in enumerate(words):
            main.charWordCounter(word)
            self.assertEqual(main.TOTAL_CHARACTER_COUNTER, totalLenghs[index])
            
    # Given symbols, ensures character counter properly
    # counts them.
    def test_symbolCharacterCount(self):
        symbols = ["?", "!", "/", ".", "@", "#"]
        totalLenghs = [1, 2, 3, 4, 5, 6]
        for index, symbol in enumerate(symbols):
            main.charWordCounter(symbol)
            self.assertEqual(main.TOTAL_CHARACTER_COUNTER, totalLenghs[index])
        
        # Given a string of symbols and characters, ensures char count is fine
        # does not count
        string = "ha@4##9$--!#($*)st"
        expectedTotalLength = 24
        main.charWordCounter(string)
        self.assertEqual(main.TOTAL_CHARACTER_COUNTER, expectedTotalLength)
        
    # Given numbers (as strings), ensures character counter properly
    # counts them.
    def test_numberCharacterCount(self):
        for number in range(0, 9):
            main.charWordCounter(str(number))
            self.assertEqual(main.TOTAL_CHARACTER_COUNTER, number+1)
            
    # Ensures printing of total characters is correct
    # given a file of many valid and identical  words.
    def test_printCharacterCount(self):
        main.readFile(testCase004)
        self.assertEqual(main.TOTAL_CHARACTER_COUNTER, 41)
        expectedString = "Total number of characters counted in document: 41"
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        main.printCharacterCount()        
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        output = output.rstrip()
        self.assertEqual(output, expectedString)
        
    # Ensures that no spaces, tabs, or newline characters
    # in a file are counted to the total
    def test_spaceTabCount(self):
        main.readFile(testCase009)
        self.assertEqual(main.TOTAL_CHARACTER_COUNTER, 0)
        self.assertGreaterEqual(1, main.TOTAL_CHARACTER_COUNTER)
        
    # Ensures printing of characters is correct even with
    # file filled with spaces, symbols, numbers, valid/invalid words.
    def test_printCharacterCountInvalidWords(self):
        main.readFile(testCase007)
        self.assertEqual(main.TOTAL_CHARACTER_COUNTER, 85)
        expectedString = "Total number of characters counted in document: 85"
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        main.printCharacterCount()        
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        output = output.rstrip()
        self.assertEqual(output, expectedString)
        self.assertEqual(main.TOTAL_CHARACTER_COUNTER, 85)
        self.assertNotEqual(main.TOTAL_CHARACTER_COUNTER, 0)
        
    # Ensures printing of characters is correct even with
    # spaces, tabs, and newlines present.
    def test_printCharacterCountWithSpaces(self):
        main.readFile(testCase006)
        expectedString = "Total number of characters counted in document: 52"
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        main.printCharacterCount()        
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        output = output.rstrip()
        self.assertEqual(output, expectedString)
        self.assertEqual(main.TOTAL_CHARACTER_COUNTER, 52)
        self.assertNotEqual(main.TOTAL_CHARACTER_COUNTER, 0)
    
if __name__ == '__main__':
    unittest.main()