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
testCase007 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase007.txt')
testCase009 = os.path.join(os.path.dirname(__file__), 'testfiledata/testcase009.txt')

class TestCharCount(unittest.TestCase):
    # clear the global FOUNDWORDS and character counter
    # so tests do not interfere with each other.
    def setUp(self):
        main.TOTAL_CHARACTER_COUNTER = 0
        main.FOUNDWORDS = {}
    
    # Given an empty file, with no words or characters
    # TOTAL_CHARACTER_COUNTER should be 0 and not increment
    def test_countEmptyFileNoLines(self):
        main.readFile(testCase003)
        self.assertEqual(main.TOTAL_CHARACTER_COUNTER, 0)
        self.assertGreaterEqual(1, main.TOTAL_CHARACTER_COUNTER)
        
if __name__ == '__main__':
    unittest.main()